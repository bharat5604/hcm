from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from .models import *
from datetime import datetime
from django.core.files.storage import FileSystemStorage
import re
from .forms import *

@login_required(login_url='user_login')
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('user_login'))

def user_login(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('dashboard'))
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('dashboard'))
        else:
            messages.error(request, 'Invalid Login Credentials!')
            return render(request, 'webadmin/login.html', context = {})
    return render(request, 'webadmin/login.html', context = {})

@login_required(login_url='user_login')
def dashboard(request):
    return render(request, 'webadmin/dashboard.html', context = {})

@csrf_exempt
def change_action(request, objectType, objectId):
     modelClass = globals()[objectType]
     model = modelClass.objects.get(id=objectId)
     get_action = request.GET['action']
     action = 'Active' if get_action == 'True' else 'Inactive'
     setattr(model,'action',action)
     model.save()
     return HttpResponse('Action Changed!')

def getDBObject(objectType,caller,objectId=None):
    modelClass = globals()[objectType]
    if caller == 'modelObjects':
        return modelClass.objects.filter(id=objectId).values()[0]
    elif caller == 'dynamicModelObjects':
        return modelClass.objects.filter(id=objectId).values()[0]
    elif caller == 'updateObject':
        return modelClass.objects.get(id=objectId)
    elif caller == 'showObjectDetails':
        return modelClass.objects.filter(id=objectId).values()[0]
    elif caller == 'showObjectList':
        return modelClass.objects.all().values()
    elif caller == 'saveObject':
        return modelClass()

def getFormClass(request, objectTypeForm, caller, objToUpdate=None):
    formClass = globals()[objectTypeForm]
    if caller == 'modelform':
        return formClass()
    elif caller == 'editform':
        return formClass(initial=objToUpdate)
    elif caller == 'saveform':
        return formClass(request.POST)

def return_object_list(objList):
    objectList = list()
    for singleObject in objList:
        obj = dict()
        for key in singleObject:
            if key == 'action':
                if singleObject[key] == 'Active':
                    obj[key] = 'checked'
                else:
                    obj[key] = ''
            else:
                obj[key] = singleObject[key]
        objectList.append(obj)
    if len(objectList) > 0:
        if len(objectList[0]) > 2:
            fieldNames = [x for x in objectList[0]]
        noEntry = False
    else:
        fieldNames = []
        noEntry = True

    return noEntry, fieldNames, objectList

@login_required(login_url='user_login')
def show_object_list(request, objectSlug):
    objectType = ''.join([x.title() for x in objectSlug.split('_')])
    noEntry = True
    objectList = []
    fieldNames = []
    objList = getDBObject(objectType,'showObjectList')
    if objList:
        noEntry, fieldNames, objectList = return_object_list(objList)

    context = {
        "noEntry":noEntry,
        "objects": objectList,
        "objectSlug": objectSlug,
        "objectType": objectType,
        "fieldNames": fieldNames,
    }

    return render(request, 'webadmin/get_pages/{}.html'.format(objectType), context = context)

@login_required(login_url='user_login')
def model_object(request, objectSlug):
    objectType = ''.join([x.title() for x in objectSlug.split('_')])
    ckeditor_list = []
    if 'edit' in request.GET:
        objectId = request.GET['objectId']
        objToUpdate = getDBObject(objectType,'modelObjects',objectId)
        context = {
            "objectType": objectType,
            "objectSlug": objectSlug,
            "objectToUpdate":objToUpdate,
        }
        if objectType in ckeditor_list:
            objectTypeForm = objectType + 'Form'
            form = getFormClass(request, objectTypeForm, 'editform', objToUpdate)
            context['form'] = form
        templateFile = 'webadmin/add_pages/{}.html'.format(objectType)
        return render(request,templateFile, context)
    else:
        context = {
            "objectType": objectType,
            "objectSlug": objectSlug,
        }
        if objectType in ckeditor_list:
            objectTypeForm = objectType + 'Form'
            form = getFormClass(request, objectTypeForm, 'modelform')
            context['form'] = form
        templateFile = 'webadmin/add_pages/{}.html'.format(objectType)
        return render(request,templateFile, context)

@csrf_exempt
def saveObject(request, objectSlug):
    objectType = ''.join([x.title() for x in objectSlug.split('_')])
    ckeditor_model_list = []
    ckeditor_fields_list = []
    if request.POST:
        objToSave = getDBObject(objectType,'saveObject')
        for key in request.POST:
            if key != 'csrfmiddlewaretoken' and len(request.POST[key]) != 0:
                if key in ckeditor_fields_list and objectType in ckeditor_model_list:
                    objectTypeForm = objectType + 'Form'
                    form = getFormClass(request, objectTypeForm, 'saveform')
                    if form.is_valid():
                        cleaned_value = form.cleaned_data[key]
                        setattr(objToSave,key,cleaned_value)
                else:
                    new_value = request.POST[key]
                    setattr(objToSave,key,new_value)
        for key in request.FILES:
            file_instance = request.FILES[key]
            tempFileName = objectType+'_'+datetime.now().strftime("%m%d%y%H%M%S")+'.'+str(request.FILES[key]).split('.')[-1]
            fs = FileSystemStorage()
            filename = fs.save(tempFileName, file_instance)
            uploaded_file_url = fs.url(filename)
            setattr(objToSave,key,uploaded_file_url)

        objToSave.save()

        context = {
        "objectType":objectType,
        "objectSlug": objectSlug,
        "objectID":objToSave.id,
        "Operation":'add',
        }

        messages.success(request, 'Record Saved!')
        return redirect('show_object_list', objectSlug=objectSlug)

@csrf_exempt
def updateObject(request,objectSlug,objectId):
    objectType = ''.join([x.title() for x in objectSlug.split('_')])
    ckeditor_model_list = []
    ckeditor_fields_list = []
    if request.POST:
        objToUpdate = getDBObject(objectType,'updateObject',objectId)
        for key in request.POST:
            if len(request.POST[key]) != 0:
                if key in ckeditor_fields_list and objectType in ckeditor_model_list:
                    objectTypeForm = objectType + 'Form'
                    form = getFormClass(request, objectTypeForm, 'saveform')
                    if form.is_valid():
                        cleaned_value = form.cleaned_data[key]
                        setattr(objToUpdate,key,cleaned_value)
                else:
                    new_value = request.POST[key]
                    setattr(objToUpdate,key,new_value)

        for key in request.FILES:
            file_instance = request.FILES[key]
            tempFileName = objectType+'_'+datetime.now().strftime("%m%d%y%H%M%S")+'.'+str(request.FILES[key]).split('.')[-1]
            fs = FileSystemStorage()
            filename = fs.save(tempFileName, file_instance)
            uploaded_file_url = fs.url(filename)
            setattr(objToUpdate,key,uploaded_file_url)

        objToUpdate.save()

        context = {
        "objectType":objectType,
        "objectSlug": objectSlug,
        "objectID":objToUpdate.id,
        "Operation":'update',
        }

        messages.success(request, 'Record Updated!')
        return redirect('show_object_list', objectSlug=objectSlug)

@csrf_exempt
def deleteObject(request,objectSlug,objectId):
    objectType = ''.join([x.title() for x in objectSlug.split('_')])
    objToUpdate = getDBObject(objectType,'updateObject',objectId)
    objToUpdate.delete()
    return HttpResponse('Record Deleted!')

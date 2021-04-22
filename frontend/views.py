from django.shortcuts import render, redirect
from webadmin.models import *
from .web_content import *
from datetime import datetime
from django.core.files.storage import FileSystemStorage
import re
from django.contrib import messages
# Create your views here.

def return_object_list(objList):
    objectList = list()
    for singleObject in objList:
        obj = dict()
        for key in singleObject:
            new_key = key.replace('_', ' ').title() if key != 'id' else 'Process Names' if key == 'function_names' else 'id'
            if key == 'action':
                if singleObject[key] == 'Active':
                    obj[new_key] = 'checked'
                else:
                    obj[new_key] = ''
            else:
                obj[new_key] = singleObject[key]
        objectList.append(obj)
    if len(objectList) > 0:
        if len(objectList[0]) > 2:
            fieldNames = [x for x in objectList[0]]
        noEntry = False
    else:
        fieldNames = []
        noEntry = True

    return noEntry, fieldNames, objectList

def basic_setup():
    navmenu_list = navmenu()
    footer_logo, footer_description, google_play_store_link, facebook_page_link, twitter_page_link, pinterest_page_link, linkedin_page_link = footer()
    partners_list = partners()
    header_logo, header_title, header_description, google_play_store_link = header()

    context = {
        'header_logo' : header_logo,
        'header_title' : header_title,
        'header_description' : header_description,
        'google_play_store_link' : google_play_store_link,
        'navmenu_list' : navmenu_list,
        'footer_logo' : footer_logo,
        'footer_description' : footer_description,
        'facebook_page_link' : facebook_page_link,
        'twitter_page_link' : twitter_page_link,
        'pinterest_page_link' : pinterest_page_link,
        'linkedin_page_link' : linkedin_page_link,
        'partners_list' : partners_list,
    }
    return context

def index(request, *args, **kwargs):
    context = basic_setup()
    seo_title, seo_description = manage_seo_content('index')
    testimonials_list = testimonials()
    print(testimonials_list)
    services_dict = services_list()
    context['seo_title'] = seo_title
    context['seo_description'] = seo_description
    context['testimonials_list'] = testimonials_list
    context['services_dict'] = services_dict
    return render(request, 'frontend/index.html', context=context)

def about(request, *args, **kwargs):
    context = basic_setup()
    seo_title, seo_description = manage_seo_content('about')
    about_heading, about_content, vision, mission = about_us()
    context['seo_title'] = seo_title
    context['seo_description'] = seo_description
    context['about_heading'] = about_heading
    context['about_content'] = about_content
    context['vision'] = vision
    context['mission'] = mission
    return render(request, 'frontend/aboutus.html', context=context)

def blog(request, *args, **kwargs):
    context = basic_setup()
    seo_title, seo_description = manage_seo_content('blog')
    blog_list = blog_objects()
    context['seo_title'] = seo_title
    context['seo_description'] = seo_description
    context['blog_list'] = blog_list
    context['archived_blogs'] = blog_archive()
    if blog_list:
        context['latest_blogs'] = reversed(blog_list[0:2])
    return render(request, 'frontend/blog.html', context=context)

def blog_detail(request, *args, **kwargs):
    context = basic_setup()
    # blog_publisher_name, blog_topic, blog_image, blog_contents, blog_published_date = blog_details(id)
    blog_list = blog_objects()
    # context['seo_title'] = blog_topic + ' - Neo Blogs'
    # context['seo_description'] = blog_contents
    # if blog_list:
    #     context['blog_list'] = blog_list[0:2]
    # context['blog_publisher_name'] = blog_publisher_name
    # context['blog_topic'] = blog_topic
    # context['blog_image'] = blog_image
    # context['blog_contents'] = blog_contents
    # context['blog_published_date'] = blog_published_date
    return render(request, 'frontend/blog-detail.html', context=context)

def contact(request, *args, **kwargs):
    context = basic_setup()
    contact_email, contact_phone_no, contact_address = contact_us()
    seo_title, seo_description = manage_seo_content('contact')
    context['contact_email'] = contact_email
    context['contact_phone_no'] = contact_phone_no
    context['contact_address'] = contact_address
    context['seo_title'] = seo_title
    context['seo_description'] = seo_description
    return render(request, 'frontend/contact-us.html', context=context)

def news_event(request, *args, **kwargs):
    context = basic_setup()
    seo_title, seo_description = manage_seo_content('news_event')
    news_media_list = manage_news_media()
    context['seo_title'] = seo_title
    context['seo_description'] = seo_description
    context['news_media_list'] = news_media_list
    if news_media_list:
        context['latest_news'] = reversed(news_media_list[0:2])
    return render(request, 'frontend/news-event.html', context=context)

def news_event_detail(request, id):
    context = basic_setup()
    news_media_topic, news_media_media_file, news_media_contents, news_media_published_date = news_media_detail(id)
    news_media_list = manage_news_media()
    context['seo_title'] = news_media_topic + ' - Neo Events'
    context['seo_description'] = news_media_contents
    context['news_media_topic'] = news_media_topic
    context['news_media_media_file'] = news_media_media_file
    context['news_media_contents'] = news_media_contents
    context['news_media_published_date'] = news_media_published_date
    if news_media_list:
        context['recommended_news_media'] = news_media_list[0:2]
    return render(request, 'frontend/news-event-detail.html', context=context)

def recruitement(request, *args, **kwargs):
    context = basic_setup()
    seo_title, seo_description = manage_seo_content('recruitement')
    services_dict = services_list()
    context['seo_title'] = seo_title
    context['seo_description'] = seo_description
    context['services_dict'] = services_dict
    return render(request, 'frontend/recruitement.html', context=context)

def attendance(request, *args, **kwargs):
    context = basic_setup()
    seo_title, seo_description = manage_seo_content('about')
    about_heading, about_content, vision, mission = about_us()
    context['seo_title'] = seo_title
    context['seo_description'] = seo_description
    context['about_heading'] = about_heading
    context['about_content'] = about_content
    context['vision'] = vision
    context['mission'] = mission
    return render(request, 'frontend/attendance.html', context=context)

def ourteam(request, *args, **kwargs):
    context = basic_setup()
    seo_title, seo_description = manage_seo_content('ourteam')
    about_heading, about_content, vision, mission = about_us()
    return render(request, 'frontend/ourteam.html', context=context)

def price(request, *args, **kwargs):
    context = basic_setup()
    seo_title, seo_description = manage_seo_content('ourteam')
    about_heading, about_content, vision, mission = about_us()
    return render(request, 'frontend/price.html', context=context)

def strategichr(request, *args, **kwargs):
    context = basic_setup()
    seo_title, seo_description = manage_seo_content('strategichr')
    about_heading, about_content, vision, mission = about_us()
    return render(request, 'frontend/strategichr.html', context=context)

def payroll(request, *args, **kwargs):
    context = basic_setup()
    seo_title, seo_description = manage_seo_content('payroll')
    about_heading, about_content, vision, mission = about_us()
    return render(request, 'frontend/payroll.html', context=context)

def compliances(request, *args, **kwargs):
    context = basic_setup()
    seo_title, seo_description = manage_seo_content('compliances')
    about_heading, about_content, vision, mission = about_us()
    return render(request, 'frontend/compliances.html', context=context)

def demo(request, *args, **kwargs):
    context = basic_setup()
    seo_title, seo_description = manage_seo_content('demo')
    about_heading, about_content, vision, mission = about_us()
    return render(request, 'frontend/demo.html', context=context)

def trial(request, *args, **kwargs):
    context = basic_setup()
    seo_title, seo_description = manage_seo_content('trial')
    about_heading, about_content, vision, mission = about_us()
    return render(request, 'frontend/trial.html', context=context)

def signin(request, *args, **kwargs):
    context = basic_setup()
    seo_title, seo_description = manage_seo_content('trial')
    about_heading, about_content, vision, mission = about_us()
    return render(request, 'frontend/signin.html', context=context)

def signup(request, *args, **kwargs):
    context = basic_setup()
    seo_title, seo_description = manage_seo_content('signup')
    about_heading, about_content, vision, mission = about_us()
    return render(request, 'frontend/signup.html', context=context)

def career(request):
    seo_title, seo_description = manage_seo_content('career')
    noEntry, fieldNames, objectList = True, [], []
    objList = PostVacancies.objects.filter(status='current-opening').values()
    if objList:
        noEntry, fieldNames, objectList = return_object_list(objList)
    context = {
        "noEntry":noEntry,
        "objects": objectList,
        "fieldNames": fieldNames,
        "seo_title": seo_title,
        "seo_description": seo_description
    }
    return render(request, 'frontend/career.html', context = context)

def apply_career(request, id):
    jobApplied = False
    objectToAdd = PostVacancies.objects.filter(id=id).values()[0]
    if request.POST:
        objToSave = ResumeReceipt()
        for key in request.POST:
            if key != 'csrfmiddlewaretoken' and len(request.POST[key]) != 0:
                new_value = request.POST[key].replace('\r', '<br>').replace('\n', '<br>')
                setattr(objToSave,key,new_value)
        for key in request.FILES:
            file_instance = request.FILES[key]
            tempFileName = 'ResumeReceipt'+'_'+datetime.now().strftime("%m%d%y%H%M%S")+'.'+str(request.FILES[key]).split('.')[-1]
            fs = FileSystemStorage()
            filename = fs.save(tempFileName, file_instance)
            uploaded_file_url = fs.url(filename)
            setattr(objToSave,key,uploaded_file_url)
        objToSave.save()
        jobApplied = True
    return render(request, 'frontend/apply-career.html', context = {'jobApplied':jobApplied,"objectToAdd":objectToAdd,"id":id,})

def apply_job(request):
    jobApplied = False
    if request.POST:
        objToSave = ResumeReceipt()
        for key in request.POST:
            if key != 'csrfmiddlewaretoken' and len(request.POST[key]) != 0:
                new_value = request.POST[key].replace('\r', '<br>').replace('\n', '<br>')
                setattr(objToSave,key,new_value)
        for key in request.FILES:
            file_instance = request.FILES[key]
            tempFileName = 'ResumeReceipt'+'_'+datetime.now().strftime("%m%d%y%H%M%S")+'.'+str(request.FILES[key]).split('.')[-1]
            fs = FileSystemStorage()
            filename = fs.save(tempFileName, file_instance)
            uploaded_file_url = fs.url(filename)
            setattr(objToSave,key,uploaded_file_url)
        objToSave.save()
        jobApplied = True
    return render(request, 'frontend/apply-job.html', context = {'jobApplied':jobApplied})

def putSpace(input):
    words = re.findall('[A-Z][a-z]*', input)
    result = []
    for word in words:
        word = chr( ord (word[0]) + 32) + word[1:]
        result.append(word)
    return ' '.join(result).title()

def footer_contents(request, objectType):
    context = {}
    page_content = footer_content(objectType)
    page_title = putSpace(objectType)
    context['seo_title'] = page_title
    if len(page_content) > 160:
        context['seo_description'] = page_content[0:160]
    else:
        context['seo_description'] = page_content
    context['page_content'] = page_content
    context['page_title'] = page_title
    return render(request, 'frontend/footercontents.html', context = context)

def manage_team(request):
    context = {}
    team_list = manage_team_members()
    context['seo_title'] = 'Team Members'
    context['seo_description'] = 'Team Members working at ADFPAY Neo Bank.'
    context['team_list'] = team_list
    return render(request, 'frontend/manageteam.html', context = context)

def advisory_board(request):
    context = {}
    team_list = advisory_board_members()
    context['seo_title'] = 'Advisory Board'
    context['seo_description'] = 'Advisory Board Members working at ADFPAY Neo Bank.'
    context['team_list'] = team_list
    return render(request, 'frontend/advisoryboard.html', context = context)

def sendmessage(request):
    if request.POST:
        name = request.POST['name']
        email = request.POST['email']
        phone_no = request.POST['phone_no']
        message = request.POST['message']
        contact = ContactUs(name=name, email=email, phone_no=phone_no, message=message)
        contact.save()
        messages.success(request, 'Message Sent!')
    return redirect('frontend:contact')

def handler404(request, exception, status = 404):
    return render(request, 'frontend/404.html')

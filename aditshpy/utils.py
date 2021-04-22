from datetime import datetime

def get_filename(filename, request):
    return filename.split('.')[0].upper() + '_' + datetime.now().strftime("%m%d%y%H%M%S") + '.' + filename.split('.')[-1]

from django.urls import path
from .views import *

app_name = 'frontend'

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('blog/', blog, name='blog'),
    path('blog_detail/', blog_detail, name='blog_detail'),
    path('news-event/', news_event, name='news_event'),
    path('news-event/<int:id>/', news_event_detail, name='news_event_detail'),
    path('recruitement/', recruitement, name='recruitement'),
    path('attendance/', attendance, name='attendance'),
    path('ourteam/', ourteam, name='ourteam'),
    path('demo/', demo, name='request-demo'),
    path('trial/', trial, name='free-trial'),
    path('contact/', contact, name='contact'),
    path('signin/', signin, name='signin'),
    path('strategichr/', strategichr, name='strategichr'),
    path('payroll/', payroll, name='payroll'),
    path('compliances/', compliances, name='compliances'),
    path('price/', price, name='price'),
    path('signup/', signup, name='signup'),
    # path('recruitement/<str:category>/<int:id>/', service_detail, name='service_detail'),
    path('career/', career, name='career'),
    path('applyjob/<int:id>/', apply_career, name='applyjob'),
    path('apply-job/', apply_job, name='apply-job'),
    path('adfpay/<str:objectType>/', footer_contents, name='footer_contents'),
    path('team-members/', manage_team, name='manage_team'),
    path('advisory-board/', advisory_board, name='advisory_board'),
    path('send-message/', sendmessage, name='sendmessage'),
]

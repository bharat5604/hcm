from django.db import models

# Create your models here.
class ManageNewsMedia(models.Model):
    topic = models.CharField(default="", max_length=300)
    content_type = models.CharField(default="", max_length=300)
    content = models.TextField(default="")
    content_display_type = models.CharField(default="", max_length=300)
    media_file = models.FileField(default="")
    published_date = models.DateField(auto_now_add=True)
    action = models.CharField(default="Active", max_length=10)

class ManageSEOContent(models.Model):
    page_name = models.CharField(default="", max_length=300)
    title = models.CharField(default="", max_length=300)
    meta_description = models.CharField(default="", max_length=1000)
    action = models.CharField(default="Active", max_length=10)

class PostVacancies(models.Model):
    location = models.CharField(default="", max_length=300)
    department = models.CharField(default="", max_length=300)
    designation = models.CharField(default="", max_length=300)
    no_of_vacancies = models.PositiveIntegerField(default=0)
    experience = models.CharField(default="", max_length=300)
    qualification = models.CharField(default="", max_length=300)
    salary_range = models.CharField(default="", max_length=300)
    requirement_type = models.CharField(default="", max_length=300)
    valid_upto = models.DateField(default="")
    job_description = models.TextField(default="")
    status = models.CharField(default="", max_length=300)
    action = models.CharField(default="Active", max_length=300)

class ResumeReceipt(models.Model):
    candidate_name = models.CharField(default="", max_length=300)
    department = models.CharField(default="", max_length=300)
    designation = models.CharField(default="", max_length=300)
    location = models.CharField(default="", max_length=300)
    resume = models.FileField(default="")
    action = models.CharField(default="Active", max_length=300)

class PublishBlogs(models.Model):
    publisher_name = models.CharField(default="", max_length=300)
    topic = models.CharField(default="", max_length=300)
    image = models.FileField(default="")
    content = models.TextField(default="")
    content_display_type = models.CharField(default="", max_length=300)
    published_date = models.DateField(auto_now_add=True)
    action = models.CharField(default="Active", max_length=300)

class Partners(models.Model):
    logo = models.FileField(default="")
    name = models.CharField(default="", max_length=300)
    action = models.CharField(default="Active", max_length=300)

class Testimonials(models.Model):
    photo = models.FileField(default="")
    name = models.CharField(default="", max_length=300)
    profession = models.CharField(default="", max_length=300)
    comment = models.CharField(default="", max_length=1000)
    action = models.CharField(default="Active", max_length=300)

class ContactUs(models.Model):
    name = models.CharField(default="", max_length=200)
    email = models.EmailField(default="", max_length=200)
    phone_no = models.CharField(default="", max_length=200)
    message = models.TextField(default="")

class AboutUs(models.Model):
    heading = models.CharField(default="", max_length=200)
    content = models.TextField()
    vision = models.TextField()
    mission = models.TextField()
    action = models.CharField(default="Active", max_length=200)

class Footer(models.Model):
    logo = models.FileField(default="")
    footer_description = models.CharField(default="", max_length=400)
    google_play_store_link = models.URLField(default="")
    facebook_page_link = models.URLField(default="")
    twitter_page_link = models.URLField(default="")
    pinterest_page_link = models.URLField(default="")
    linkedin_page_link = models.URLField(default="")
    action = models.CharField(default="Active", max_length=200)

class Header(models.Model):
    logo = models.FileField(default="")
    header_title = models.CharField(default="", max_length=200)
    header_description = models.TextField()
    google_play_store_link = models.URLField(default="")
    action = models.CharField(default="Active", max_length=200)

class NavigationMenu(models.Model):
    nav_item = models.CharField(default="", max_length=200)
    nav_link = models.URLField(default="")
    action = models.CharField(default="Active", max_length=200)

class SliderHeader(models.Model):
    image = models.FileField(default="")
    title = models.CharField(default="", max_length=200)
    short_description = models.CharField(default="", max_length=300)
    call_to_action_link = models.URLField(default="")
    action = models.CharField(default="Active", max_length=200)

class Services(models.Model):
    category = models.CharField(default="", max_length=200)
    name = models.CharField(default="", max_length=200)
    image = models.FileField(default="")
    content = models.TextField()
    action = models.CharField(default="Active", max_length=200)

class ManagementTeam(models.Model):
    name = models.CharField(default="", max_length=200)
    designation = models.CharField(default="", max_length=200)
    image = models.FileField(default="")
    content = models.TextField()
    action = models.CharField(default="Active", max_length=200)

class AdvisoryBoard(models.Model):
    name = models.CharField(default="", max_length=200)
    designation = models.CharField(default="", max_length=200)
    image = models.FileField(default="")
    content = models.TextField()
    action = models.CharField(default="Active", max_length=200)

class TermsAndConditions(models.Model):
    content = models.TextField()
    action = models.CharField(default="Active", max_length=200)

class TermsOfUse(models.Model):
    content = models.TextField()
    action = models.CharField(default="Active", max_length=200)

class FairPracticeCode(models.Model):
    content = models.TextField()
    action = models.CharField(default="Active", max_length=200)

class PrivacyPolicy(models.Model):
    content = models.TextField()
    action = models.CharField(default="Active", max_length=200)

class Disclaimer(models.Model):
    content = models.TextField()
    action = models.CharField(default="Active", max_length=200)

class GrievanceAddressMechanism(models.Model):
    content = models.TextField()
    action = models.CharField(default="Active", max_length=200)

class Faq(models.Model):
    content = models.TextField()
    action = models.CharField(default="Active", max_length=200)

class LifeAtAdfpay(models.Model):
    content = models.TextField()
    action = models.CharField(default="Active", max_length=200)

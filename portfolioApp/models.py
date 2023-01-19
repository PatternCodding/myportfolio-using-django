from django.db import models


# SideProfile
class SideProfile(models.Model):
    picture = models.ImageField(upload_to='picture/')
    name_text = models.CharField(max_length=20,default='PatternCodding')
    carreer_text = models.CharField(max_length=80,default='Full stact developer')
    email_text = models.EmailField(max_length=255,default='patterncodding@gmail.com')
    number_text = models.CharField(max_length=15,default='+2348101224630')
    birth_text = models.CharField(max_length=20,default='')
    location_text = models.CharField(max_length=50,default='P3 Ishieke Campus villa Ebonyi state, Nigeria')
   
    # save time when modified
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name_text
       
class Navbar(models.Model):
    navbar = models.CharField(max_length=15)
    
    def __str__(self):
        return self.navbar


# About
class About(models.Model):
    about_heading = models.CharField(max_length=20)
    text_1 = models.TextField(blank=True,null=True)
    text_2 = models.TextField(blank=True,null=True)
    
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.about_heading
    
    
    # Working as
class Duty(models.Model):
    duty_img = models.ImageField(upload_to='duty_image/')
    duty_text = models.CharField(max_length=50)
    duty_description = models.TextField(blank=False)
    
    def __str__(self):
        return self.duty_text
      

# Testimonial
class Testimonials(models.Model):
    testimoial_date = models.CharField(max_length=50,default='Y-M-D')
    testimony_image = models.ImageField(upload_to='testimony_image/') 
    testimoial_name = models.CharField(max_length=50, blank=True)    
    testimony_text = models.TextField(blank=True) 
    
    def __str__(self):
        return self.testimoial_name
    
# Clients
class Client(models.Model):
    # client_header = models.CharField(default='', max_length=30)
    client_image = models.ImageField(upload_to='client_image/')
    
    
    
# Education
class Education(models.Model):
    school = models.CharField(default='', max_length=50)
    educ_date = models.CharField(default='2018-2022',max_length=15)
    edu_description = models.TextField(blank=True, null=True)
        
    def __str__(self):
        return self.school

# Experiences
class Experience(models.Model):
    experience_name = models.CharField(default='', max_length=50)
    exp_year = models.CharField(default='2018-2022',max_length=20)
    exp_description = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.experience_name

# Skill
class Skill(models.Model):
    skills_name = models.CharField(default='', max_length=50)
    skills_perc = models.IntegerField()
    
    def __str__(self):
        return self.skills_name
    

# Portfolio
class Portfolio(models.Model):
    portolio_img = models.ImageField(upload_to='portfolio_img/')
    portolio_name = models.CharField(max_length=50,default='')
    portolio_desc = models.CharField(max_length=50,default='')
    uploaded = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.portolio_name




# Blog
class Blog(models.Model):
    blog_img = models.ImageField(upload_to='blogs_img')
    blog_date = models.DateTimeField(auto_now_add=True)
    blog_description = models.CharField(max_length=50)
    blog_contents = models.TextField(default='',blank=True, null=True)
    
    def __str__(self):
        return self.blog_description
    
# Contack
class Contact(models.Model):
    fullname = models.CharField(max_length=255)
    email = models.EmailField(default='', max_length=255)
    messages = models.TextField(default='')
    
    def __str__(self):
        return self.fullname
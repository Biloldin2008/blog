from django.db import models

class Welcome(models.Model):
    nomi = models.CharField(max_length=90)
    text = models.TextField()
    tugma = models.CharField(max_length=90)
    def __str__(self):
        return self.nomi

class Minus(models.Model):
    nomi = models.CharField(max_length=90)
    text = models.TextField()
    text1 = models.TextField()
    name = models.CharField(max_length=90)
    text2 = models.TextField()
    def __str__(self):
        return self.nomi

class SMS(models.Model):
    name = models.CharField(max_length=90)
    phone = models.IntegerField()
    email = models.EmailField()
    text = models.TextField()
    def __str__(self):
        return self.name

class Cons(models.Model):
    nomi = models.CharField(max_length=90)
    text = models.TextField()
    rasm = models.ImageField(upload_to='media/')
    nomi1 = models.CharField(max_length=90)
    text1 = models.TextField()
    def __str__(self):
        return self.nomi

class Service(models.Model):
    icon = models.CharField(max_length=90)
    nomi = models.CharField(max_length=90)
    text = models.TextField()
    tugma = models.CharField(max_length=90)
    def __str__(self):
        return self.nomi

class Enim(models.Model):
    rasm = models.ImageField(upload_to='media/')
    icon = models.CharField(max_length=90)
    nomi1 = models.CharField(max_length=90)
    text1 = models.TextField()
    def __str__(self):
        return self.nomi1

class Mod(models.Model):
    name = models.CharField(max_length=90)
    text = models.TextField()
    text1 = models.TextField()
    text2 = models.TextField()
    text3 = models.TextField()
    rasm = models.ImageField(upload_to='media/')
    def __str__(self):
        return self.name

class Ho(models.Model):
    name = models.CharField(max_length=90)
    text = models.TextField()
    text1 = models.TextField()
    text2 = models.TextField()
    text3 = models.TextField()
    text4 = models.TextField()
    rasm = models.ImageField(upload_to='media/')
    def __str__(self):
        return self.name

class Tu(models.Model):
    name = models.CharField(max_length=90)
    text = models.TextField()
    text1 = models.TextField()
    text2 = models.TextField()
    text3 = models.TextField()
    rasm = models.ImageField(upload_to='media/')
    def __str__(self):
        return self.name

class Biz(models.Model):
    name = models.CharField(max_length=90)
    text = models.TextField()
    text1 = models.TextField()
    text2 = models.TextField()
    text3 = models.TextField()
    rasm = models.ImageField(upload_to='media/')
    def __str__(self):
        return self.name

class Test(models.Model):
    rasm = models.ImageField(upload_to='media/')
    ism = models.CharField(max_length=90)
    ish = models.CharField(max_length=90)
    text = models.TextField()
    def __str__(self):
        return self.ism

class Blog1(models.Model):
    rasm = models.ImageField(upload_to='media/')
    sana = models.DateField()
    nomi = models.CharField(max_length=90)
    ism = models.CharField(max_length=90)
    ish = models.CharField(max_length=90)
    tugma = models.CharField(max_length=90)
    def __str__ (self):
        return self.nomi
    
class Et(models.Model):
    rasm = models.ImageField(upload_to='media/')
    nomi = models.CharField(max_length=90)
    sana = models.CharField(max_length=90)
    nomi1 = models.CharField(max_length=90)
    text = models.TextField()
    text1 = models.TextField()
    text2 = models.TextField()
    text3 = models.TextField()
    text4 = models.TextField()
    def __str__(self):
        return self.nomi

class Stat(models.Model):
    nomi = models.CharField(max_length=90)
    text = models.TextField()
    raqam = models.IntegerField()
    name = models.CharField(max_length=90)
    raqam1 = models.IntegerField()
    name1 = models.CharField(max_length=90)
    raqam2 = models.IntegerField()
    name2 = models.CharField(max_length=90)
    raqam3 = models.IntegerField()
    name3 = models.CharField(max_length=90)
    def __str__(self):
        return self.nomi

class Est(models.Model):
    rasm = models.ImageField(upload_to='media/')
    nomi = models.CharField(max_length=90)
    text = models.TextField()
    name = models.CharField(max_length=90)
    text1 = models.TextField()
    name1 = models.CharField(max_length=90)
    text2 = models.TextField()
    name2 = models.CharField(max_length=90)
    text3 = models.TextField()
    name3 = models.CharField(max_length=90)
    text4 = models.TextField()
    def __str__(self):
        return self.nomi

class Team(models.Model):
    rasm = models.ImageField(upload_to='media/')
    ism = models.CharField(max_length=90)
    ish = models.CharField(max_length=90)
    text = models.TextField()
    def __str__(self):
        return self.ism

class Timon(models.Model):
    rasm = models.ImageField(upload_to='media/')
    ism = models.CharField(max_length=90)
    ish = models.CharField(max_length=90)
    text = models.TextField()
    def __str__(self):
        return self.ism

class Omnis(models.Model):
    nomi = models.CharField(max_length=90)
    text = models.TextField()
    text1 = models.TextField()
    text2 = models.TextField()
    text3 = models.TextField()
    def __str__(self):
        return self.nomi

class Rasm(models.Model):
    rasm = models.ImageField(upload_to='media/')
    

class This(models.Model):
    nomi = models.CharField(max_length=90)
    text = models.TextField()
    text1 = models.TextField()
    text2 = models.TextField()
    rasm = models.ImageField(upload_to='media/')
    ism = models.CharField(max_length=90)
    ish = models.CharField(max_length=90)
    text3 = models.TextField()
    text4 = models.TextField()
    def __str__(self):
        return self.nomi

class Project(models.Model):
    nomi = models.CharField(max_length=90)
    nomi1 = models.CharField(max_length=90)
    ish = models.CharField(max_length=90)
    nomi2 = models.CharField(max_length=90)
    ish1 = models.CharField(max_length=90) 
    nomi3 = models.CharField(max_length=90)
    ish2 = models.CharField(max_length=90)
    nomi4 = models.CharField(max_length=90)
    ish3 = models.CharField(max_length=90)
    tugma = models.CharField(max_length=90)
    def __str__(self):
        return self.nomi


class Col(models.Model):
    nomi = models.CharField(max_length=90)
    ish = models.TextField()
    def __str__(self):
        return self.nomi
# Create your models here.

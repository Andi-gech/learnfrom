from datetime import date
from secrets import choice
from statistics import mode

from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class student_extra(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = CloudinaryField('image', default="f3kbfn1ewj0z4oiu3mv3")

    @property
    def get_id(self):
        return self.user.id

    @property
    def get_lastname(self):
        return self.user.last_name

    @property
    def get_firstname(self):
        return self.user.first_name

    def __str__(self):
        return self.user.username


class teacher_extra(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = CloudinaryField('image', default="f3kbfn1ewj0z4oiu3mv3")
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username


class admin_extra(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = CloudinaryField('image', default="f3kbfn1ewj0z4oiu3mv3")


catagory = (
    ('science', 'science'),
    ('code', 'code'),
    ('math', 'math'),
    ('other', 'other')
)


class question(models.Model):
    Title = models.CharField(max_length=50)
    discription = models.TextField()
    image_q = CloudinaryField(
        'image', blank=True, null=True)
    date = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(student_extra, on_delete=models.CASCADE)

    cat_name = models.CharField(
        choices=catagory, default='math', max_length=20)


class answers(models.Model):
    answer = models.TextField()
    quation = models.ForeignKey(question, on_delete=models.CASCADE)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='zones')
    likes = models.ManyToManyField(
        User, related_name='answers_like', null=True)
    value = models.BooleanField(default=False, null=True)
    image_a = CloudinaryField(
        'image', blank=True, null=True)
    date = models.DateTimeField(auto_now=True)

    def liker(self):
        return self.likes.all()

    def number_of_likes(self):
        return self.likes.count()

    @property
    def get_user(self):
        return self.get_user

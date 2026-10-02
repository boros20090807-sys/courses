from django.contrib.auth.models import User
from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=100)
    level = models.CharField(max_length=50)
    teacher = models.ForeignKey(User,on_delete=models.CASCADE,related_name='courses')
    students = models.ManyToManyField(User,related_name='enrolled_courses',blank=True)

    class Meta:
        verbose_name = "Курсы"
        verbose_name_plural = "Курсы"

    def str(self):
        return self.title


class Lesson(models.Model):
    course = models.ForeignKey(Course,on_delete=models.CASCADE,related_name='lessons')
    title = models.CharField(max_length=255)
    content = models.TextField()

    class Meta:
        verbose_name = "Уроки"
        verbose_name_plural = "Уроки"

    def str(self):
        return self.title


class Homework(models.Model):
    lesson = models.ForeignKey(Lesson,on_delete=models.CASCADE,related_name='homeworks')
    student = models.ForeignKey(User,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    text = models.TextField()
    
    class Meta:
        verbose_name = "Домашние задания"
        verbose_name_plural = "Домашние задании"
    

    def str(self):
        return f"{self.student.username} - {self.lesson.title}"


class Comment(models.Model):
    lesson = models.ForeignKey(Lesson,on_delete=models.CASCADE,related_name='comments')
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    text = models.TextField()

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"

    def str(self):
        return self.user.username
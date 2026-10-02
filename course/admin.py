from django.contrib import admin
from .models import Course, Lesson, Homework, Comment


class CourseAdmin(admin.ModelAdmin):
    list_display = ('id','title','category','level','teacher',)
    search_fields = ('title','category','teacher__username',)
    list_filter = ('category','level',)


class LessonAdmin(admin.ModelAdmin):
    list_display = ('id','title','course',)
    search_fields = ('title','course__title',)
    list_filter = ('course',)


class HomeworkAdmin(admin.ModelAdmin):
    list_display = ('id','student','lesson','created_at',)
    search_fields = ('student__username','lesson__title',)
    list_filter = ('created_at','lesson',)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('id','user','lesson','created_at',)
    sch_fields = ('user__username','text',)
    l_filter = ('created_at','lesson',)

admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Homework, HomeworkAdmin)
admin.site.register(Comment, CommentAdmin)
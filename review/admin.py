from django.contrib import admin
from review.models import Employee, Review, Criteria, Expectation, Answer, Survey


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('user', 'role', 'position')


class ReviewerAdmin(admin.ModelAdmin):
    list_display = ('employee', 'group')


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('reviewee', 'date')


class CriteriaAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')


class ExpectationAdmin(admin.ModelAdmin):
    list_display = ('criteria', 'position', 'description')


class AnswerAdmin(admin.ModelAdmin):
    pass


class SurveyAdmin(admin.ModelAdmin):
    pass


admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Criteria, CriteriaAdmin)
admin.site.register(Expectation, ExpectationAdmin)
admin.site.register(Answer, AnswerAdmin)
admin.site.register(Survey, SurveyAdmin)

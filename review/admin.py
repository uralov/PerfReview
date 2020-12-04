from django.contrib import admin
from review.models import Employee, Reviewer, Review, Criteria, Expectation, Answer


class EmployeeAdmin(admin.ModelAdmin):
    pass


class ReviewerAdmin(admin.ModelAdmin):
    pass


class ReviewAdmin(admin.ModelAdmin):
    pass


class CriteriaAdmin(admin.ModelAdmin):
    pass


class ExpectationAdmin(admin.ModelAdmin):
    pass


class AnswerAdmin(admin.ModelAdmin):
    pass


admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Reviewer, ReviewerAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Criteria, CriteriaAdmin)
admin.site.register(Expectation, ExpectationAdmin)
admin.site.register(Answer, AnswerAdmin)

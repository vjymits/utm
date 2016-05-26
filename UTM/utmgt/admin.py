from django.contrib import admin
from models import TestCases, TestRuns, TestSuites
from django.contrib.admin import AdminSite
from django.utils.translation import ugettext_lazy

import time

# Register your models here.


class TestCaseInline(admin.TabularInline):
    list_display = fields = ['testCase', 'result', 'output']
    model = TestCases
    def save_model(self, request, obj, form, change):
        if getattr(obj, 'submitter', None) is None:
            obj.submitter = request.user
        obj.created = time.time() * 1000
        obj.save()

class TestSuitesAdmin(admin.ModelAdmin):
    fields = ['name', 'description', 'reviewUri']
    list_display = ['name', 'description', 'reviewUri']
    inlines= [TestCaseInline]


    def save_model(self, request, obj, form, change):
        if getattr(obj, 'submitter', None) is None:
            obj.submitter = request.user
        obj.created = time.time() * 1000
        reportFile = obj.name+
        obj.save()

class TestCasesAdmin(admin.ModelAdmin):
    list_display = fields = ['testSuite', 'testCase']

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'submitter', None) is None:
            obj.submitter = request.user
        obj.created = time.time() * 1000
        obj.save()

class TestRunsAdmin(admin.ModelAdmin):
    #inlines = [TestCasesAdmin, TestSuitesAdmin]
    list_display = fields = ['testCase', 'result', 'description', 'attach']

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'submitter', None) is None:
            obj.submitter = request.user
        obj.created = time.time() * 1000
        obj.save()


admin.site.register(TestSuites, TestSuitesAdmin)
#admin.site.register(TestRuns, TestRunsAdmin)
#admin.site.register(TestCases, TestCasesAdmin)
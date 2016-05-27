from django.db import models
from django.contrib.auth.models import User
from util import RESULTCASES

class TestSuites(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=256, blank=True, null=True)
    reviewUri = models.URLField(max_length=256, blank=True, null=True)
    report = models.FileField(max_length=256, blank=True, null=True)
    submitter = models.ForeignKey(User, null=True, blank=True)
    created = models.BigIntegerField(blank=True, null=True)
    class Meta:
        managed = True
        db_table = 'utm_test_suites'

    def __str__(self):
        return self.name

class TestCases(models.Model):
    id = models.AutoField(primary_key=True)
    testSuite= models.ForeignKey(TestSuites, null=True, blank=True)
    result = models.CharField(max_length=10, choices=RESULTCASES, default=RESULTCASES[0][0])
    testCase = models.CharField(max_length=256, blank=True, null=True)
    output = models.FileField(blank=True, null=True)
    submitter = models.ForeignKey(User, null=True, blank=True)
    created = models.BigIntegerField(blank=True, null=True)
    class Meta:
        managed = True
        db_table = 'utm_test_cases'

    def __str__(self):
        return self.testCase

class TestRuns(models.Model):
    id = models.AutoField(primary_key=True)
    testCase = models.ForeignKey(TestCases, null=True, blank=True)
    result = models.CharField(max_length=10, choices=RESULTCASES, default=RESULTCASES[0][0])
    description = models.CharField(max_length=256, blank=True, null=True)
    attach = models.FilePathField(blank= True, null=True)
    submitter = models.ForeignKey(User, null=True, blank=True)
    created = models.BigIntegerField(blank=True, null=True)
    class Meta:
        managed = True
        db_table = 'utm_test_reports'

    def __str__(self):
        return self.testCase.testCase


# -*- coding: utf-8 -*-
#admin username: softdev
#admin password: softdev123
from __future__ import unicode_literals

from django.contrib import admin
from .models import StudentSite

# Register your models here.
class StudentSiteAdmin(admin.ModelAdmin):
	list_display = ["__unicode__","timestamp","updated_on"]
	class Meta:
		model = StudentSite

admin.site.register(StudentSite,StudentSiteAdmin)

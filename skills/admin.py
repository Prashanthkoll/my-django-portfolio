from django.contrib import admin

# Register your models here.
from skills.models import Skills
class SkillDisplay(admin.ModelAdmin):
    list_display=['id','title','point']
    ordering=['id']
admin.site.register(Skills,SkillDisplay)
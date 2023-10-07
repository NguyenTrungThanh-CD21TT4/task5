from django.contrib import admin
from first_app.models import AccessRecord,Topic,Webpage,UserModel
# Register your models here.
admin.site.register(AccessRecord)
admin.site.register(Topic)
admin.site.register(Webpage)

class MemberAdmin(admin.ModelAdmin):
    list_display = ('name','email','text')
    list_editable = ('email',)
    search_fields =('name','email','text')
admin.site.register(UserModel,MemberAdmin)
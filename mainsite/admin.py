from django.contrib import admin
from mainsite.models import Post,company,companyplace
admin.site.register(Post)

class companyadmin(admin.ModelAdmin):
    list_display = ('time','place','die','injured','car','longitude','latitude')
admin.site.register(company,companyadmin)
class Company_Place(admin.ModelAdmin):
    list_display = ('City_place','City_number')
admin.site.register(companyplace,Company_Place)
# Register your models here.

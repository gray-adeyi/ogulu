from django.contrib import admin
from . import models

admin.AdminSite.site_header = "Oluwadamilola's website administration"
admin.AdminSite.index_title = "With great power, comes great responsibility"

# Register your models here.
admin.site.register(models.Site)
admin.site.register(models.MyInformation)
admin.site.register(models.PictureCategory)
admin.site.register(models.MyImage)
admin.site.register(models.ProjectCategory)
admin.site.register(models.Project)
admin.site.register(models.ProjectImage)
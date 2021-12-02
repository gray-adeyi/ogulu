from django.contrib import admin
from django.utils.html import format_html
from . import models

admin.AdminSite.site_header = "Oluwadamilola's website administration"
admin.AdminSite.index_title = "With great power, comes great responsibility"

# Register your models here.


# Inlines
class InterestInline(admin.TabularInline):
    model = models.Interest
    extra = 1

class ServiceInline(admin.StackedInline):
    model = models.Service
    extra = 1

class SkillInline(admin.StackedInline):
    model = models.Skill
    extra = 2

class PhoneNumberInline(admin.StackedInline):
    model = models.PhoneNumber
    extra = 2

class EmailInline(admin.TabularInline):
    model = models.Email
    extra = 1

class SocialAccountInline(admin.TabularInline):
    model = models.SocialAccount
    extra = 1

class SummaryInline(admin.StackedInline):
    model = models.Summary

class EducationInline(admin.StackedInline):
    model = models.Education
    extra = 1

class ProfessionalExperienceInline(admin.StackedInline):
    model = models.ProfessionalExperience
    extra = 1

class HighlightInline(admin.StackedInline):
    model = models.Highlight
    extra = 1

class ProjectImageInline(admin.StackedInline):
    model = models.ProjectImage
    extra = 1

@admin.register(models.Site)
class SiteAdmin(admin.ModelAdmin):
    search_fields = [
        'name',
    ]

@admin.register(models.MyInformation)
class MyInformationAdmin(admin.ModelAdmin):
    autocomplete_fields = ['site',]
    search_fields = [
        'firstname',
        'lastname',
        'nickname',
    ]
    list_display = [
        'fullname',
        'nickname',
        'display_text'
    ]
    list_editable = ['display_text']

    fieldsets = (
        ("Personal Information", {"fields": (
            "lastname",
            "firstname",
            "nickname",
            "dob",
            "age",
            "bio",
            "occupation",
            "quote",
            "address",
            "city",
            "degree",
        )}),
        ("Site Configurations",{"fields":(
            "site",
            "display_text",
            "background_image",
            "about_image",
        )})
    )
    inlines = [
        InterestInline,
        ServiceInline,
        SkillInline,
        PhoneNumberInline,
        EmailInline,
        SocialAccountInline,
    ]

    def fullname(self, obj):
        return f"{obj.firstname} {obj.lastname}"


@admin.register(models.Resume)
class ResumeAdmin(admin.ModelAdmin):
    search_fields = ['info']
    autocomplete_fields = [
        'info',
        ]
    inlines = [
        SummaryInline,
        EducationInline,
        ProfessionalExperienceInline,
    ]

@admin.register(models.ProfessionalExperience)
class ProfessionalExperienceAdmin(admin.ModelAdmin):
    inlines = [
        HighlightInline,
    ]
    autocomplete_fields = [
        'resume',
        ]

@admin.register(models.ProjectCategory)
class ProjectCategoryAdmin(admin.ModelAdmin):
    search_fields = [
        'name'
    ]

@admin.register(models.Project)
class ProjectAdmin(admin.ModelAdmin):
    autocomplete_fields = ['categories']
    inlines = [
        ProjectImageInline,
    ]
    
@admin.register(models.PictureCategory)
class PictureCategoryAdmin(admin.ModelAdmin):
    search_fields = ['name']

@admin.register(models.MyImage)
class MyImageAdmin(admin.ModelAdmin):
    autocomplete_fields = [
        'info',
        'categories',
    ]
    


@admin.register(models.Transaction)
class TransactionAdmin(admin.ModelAdmin):
    pass
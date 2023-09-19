from django.contrib import admin
# Register your models here.
from .models import Education, Address, LicensesCertifications,Skills, Person, Resources, GeneralInformation

admin.site.register(Education)
admin.site.register(Address)
admin.site.register(LicensesCertifications)
admin.site.register(Person)
admin.site.register(Resources)
admin.site.register(GeneralInformation)
admin.site.register(Skills)

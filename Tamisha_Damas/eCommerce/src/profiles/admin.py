from django.contrib import admin

# Register your models here.
# since models.py is in the same folder we say from .models import class profile
from .models import profile

# to make profile model manageable through Django admin
class profileAdmin(admin.ModelAdmin):
    class Meta:
        model = profile

admin.site.register(profile, profileAdmin)

from django.contrib import admin
from .models import organization, user, shoutout


admin.site.register(organization)
admin.site.register(user)
admin.site.register(shoutout)

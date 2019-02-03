from django.contrib import admin
from .models import User, Track
from django.contrib.auth.admin import UserAdmin
from audiofield.admin import AudioFileAdmin



admin.site.register(User, UserAdmin)
admin.site.register(Track, AudioFileAdmin)



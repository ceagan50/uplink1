from django.contrib import admin
from .models import Sermon, Event, ContactMessage


admin.site.register(Sermon)
admin.site.register(Event)
admin.site.register(ContactMessage)

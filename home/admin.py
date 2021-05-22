from django.contrib import admin
from .models import Contact
from .models import Feedback
from .models import Resources

# Register your models here.
admin.site.register(Contact)
admin.site.register(Feedback)
admin.site.register(Resources)

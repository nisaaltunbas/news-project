from django.contrib import admin
from .models import Articles,Author,Category,Comments

# Register your models here.
admin.site.register(Articles)
admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Comments)

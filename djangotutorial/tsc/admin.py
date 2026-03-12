from django.contrib import admin

from .models import Scene, Object

class ObjectInline(admin.TabularInline):
    model = Object
    extra = 3


class SceneAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["scene_id", "scene_description"]}),
    ]
    inlines = [ObjectInline]

admin.site.register(Scene, SceneAdmin)

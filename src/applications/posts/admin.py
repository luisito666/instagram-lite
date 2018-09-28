from django.contrib import admin

# Register your models here.
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):

    list_display = ('title', 'photo')
    readonly_fields = ('created', 'modified')
    fieldsets = (
        ('Post', {
            "fields": (
                ('title', 'photo'),
            ),
        }),
        ('Metadata', {
            "fields": (
                ('created', 'modified'),
            )
        })
    )
    list_filter = (
        'created', 
        'modified',
    )


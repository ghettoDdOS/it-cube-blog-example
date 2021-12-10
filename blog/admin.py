from django.contrib import admin

from .models import News


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    """Админка новостей"""

    list_display = [
        "title",
        "date_of_publication",
    ]

from django.contrib import admin

from .models import Users
from .models import Requests
from .models import Notify


@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    list_display = ('id', 'tg_id', 'username',
                    'descrtext', 'first_token', 'token_requests_count')


@admin.register(Requests)
class RequestsAdmin(admin.ModelAdmin):
    list_display = ('id', 'tg_id', 'ts', 'request_text')


@admin.register(Notify)
class NotifyAdmin(admin.ModelAdmin):
    list_display = ('id', 'tg_id', 'notify_text', 'sended')
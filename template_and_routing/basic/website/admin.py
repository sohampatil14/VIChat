from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from .models import connection
from .models import Account
from .models import UserConnection
from .models import ChatHistory

# Register your models here.

admin.site.register(connection)
# admin.site.register(user)


class AccountInLine(admin.StackedInline):
    model = Account
    can_delete = False
    verbose_name_plural = 'Accounts'


class CustomizedUserAdmin(UserAdmin):
    inlines = (AccountInLine, )


admin.site.unregister(User)
admin.site.register(UserConnection)
admin.site.register(ChatHistory)
admin.site.register(User, CustomizedUserAdmin)

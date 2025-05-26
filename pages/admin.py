from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, Songs, News, Gallery, Links, Documents, Set, SetList, Dances



class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = [
        "email",
        "username",
        "is_staff",
        "is_active",
    ]
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Songs)
admin.site.register(News)
admin.site.register(Gallery)
admin.site.register(Links)
admin.site.register(Documents)
admin.site.register(Set)
admin.site.register(SetList)
admin.site.register(Dances)
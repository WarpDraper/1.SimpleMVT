from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model

User = get_user_model()

class CustomUserAdmin(UserAdmin):
    # обмежимо список, кого бачить користувач
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        # звичайні менеджери бачать тільки себе
        return qs.filter(id=request.user.id)

    # дозволимо додавати користувачів тільки тим, хто має дозвіл
    def has_add_permission(self, request):
        return request.user.has_perm('auth.add_user')

admin.site.register(User, CustomUserAdmin)

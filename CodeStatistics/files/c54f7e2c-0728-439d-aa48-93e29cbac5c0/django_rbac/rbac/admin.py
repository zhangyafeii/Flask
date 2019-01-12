from django.contrib import admin
from rbac.models import *


admin.site.register(UserInfo)
admin.site.register(Role)
admin.site.register(UserinfoToRole)
admin.site.register(Permission)
admin.site.register(Action)
admin.site.register(PermissionToAction)
admin.site.register(RoleToPremissionToAction)
admin.site.register(Menu)

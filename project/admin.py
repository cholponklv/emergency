from django.contrib import admin
from .models import Project, Team, MemberTeam,Photo
# Register your models here.
admin.site.register(Project)
admin.site.register(Team)
admin.site.register(MemberTeam)
admin.site.register(Photo)

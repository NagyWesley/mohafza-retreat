from django.contrib import admin

# Register your models here.


from .models import Match, Member, Team,Game,Room

admin.site.register(Match)
admin.site.register(Member)
admin.site.register(Team)
admin.site.register(Game)
admin.site.register(Room)

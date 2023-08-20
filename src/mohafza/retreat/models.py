from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Room(models.Model):
    id = models.IntegerField(primary_key=True)
    number = models.CharField(max_length=20,db_index=True)

    def __str__(self):
        return self.number

class Team(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20,db_index=True)

    def __str__(self):
        return self.name

class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room,on_delete=models.DO_NOTHING,blank=True,null=True)
    team_leading = models.ForeignKey(Team,on_delete=models.DO_NOTHING, related_name="leaders", blank=True,null=True)
    team_membership = models.ForeignKey(Team,on_delete=models.DO_NOTHING, related_name="members",blank=True,null=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"

class Game(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20,db_index=True)
    rules = models.CharField(max_length=100)
    can_draw=models.BooleanField("can game end in draw?",default=False)
    win_points=models.IntegerField(default=0)
    draw_points=models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Match(models.Model):
    id = models.IntegerField(primary_key=True)
    game = models.ForeignKey(Game,on_delete=models.CASCADE)
    teams = models.ManyToManyField(Team)
    is_draw = models.BooleanField(default=False)
    winner = models.ForeignKey(Team,on_delete=models.DO_NOTHING, related_name="winner")

    def __str__(self):
        return f"{self.game}:"



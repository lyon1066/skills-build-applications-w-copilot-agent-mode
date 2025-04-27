from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from django.conf import settings
from pymongo import MongoClient
from datetime import timedelta
from bson import ObjectId

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activity, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        # Connect to MongoDB
        client = MongoClient(settings.DATABASES['default']['CLIENT']['host'], settings.DATABASES['default']['CLIENT']['port'])
        db = client[settings.DATABASES['default']['NAME']]

        # Drop existing collections
        db.users.drop()
        db.teams.drop()
        db.activity.drop()
        db.leaderboard.drop()
        db.workouts.drop()

        # Create users
        users = [
            User(_id=ObjectId(), email='thundergod@mhigh.edu', name='thundergod', password='thundergodpassword'),
            User(_id=ObjectId(), email='metalgeek@mhigh.edu', name='metalgeek', password='metalgeekpassword'),
            User(_id=ObjectId(), email='zerocool@mhigh.edu', name='zerocool', password='zerocoolpassword'),
            User(_id=ObjectId(), email='crashoverride@hmhigh.edu', name='crashoverride', password='crashoverridepassword'),
            User(_id=ObjectId(), email='sleeptoken@mhigh.edu', name='sleeptoken', password='sleeptokenpassword'),
        ]
        User.objects.bulk_create(users)

        # Create teams
        blue_team = Team(_id=ObjectId(), name='Blue Team')
        gold_team = Team(_id=ObjectId(), name='Gold Team')
        blue_team.save()
        gold_team.save()
        for user in users:
            blue_team.members.add(user)
            gold_team.members.add(user)

        # Create activities
        activities = [
            Activity(_id=ObjectId(), user=users[0], activity_type='Cycling', duration=60, date=None, points=10),
            Activity(_id=ObjectId(), user=users[1], activity_type='Crossfit', duration=120, date=None, points=20),
            Activity(_id=ObjectId(), user=users[2], activity_type='Running', duration=90, date=None, points=15),
            Activity(_id=ObjectId(), user=users[3], activity_type='Strength', duration=30, date=None, points=5),
            Activity(_id=ObjectId(), user=users[4], activity_type='Swimming', duration=75, date=None, points=12),
        ]
        Activity.objects.bulk_create(activities)

        # Create leaderboard entries
        leaderboard_entries = [
            Leaderboard(_id=ObjectId(), team=blue_team, score=100),
            Leaderboard(_id=ObjectId(), team=gold_team, score=90),
        ]
        Leaderboard.objects.bulk_create(leaderboard_entries)

        # Create workouts
        workouts = [
            Workout(_id=ObjectId(), user=users[0], workout_type='Cycling Training', details={'description': 'Training for a road cycling event'}, date=None),
            Workout(_id=ObjectId(), user=users[1], workout_type='Crossfit', details={'description': 'Training for a crossfit competition'}, date=None),
            Workout(_id=ObjectId(), user=users[2], workout_type='Running Training', details={'description': 'Training for a marathon'}, date=None),
            Workout(_id=ObjectId(), user=users[3], workout_type='Strength Training', details={'description': 'Training for strength'}, date=None),
            Workout(_id=ObjectId(), user=users[4], workout_type='Swimming Training', details={'description': 'Training for a swimming competition'}, date=None),
        ]
        Workout.objects.bulk_create(workouts)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))

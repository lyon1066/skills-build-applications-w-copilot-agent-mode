from django.core.management.base import BaseCommand
from django.conf import settings
from pymongo import MongoClient
from bson import ObjectId
from datetime import datetime

class Command(BaseCommand):
    help = 'Directly populate the octofit_db MongoDB database with test data for users, teams, activities, leaderboard, and workouts.'

    def handle(self, *args, **kwargs):
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
            {'_id': ObjectId(), 'email': 'thundergod@mhigh.edu', 'name': 'thundergod', 'password': 'thundergodpassword'},
            {'_id': ObjectId(), 'email': 'metalgeek@mhigh.edu', 'name': 'metalgeek', 'password': 'metalgeekpassword'},
            {'_id': ObjectId(), 'email': 'zerocool@mhigh.edu', 'name': 'zerocool', 'password': 'zerocoolpassword'},
            {'_id': ObjectId(), 'email': 'crashoverride@hmhigh.edu', 'name': 'crashoverride', 'password': 'crashoverridepassword'},
            {'_id': ObjectId(), 'email': 'sleeptoken@mhigh.edu', 'name': 'sleeptoken', 'password': 'sleeptokenpassword'},
        ]
        db.users.insert_many(users)

        # Create teams (each team has all users as members)
        team_ids = [ObjectId(), ObjectId()]
        teams = [
            {'_id': team_ids[0], 'name': 'Blue Team', 'members': [u['_id'] for u in users]},
            {'_id': team_ids[1], 'name': 'Gold Team', 'members': [u['_id'] for u in users]},
        ]
        db.teams.insert_many(teams)

        # Create activities
        activities = [
            {'_id': ObjectId(), 'user': users[0]['_id'], 'activity_type': 'Cycling', 'duration': 60, 'date': datetime.utcnow(), 'points': 10},
            {'_id': ObjectId(), 'user': users[1]['_id'], 'activity_type': 'Crossfit', 'duration': 120, 'date': datetime.utcnow(), 'points': 20},
            {'_id': ObjectId(), 'user': users[2]['_id'], 'activity_type': 'Running', 'duration': 90, 'date': datetime.utcnow(), 'points': 15},
            {'_id': ObjectId(), 'user': users[3]['_id'], 'activity_type': 'Strength', 'duration': 30, 'date': datetime.utcnow(), 'points': 5},
            {'_id': ObjectId(), 'user': users[4]['_id'], 'activity_type': 'Swimming', 'duration': 75, 'date': datetime.utcnow(), 'points': 12},
        ]
        db.activity.insert_many(activities)

        # Create leaderboard entries (one per team)
        leaderboard = [
            {'_id': ObjectId(), 'team': team_ids[0], 'score': 100},
            {'_id': ObjectId(), 'team': team_ids[1], 'score': 90},
        ]
        db.leaderboard.insert_many(leaderboard)

        # Create workouts (one per user)
        workouts = [
            {'_id': ObjectId(), 'user': users[0]['_id'], 'workout_type': 'Cycling Training', 'details': {'description': 'Training for a road cycling event'}, 'date': datetime.utcnow()},
            {'_id': ObjectId(), 'user': users[1]['_id'], 'workout_type': 'Crossfit', 'details': {'description': 'Training for a crossfit competition'}, 'date': datetime.utcnow()},
            {'_id': ObjectId(), 'user': users[2]['_id'], 'workout_type': 'Running Training', 'details': {'description': 'Training for a marathon'}, 'date': datetime.utcnow()},
            {'_id': ObjectId(), 'user': users[3]['_id'], 'workout_type': 'Strength Training', 'details': {'description': 'Training for strength'}, 'date': datetime.utcnow()},
            {'_id': ObjectId(), 'user': users[4]['_id'], 'workout_type': 'Swimming Training', 'details': {'description': 'Training for a swimming competition'}, 'date': datetime.utcnow()},
        ]
        db.workouts.insert_many(workouts)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data using PyMongo.'))

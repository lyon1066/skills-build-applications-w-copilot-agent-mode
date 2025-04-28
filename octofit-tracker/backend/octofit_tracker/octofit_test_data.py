# Test data for OctoFit Tracker (Mergington High School)
# This file is for reference only. Actual population is done via the management command.

TEST_USERS = [
    dict(username='thundergod', email='thundergod@mhigh.edu', password='thundergodpassword'),
    dict(username='metalgeek', email='metalgeek@mhigh.edu', password='metalgeekpassword'),
    dict(username='zerocool', email='zerocool@mhigh.edu', password='zerocoolpassword'),
    dict(username='crashoverride', email='crashoverride@hmhigh.edu', password='crashoverridepassword'),
    dict(username='sleeptoken', email='sleeptoken@mhigh.edu', password='sleeptokenpassword'),
]

TEST_TEAMS = [
    dict(name='Blue Team'),
    dict(name='Gold Team'),
]

TEST_ACTIVITIES = [
    dict(activity_type='Cycling', duration=60),
    dict(activity_type='Crossfit', duration=120),
    dict(activity_type='Running', duration=90),
    dict(activity_type='Strength', duration=30),
    dict(activity_type='Swimming', duration=75),
]

TEST_LEADERBOARD = [
    dict(score=100),
    dict(score=90),
    dict(score=95),
    dict(score=85),
    dict(score=80),
]

TEST_WORKOUTS = [
    dict(name='Cycling Training', description='Training for a road cycling event'),
    dict(name='Crossfit', description='Training for a crossfit competition'),
    dict(name='Running Training', description='Training for a marathon'),
    dict(name='Strength Training', description='Training for strength'),
    dict(name='Swimming Training', description='Training for a swimming competition'),
]

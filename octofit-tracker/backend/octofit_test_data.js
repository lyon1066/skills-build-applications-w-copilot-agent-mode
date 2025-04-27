use octofit_db

db.users.insertMany([
  { email: 'thundergod@mhigh.edu', name: 'thundergod', password: 'thundergodpassword' },
  { email: 'metalgeek@mhigh.edu', name: 'metalgeek', password: 'metalgeekpassword' },
  { email: 'zerocool@mhigh.edu', name: 'zerocool', password: 'zerocoolpassword' },
  { email: 'crashoverride@hmhigh.edu', name: 'crashoverride', password: 'crashoverridepassword' },
  { email: 'sleeptoken@mhigh.edu', name: 'sleeptoken', password: 'sleeptokenpassword' }
]);

db.teams.insertMany([
  { name: 'Blue Team', members: [ 'thundergod@mhigh.edu', 'metalgeek@mhigh.edu', 'zerocool@mhigh.edu', 'crashoverride@hmhigh.edu', 'sleeptoken@mhigh.edu' ] },
  { name: 'Gold Team', members: [ 'thundergod@mhigh.edu', 'metalgeek@mhigh.edu', 'zerocool@mhigh.edu', 'crashoverride@hmhigh.edu', 'sleeptoken@mhigh.edu' ] }
]);

db.activity.insertMany([
  { user: 'thundergod@mhigh.edu', activity_type: 'Cycling', duration: 60, points: 10 },
  { user: 'metalgeek@mhigh.edu', activity_type: 'Crossfit', duration: 120, points: 20 },
  { user: 'zerocool@mhigh.edu', activity_type: 'Running', duration: 90, points: 15 },
  { user: 'crashoverride@hmhigh.edu', activity_type: 'Strength', duration: 30, points: 5 },
  { user: 'sleeptoken@mhigh.edu', activity_type: 'Swimming', duration: 75, points: 12 }
]);

db.leaderboard.insertMany([
  { team: 'Blue Team', score: 100 },
  { team: 'Gold Team', score: 90 }
]);

db.workouts.insertMany([
  { user: 'thundergod@mhigh.edu', workout_type: 'Cycling Training', details: { description: 'Training for a road cycling event' } },
  { user: 'metalgeek@mhigh.edu', workout_type: 'Crossfit', details: { description: 'Training for a crossfit competition' } },
  { user: 'zerocool@mhigh.edu', workout_type: 'Running Training', details: { description: 'Training for a marathon' } },
  { user: 'crashoverride@hmhigh.edu', workout_type: 'Strength Training', details: { description: 'Training for strength' } },
  { user: 'sleeptoken@mhigh.edu', workout_type: 'Swimming Training', details: { description: 'Training for a swimming competition' } }
]);

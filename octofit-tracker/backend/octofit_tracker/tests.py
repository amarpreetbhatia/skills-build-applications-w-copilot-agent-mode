from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class UserTest(TestCase):
    def test_user_creation(self):
        user = User.objects.create(username="testuser", email="testuser@example.com")
        self.assertEqual(user.username, "testuser")
        self.assertEqual(user.email, "testuser@example.com")

class TeamTest(TestCase):
    def test_team_creation(self):
        team = Team.objects.create(name="Test Team")
        self.assertEqual(team.name, "Test Team")

class ActivityTest(TestCase):
    def test_activity_creation(self):
        activity = Activity.objects.create(name="Running", duration=30)
        self.assertEqual(activity.name, "Running")
        self.assertEqual(activity.duration, 30)

class LeaderboardTest(TestCase):
    def test_leaderboard_creation(self):
        leaderboard = Leaderboard.objects.create(rank=1, score=100)
        self.assertEqual(leaderboard.rank, 1)
        self.assertEqual(leaderboard.score, 100)

class WorkoutTest(TestCase):
    def test_workout_creation(self):
        workout = Workout.objects.create(name="Morning Workout", calories_burned=200)
        self.assertEqual(workout.name, "Morning Workout")
        self.assertEqual(workout.calories_burned, 200)

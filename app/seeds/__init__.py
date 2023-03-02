from flask.cli import AppGroup
from .users import seed_users, undo_users
from .courts import seed_courts, undo_courts
from .members import seed_members, undo_members
from .parks import seed_parks, undo_parks
from .games import seed_games, undo_games
from .teams import seed_teams, undo_teams
from .userTeams import seed_user_teams, undo_user_teams
from .queues import seed_queues, undo_queues

from app.models.db import db, environment, SCHEMA

# Creates a seed group to hold our commands
# So we can type `flask seed --help`
seed_commands = AppGroup('seed')


# Creates the `flask seed all` command
@seed_commands.command('all')
def seed():
    if environment == 'production':
        # Before seeding in production, you want to run the seed undo
        # command, which will  truncate all tables prefixed with
        # the schema name (see comment in users.py undo_users function).
        # Make sure to add all your other model's undo functions below
        undo_users()
        undo_parks()
        undo_members()
        undo_courts()
        undo_games()
        undo_teams()
        undo_user_teams()
        undo_queues()
    seed_users()
    seed_parks()
    seed_members()
    seed_courts()
    seed_games()
    seed_teams()
    seed_user_teams()
    seed_queues()

    # Add other seed functions here


# Creates the `flask seed undo` command
@seed_commands.command('undo')
def undo():
    undo_queues()
    undo_user_teams()
    undo_teams()
    undo_games()
    undo_courts()
    undo_members()
    undo_parks()
    undo_users()

    # Add other undo functions here

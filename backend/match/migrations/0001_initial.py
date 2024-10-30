# Generated by Django 5.0.3 on 2024-10-30 11:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("team", "0001_initial"),
        ("tournament", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Match",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date", models.DateField()),
                ("score_team1", models.IntegerField(blank=True, null=True)),
                ("score_team2", models.IntegerField(blank=True, null=True)),
                ("deciding_factor", models.FloatField(blank=True, null=True)),
                ("is_finished", models.BooleanField(default=False)),
                ("is_tie", models.BooleanField(default=False)),
                (
                    "team1",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="home_matches",
                        to="team.team",
                    ),
                ),
                (
                    "team2",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="away_matches",
                        to="team.team",
                    ),
                ),
                (
                    "tournament",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="matches",
                        to="tournament.tournament",
                    ),
                ),
            ],
        ),
    ]
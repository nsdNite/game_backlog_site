# Generated by Django 4.2.7 on 2023-12-14 17:34

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("backlog", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="developer",
            options={"ordering": ["id"]},
        ),
        migrations.RemoveField(
            model_name="game",
            name="developer",
        ),
        migrations.RemoveField(
            model_name="game",
            name="image",
        ),
        migrations.AddField(
            model_name="game",
            name="added_to_backlog_at",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="game",
            name="developers",
            field=models.ManyToManyField(related_name="games", to="backlog.developer"),
        ),
        migrations.AlterField(
            model_name="game",
            name="description",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="game",
            name="meta_score",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="game",
            name="release_date",
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="game",
            name="title",
            field=models.CharField(max_length=255),
        ),
    ]
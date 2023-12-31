# Generated by Django 4.2.6 on 2023-10-25 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("saving_app", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="savingsaccount",
            name="account_holder_name",
        ),
        migrations.RemoveField(
            model_name="savingsaccount",
            name="created_at",
        ),
        migrations.RemoveField(
            model_name="savingsaccount",
            name="interest_rate",
        ),
        migrations.RemoveField(
            model_name="savingsaccount",
            name="last_transaction_at",
        ),
        migrations.AddField(
            model_name="savingsaccount",
            name="user",
            field=models.CharField(default="default user", max_length=50),
        ),
        migrations.AlterField(
            model_name="savingsaccount",
            name="account_number",
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name="savingsaccount",
            name="balance",
            field=models.FloatField(default=0),
        ),
    ]

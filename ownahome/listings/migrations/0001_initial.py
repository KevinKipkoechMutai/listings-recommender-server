# Generated by Django 4.2.16 on 2024-11-25 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=100)),
                ('price_cash', models.DecimalField(decimal_places=2, max_digits=15)),
                ('price_mortgage', models.DecimalField(decimal_places=2, max_digits=15)),
                ('development_status', models.CharField(choices=[('completed', 'Completed'), ('under_construction', 'Under Construction'), ('offplan', 'Off-plan')], max_length=20)),
                ('description', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('salary', models.DecimalField(decimal_places=2, max_digits=10)),
                ('existing_loans', models.DecimalField(decimal_places=2, max_digits=10)),
                ('savings', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
            ],
        ),
    ]

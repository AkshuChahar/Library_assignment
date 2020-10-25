# Generated by Django 3.1.2 on 2020-10-25 17:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(max_length=200, verbose_name='Book')),
                ('author', models.CharField(max_length=200, verbose_name='Author')),
                ('isbn', models.CharField(max_length=13, verbose_name='ISBN')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=200, verbose_name='Last Name')),
                ('mobile', models.CharField(max_length=10, verbose_name='Mobile')),
                ('address', models.CharField(max_length=400, verbose_name='Address')),
                ('joined_on', models.DateField()),
                ('book_issued', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.book')),
            ],
        ),
        migrations.CreateModel(
            name='BookInstance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('issued', models.DateField(blank=True, null=True)),
                ('due_date', models.DateField(blank=True, null=True)),
                ('book', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.book')),
                ('borrower', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.student')),
            ],
            options={
                'ordering': ['issued', 'due_date'],
                'permissions': [('can_mark_issued', 'Set book as issued'), ('can_mark_returned', 'Set book as returned')],
            },
        ),
    ]
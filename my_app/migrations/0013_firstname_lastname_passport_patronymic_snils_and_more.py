# Generated by Django 4.2 on 2023-04-09 14:08

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import my_app.models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0012_alter_user_options_alter_user_managers_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='FirstName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nominative', my_app.models.CyrillicCharField(max_length=16)),
                ('genitive', my_app.models.CyrillicCharField(max_length=16)),
                ('dative', my_app.models.CyrillicCharField(max_length=16)),
                ('accusative', my_app.models.CyrillicCharField(max_length=16)),
                ('instrumental', my_app.models.CyrillicCharField(max_length=16)),
                ('prepositional', my_app.models.CyrillicCharField(max_length=16)),
                ('latin', models.CharField(max_length=16)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='LastName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nominative', my_app.models.CyrillicCharField(max_length=16)),
                ('genitive', my_app.models.CyrillicCharField(max_length=16)),
                ('dative', my_app.models.CyrillicCharField(max_length=16)),
                ('accusative', my_app.models.CyrillicCharField(max_length=16)),
                ('instrumental', my_app.models.CyrillicCharField(max_length=16)),
                ('prepositional', my_app.models.CyrillicCharField(max_length=16)),
                ('latin', models.CharField(max_length=16)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Passport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('series', models.CharField(max_length=4, validators=[django.core.validators.RegexValidator(message='Серия паспорта должна состоять из 4 цифр', regex='^\\d{4}$')])),
                ('number', models.CharField(max_length=6, validators=[django.core.validators.RegexValidator(message='Номер паспорта должен состоять из 6 цифр', regex='^\\d{6}$')])),
                ('issued_date', models.DateField()),
                ('issued_by', models.CharField(max_length=64, validators=[django.core.validators.RegexValidator(message='Некорректное значение', regex='^[А-Яа-я\\s\\d.,/-]+$')])),
                ('department_code', models.CharField(max_length=7, validators=[django.core.validators.RegexValidator(message='Код подразделения должен иметь формат XXX-XXX', regex='^\\d{3}-\\d{3}$')])),
                ('is_valid', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Patronymic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nominative', my_app.models.CyrillicCharField(max_length=16)),
                ('genitive', my_app.models.CyrillicCharField(max_length=16)),
                ('dative', my_app.models.CyrillicCharField(max_length=16)),
                ('accusative', my_app.models.CyrillicCharField(max_length=16)),
                ('instrumental', my_app.models.CyrillicCharField(max_length=16)),
                ('prepositional', my_app.models.CyrillicCharField(max_length=16)),
                ('latin', models.CharField(max_length=16)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Snils',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=14, validators=[django.core.validators.RegexValidator(message='Номер СНИЛС должен иметь формат XXX-XXX-XXX XX', regex='^\\d{3}-\\d{3}-\\d{3} \\d{2}$')])),
            ],
        ),
        migrations.AlterField(
            model_name='role',
            name='role',
            field=models.CharField(max_length=16),
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(error_messages={'invalid': 'Недопустимый адрес'}, max_length=32)),
                ('phone_number', models.CharField(max_length=12, validators=[django.core.validators.RegexValidator(message='Номер телефона должен быть в формате "+7XXXXXXXXXX"', regex='^\\+7\\d{10}$')])),
                ('birthday', models.DateField()),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='my_app.firstname')),
                ('passport', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='my_app.passport')),
                ('patronymic', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='my_app.patronymic')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='my_app.role')),
                ('snils', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='my_app.snils')),
                ('surname', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='my_app.lastname')),
            ],
        ),
    ]
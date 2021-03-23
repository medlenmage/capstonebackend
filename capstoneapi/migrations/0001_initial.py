# Generated by Django 3.1.7 on 2021-03-23 00:20

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Benefits',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('health_ins', models.CharField(max_length=30)),
                ('dental_ins', models.CharField(max_length=30)),
                ('life_ins', models.CharField(max_length=30)),
                ('vacation_days', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('sick_days', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
            ],
        ),
        migrations.CreateModel(
            name='CompanyContact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=30)),
                ('contact_name', models.CharField(max_length=30)),
                ('contact_phone_number', models.CharField(max_length=30)),
                ('contact_email', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Curriculum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('permit_lessons', models.CharField(max_length=50)),
                ('driving_course', models.CharField(max_length=50)),
                ('backing_course', models.CharField(max_length=50)),
                ('pretrip_test', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='DirectDeposit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.DateTimeField(editable=False, null=True)),
                ('account_number', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('routing_number', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('bank_name', models.CharField(max_length=25)),
                ('account_name', models.CharField(max_length=25)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_admin', models.BooleanField(default=False)),
                ('benefits_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='capstoneapi.benefits')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('equipment_type', models.CharField(max_length=30)),
                ('is_available', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Grouping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instructor', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='capstoneapi.employee')),
            ],
        ),
        migrations.CreateModel(
            name='PaymentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.DateTimeField(editable=False, null=True)),
                ('account_number', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('routing_number', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('bank_name', models.CharField(max_length=25)),
                ('payment_name', models.CharField(max_length=25)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balance', models.IntegerField(default=4800, validators=[django.core.validators.MinValueValidator(0)])),
                ('application_status', models.BooleanField(default=False)),
                ('payment_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='capstoneapi.paymenttype')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('curriculum_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='capstoneapi.curriculum')),
                ('employee_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='capstoneapi.employee')),
                ('equipment_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='capstoneapi.equipment')),
                ('grouping_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='capstoneapi.grouping')),
            ],
        ),
        migrations.CreateModel(
            name='Paystub',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.DateTimeField(editable=False, null=True)),
                ('salary', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('pay_period', models.DateField(default='0000-00-00')),
                ('deposit_date', models.DateField(default='0000-00-00')),
                ('deposit_account', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='capstoneapi.directdeposit')),
                ('employee_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='capstoneapi.employee')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='grouping',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='groupings', to='capstoneapi.student'),
        ),
        migrations.AddField(
            model_name='directdeposit',
            name='employee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='direct_deposit', to='capstoneapi.employee'),
        ),
    ]

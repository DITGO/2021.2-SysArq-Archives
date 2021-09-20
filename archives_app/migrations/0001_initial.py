import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BoxAbbreviations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(blank=True)),
                ('abbreviation', models.CharField(blank=True, max_length=20)),
                ('name', models.CharField(blank=True, max_length=100)),
                ('year', models.IntegerField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('process_number', models.CharField(max_length=20)),
                ('notes', models.CharField(blank=True, max_length=300, null=True)),
                ('filer_user', models.CharField(max_length=150)),
                ('abbreviation_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='archives_app.boxabbreviations')),
            ],
        ),
        migrations.CreateModel(
            name='DocumentSubject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_name', models.CharField(blank=True, max_length=100)),
                ('temporality', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='DocumentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document_name', models.CharField(blank=True, max_length=100)),
                ('temporality', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='FrontCover',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('box_abbreviation', models.CharField(blank=True, max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='OriginBoxSubject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('dates', django.contrib.postgres.fields.ArrayField(base_field=models.DateField(), size=None)),
            ],
        ),
        migrations.CreateModel(
            name='PublicWorker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100)),
                ('cpf', models.CharField(blank=True, max_length=11)),
                ('office', models.CharField(blank=True, max_length=100)),
                ('class_worker', models.CharField(blank=True, max_length=100)),
                ('capacity', models.CharField(blank=True, max_length=100)),
                ('county', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Shelf',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shelfe_number', models.IntegerField(blank=True)),
                ('shelfp_number', models.IntegerField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_filed', models.BooleanField(blank=True)),
                ('eliminated', models.BooleanField(blank=True)),
                ('sent_from', models.CharField(blank=True, max_length=100)),
                ('requested_document', models.CharField(blank=True, max_length=100)),
                ('send_date', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Unity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unity_name', models.CharField(blank=True, max_length=100)),
                ('unity_abbreviation', models.CharField(blank=True, max_length=20)),
                ('administrative_bond', models.CharField(blank=True, max_length=100)),
                ('bond_abbreviation', models.CharField(blank=True, max_length=20)),
                ('type_of_unity', models.CharField(blank=True, max_length=30)),
                ('municipality', models.CharField(blank=True, max_length=100)),
                ('telephone_number', models.CharField(blank=True, max_length=11)),
                ('notes', models.CharField(blank=True, max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Relation',
            fields=[
                ('document_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='archives_app.document')),
                ('number', models.CharField(max_length=20)),
                ('received_date', models.DateField()),
                ('document_type_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='archives_app.documenttype')),
            ],
            bases=('archives_app.document',),
        ),
        migrations.CreateModel(
            name='OriginBox',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=20)),
                ('year', models.IntegerField()),
                ('subject', models.ManyToManyField(to='archives_app.OriginBoxSubject')),
            ],
        ),
        migrations.CreateModel(
            name='FrequencySheet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('person_name', models.CharField(max_length=150)),
                ('cpf', models.CharField(max_length=11)),
                ('role', models.CharField(max_length=100)),
                ('category', models.CharField(blank=True, max_length=100, null=True)),
                ('workplace', models.CharField(max_length=100)),
                ('municipal_area', models.CharField(max_length=100)),
                ('reference_period', django.contrib.postgres.fields.ArrayField(base_field=models.DateField(), size=None)),
                ('notes', models.CharField(blank=True, max_length=300, null=True)),
                ('process_number', models.CharField(blank=True, max_length=20, null=True)),
                ('abbreviation_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='archives_app.boxabbreviations')),
                ('shelf_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='archives_app.shelf')),
            ],
        ),
        migrations.AddField(
            model_name='document',
            name='sender_unity',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='archives_app.unity'),
        ),
        migrations.AddField(
            model_name='document',
            name='shelf_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='archives_app.shelf'),
        ),
        migrations.CreateModel(
            name='FrequencyRelation',
            fields=[
                ('relation_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='archives_app.relation')),
                ('reference_period', django.contrib.postgres.fields.ArrayField(base_field=models.DateField(), size=None)),
            ],
            bases=('archives_app.relation',),
        ),
        migrations.CreateModel(
            name='AdministrativeProcess',
            fields=[
                ('document_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='archives_app.document')),
                ('notice_date', models.DateField()),
                ('interested', models.CharField(max_length=150)),
                ('cpf_cnpj', models.CharField(blank=True, max_length=15, null=True)),
                ('reference_month_year', models.DateField(blank=True, null=True)),
                ('sender_user', models.CharField(blank=True, max_length=150, null=True)),
                ('archiving_date', models.DateField(blank=True, null=True)),
                ('dest_unity_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='archives_app.unity')),
                ('status_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='archives_app.status')),
                ('subject_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='archives_app.documentsubject')),
            ],
            bases=('archives_app.document',),
        ),
        migrations.CreateModel(
            name='ArchivalRelation',
            fields=[
                ('relation_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='archives_app.relation')),
                ('number_of_boxes', models.IntegerField(blank=True, null=True)),
                ('document_url', models.URLField(blank=True, null=True)),
                ('cover_sheet', models.CharField(blank=True, max_length=100, null=True)),
                ('origin_box_id', models.ManyToManyField(to='archives_app.OriginBox')),
            ],
            bases=('archives_app.relation',),
        ),
    ]

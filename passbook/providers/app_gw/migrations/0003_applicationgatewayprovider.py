# Generated by Django 2.2.7 on 2019-11-11 17:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('passbook_core', '0005_merge_20191025_2022'),
        ('oidc_provider', '0026_client_multiple_response_types'),
        ('passbook_providers_app_gw', '0002_auto_20191111_1703'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApplicationGatewayProvider',
            fields=[
                ('provider_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='passbook_core.Provider')),
                ('name', models.TextField()),
                ('host', models.TextField()),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='oidc_provider.Client')),
            ],
            options={
                'verbose_name': 'Application Gateway Provider',
                'verbose_name_plural': 'Application Gateway Providers',
            },
            bases=('passbook_core.provider',),
        ),
    ]

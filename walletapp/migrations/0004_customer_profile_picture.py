# Generated by Django 4.0.6 on 2022-08-02 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('walletapp', '0003_card_cardstatus_card_pin_card_signature'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='profile_picture',
            field=models.ImageField(default='default.jpg', upload_to='profile_pics'),
        ),
    ]

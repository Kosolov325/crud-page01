# Generated by Django 4.0.3 on 2022-03-26 23:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='photo',
            field=models.ImageField(default='https://cdn.motor1.com/images/mgl/2gwok/s3/mercedes-benz-e-300-exclusive.jpg', upload_to='assets', verbose_name='foto'),
        ),
        migrations.AlterField(
            model_name='car',
            name='marca',
            field=models.CharField(choices=[('Nizan', 'Nizan'), ('Wolkswaggen', 'Wolkswaggen'), ('Forde', 'Forde'), ('Macetes-Bens', 'Macetes-Bens'), ('Seburu', 'Seburu'), ('Heundie', 'Heundie'), ('Fito', 'Fito'), ('Cheyvroule', 'Cheyvroule')], default=('Macetes-Bens', 'Macetes-Bens'), max_length=50, verbose_name='Marca'),
        ),
    ]

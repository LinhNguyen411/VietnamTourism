from django.contrib.postgres.operations import UnaccentExtension
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_category_rename_description_region_introduction_and_more'),
    ]

    operations = [
        UnaccentExtension()
    ]
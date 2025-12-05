# blog/migrations/0004_alter_post_tags.py

from django.db import migrations

def remove_tags(apps, schema_editor):
    # Custom logic to handle tags or remove previous erroneous migrations
    pass

class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20230922_1234'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='tags',
        ),
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(to='taggit.Tag'),
        ),
    ]

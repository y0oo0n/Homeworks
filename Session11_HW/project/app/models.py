from django.db import migrations, models
from django.contrib.auth.models import User


class Migration(migrations.Migration):

    dependencies = [
        ('invests', '0001_xxxxxx'),
    ]

    operations = [
        migrations.AddField(
            model_name='invest',
            name='ref_id',
            field=models.CharField(default='', max_length=255, null=True),
        ),
    ]

# Create your models here.
class Song(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(User, models.CASCADE, related_name="songs")

    def __str__(self):
        return self.title

class Comment(models.Model):
    song = models.ForeignKey(Song, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    author = models.ForeignKey(User, models.CASCADE, related_name="comments")

    def __str__(self):
        return self.content
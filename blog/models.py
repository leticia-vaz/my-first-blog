from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

#significa que o Post é um modelo de Django, então o Django sabe que ele deve ser salvo no banco de dados.
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
    
class Profile(models.Model):
    THEMES = [
        ('orange', 'Laranja'),
        ('pink', 'Rosa'),
        ('blue', 'Azul'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    theme = models.CharField(
        max_length=20,
        choices=THEMES,
        default='orange'
    )

    display_name = models.CharField(
        max_length=50,
        blank=True
     )

    def __str__(self):
        return self.user.username
from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(blank=True, null=True)
    custom_html = models.TextField(blank=True, null=True)  # Użytkownik może tu wpisać własny kod HTML
    custom_css = models.TextField(blank=True, null=True)  # Użytkownik może tu wpisać własny kod CSS

    def __str__(self):
        return self.user.username

class Friendship(models.Model):
    from_user = models.ForeignKey(User, related_name='sent_requests', on_delete=models.CASCADE)
    to_user = models.ForeignKey(User, related_name='received_requests', on_delete=models.CASCADE)
    accepted = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.from_user} -> {self.to_user} ({'Accepted' if self.accepted else 'Pending'})"

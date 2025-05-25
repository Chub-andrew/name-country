from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from telegram_bot.bot import send_telegram_message

class Country(models.Model):
    code = models.CharField(max_length=3, unique=True)
    name = models.CharField(max_length=100)
    region = models.CharField(max_length=100, blank=True)
    independent = models.BooleanField(null=True, blank=True)
    google_maps = models.URLField(blank=True)
    open_street_map = models.URLField(blank=True)
    capital_name = models.CharField(max_length=100, blank=True)
    capital_lat = models.FloatField(null=True, blank=True)
    capital_lng = models.FloatField(null=True, blank=True)
    flag_png = models.URLField(blank=True)
    flag_svg = models.URLField(blank=True)
    flag_alt = models.CharField(max_length=255, null=True, blank=True)
    coat_of_arms_png = models.URLField(null=True, blank=True)
    coat_of_arms_svg = models.URLField(null=True, blank=True)
    population = models.BigIntegerField(null=True, blank=True)
    borders_with = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f"{self.name} ({self.code})"

class Border(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='borders')
    border_with = models.CharField(max_length=3)  # store country codes

class Name(models.Model):
    name = models.CharField(max_length=50, unique=True)
    request_count = models.PositiveIntegerField(default=0)
    last_accessed = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name

class NameCountryProbability(models.Model):
    name = models.ForeignKey(Name, on_delete=models.CASCADE, related_name='probabilities')
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    probability = models.FloatField()

    class Meta:
        unique_together = ('name', 'country')

@receiver(post_save, sender=Name)
@receiver(post_save, sender=Country)
def send_telegram_notification(sender, instance, created, **kwargs):
    if not created:
        return
    if isinstance(instance, Name):
        message = f"New Name: '{instance.name}' was added to the Names!"
    elif isinstance(instance, Country):
        message = f"New Country: '{instance.name}' was added to the Countries!"

    send_telegram_message(message)

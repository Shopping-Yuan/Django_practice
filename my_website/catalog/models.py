from django.db import models

# Create your models here.
class all_card(models.Model):
    card_ID = models.IntegerField(primary_key=True,help_text="card_ID")
    card_name = models.CharField(max_length = 255 ,help_text="card_name")
    card_type = models.CharField(max_length = 255 ,help_text="card_type")
    
    class Meta:
        ordering = ['card_ID']
    
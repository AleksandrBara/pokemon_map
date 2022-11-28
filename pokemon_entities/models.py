from django.db import models  # noqa F401

# your models here
class Pokemon(models.Model):
    title = models.CharField(max_length=100, blank=True)
    image = models.ImageField(upload_to='pokemons', null=True)

    def __str__(self):
        return f'{self.title}'



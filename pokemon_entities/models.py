from django.db import models  # noqa F401


class Pokemon(models.Model):
    title = models.CharField(max_length=100, blank=True)
    image = models.ImageField(upload_to='pokemons', blank=True)

    def __str__(self):
        return f'{self.title}'


class PokemonEntity(models.Model):
    lat =models.FloatField(null=True)
    lon = models.FloatField(null=True)
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)
    appeared_at = models.DateTimeField(default=None)
    disappeared_at = models.DateTimeField(default=None)


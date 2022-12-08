from django.db import models  # noqa F401


class Pokemon(models.Model):
    title = models.CharField(max_length=100, blank=True)
    image = models.ImageField(upload_to='pokemons', blank=True)
    title_en = models.CharField(max_length=200, blank=True)
    title_jp = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)
    previous_evolution = models.ForeignKey(
        'self', null=True, related_name='next_evolutions',
        blank=True, on_delete=models.SET_NULL,
    )

    def __str__(self):
        return f'{self.title}'


class PokemonEntity(models.Model):
    lat =models.FloatField(null=True)
    lon = models.FloatField(null=True)
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)
    appeared_at = models.DateTimeField(default=None)
    disappeared_at = models.DateTimeField(default=None)
    level = models.IntegerField(default=0)
    health = models.IntegerField(default=0)
    strength = models.IntegerField(default=0)
    defence = models.IntegerField(default=0)
    stamina = models.IntegerField(default=0)


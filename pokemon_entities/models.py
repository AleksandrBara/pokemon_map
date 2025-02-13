from django.db import models  # noqa F401


class Pokemon(models.Model):
    title = models.CharField(max_length=100, verbose_name='русское название')
    image = models.ImageField(upload_to='pokemons', verbose_name='изображение')
    title_en = models.CharField(max_length=200, blank=True, verbose_name='английское название')
    title_jp = models.CharField(max_length=200, blank=True, verbose_name='японское название')
    description = models.TextField(blank=True, verbose_name='орисание покемона')
    previous_evolution = models.ForeignKey(
        'self', null=True,
        related_name='next_evolution',
        on_delete=models.SET_NULL,
        verbose_name='эволюция',
        blank=True
    )

    def __str__(self):
        return self.title


class PokemonEntity(models.Model):
    lat = models.FloatField(null=True, verbose_name='широта')
    lon = models.FloatField(null=True, verbose_name='долгота')
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE, verbose_name='покемон')
    appeared_at = models.DateTimeField(default=None, verbose_name='появление')
    disappeared_at = models.DateTimeField(default=None, verbose_name='исчезновение')
    level = models.IntegerField(default=None, verbose_name='уровень', blank=True)
    health = models.IntegerField(default=None, verbose_name='здоровье', blank=True)
    strength = models.IntegerField(default=None, verbose_name='сила', blank=True)
    defence = models.IntegerField(default=None, verbose_name='защита', blank=True)
    stamina = models.IntegerField(default=None, verbose_name='выносливость', blank=True)

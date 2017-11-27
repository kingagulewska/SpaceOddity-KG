from django.test import TestCase
from main_app.models import Planet
from django.template.loader import render_to_string
# Create your tests here.
from main_app.views import get_search_results


class TestPlanets(TestCase):
    def test_if_planets_creation_is_working(self):
        self.assertEqual(Planet.objects.count(), 0)

        earth = Planet.objects.create(
            name='Earth',
            main_photo='http://images.clipartpanda.com/earth-clip-art-earth_globe_dan_gerhrad_05r.png',
            small_photo='http://images.clipartpanda.com/earth-clip-art-earth_globe_dan_gerhrad_05r.png',
            description='Pretty neat planet',
            description_long='It is a very very very ver very neat planet.'
        )

        self.assertEqual(Planet.objects.count(), 1)


    def test_if_search_is_working(self):
        planet_names = ('Earth{}'.format(i) for i in range(50))

        for i, planet_name in enumerate(planet_names):
            Planet.objects.create(
                name=planet_name,
                main_photo='http://images.clipartpanda.com/earth-clip-art-earth_globe_dan_gerhrad_05r.png',
                small_photo='http://images.clipartpanda.com/earth-clip-art-earth_globe_dan_gerhrad_05r.png',
                description='Pretty neat planet number {}'.format(i),
                description_long='It is a very very very ver very neat planet number {}.'.format(i)
            )

        self.assertEqual(Planet.objects.count(), 50)

        rendered_response = render_to_string('results.html', get_search_results('Earth'))

        for planet_name in planet_names:
            self.assertIn(planet_name, rendered_response)
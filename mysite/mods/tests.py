from django.test import TestCase
from .models import Mod
from .forms import PublishForm


class ModTestClass(TestCase):

    def setUp(self):
        print("setUpTestData: Run once to set up non-modified data for all class methods.")

        Mod.objects.create(mod_title='test title',
                           mod_author='test author',
                           mod_game='test game',
                           mod_source='test source',
                           mod_description='test desc.')
        pass

    def test_mod_title(self):
        mod = Mod.objects.get(id=1)
        self.assertEqual(mod.mod_title, 'test title')

    def test_mod_author(self):
        mod = Mod.objects.get(id=1)
        self.assertEqual(mod.mod_author, 'test author')

    def test_mod_game(self):
        mod = Mod.objects.get(id=1)
        self.assertEqual(mod.mod_game, 'test game')

    def test_mod_source(self):
        mod = Mod.objects.get(id=1)
        self.assertEqual(mod.mod_source, 'test source')

    def test_mod_description(self):
        mod = Mod.objects.get(id=1)
        self.assertEqual(mod.mod_description, 'test desc.')

    def test_mod_str(self):
       mod = Mod.objects.get(id=1)
       self.assertEqual(mod.__str__(), 'test title')


# class RegisterFormTestClass(TestCase):

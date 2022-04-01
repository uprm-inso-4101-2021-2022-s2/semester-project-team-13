from django.test import TestCase
from .models import Mod


class ModTestClass(TestCase):

    def setUp(self):
        print("setUpTestData: Run once to set up non-modified data for all class methods.")

        Mod.objects.create(mod_title='test title',
                           mod_author='test author',
                           mod_game='test game',
                           mod_source='test source',
                           mod_description='test desc.')
        pass

    def test_mod_title_label(self):
        mod = Mod.objects.get(id=1)
        field_label = mod._meta.get_field('mod_title').verbose_name
        self.assertEqual(field_label, 'mod_title')

    def test_mod_author_label(self):
        mod = Mod.objects.get(id=1)
        field_label = mod._meta.get_field('mod_author').verbose_name
        self.assertEqual(field_label, 'mod_author')

    def test_mod_game_label(self):
        mod = Mod.objects.get(id=1)
        field_label = mod._meta.get_field('mod_game').verbose_name
        self.assertEqual(field_label, 'mod_game')

    def test_mod_source_label(self):
        mod = Mod.objects.get(id=1)
        field_label = mod._meta.get_field('mod_source').verbose_name
        self.assertEqual(field_label, 'mod_source')

    def test_mod_description_label(self):
        mod = Mod.objects.get(id=1)
        field_label = mod._meta.get_field('mod_description').verbose_name
        self.assertEqual(field_label, 'mod_description')


#
# class YourTestClass(TestCase):
#     @classmethod
#     def setUpTestData(cls):
#         print("setUpTestData: Run once to set up non-modified data for all class methods.")
#         pass
#
#     def setUp(self):
#         print("setUp: Run once for every test method to setup clean data.")
#         pass
#
#     def test_false_is_false(self):
#         print("Method: test_false_is_false.")
#         self.assertFalse(False)
#
#     def test_false_is_true(self):
#         print("Method: test_false_is_true.")
#         self.assertTrue(False)
#
#     def test_one_plus_one_equals_two(self):
#         print("Method: test_one_plus_one_equals_two.")
#         self.assertEqual(1 + 1, 2)
#

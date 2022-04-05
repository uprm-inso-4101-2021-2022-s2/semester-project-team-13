from django.test import TestCase
from django.urls import reverse
import random, string

from .models import Mod, Discussion, Reply
from .forms import CustomUserCreationForm, PublishForm, ReplyForm, DiscussionForm


# def setUp(self):
#     number_of_mods = 10
#
#     for mod_id in range(number_of_mods):
#         Mod.objects.create(
#             mod_title= f'title {mod_id}',
#             mod_author= f'author {mod_id}',
#             mod_game=f'game {mod_id}',
#             mod_source=f'source {mod_id}',
#             mod_description=f'description {mod_id}'
#         )
#     pass

class NewIndexViewTestClass(TestCase):

    def test_NewIndex_view_url_exists_at_desired_location(self):
        response = self.client.get('/mods/NewIndex.html')
        self.assertEqual(response.status_code, 200)

    def test_NewIndex_view_accessible_by_name(self):
        response = self.client.get(reverse('NewIndex'))
        self.assertEqual(response.status_code, 200)

    def test_NewIndex_view_uses_correct_template(self):
        response = self.client.get(reverse('NewIndex'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'mods/NewIndex.html')


class LoginFormViewTestClass(TestCase):

    def test_LoginForm_view_url_exists_at_desired_location(self):
        response = self.client.get('/mods/LoginForm.html')
        self.assertEqual(response.status_code, 200)

    def test_LoginForm_view_accessible_by_name(self):
        response = self.client.get(reverse('LoginForm'))
        self.assertEqual(response.status_code, 200)

    def test_LoginForm_view_uses_correct_template(self):
        response = self.client.get(reverse('LoginForm'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'mods/LoginForm.html')


class ModListViewTestClass(TestCase):
    def test_modList_view_url_exists_at_desired_location(self):
        response = self.client.get('/mods/modList.html')
        self.assertEqual(response.status_code, 200)

    def test_modList_view_accessible_by_name(self):
        response = self.client.get(reverse('modList'))
        self.assertEqual(response.status_code, 200)

    def test_modList_view_uses_correct_template(self):
        response = self.client.get(reverse('modList'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'mods/modList.html')


class GameListViewTestClass(TestCase):
    def test_gameList_view_url_exists_at_desired_location(self):
        response = self.client.get('/mods/gameList.html')
        self.assertEqual(response.status_code, 200)

    def test_gameList_view_accessible_by_name(self):
        response = self.client.get(reverse('gameList'))
        self.assertEqual(response.status_code, 200)

    def test_gameList_view_uses_correct_template(self):
        response = self.client.get(reverse('gameList'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'mods/gameList.html')


class ModDetailsViewTestClass(TestCase):
    def setUp(self):
        Mod.objects.create(mod_title='test title',
                           mod_author='test author',
                           mod_game='test game',
                           mod_source='test source',
                           mod_description='test desc.')
        pass

    def test_mod_details_view_url_exists_at_desired_location(self):
        response = self.client.get('/mods/1/')
        self.assertEqual(response.status_code, 200)

    def test_NewIndex_view_accessible_by_name(self):
        response = self.client.get(reverse('details', args=[1]))
        self.assertEqual(response.status_code, 200)

    def test_NewIndex_view_uses_correct_template(self):
        response = self.client.get(reverse('details', args=[1]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'mods/details.html')
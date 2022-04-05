from django.contrib.auth.models import User
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


class BoardsViewTestClass(TestCase):
    def test_mod_details_view_url_exists_at_desired_location(self):
        response = self.client.get('/mods/boards.html')
        self.assertEqual(response.status_code, 200)

    def test_NewIndex_view_accessible_by_name(self):
        response = self.client.get(reverse('boards'))
        self.assertEqual(response.status_code, 200)

    def test_NewIndex_view_uses_correct_template(self):
        response = self.client.get(reverse('boards'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'mods/boards.html')


class DiscussionViewTestClass(TestCase):
    def setUp(self):
        Discussion.objects.create(
            dis_title='title',
            dis_author='author',
            dis_type='Mod',
            dis='Discussion'
        )
        pass

    def test_discussion_view_url_exists_at_desired_location(self):
        response = self.client.get('/mods/boards/1/')
        self.assertEqual(response.status_code, 200)

    def test_discussion_view_accessible_by_name(self):
        response = self.client.get(reverse('discussion', args=[1]))
        self.assertEqual(response.status_code, 200)

    def test_discussion_view_uses_correct_template(self):
        response = self.client.get(reverse('discussion', args=[1]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'mods/discussion.html')


class PublishViewTestClass(TestCase):
    def test_publish_view_url_exists_at_desired_location(self):
        response = self.client.get('/mods/publish.html')
        self.assertEqual(response.status_code, 200)

    def test_publish_view_accessible_by_name(self):
        response = self.client.get(reverse('publish'))
        self.assertEqual(response.status_code, 200)

    def test_publish_view_uses_correct_template(self):
        response = self.client.get(reverse('publish'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'mods/publish.html')

    def test_publish_view_saves_mod(self):
        response = self.client.post('/mods/publish.html',{
            'mod_title': 'title',
            'mod_author': 'author',
            'mod_game': 'game',
            'mod_source': 'source',
            'mod_description': 'description'
        })
        self.assertTrue(Mod.objects.filter(mod_title='title').exists())

    def test_publish_redirects_to_desired_location_after_post(self):
        response = self.client.post('/mods/publish.html', {
            'mod_title': 'title',
            'mod_author': 'author',
            'mod_game': 'game',
            'mod_source': 'source',
            'mod_description': 'description'
        })
        self.assertEqual(response.status_code, 200)


class NewDiscussionViewTestClass(TestCase):

    def test_new_discussion_view_url_exists_at_desired_location(self):
        response = self.client.get('/mods/new_discussion.html')
        self.assertEqual(response.status_code, 200)

    def test_new_discussion_view_accessible_by_name(self):
        response = self.client.get(reverse('new_discussion'))
        self.assertEqual(response.status_code, 200)

    def test_new_discussion_view_uses_correct_template(self):
        response = self.client.get(reverse('new_discussion'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'mods/new_discussion.html')

    def test_new_discussion_view_saves_discussion(self):
        response = self.client.post('/mods/new_discussion.html', {
            'dis_title': 'title',
            'dis_author': 'author',
            'dis_type' : 'Mod',
            'dis': 'Discussion'
        })
        self.assertTrue(Discussion.objects.filter(dis_title='title').exists())

    def test_new_discussion_redirects_to_desired_location_after_post(self):
        response = self.client.post('/mods/new_discussion.html', {
            'dis_title': 'title',
            'dis_author': 'author',
            'dis_type': 'Mod',
            'dis': 'Discussion'
        })
        self.assertEqual(response.status_code, 200)


class NewReplyViewTestClass(TestCase):
    def setUp(self):
        Discussion.objects.create(
            dis_title='title',
            dis_author='author',
            dis_type='Mod',
            dis='Discussion'
        )
        Reply.objects.create(
            rep_title='title',
            rep_author='author',
            rep_parent=Discussion.objects.get(id=1),
            rep='rep'
        )
        pass

    def test_new_reply_view_url_exists_at_desired_location(self):
        response = self.client.get('/mods/new_reply.html')
        self.assertEqual(response.status_code, 200)

    def test_new_reply_view_accessible_by_name(self):
        response = self.client.get(reverse('new_reply'))
        self.assertEqual(response.status_code, 200)

    def test_new_reply_view_uses_correct_template(self):
        response = self.client.get(reverse('new_reply'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'mods/new_reply.html')

    def test_new_reply_view_saves_discussion(self):
        response = self.client.post('/mods/new_reply.html', {
            'rep_title': 'title',
            'rep_author': 'author',
            'rep_parent': Discussion.objects.get(id=1),
            'rep': 'rep'
        })
        self.assertTrue(Reply.objects.filter(rep_title='title').exists())

    def test_new_reply_redirects_to_desired_location_after_post(self):
        response = self.client.post('/mods/new_reply.html', {
            'rep_title': 'title',
            'rep_author': 'author',
            'rep_parent': Discussion.objects.get(id=1),
            'rep': 'rep'
        })
        self.assertEqual(response.status_code, 200)


class SearchViewTestClass(TestCase):
    def test_search_view_url_exists_at_desired_location(self):
        response = self.client.get('/mods/search.html')
        self.assertEqual(response.status_code, 200)

    def test_search_view_accessible_by_name(self):
        response = self.client.get(reverse('search'))
        self.assertEqual(response.status_code, 200)

    def test_search_view_uses_correct_template(self):
        response = self.client.get(reverse('search'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'mods/search.html')


class RegisterViewTestClass(TestCase):
    def test_register_view_url_exists_at_desired_location(self):
        response = self.client.get('/mods/register.html')
        self.assertEqual(response.status_code, 200)

    def test_register_view_accessible_by_name(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)

    def test_register_view_uses_correct_template(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'mods/register.html')

    def test_register_view_saves_user(self):
        response = self.client.post('/mods/register.html', {
            'username': 'username123',
            'email': 'email@example.com',
            'password1': 'password',
            'password2': 'password'
        })
        self.assertTrue(User.objects.filter(username='username123').exists())

    def test_register_redirects_to_desired_location_after_post(self):
        response = self.client.post('/mods/NewIndex.html', {
            'username': 'username',
            'email': 'email@example.com',
            'password1': 'password',
            'password2': 'password'
        })
        self.assertEqual(response.status_code, 200)
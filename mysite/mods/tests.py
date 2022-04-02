from django.test import TestCase
from django.urls import reverse

from .models import Mod
from .forms import CustomUserCreationForm, PublishForm, ReplyForm, DiscussionForm


class ModTestClass(TestCase):

    def setUp(self):
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


class PublishFormTestClass(TestCase):

    def test_publish_form_title_field(self):
        form = PublishForm()
        fields = ['Mod title', 'Mod author', 'Mod game', 'Mod source', 'Mod description']
        self.assertEqual(form.fields['mod_title'].label, fields[0])

    def test_publish_form_author_field(self):
        form = PublishForm()
        fields = ['Mod title', 'Mod author', 'Mod game', 'Mod source', 'Mod description']
        self.assertEqual(form.fields['mod_author'].label, fields[1])

    def test_publish_form_game_field(self):
        form = PublishForm()
        fields = ['Mod title', 'Mod author', 'Mod game', 'Mod source', 'Mod description']
        self.assertEqual(form.fields['mod_game'].label, fields[2])

    def test_publish_form_source_field(self):
        form = PublishForm()
        fields = ['Mod title', 'Mod author', 'Mod game', 'Mod source', 'Mod description']
        self.assertEqual(form.fields['mod_source'].label, fields[3])

    def test_publish_form_title_field(self):
        form = PublishForm()
        fields = ['Mod title', 'Mod author', 'Mod game', 'Mod source', 'Mod description']
        self.assertEqual(form.fields['mod_description'].label, fields[4])


class NewIndexViewTestClass(TestCase):
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

from django.test import TestCase
import random, string

from .models import Mod, Discussion, Reply
from .forms import CustomUserCreationForm, PublishForm, ReplyForm, DiscussionForm


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

    def test_publish_form_valid(self):
        mod = Mod.objects.create(mod_title='test title',
                                 mod_author='test author',
                                 mod_game='test game',
                                 mod_source='test source',
                                 mod_description='test desc.')
        data = {'mod_title': mod.mod_title,
                'mod_author': mod.mod_author,
                'mod_game': mod.mod_game,
                'mod_source': mod.mod_source,
                'mod_description': mod.mod_description}
        form = PublishForm(data=data)
        self.assertTrue(form.is_valid())

    def test_publish_form_invalid_no_title(self):
        mod = Mod.objects.create(mod_title='',
                                 mod_author='test author',
                                 mod_game='test game',
                                 mod_source='test source',
                                 mod_description='test description')
        data = {'mod_title': mod.mod_title,
                'mod_author': mod.mod_author,
                'mod_game': mod.mod_game,
                'mod_source': mod.mod_source,
                'mod_description': mod.mod_description}
        form = PublishForm(data=data)
        self.assertFalse(form.is_valid())

    def test_publish_form_invalid_no_author(self):
        mod = Mod.objects.create(mod_title='test title',
                                 mod_author='',
                                 mod_game='test game',
                                 mod_source='test source',
                                 mod_description='test description')
        data = {'mod_title': mod.mod_title,
                'mod_author': mod.mod_author,
                'mod_game': mod.mod_game,
                'mod_source': mod.mod_source,
                'mod_description': mod.mod_description}
        form = PublishForm(data=data)
        self.assertFalse(form.is_valid())

    def test_publish_form_invalid_no_game(self):
        mod = Mod.objects.create(mod_title='test title',
                                 mod_author='test author',
                                 mod_game='',
                                 mod_source='test source',
                                 mod_description='test description')
        data = {'mod_title': mod.mod_title,
                'mod_author': mod.mod_author,
                'mod_game': mod.mod_game,
                'mod_source': mod.mod_source,
                'mod_description': mod.mod_description}
        form = PublishForm(data=data)
        self.assertFalse(form.is_valid())

    def test_publish_form_invalid_no_source(self):
        mod = Mod.objects.create(mod_title='test title',
                                 mod_author='test author',
                                 mod_game='test game',
                                 mod_source='',
                                 mod_description='test description')
        data = {'mod_title': mod.mod_title,
                'mod_author': mod.mod_author,
                'mod_game': mod.mod_game,
                'mod_source': mod.mod_source,
                'mod_description': mod.mod_description}
        form = PublishForm(data=data)
        self.assertFalse(form.is_valid())

    def test_publish_form_invalid_no_description(self):
        mod = Mod.objects.create(mod_title='test title',
                                 mod_author='test author',
                                 mod_game='test game',
                                 mod_source='test source',
                                 mod_description='')
        data = {'mod_title': mod.mod_title,
                'mod_author': mod.mod_author,
                'mod_game': mod.mod_game,
                'mod_source': mod.mod_source,
                'mod_description': mod.mod_description}
        form = PublishForm(data=data)
        self.assertFalse(form.is_valid())


class CustomUserCreationFormTestClass(TestCase):
    def test_user_form_username_field(self):
        form = CustomUserCreationForm()
        fields = ['Username', 'email', 'Password', 'Confirm Password']
        self.assertEqual(form.fields['username'].label, fields[0])

    def test_user_form_email_field(self):
        form = CustomUserCreationForm()
        fields = ['Username', 'Email address', 'Password', 'Password']
        self.assertEqual(form.fields['email'].label, fields[1])

    def test_user_form_password1_field(self):
        form = CustomUserCreationForm()
        fields = ['Username', 'email', 'Password', 'Confirm Password']
        self.assertEqual(form.fields['password1'].label, fields[2])

    def test_user_form_password2_field(self):
        form = CustomUserCreationForm()
        fields = ['Username', 'email', 'Password', 'Password confirmation']
        self.assertEqual(form.fields['password2'].label, fields[3])

    def test_user_form_is_valid(self):
        data = {'username': 'username',
                'email': 'email@example.com',
                'password1': 'password',
                'password2': 'password'}
        form = CustomUserCreationForm(data=data)
        self.assertTrue(form.is_valid())

    def test_user_form_is_invalid_diff_passwords(self):
        data = {'username': 'username',
                'email': 'email@example.com',
                'password1': 'password2',
                'password2': 'password'}
        form = CustomUserCreationForm(data=data)
        self.assertFalse(form.is_valid())

    def test_user_form_is_invalid_email(self):
        data = {'username': 'username',
                'email': 'email',
                'password1': 'password',
                'password2': 'password'}
        form = CustomUserCreationForm(data=data)
        self.assertFalse(form.is_valid())

    def test_user_form_is_invalid_no_username(self):
        data = {'username': '',
                'email': 'email@example.com',
                'password1': 'password',
                'password2': 'password'}
        form = CustomUserCreationForm(data=data)
        self.assertFalse(form.is_valid())

    def test_user_form_is_invalid_no_password(self):
        data = {'username': 'username',
                'email': 'email@example.com',
                'password1': '',
                'password2': ''}
        form = CustomUserCreationForm(data=data)
        self.assertFalse(form.is_valid())


class DiscussionFormTestClass(TestCase):
    def test_dis_form_title_field(self):
        form = DiscussionForm()
        fields = ['Dis title', 'Dis author', 'Dis mod', 'Dis parent', 'Dis']
        self.assertEqual(form.fields['dis_title'].label, fields[0])

    def test_dis_form_author_field(self):
        form = DiscussionForm()
        fields = ['Dis title', 'Dis author', 'Dis mod', 'Dis parent', 'Dis']
        self.assertEqual(form.fields['dis_author'].label, fields[1])

    def test_dis_form_dis_field(self):
        form = DiscussionForm()
        fields = ['Dis title', 'Dis author', 'Dis mod', 'Dis parent', 'Dis']
        self.assertEqual(form.fields['dis'].label, fields[4])

    def test_dis_form_valid(self):
        data = {'dis_title': 'title',
                'dis_author': 'author',
                'dis_type' : 'Mod',
                'dis': 'Discussion'
        }
        form = DiscussionForm(data=data)
        self.assertTrue(form.is_valid())

    def test_dis_form_invalid_no_title(self):
        data = {'dis_title': '',
                'dis_author': 'author',
                'dis_type': 'Mod',
                'dis': 'Discussion'
                }
        form = DiscussionForm(data=data)
        self.assertFalse(form.is_valid())

    def test_dis_form_invalid_no_author(self):
        data = {'dis_title': 'title',
                'dis_author': '',
                'dis_type': 'Mod',
                'dis': 'Discussion'
                }
        form = DiscussionForm(data=data)
        self.assertFalse(form.is_valid())

    def test_dis_form_invalid_no_type(self):
        data = {'dis_title': 'title',
                'dis_author': 'author',
                'dis_type': '',
                'dis': 'Discussion'
                }
        form = DiscussionForm(data=data)
        self.assertFalse(form.is_valid())

    def test_dis_form_invalid_no_dis(self):
        data = {'dis_title': 'title',
                'dis_author': 'author',
                'dis_type': 'Mod',
                'dis': ''
                }
        form = DiscussionForm(data=data)
        self.assertFalse(form.is_valid())

    def test_dis_form_invalid_wrong_type(self):
        data = {'dis_title': 'title',
                'dis_author': 'author',
                'dis_type': 'A type',
                'dis': 'Discussion'
                }
        form = DiscussionForm(data=data)
        self.assertFalse(form.is_valid())

    def test_dis_form_max_char_title(self):
        letters = string.ascii_letters
        astring = ''
        astring = astring.join(random.choice(letters) for i in range(201))
        data = {'dis_title': astring,
                'dis_author': 'author',
                'dis_type': 'Mod',
                'dis': 'Discussion'
                }
        form = DiscussionForm(data=data)
        self.assertFalse(form.is_valid())

    def test_dis_form_max_char_author(self):
        letters = string.ascii_letters
        astring = ''
        astring = astring.join(random.choice(letters) for i in range(201))
        data = {'dis_title': 'title',
                'dis_author': astring,
                'dis_type': 'Mod',
                'dis': 'Discussion'
                }
        form = DiscussionForm(data=data)
        self.assertFalse(form.is_valid())


class ReplyFormTestClass(TestCase):
    def setUp(self):
        Discussion.objects.create(dis_title= 'title',
                dis_author= 'author',
                dis_type= 'Mod',
                dis= 'Discussion'
        )
        pass

    def test_rep_form_title_field(self):
        form = ReplyForm()
        fields = ['Rep title', 'Rep author', 'Rep mod', 'Rep parent', 'Dis']
        self.assertEqual(form.fields['rep_title'].label, fields[0])

    def test_rep_form_author_field(self):
        form = ReplyForm()
        fields = ['Rep title', 'Rep author', 'Rep mod', 'Rep parent', 'Dis']
        self.assertEqual(form.fields['rep_author'].label, fields[1])

    def test_rep_form_rep_field(self):
        form = ReplyForm()
        fields = ['Dis title', 'Dis author', 'Dis mod', 'Dis parent', 'Rep']
        self.assertEqual(form.fields['rep'].label, fields[4])

    def test_rep_form_valid_parent(self):
        data = {'rep_title': 'title',
                'rep_author': 'author',
                'rep_parent': Discussion.objects.get(id=1),
                'rep': 'rep'
                }
        form = ReplyForm(data=data)
        self.assertTrue(form.is_valid())

    def test_rep_form_invalid_no_parent(self):
        data = {'rep_title': 'title',
                'rep_author': 'author',
                'rep_parent': '',
                'rep': 'rep'
                }
        form = ReplyForm(data=data)
        self.assertFalse(form.is_valid())

    def test_rep_form_invalid_wrong_parent(self):
        data = {'rep_title': 'title',
                'rep_author': 'author',
                'rep_parent': 'Mod',
                'rep': 'rep'
                }
        form = ReplyForm(data=data)
        self.assertFalse(form.is_valid())

    def test_rep_form_invalid_no_title(self):
        data = {'rep_title': '',
                'rep_author': 'author',
                'rep_parent': Discussion.objects.get(id=1),
                'rep': 'rep'
                }
        form = ReplyForm(data=data)
        self.assertFalse(form.is_valid())

    def test_rep_form_invalid_no_rep(self):
        data = {'rep_title': 'title',
                'rep_author': 'author',
                'rep_parent': Discussion.objects.get(id=1),
                'rep': ''
                }
        form = DiscussionForm(data=data)
        self.assertFalse(form.is_valid())

    def test_rep_form_max_char_title(self):
        letters = string.ascii_letters
        astring = ''
        astring = astring.join(random.choice(letters) for i in range(201))
        data = {'rep_title': astring,
                'rep_author': 'author',
                'rep_parent': Discussion.objects.get(id=1),
                'rep': 'rep'
                }
        form = DiscussionForm(data=data)
        self.assertFalse(form.is_valid())

    def test_rep_form_max_char_author(self):
        letters = string.ascii_letters
        astring = ''
        astring = astring.join(random.choice(letters) for i in range(201))
        data = {'rep_title': 'title',
                'rep_author': astring,
                'rep_parent': Discussion.objects.get(id=1),
                'rep': 'rep'
                }
        form = DiscussionForm(data=data)
        self.assertFalse(form.is_valid())

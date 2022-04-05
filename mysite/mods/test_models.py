from django.test import TestCase
import random, string

from .models import Mod, Discussion, Reply


class ModTestClass(TestCase):
    def setUp(self):
        Mod.objects.create(mod_title='test title',
                           mod_author='test author',
                           mod_game='test game',
                           mod_source='test source',
                           mod_description='test desc.')
        number_of_mods = 4

        for mod_id in range(number_of_mods):
            Mod.objects.create(
                mod_title= f'title {mod_id}',
                mod_author= f'author {mod_id}',
                mod_game=f'game {mod_id}',
                mod_source=f'source {mod_id}',
                mod_description=f'description {mod_id}'
            )
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

    def test_mod_object_creation_count(self):
        self.assertEqual(5,Mod.objects.count())


class DiscussionTestClass(TestCase):
    def setUp(self):
        Mod.objects.create(mod_title='test title',
                           mod_author='test author',
                           mod_game='test game',
                           mod_source='test source',
                           mod_description='test desc.')

        Discussion.objects.create(
            dis_title='title',
            dis_author='author',
            dis_type='Mod',
            dis_mod=Mod.objects.get(id=1),
            dis='Discussion'
        )
        number_of_dis = 4

        for id in range(number_of_dis):
            Discussion.objects.create(
                dis_title=f'title {id}',
                dis_author=f'author {id}',
                dis_type='Mod',
                dis=f'Discussion  {id}'
            )
        pass

    def test_dis_title(self):
        dis = Discussion.objects.get(id=1)
        self.assertEqual(dis.dis_title, 'title')

    def test_dis_author(self):
        dis = Discussion.objects.get(id=1)
        self.assertEqual(dis.dis_author, 'author')

    def test_dis_discussion(self):
        dis = Discussion.objects.get(id=1)
        self.assertEqual(dis.dis, 'Discussion')

    def test_dis_mod(self):
        dis = Discussion.objects.get(id=1)
        mod = Mod.objects.get(id=1)
        self.assertEqual(dis.dis_mod, mod)

    def test_dis_str(self):
       dis = Discussion.objects.get(id=1)
       self.assertEqual(dis.__str__(), 'title')

    def test_dis_object_creation_count(self):
        self.assertEqual(5,Discussion.objects.count())


class ReplyTestClass(TestCase):
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
        number_of_dis = 4

        for id in range(number_of_dis):
            Reply.objects.create(
                rep_title=f'title {id}',
                rep_author=f'author {id}',
                rep_parent=Discussion.objects.get(id=1),
                rep=f'rep  {id}'
            )
        pass

    def test_rep_title(self):
        rep = Reply.objects.get(id=1)
        self.assertEqual(rep.rep_title, 'title')

    def test_rep_author(self):
        rep = Reply.objects.get(id=1)
        self.assertEqual(rep.rep_author, 'author')

    def test_rep_discussion(self):
        rep = Reply.objects.get(id=1)
        self.assertEqual(rep.rep, 'rep')

    def test_rep_parent(self):
        rep = Reply.objects.get(id=1)
        parent = Discussion.objects.get(id=1)
        self.assertEqual(rep.rep_parent, parent)

    def test_rep_str(self):
       rep = Reply.objects.get(id=1)
       self.assertEqual(rep.__str__(), 'title')

    def test_rep_object_creation_count(self):
        self.assertEqual(5,Reply.objects.count())



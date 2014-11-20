# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Trait'
        db.create_table('main_trait', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('text', self.gf('django.db.models.fields.CharField')(max_length=300)),
        ))
        db.send_create_signal('main', ['Trait'])

        # Adding model 'Example'
        db.create_table('main_example', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('text', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('link', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('order', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('main', ['Example'])

        # Adding model 'Contact'
        db.create_table('main_contact', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('company', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('skype', self.gf('django.db.models.fields.CharField')(blank=True, max_length=40, null=True)),
            ('message', self.gf('django.db.models.fields.CharField')(max_length=2000)),
        ))
        db.send_create_signal('main', ['Contact'])


    def backwards(self, orm):
        # Deleting model 'Trait'
        db.delete_table('main_trait')

        # Deleting model 'Example'
        db.delete_table('main_example')

        # Deleting model 'Contact'
        db.delete_table('main_contact')


    models = {
        'main.contact': {
            'Meta': {'object_name': 'Contact'},
            'company': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message': ('django.db.models.fields.CharField', [], {'max_length': '2000'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'skype': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '40', 'null': 'True'})
        },
        'main.example': {
            'Meta': {'ordering': "['order']", 'object_name': 'Example'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'link': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'order': ('django.db.models.fields.IntegerField', [], {}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'main.trait': {
            'Meta': {'object_name': 'Trait'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['main']
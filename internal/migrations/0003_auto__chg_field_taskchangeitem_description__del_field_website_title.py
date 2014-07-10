# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'TaskChangeItem.description'
        db.alter_column('internal_taskchangeitem', 'description', self.gf('django.db.models.fields.TextField')(null=True))
        # Deleting field 'Website.title'
        db.delete_column('internal_website', 'title')


    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'TaskChangeItem.description'
        raise RuntimeError("Cannot reverse this migration. 'TaskChangeItem.description' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'TaskChangeItem.description'
        db.alter_column('internal_taskchangeitem', 'description', self.gf('django.db.models.fields.TextField')())

        # User chose to not deal with backwards NULL issues for 'Website.title'
        raise RuntimeError("Cannot reverse this migration. 'Website.title' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Website.title'
        db.add_column('internal_website', 'title',
                      self.gf('django.db.models.fields.CharField')(max_length=30),
                      keep_default=False)


    models = {
        'internal.client': {
            'Meta': {'object_name': 'Client'},
            'contacts': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['internal.Contact']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'internal.contact': {
            'Meta': {'object_name': 'Contact'},
            'contact_email': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '50', 'blank': 'True'}),
            'contact_first_name': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '25', 'blank': 'True'}),
            'contact_last_name': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '25', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'internal.project': {
            'Meta': {'object_name': 'Project'},
            'client': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['internal.Client']"}),
            'contacts': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['internal.Contact']"}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pay_amount': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'decimal_places': '2', 'blank': 'True', 'max_digits': '5'}),
            'pay_cycle': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '1', 'default': "'O'", 'blank': 'True'}),
            'pay_type': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '1', 'default': "'P'", 'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '1', 'default': "'N'"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'internal.projectcontact': {
            'Meta': {'object_name': 'ProjectContact'},
            'contact_email': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '50', 'blank': 'True'}),
            'contact_name': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '50', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['internal.Project']"})
        },
        'internal.task': {
            'Meta': {'object_name': 'Task'},
            'complete_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'notify_client': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['internal.Project']"}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'internal.taskchangeitem': {
            'Meta': {'object_name': 'TaskChangeItem'},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'file': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'task': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['internal.Task']"})
        },
        'internal.website': {
            'Meta': {'object_name': 'Website'},
            'css_library': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'django_version': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'js_library': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['internal.Project']"}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '1', 'default': "'N'"})
        }
    }

    complete_apps = ['internal']
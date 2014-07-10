# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Project.status'
        db.delete_column('internal_project', 'status')

        # Adding field 'Project.active'
        db.add_column('internal_project', 'active',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Project.status'
        db.add_column('internal_project', 'status',
                      self.gf('django.db.models.fields.CharField')(max_length=1, default='N'),
                      keep_default=False)

        # Deleting field 'Project.active'
        db.delete_column('internal_project', 'active')


    models = {
        'internal.client': {
            'Meta': {'object_name': 'Client'},
            'contacts': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['internal.Contact']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'internal.contact': {
            'Meta': {'object_name': 'Contact'},
            'contact_email': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '50'}),
            'contact_first_name': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '25'}),
            'contact_last_name': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '25'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'internal.project': {
            'Meta': {'object_name': 'Project'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'client': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['internal.Client']"}),
            'contacts': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['internal.Contact']", 'symmetrical': 'False'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pay_amount': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'null': 'True', 'blank': 'True', 'decimal_places': '2'}),
            'pay_cycle': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '1', 'default': "'O'"}),
            'pay_type': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '1', 'default': "'P'"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'internal.projectcontact': {
            'Meta': {'object_name': 'ProjectContact'},
            'contact_email': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '50'}),
            'contact_name': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '50'}),
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
            'sent_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'})
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
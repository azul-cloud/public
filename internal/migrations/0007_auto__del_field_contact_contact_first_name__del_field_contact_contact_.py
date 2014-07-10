# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Contact.contact_first_name'
        db.delete_column('internal_contact', 'contact_first_name')

        # Deleting field 'Contact.contact_email'
        db.delete_column('internal_contact', 'contact_email')

        # Deleting field 'Contact.contact_last_name'
        db.delete_column('internal_contact', 'contact_last_name')

        # Adding field 'Contact.first_name'
        db.add_column('internal_contact', 'first_name',
                      self.gf('django.db.models.fields.CharField')(null=True, blank=True, max_length=25),
                      keep_default=False)

        # Adding field 'Contact.last_name'
        db.add_column('internal_contact', 'last_name',
                      self.gf('django.db.models.fields.CharField')(null=True, blank=True, max_length=25),
                      keep_default=False)

        # Adding field 'Contact.email'
        db.add_column('internal_contact', 'email',
                      self.gf('django.db.models.fields.CharField')(null=True, blank=True, max_length=50),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Contact.contact_first_name'
        db.add_column('internal_contact', 'contact_first_name',
                      self.gf('django.db.models.fields.CharField')(null=True, blank=True, max_length=25),
                      keep_default=False)

        # Adding field 'Contact.contact_email'
        db.add_column('internal_contact', 'contact_email',
                      self.gf('django.db.models.fields.CharField')(null=True, blank=True, max_length=50),
                      keep_default=False)

        # Adding field 'Contact.contact_last_name'
        db.add_column('internal_contact', 'contact_last_name',
                      self.gf('django.db.models.fields.CharField')(null=True, blank=True, max_length=25),
                      keep_default=False)

        # Deleting field 'Contact.first_name'
        db.delete_column('internal_contact', 'first_name')

        # Deleting field 'Contact.last_name'
        db.delete_column('internal_contact', 'last_name')

        # Deleting field 'Contact.email'
        db.delete_column('internal_contact', 'email')


    models = {
        'internal.client': {
            'Meta': {'object_name': 'Client'},
            'contacts': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['internal.Contact']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'internal.contact': {
            'Meta': {'object_name': 'Contact'},
            'email': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '50'}),
            'first_name': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '25'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '25'})
        },
        'internal.project': {
            'Meta': {'object_name': 'Project'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'client': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['internal.Client']"}),
            'contacts': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['internal.Contact']", 'symmetrical': 'False'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pay_amount': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'blank': 'True', 'decimal_places': '2'}),
            'pay_cycle': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'default': "'O'", 'max_length': '1'}),
            'pay_type': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'default': "'P'", 'max_length': '1'}),
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
            'status': ('django.db.models.fields.CharField', [], {'default': "'N'", 'max_length': '1'})
        }
    }

    complete_apps = ['internal']
# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Invoice.expense'
        db.add_column('internal_invoice', 'expense',
                      self.gf('django.db.models.fields.DecimalField')(max_digits=5, default=0.0, decimal_places=2),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Invoice.expense'
        db.delete_column('internal_invoice', 'expense')


    models = {
        'internal.client': {
            'Meta': {'object_name': 'Client'},
            'contacts': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['internal.Contact']", 'null': 'True', 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'internal.contact': {
            'Meta': {'object_name': 'Contact'},
            'email': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '25'})
        },
        'internal.hours': {
            'Meta': {'ordering': "['project__title', 'date']", 'object_name': 'Hours'},
            'date': ('django.db.models.fields.DateField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True', 'null': 'True'}),
            'hours': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'invoice': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['internal.Invoice']", 'blank': 'True', 'null': 'True'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['internal.Project']"})
        },
        'internal.invoice': {
            'Meta': {'ordering': "['-id']", 'object_name': 'Invoice'},
            'due_date': ('django.db.models.fields.DateField', [], {'blank': 'True', 'null': 'True'}),
            'end_date': ('django.db.models.fields.DateField', [], {'blank': 'True', 'null': 'True'}),
            'expense': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'default': '0.0', 'decimal_places': '2'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'invoice_date': ('django.db.models.fields.DateField', [], {'blank': 'True', 'null': 'True'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['internal.Project']"}),
            'rate': ('django.db.models.fields.DecimalField', [], {'blank': 'True', 'max_digits': '5', 'null': 'True', 'decimal_places': '2'}),
            'start_date': ('django.db.models.fields.DateField', [], {'blank': 'True', 'null': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'P'", 'max_length': '1'})
        },
        'internal.project': {
            'Meta': {'object_name': 'Project'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'client': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['internal.Client']"}),
            'contacts': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['internal.Contact']", 'null': 'True', 'symmetrical': 'False'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pay_amount': ('django.db.models.fields.DecimalField', [], {'blank': 'True', 'max_digits': '5', 'null': 'True', 'decimal_places': '2'}),
            'pay_cycle': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'default': "'O'", 'max_length': '1'}),
            'pay_type': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'default': "'P'", 'max_length': '1'}),
            'payroll_contacts': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['internal.Contact']", 'symmetrical': 'False', 'blank': 'True', 'related_name': "'payroll_contacts'", 'null': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '30'})
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
# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Invoice.rate'
        db.add_column('internal_invoice', 'rate',
                      self.gf('django.db.models.fields.DecimalField')(null=True, blank=True, decimal_places=2, max_digits=5),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Invoice.rate'
        db.delete_column('internal_invoice', 'rate')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'blank': 'True', 'symmetrical': 'False'})
        },
        'auth.permission': {
            'Meta': {'object_name': 'Permission', 'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)"},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'blank': 'True', 'max_length': '75'}),
            'first_name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '30'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'blank': 'True', 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '30'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'blank': 'True', 'symmetrical': 'False'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'object_name': 'ContentType', 'db_table': "'django_content_type'", 'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'internal.client': {
            'Meta': {'object_name': 'Client'},
            'contacts': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['internal.Contact']", 'symmetrical': 'False'}),
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
            'Meta': {'object_name': 'Hours', 'ordering': "['project__title', 'date']"},
            'date': ('django.db.models.fields.DateField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'hours': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'invoice': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'blank': 'True', 'to': "orm['internal.Invoice']"}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['internal.Project']"})
        },
        'internal.invoice': {
            'Meta': {'object_name': 'Invoice', 'ordering': "['-id']"},
            'due_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'invoice_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['internal.Project']"}),
            'rate': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'blank': 'True', 'decimal_places': '2', 'max_digits': '5'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'P'", 'max_length': '1'})
        },
        'internal.project': {
            'Meta': {'object_name': 'Project'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'client': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['internal.Client']"}),
            'contacts': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['internal.Contact']", 'symmetrical': 'False'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pay_amount': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'blank': 'True', 'decimal_places': '2', 'max_digits': '5'}),
            'pay_cycle': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'default': "'O'", 'max_length': '1'}),
            'pay_type': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'default': "'P'", 'max_length': '1'}),
            'payroll_contacts': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'payroll_contacts'", 'to': "orm['internal.Contact']", 'null': 'True', 'blank': 'True', 'symmetrical': 'False'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'internal.task': {
            'Meta': {'object_name': 'Task'},
            'assigned_to': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'default': '1'}),
            'complete_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'create_date': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'dev_notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'notify_client': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['internal.Project']"}),
            'sent_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'})
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
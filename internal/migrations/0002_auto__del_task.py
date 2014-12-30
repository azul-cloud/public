# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Task'
        db.delete_table('internal_task')


    def backwards(self, orm):
        # Adding model 'Task'
        db.create_table('internal_task', (
            ('status', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('assigned_to', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], default=1)),
            ('sent_date', self.gf('django.db.models.fields.DateField')(blank=True, null=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('create_date', self.gf('django.db.models.fields.DateField')(blank=True, auto_now_add=True)),
            ('complete_date', self.gf('django.db.models.fields.DateField')(blank=True, null=True)),
            ('dev_notes', self.gf('django.db.models.fields.TextField')(blank=True, null=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('notify_client', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('project', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['internal.Project'])),
        ))
        db.send_create_signal('internal', ['Task'])


    models = {
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
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True', 'null': 'True'}),
            'hours': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'invoice': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'to': "orm['internal.Invoice']", 'null': 'True'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['internal.Project']"})
        },
        'internal.invoice': {
            'Meta': {'object_name': 'Invoice', 'ordering': "['-id']"},
            'due_date': ('django.db.models.fields.DateField', [], {'blank': 'True', 'null': 'True'}),
            'end_date': ('django.db.models.fields.DateField', [], {'blank': 'True', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'invoice_date': ('django.db.models.fields.DateField', [], {'blank': 'True', 'null': 'True'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['internal.Project']"}),
            'rate': ('django.db.models.fields.DecimalField', [], {'blank': 'True', 'max_digits': '5', 'decimal_places': '2', 'null': 'True'}),
            'start_date': ('django.db.models.fields.DateField', [], {'blank': 'True', 'null': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'P'", 'max_length': '1'})
        },
        'internal.project': {
            'Meta': {'object_name': 'Project'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'client': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['internal.Client']"}),
            'contacts': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['internal.Contact']", 'symmetrical': 'False'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pay_amount': ('django.db.models.fields.DecimalField', [], {'blank': 'True', 'max_digits': '5', 'decimal_places': '2', 'null': 'True'}),
            'pay_cycle': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "'O'", 'max_length': '1', 'null': 'True'}),
            'pay_type': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "'P'", 'max_length': '1', 'null': 'True'}),
            'payroll_contacts': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'to': "orm['internal.Contact']", 'symmetrical': 'False', 'related_name': "'payroll_contacts'", 'null': 'True'}),
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
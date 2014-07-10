# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Client'
        db.create_table('internal_client', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal('internal', ['Client'])

        # Adding model 'ClientContact'
        db.create_table('internal_clientcontact', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('contact_name', self.gf('django.db.models.fields.CharField')(null=True, max_length=50, blank=True)),
            ('contact_email', self.gf('django.db.models.fields.CharField')(null=True, max_length=50, blank=True)),
            ('client', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['internal.Client'])),
        ))
        db.send_create_signal('internal', ['ClientContact'])

        # Adding model 'Project'
        db.create_table('internal_project', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('client', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['internal.Client'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('status', self.gf('django.db.models.fields.CharField')(default='N', max_length=1)),
            ('pay_amount', self.gf('django.db.models.fields.DecimalField')(max_digits=5, decimal_places=2, null=True, blank=True)),
            ('pay_type', self.gf('django.db.models.fields.CharField')(default='P', null=True, max_length=1, blank=True)),
            ('pay_cycle', self.gf('django.db.models.fields.CharField')(default='O', null=True, max_length=1, blank=True)),
        ))
        db.send_create_signal('internal', ['Project'])

        # Adding model 'ProjectContact'
        db.create_table('internal_projectcontact', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('contact_name', self.gf('django.db.models.fields.CharField')(null=True, max_length=50, blank=True)),
            ('contact_email', self.gf('django.db.models.fields.CharField')(null=True, max_length=50, blank=True)),
            ('project', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['internal.Project'])),
        ))
        db.send_create_signal('internal', ['ProjectContact'])

        # Adding model 'Website'
        db.create_table('internal_website', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('project', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['internal.Project'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('status', self.gf('django.db.models.fields.CharField')(default='N', max_length=1)),
            ('css_library', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('js_library', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('django_version', self.gf('django.db.models.fields.CharField')(max_length=3)),
        ))
        db.send_create_signal('internal', ['Website'])

        # Adding model 'Task'
        db.create_table('internal_task', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('project', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['internal.Project'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('status', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('complete_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('notify_client', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal('internal', ['Task'])

        # Adding model 'TaskChangeItem'
        db.create_table('internal_taskchangeitem', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('task', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['internal.Task'])),
            ('file', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('internal', ['TaskChangeItem'])


    def backwards(self, orm):
        # Deleting model 'Client'
        db.delete_table('internal_client')

        # Deleting model 'ClientContact'
        db.delete_table('internal_clientcontact')

        # Deleting model 'Project'
        db.delete_table('internal_project')

        # Deleting model 'ProjectContact'
        db.delete_table('internal_projectcontact')

        # Deleting model 'Website'
        db.delete_table('internal_website')

        # Deleting model 'Task'
        db.delete_table('internal_task')

        # Deleting model 'TaskChangeItem'
        db.delete_table('internal_taskchangeitem')


    models = {
        'internal.client': {
            'Meta': {'object_name': 'Client'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'internal.clientcontact': {
            'Meta': {'object_name': 'ClientContact'},
            'client': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['internal.Client']"}),
            'contact_email': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '50', 'blank': 'True'}),
            'contact_name': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '50', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'internal.project': {
            'Meta': {'object_name': 'Project'},
            'client': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['internal.Client']"}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pay_amount': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '2', 'null': 'True', 'blank': 'True'}),
            'pay_cycle': ('django.db.models.fields.CharField', [], {'default': "'O'", 'null': 'True', 'max_length': '1', 'blank': 'True'}),
            'pay_type': ('django.db.models.fields.CharField', [], {'default': "'P'", 'null': 'True', 'max_length': '1', 'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'N'", 'max_length': '1'}),
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
            'description': ('django.db.models.fields.TextField', [], {}),
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
            'status': ('django.db.models.fields.CharField', [], {'default': "'N'", 'max_length': '1'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['internal']
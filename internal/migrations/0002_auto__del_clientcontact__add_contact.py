# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'ClientContact'
        db.delete_table('internal_clientcontact')

        # Adding model 'Contact'
        db.create_table('internal_contact', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('contact_first_name', self.gf('django.db.models.fields.CharField')(max_length=25, null=True, blank=True)),
            ('contact_last_name', self.gf('django.db.models.fields.CharField')(max_length=25, null=True, blank=True)),
            ('contact_email', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
        ))
        db.send_create_signal('internal', ['Contact'])

        # Adding M2M table for field contacts on 'Project'
        m2m_table_name = db.shorten_name('internal_project_contacts')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('project', models.ForeignKey(orm['internal.project'], null=False)),
            ('contact', models.ForeignKey(orm['internal.contact'], null=False))
        ))
        db.create_unique(m2m_table_name, ['project_id', 'contact_id'])

        # Adding M2M table for field contacts on 'Client'
        m2m_table_name = db.shorten_name('internal_client_contacts')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('client', models.ForeignKey(orm['internal.client'], null=False)),
            ('contact', models.ForeignKey(orm['internal.contact'], null=False))
        ))
        db.create_unique(m2m_table_name, ['client_id', 'contact_id'])


    def backwards(self, orm):
        # Adding model 'ClientContact'
        db.create_table('internal_clientcontact', (
            ('contact_name', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('contact_email', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('client', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['internal.Client'])),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('internal', ['ClientContact'])

        # Deleting model 'Contact'
        db.delete_table('internal_contact')

        # Removing M2M table for field contacts on 'Project'
        db.delete_table(db.shorten_name('internal_project_contacts'))

        # Removing M2M table for field contacts on 'Client'
        db.delete_table(db.shorten_name('internal_client_contacts'))


    models = {
        'internal.client': {
            'Meta': {'object_name': 'Client'},
            'contacts': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['internal.Contact']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'internal.contact': {
            'Meta': {'object_name': 'Contact'},
            'contact_email': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'contact_first_name': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'contact_last_name': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'internal.project': {
            'Meta': {'object_name': 'Project'},
            'client': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['internal.Client']"}),
            'contacts': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['internal.Contact']"}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pay_amount': ('django.db.models.fields.DecimalField', [], {'decimal_places': '2', 'max_digits': '5', 'null': 'True', 'blank': 'True'}),
            'pay_cycle': ('django.db.models.fields.CharField', [], {'max_length': '1', 'default': "'O'", 'null': 'True', 'blank': 'True'}),
            'pay_type': ('django.db.models.fields.CharField', [], {'max_length': '1', 'default': "'P'", 'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '1', 'default': "'N'"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'internal.projectcontact': {
            'Meta': {'object_name': 'ProjectContact'},
            'contact_email': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'contact_name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
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
            'status': ('django.db.models.fields.CharField', [], {'max_length': '1', 'default': "'N'"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['internal']
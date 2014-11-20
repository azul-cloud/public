# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Contact'
        db.create_table('internal_contact', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('internal', ['Contact'])

        # Adding model 'Client'
        db.create_table('internal_client', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal('internal', ['Client'])

        # Adding M2M table for field contacts on 'Client'
        m2m_table_name = db.shorten_name('internal_client_contacts')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('client', models.ForeignKey(orm['internal.client'], null=False)),
            ('contact', models.ForeignKey(orm['internal.contact'], null=False))
        ))
        db.create_unique(m2m_table_name, ['client_id', 'contact_id'])

        # Adding model 'Project'
        db.create_table('internal_project', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('client', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['internal.Client'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('pay_amount', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=5, decimal_places=2, blank=True)),
            ('pay_type', self.gf('django.db.models.fields.CharField')(max_length=1, null=True, default='P', blank=True)),
            ('pay_cycle', self.gf('django.db.models.fields.CharField')(max_length=1, null=True, default='O', blank=True)),
        ))
        db.send_create_signal('internal', ['Project'])

        # Adding M2M table for field contacts on 'Project'
        m2m_table_name = db.shorten_name('internal_project_contacts')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('project', models.ForeignKey(orm['internal.project'], null=False)),
            ('contact', models.ForeignKey(orm['internal.contact'], null=False))
        ))
        db.create_unique(m2m_table_name, ['project_id', 'contact_id'])

        # Adding M2M table for field payroll_contacts on 'Project'
        m2m_table_name = db.shorten_name('internal_project_payroll_contacts')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('project', models.ForeignKey(orm['internal.project'], null=False)),
            ('contact', models.ForeignKey(orm['internal.contact'], null=False))
        ))
        db.create_unique(m2m_table_name, ['project_id', 'contact_id'])

        # Adding model 'Website'
        db.create_table('internal_website', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('project', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['internal.Project'])),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('status', self.gf('django.db.models.fields.CharField')(max_length=1, default='N')),
            ('css_library', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('js_library', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('django_version', self.gf('django.db.models.fields.CharField')(max_length=3)),
        ))
        db.send_create_signal('internal', ['Website'])

        # Adding model 'Task'
        db.create_table('internal_task', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('project', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['internal.Project'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('dev_notes', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('status', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('complete_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('notify_client', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('sent_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('create_date', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('assigned_to', self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['auth.User'])),
        ))
        db.send_create_signal('internal', ['Task'])

        # Adding model 'Invoice'
        db.create_table('internal_invoice', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('project', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['internal.Project'])),
            ('status', self.gf('django.db.models.fields.CharField')(max_length=1, default='P')),
            ('rate', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=5, decimal_places=2, blank=True)),
            ('due_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('invoice_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('start_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('end_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
        ))
        db.send_create_signal('internal', ['Invoice'])

        # Adding model 'Hours'
        db.create_table('internal_hours', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('project', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['internal.Project'])),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('hours', self.gf('django.db.models.fields.IntegerField')()),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('invoice', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['internal.Invoice'], blank=True)),
        ))
        db.send_create_signal('internal', ['Hours'])


    def backwards(self, orm):
        # Deleting model 'Contact'
        db.delete_table('internal_contact')

        # Deleting model 'Client'
        db.delete_table('internal_client')

        # Removing M2M table for field contacts on 'Client'
        db.delete_table(db.shorten_name('internal_client_contacts'))

        # Deleting model 'Project'
        db.delete_table('internal_project')

        # Removing M2M table for field contacts on 'Project'
        db.delete_table(db.shorten_name('internal_project_contacts'))

        # Removing M2M table for field payroll_contacts on 'Project'
        db.delete_table(db.shorten_name('internal_project_payroll_contacts'))

        # Deleting model 'Website'
        db.delete_table('internal_website')

        # Deleting model 'Task'
        db.delete_table('internal_task')

        # Deleting model 'Invoice'
        db.delete_table('internal_invoice')

        # Deleting model 'Hours'
        db.delete_table('internal_hours')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '80', 'unique': 'True'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'user_set'", 'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'user_set'", 'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '30', 'unique': 'True'})
        },
        'contenttypes.contenttype': {
            'Meta': {'db_table': "'django_content_type'", 'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType'},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'internal.client': {
            'Meta': {'object_name': 'Client'},
            'contacts': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['internal.Contact']"}),
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
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'hours': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'invoice': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['internal.Invoice']", 'blank': 'True'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['internal.Project']"})
        },
        'internal.invoice': {
            'Meta': {'ordering': "['-id']", 'object_name': 'Invoice'},
            'due_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'end_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'invoice_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['internal.Project']"}),
            'rate': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '2', 'blank': 'True'}),
            'start_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '1', 'default': "'P'"})
        },
        'internal.project': {
            'Meta': {'object_name': 'Project'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'client': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['internal.Client']"}),
            'contacts': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['internal.Contact']"}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pay_amount': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '2', 'blank': 'True'}),
            'pay_cycle': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'default': "'O'", 'blank': 'True'}),
            'pay_type': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'default': "'P'", 'blank': 'True'}),
            'payroll_contacts': ('django.db.models.fields.related.ManyToManyField', [], {'null': 'True', 'related_name': "'payroll_contacts'", 'to': "orm['internal.Contact']", 'symmetrical': 'False', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'internal.task': {
            'Meta': {'object_name': 'Task'},
            'assigned_to': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': "orm['auth.User']"}),
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
            'status': ('django.db.models.fields.CharField', [], {'max_length': '1', 'default': "'N'"})
        }
    }

    complete_apps = ['internal']
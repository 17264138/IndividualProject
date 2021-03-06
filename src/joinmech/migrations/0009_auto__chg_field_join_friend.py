# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Join.friend'
        db.alter_column(u'joinmech_join', 'friend_id', self.gf('django.db.models.fields.related.ForeignKey')(default='', to=orm['joinmech.Join']))

    def backwards(self, orm):

        # Changing field 'Join.friend'
        db.alter_column(u'joinmech_join', 'friend_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['joinmech.Join']))

    models = {
        u'joinmech.join': {
            'Meta': {'unique_together': "(('email', 'ref_id'),)", 'object_name': 'Join'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'friend': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'referral'", 'to': u"orm['joinmech.Join']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip_address': ('django.db.models.fields.CharField', [], {'default': "'ABC'", 'max_length': '120'}),
            'ref_id': ('django.db.models.fields.CharField', [], {'default': "'ABC'", 'unique': 'True', 'max_length': '120'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['joinmech']
from rest_framework import serializers
from .models import organization, user, shoutout


class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = organization
        fields = ['name', 'slack_org_id', 'channel_name', 'channel_id',
                  'access_token', 'installation_date', 'bot_access_token']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = user
        fields = ['org_id', 'slack_mem_id', 'email', 'name',
                  'avatar']


class ShoutoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = shoutout
        fields = ['giver_id', 'receiver_id', 'message', 'timestamps',
                  'message_ts']

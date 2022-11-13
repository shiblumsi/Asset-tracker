from rest_framework import serializers
from .models import *


class AddEmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('name','phone','email','designation')


class AddAssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asset
        fields = '__all__'


class DelegateToSerializer(serializers.ModelSerializer):
    
    #assets = serializers.StringRelatedField(many=True, read_only=True)
    #employee = serializers.StringRelatedField(read_only=True)
    
    class Meta:
        model = DelegateTo
        fields = ('employee','assets','checked_out_at','condition')


class WhenGiveAndReturnSerializer(serializers.ModelSerializer):
    model = serializers.StringRelatedField( read_only=True)
    class Meta:
        model = GiveBack
        fields = ('asset_type','model','brand','checked_out_time','returned_date')


class ConditionGiveAndReturnSerializer(serializers.ModelSerializer):
    model = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = GiveBack
        fields = ('employee_name','asset_type','model','brand','delegate_condition','returned_condition')
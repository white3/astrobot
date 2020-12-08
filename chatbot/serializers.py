# -*- coding: utf-8 -*- 
from rest_framework import serializers
from .models import Question

class DynamicFieldsModelSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        fields = kwargs.pop('fields', None) # 提取fields
		
		# 实例化父类
        super(DynamicFieldsModelSerializer, self).__init__(*args, **kwargs)

        if fields is not None:
            # 删除fields参数中未指定的任何字段
            allowed = set(fields)
            existing = set(self.fields.keys())
            if allowed:
                for field_name in existing - allowed:
                    self.fields.pop(field_name)
            else:
            	# fields参数为空，则取全部字段
                pass
                
# 继承自定义的类
class Sence3Serializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Question
        fields = "__all__" # 这里可以写全部，在外面传fields修改

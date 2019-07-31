from rest_framework import serializers
from books.models import BookInfo


class BookInfoSerializer(serializers.Serializer):
    """
    图书序列化器
    """
    # id = serializers.IntegerField()
    btitle = serializers.CharField()
    bpub_date = serializers.DateField()
    bread = serializers.IntegerField()
    bcomment = serializers.IntegerField()

    # 父表嵌套子表返回 PrimaryKeyRelatedField 嵌套返回id
    # heros = serializers.PrimaryKeyRelatedField(read_only=True, many=True)
    # StringRelatedField 返回子表模型类中__str__方法的结果
    # heros = serializers.StringRelatedField(read_only=True, many=True)
    # 根据另外一个序列化器返回相应的嵌套字段
    # heros = HeroInfoSerializer(read_only=True, many=True)



class HeroInfoSerializer(serializers.Serializer):
    """
    英雄序列化器
    """
    hname = serializers.CharField()
    hgender = serializers.IntegerField()
    hcomment = serializers.CharField()

    # 子表嵌套父表返回
    # hbook = serializers.PrimaryKeyRelatedField(read_only=True)
    hbook_id = serializers.IntegerField()
    # hbook = serializers.StringRelatedField(read_only=True)
    # hbook = BookSerializer(read_only=True)

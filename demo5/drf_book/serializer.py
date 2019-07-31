from rest_framework import serializers


class BookInfoSerializer(serializers.Serializer):
    """
    图书序列化器
    """
    id = serializers.IntegerField()
    btitle = serializers.CharField()
    bpub_date = serializers.DateField()
    bread = serializers.IntegerField()
    bcomment = serializers.IntegerField()

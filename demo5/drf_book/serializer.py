from rest_framework import serializers
from books.models import BookInfo


class BookInfoSerializer(serializers.Serializer):
    """
    图书序列化器
    """
    # id = serializers.IntegerField()
    btitle = serializers.CharField(max_length=20, min_length=4)
    bpub_date = serializers.DateField(required=False) # read_only=True表明该字段只参与序列化
    bread = serializers.IntegerField(max_value=100, min_value=1, write_only=True)  # write_only=True表明该字段只参与反序列化
    bcomment = serializers.IntegerField(default=0, write_only=True)

    # 父表嵌套子表返回 PrimaryKeyRelatedField 嵌套返回id
    # heros = serializers.PrimaryKeyRelatedField(read_only=True, many=True)
    # StringRelatedField 返回子表模型类中__str__方法的结果
    # heros = serializers.StringRelatedField(read_only=True, many=True)
    # 根据另外一个序列化器返回相应的嵌套字段
    # heros = HeroInfoSerializer(read_only=True, many=True)

    # 单一字段验证方法
    def validate_btitle(self, attrs):
        """
        :param attrs:接受要验证的字段数据
        :return:
        """
        if attrs == 'python':
            raise serializers.ValidationError('书名不能为python')
        # 注意！！！！ 验证完成之后，一定要返回验证后的数据
        return attrs
    # 多个字段验证方法
    def validate(self, attrs):
        """
        :param attrs: 接受多个字段验证数据  是一个字典类型
        :return:
        """
        if attrs['bread'] > attrs['bcomment']:
            raise serializers.ValidationError('阅读量大于评论量')
        return attrs
    #封装保存方法
    def create(self, validated_data):
        """
        保存数据
        :param validated_data: 接受验证后字段数据 字典
        :return:
        """
        # 编写保存数据库的业务逻辑
        book = BookInfo.objects.create(**validated_data)
        # 返回保存后的数据对象
        return book
    # 封装更新方法
    def update(self, instance, validated_data):
        """
        :param instance: 接受的是更新的数据对象
        :param validated_data: 接受验证后字段数据 字典
        :return:
        """
        instance.btitle = validated_data['btitle']
        instance.save()
        return instance
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

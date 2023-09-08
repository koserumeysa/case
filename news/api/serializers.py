from rest_framework import serializers
from news.models import Essay, Reporter

from datetime import datetime
from django.utils.timesince import timesince


class EssaySerializer(serializers.ModelSerializer):
    
    time_since_pub = serializers.SerializerMethodField()
    
    #author = ReporterSerializer(read_only=True) #This means that do not anything with this in the backend.
    #If we cannot use this, every author has an id.
    #author = serializers.StringRelatedField() #This returns of the reporter.

    class Meta:
        model = Essay
        fields = '__all__'
        #If we want to include all fields, we can use this.
        #If we want to show some fields, we can use this.
        #fields =['author','title','body']
        #If we want to exclude some fields, we can use this.
        #exclude = ['id','isActive','cre_date','up_date','pub_date']
        read_only_fields = ['id','up_date','cre_date']

    def get_time_since_pub(self, object):
        now = datetime.now()
        pub_date = object.pub_date
        if object.isActive:
            time_delta = timesince(pub_date, now)
            return time_delta
        else:
            return 'Not Active'


    
    def validate_pub_date(self, value):
        if value > datetime.now().date():
            raise serializers.ValidationError('Pub date cannot be in the future.')
        return value


class ReporterSerializer(serializers.ModelSerializer):

    #essays = EssaySerializer(many=True, read_only=True)
    #When we use Hyperlinked then we can update the context in views.
    essays = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='essay-detail'
        )
    
    class Meta:
        model = Reporter
        fields = '__all__'










#STANDARD SERIALIZER
class EssayDefaultSerializer(serializers.Serializer):
    #This is for the id field.
    id = serializers.IntegerField(read_only=True)
    author = serializers.CharField()
    title = serializers.CharField()
    body = serializers.CharField()
    isActive = serializers.BooleanField()
    cre_date = serializers.DateTimeField()
    up_date = serializers.DateTimeField()
    pub_date = serializers.DateField()

    def create(self, validated_data):
        #Coming data is a dictionary. That's why we use **validated_data.
        #So that it opens the dictionary and takes the values.
        return Essay.objects.create(**validated_data)

    #This is for updating the data. And we should check whether the data can be updated or not.
    def update(self, instance, validated_data):
        #If there is a value for author in validated data, then it will be updated.
        #Otherwise, it will remain the same like instance data.
        instance.author = validated_data.get('author', instance.author)
        instance.title = validated_data.get('title', instance.title)
        instance.body = validated_data.get('body', instance.body)
        instance.isActive = validated_data.get('isActive', instance.isActive)
        instance.pub_date = validated_data.get('pub_date', instance.pub_date)
        instance.cre_date = validated_data.get('cre_date', instance.cre_date)
        instance.up_date = validated_data.get('up_date', instance.up_date)
        instance.save() #This is for saving the data.
        return instance 
    
    #Custom Validation
    def validate(self, data):
        if data['title'] == data['body']:
            raise serializers.ValidationError('Title and Body must be different from each other.')
        return data
    
    #If we want to check for only one area, we can use this.
    #This is called object level.
    def validate_title(self, value):
        if len(value) < 20:
            raise serializers.ValidationError(f'Title must be at least 60 characters long. You entered {len(value)} characters.')
        return value
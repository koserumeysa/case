from rest_framework import serializers
from news.models import Essay

class EssaySerializer(serializers.Serializer):
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
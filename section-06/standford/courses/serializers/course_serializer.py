from wsgiref.validate import validator
from rest_framework.serializers import *
from rest_framework.validators import UniqueValidator, UniqueTogetherValidator
from courses.models.course import Course

class CourseSerializer(Serializer):
    id = IntegerField(read_only=True)
    name = CharField(
        max_length=100,
        validators=[
            UniqueValidator(
                queryset=Course.objects.all(),
                message="Course name must be unique"
            )
        ]
    )
    code = CharField(
        validators=[
            UniqueValidator(
                queryset=Course.objects.all(),
                message="Code must be unique"
            )
        ]
    )
    description = CharField(max_length=600)
    # exams = HyperlinkedRelatedField(many=True, read_only=True, view_name='courses:exam-detail')
    exams = StringRelatedField(many=True)

    # fucntion based validator
    def validate_description(self, value):
        """This method validates the description field and ensures there's no swear words -> fuck, shit """
        if value.count("shit") or value.count("fuck") :
            raise ValidationError("Course description violates standford standard")
        return value

    def validate_code(self, value):
        """This method checks if course code starts with CSC """
        if not value.startswith("CSC")  :
            raise ValidationError("Course code must start with CSC")
        return value

    # class Meta:
    #     validators = [
    #         UniqueTogetherValidator(
    #             queryset=Course.objects.all(),
    #             fields=['name', 'code'],
    #             message="Every course must have a unique name and code"
    #         )
    #     ]


    def create(self, validated_data):
        """
        Create and return a new `Course` instance, given the validated data.
        """
        return Course.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Course` instance, given the validated data.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.code = validated_data.get('code', instance.code)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance

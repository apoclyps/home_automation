from rest_framework import serializers


class UUIDField(serializers.UUIDField):
    """This is just a stricter implementation of serializers.UUIDField which
    will explicitly convert data to a string before serialization. The default
    implementation treats other types (such as int) as valid, which is not what
    we want!
    """

    def to_internal_value(self, data):
        return super().to_internal_value(str(data))

    def to_representation(self, value):
        return str(value)

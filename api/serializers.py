from rest_framework import serializers
from django.conf import settings


langs = settings.LANGUAGES


class StdImageSerializer(serializers.ImageField):
    """
    Get all the variations of the StdImageField
    """

    def to_native(self, obj):
        return self.get_variations_urls(obj)

    def to_representation(self, obj):
        if not obj:
            return None
        return self.get_variations_urls(obj)

    def get_variations_urls(self, obj):
        """
        Get all the logo urls.
        """

        # Initiate return object
        return_object = {}

        # Get the field of the object
        field = obj.field

        # A lot of ifs going araound, first check if it has the field variations
        if hasattr(field, 'variations'):
            # Get the variations
            variations = field.variations
            # Go through the variations dict
            for key in variations.keys():
                # Just to be sure if the stdimage object has it stored in the obj
                if hasattr(obj, key):
                    # get the by stdimage properties
                    field_obj = getattr(obj, key, None)
                    if field_obj and hasattr(field_obj, 'url'):
                        # store it, with the name of the variation type into our return object
                        return_object[key] = super(StdImageSerializer, self).to_representation(field_obj)

        # Also include the original (if possible)
        if hasattr(obj, 'url'):
            return_object['original'] = super(StdImageSerializer, self).to_representation(obj)

        return return_object


class NameISOSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    title = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()
    short_description = serializers.SerializerMethodField()
    position = serializers.SerializerMethodField()

    def get_title(self, obj):
        lang_code = self.context["request"].LANGUAGE_CODE
        return getattr(obj, f'title_{lang_code}', None)
        
    def get_name(self, obj):
        lang_code = self.context["request"].LANGUAGE_CODE
        return getattr(obj, f'name_{lang_code}', None)

    def get_short_description(self, obj):
        lang_code = self.context["request"].LANGUAGE_CODE
        return getattr(obj, f'short_description_{lang_code}', None)

    def get_description(self, obj):
        lang_code = self.context["request"].LANGUAGE_CODE
        return getattr(obj, f'description_{lang_code}', None)

    def get_position(self, obj):
        lang_code = self.context["request"].LANGUAGE_CODE
        return getattr(obj, f'position_{lang_code}', None)

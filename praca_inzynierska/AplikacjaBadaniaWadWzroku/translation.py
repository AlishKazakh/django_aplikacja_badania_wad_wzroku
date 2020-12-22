from modeltranslation.translator import register, TranslationOptions
from .models import Test, Exercises, Information, Information1


@register(Test)
class TestTranslationOptions(TranslationOptions):
    fields = ('question', 'option_one', 'option_two', 'option_three', 'option_four', 'answer')


@register(Exercises)
class ExerciseTranslationOptions(TranslationOptions):
    fields = ('text_exercise', 'image_exercise')


@register(Information)
class InformationTranslationOptions(TranslationOptions):
    fields = ('astigmatism_information', 'astigmatism_symptoms', 'astigmatism_treatment', 'color_blindness_information', 'color_blindness_symptoms', 'color_blindness_treatment', 'macular_degeneration_information', 'macular_degeneration_symptoms', 'macular_degeneration_treatment', 'dry_eye_information', 'dry_eye_symptoms', 'dry_eye_treatment')

@register(Information1)
class InformationTranslationOptions(TranslationOptions):
    fields = ('disease_information', 'disease_symptoms', 'disease_treatment', 'disease_name')

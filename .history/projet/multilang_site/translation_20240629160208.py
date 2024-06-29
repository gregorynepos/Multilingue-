from modeltranslation.translator import TranslationOptions, register
from .app.models import Article

@register(Article)
class ArticleTranslationOptions(TranslationOptions):
    fields = ('title', 'content')
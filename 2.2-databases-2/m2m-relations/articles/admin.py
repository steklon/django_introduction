from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Tag, Scope


class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        is_main_counter = 0
        tag_list = list()
        for form in self.forms:
            try:
                if form.cleaned_data:
                    tag_list.append(form.cleaned_data['tag'])
                    if form.cleaned_data['is_main']:
                        is_main_counter += 1
            except KeyError:
                raise ValidationError('Для удаления раздела из статьи используйте "УДАЛИТЬ"')

            if len(tag_list) != len(set(tag_list)):
                raise ValidationError('В статье дублируются разделы')
            if is_main_counter > 1:
                raise ValidationError('Основной раздел может быть только один')
        return super().clean()


class ScopeInline(admin.TabularInline):
    model = Scope
    extra = 3
    formset = ScopeInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'text', 'published_at', 'image']
    inlines = [ScopeInline]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']

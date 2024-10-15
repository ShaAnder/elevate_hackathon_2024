from django import forms
from .models import UserQuestionKnowledge


class UserQuestionKnowledgeForm(forms.ModelForm):
    class Meta:
        model = UserQuestionKnowledge
        fields = ["knowledge_status"]

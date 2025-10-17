from django import forms
from .models import Lead

class LeadForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = ["full_name", "phone", "email", "product", "comment"]
        widgets = {
            "comment": forms.Textarea(attrs={"rows": 4}),
        }

    def clean_full_name(self):
        full_name = self.cleaned_data.get("full_name")
        if not full_name:
            raise forms.ValidationError("Поле Имя обязательно для заполнения.")
        full_name = full_name.strip()
        if len(full_name) < 2:
            raise forms.ValidationError("Имя должно содержать минимум 2 символа.")
        return full_name

    def clean_phone(self):
        phone = self.cleaned_data.get("phone")
        if not phone:
            raise forms.ValidationError("Поле Телефон обязательно для заполнения.")
        phone = phone.strip()
        if not phone.startswith("+7") or len(phone.replace("+", "").replace(" ", "").replace("(", "").replace(")", "")) < 11:
            raise forms.ValidationError("Введите корректный номер телефона.")
        return phone

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if not email:
            return ""
        email = email.strip()
        if "@" not in email:
            raise forms.ValidationError("Введите корректный email.")
        return email

    def clean_comment(self):
        comment = self.cleaned_data.get("comment")
        if not comment:
            return ""
        comment = comment.strip()
        if len(comment) > 300:
            raise forms.ValidationError("Комментарий не должен превышать 300 символов.")
        return comment

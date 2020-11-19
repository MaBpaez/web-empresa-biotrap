from django import forms


class Contacto(forms.Form):
    nombre = forms.CharField(max_length=20)
    asunto = forms.CharField(max_length=50)
    correo = forms.EmailField(max_length=100)
    telefono = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "type": "tel",
                "pattern": "[0-9]{9}",
                "placeholder": "Teléfono 123456789",
            }
        ),
        max_length=10,
    )
    mensaje = forms.CharField(
        widget=forms.Textarea(attrs={"placeholder": "Su mensaje...", "rows": "6"})
    )
    politica = forms.BooleanField(required=False)

    # widgets
    nombre.widget.attrs.update({"placeholder": "Nombre", "pattern": "[A-Za-z ]{3,20}"})
    asunto.widget.attrs.update(
        {"placeholder": "Asunto", "pattern": "[A-Za-z ]{3,50}"}
    )
    correo.widget.attrs.update({"placeholder": "correo@correo.com"})

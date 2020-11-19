from django.shortcuts import render, redirect
from .forms import Contacto


def home(request):
    if request.method == "POST":
        # vinculamos el formulario
        form = Contacto(request.POST)
        if form.is_valid():
            from django.core.mail import send_mail
            cd = form.cleaned_data

            # enviamos datos al correo
            send_mail(
                f"Asunto: {cd['asunto']}",
                f"Nombre: {cd['nombre']}\n"
                f"Teléfono: {cd['telefono']}\nCorreo electrónico: {cd['correo']}\n"
                f"Mensaje:\n\n{cd['mensaje']}",
                "bravopaezm.15@gmail.com",
                ["bravopaezm.15@gmail.com"],
            )

            # redireccionamos usando redirect y el nombre de la vista successfully
            return redirect('successfully')
    else:
        # formulari sin vincular
        form = Contacto()

    return render(request, "core/home.html", {"form": form})


def successfully(request):
    return render(request, 'core/successfully.html')

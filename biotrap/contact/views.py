from django.shortcuts import render, redirect
from .forms import Contacto


def contact(request):
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

            # redireccionamos
            return redirect('successfully')
    else:
        # formulari sin vincular
        form = Contacto()

    return render(request, "contact/contact.html", {"form": form})

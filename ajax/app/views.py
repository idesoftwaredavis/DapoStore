from django.views.generic import TemplateView
from django.shortcuts import redirect, render
from django.http import JsonResponse


from app.forms import ContactForm
def contact_form(request):
    # Hago el llamado del formulario
    form = ContactForm()
    if request.method == 'POST' and request.is_ajax():
        # relleno los datos del usuario en los campos del formulario
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            form.save()
            return JsonResponse(
            {
                'name':name
            }, status=200)
        else:
            errors = forms.errors.as_json()
            return JsonResponse({'errors':errors}, status=400)
    return render(request, 'contact.html', {'form':form})

from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import send_mail
from django.contrib import messages
from .models import Contact
from .forms import ContactForm

def contact_list(request):
    query = request.GET.get('search')
    if query:
        contacts = Contact.objects.filter(name__icontains=query) | Contact.objects.filter(email__icontains=query)
    else:
        contacts = Contact.objects.all()
    return render(request, 'contact_list.html', {'contacts': contacts})

def add_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save()
            messages.success(request, 'Contact added successfully!')
            return redirect('contact_list')
    else:
        form = ContactForm()
    return render(request, 'add_contact.html', {'form': form})

def delete_contact(request, contact_id):
    contact = get_object_or_404(Contact, id=contact_id)
    contact.delete()
    messages.success(request, 'Contact deleted successfully!')
    return redirect('contact_list')

def send_contact_email(request, contact_id):
    contact = get_object_or_404(Contact, id=contact_id)
    if request.method == 'POST':
        recipient_email = request.POST.get('recipient_email')
        send_mail(
            f'Contact Details: {contact.name}',
            f'Name: {contact.name}\nEmail: {contact.email}\nPhone: {contact.phone_number}\nAddress: {contact.address}',
            'your-email@example.com',
            [recipient_email]
        )
        messages.success(request, 'Contact details sent successfully!')
        return redirect('contact_list')
    return render(request, 'send_contact_email.html', {'contact': contact})


from django.shortcuts import render, get_object_or_404, redirect
from .models import Contact
from .forms import ContactForm

def contact_list(request):
    contacts = Contact.objects.all()
    return render(request, 'phonebook/contact_list.html', {'contacts': contacts})

def add_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact_list')
    else:
        form = ContactForm()
    return render(request, 'phonebook/add_contact.html', {'form': form})

def edit_contact(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect('contact_list')
    else:
        form = ContactForm(instance=contact)
    return render(request, 'phonebook/edit_contact.html', {'form': form})

def delete_contact(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    contact.delete()
    return redirect('contact_list')

def search_contact(request):
    if 'q' in request.GET:
        query = request.GET['q']
        results = Contact.objects.filter(name__icontains=query)
        return render(request, 'phonebook/search_contact.html', {'results': results, 'query': query})
    else:
        return render(request, 'phonebook/search_contact.html')


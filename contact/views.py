from django.shortcuts import render, get_object_or_404, redirect
from .models import Person
#from django.urls import reverse_lazy
#from django.views.generic import View, CreateView


#class Person(CreateView):
#	model = Person
#	success_url = reverse_lazy("contact")


def contact_list(request):
	persons = Person.objects.all().order_by('first_name')
	return render(request, 'contact/contact_list.html', {'persons': persons})

def contact_new(request):
	if request.method == 'POST':
		form = PersonForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')
	else:
		form = PersonForm()
	return render(request, 'contact/contact_edit.html', {'form': form})

def contact_edit(request, pk):
	person = get_object_or_404(Person, pk=pk)
	if request.method == 'POST':
		form = PersonForm(request.POST, instance=person)
		if form.is_valid():
			form.save()
			return redirect('/person/' + str(person.pk))
	else:
		form = PersonForm(instance=person)
	return render(request, 'contact/contact_edit.html', {'form': form})

from django.shortcuts import render, get_object_or_404
from .models import Note


# Each def represents one section of notes and code snippets.
def my_python(request):
    python_notes = Note.objects.filter(category__category="Python", sub_category__sub_category="Notes")
    python_snippets = Note.objects.filter(category__category="Python", sub_category__sub_category="Code_Snippets")
    context = {
        'python_notes': python_notes,
        'python_snippets': python_snippets
    }
    return render(request, 'notes/my_python.html', context)

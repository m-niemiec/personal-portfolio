from django.shortcuts import render, get_object_or_404
from .models import Note


def my_notes(request):
    category = request.GET['category']
    notes = Note.objects.filter(category__category=category, sub_category__sub_category="Notes")
    snippets = Note.objects.filter(category__category=category, sub_category__sub_category="Code_Snippets")
    context = {
        'notes': notes,
        'snippets': snippets,
        'category': category
    }
    return render(request, 'my_notes.html', context)

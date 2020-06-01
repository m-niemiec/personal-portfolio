from django.shortcuts import render, get_object_or_404
from .models import Note


def my_python(request):
    notes = Note.objects.all()
    python_notes = Note.objects.filter(category__category="Python", sub_category__sub_category="Notes")
    python_notes_number = 1
    python_snippets = Note.objects.filter(category__category="Python", sub_category__sub_category="Code_Snippets")
    python_snippets_number = 1
    context = {
        'notes': notes,
        'python_notes': python_notes,
        'python_notes_number': python_notes_number,
        'python_snippets': python_snippets,
        'python_snippets_number': python_snippets_number
    }
    return render(request, 'notes/my_python.html', context)


def view_note(request, note_id):
    note = get_object_or_404(Note, pk=note_id)
    context = {
        'note': note
    }
    return render(request, 'notes/view_note.html', context)

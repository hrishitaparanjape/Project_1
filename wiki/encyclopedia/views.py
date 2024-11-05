from django.shortcuts import render
from .util import get_entry
import markdown
from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, entry_name):
    content = get_entry(entry_name)
    if content:
        return render(request, "encyclopedia/entry.html",{"title": entry_name, "content": content})
    else:
        return render(request, "error.html", {"message": "Entry not found"})

from django.shortcuts import render, redirect
from .models import Note
from .models import Tag

def index(request):
    if request.method == 'POST':
        acao = request.POST.get('acao')

        if acao == 'add':
            title = request.POST.get('titulo')
            content = request.POST.get('detalhes')
            tag_id = request.POST.get('tag')
            tag = Tag.objects.get(id=tag_id)
            n = Note(title=title, content=content, tag=tag)
            n.save()

        if acao == 'delete':
            note_id = request.POST.get('note_id')
            Note.objects.filter(id = note_id).delete()
            
        if acao == 'edit':
            note_id = request.POST.get('note_id')
            novo_title = request.POST.get('novo_titulo')
            novo_content = request.POST.get('nova_desc')
            id_nova_tag = request.POST.get('nova_tag')
            tag = Tag.objects.get(id = id_nova_tag)
            Note.objects.filter(id = note_id).update(title=novo_title, content=novo_content, tag=tag)

        if acao == "addTag":
            new_tag_name = request.POST.get('new_tag_name')
            t = Tag(name = new_tag_name)
            t.save()

        if acao == "removeTag":
            tag_id_delete = request.POST.get('tag_id_delete')
            Tag.objects.filter(id = tag_id_delete).delete()

        if acao == "filtrar":
            valor_filtro = request.POST.get('valor_filtro')
            if valor_filtro == '0':
                return redirect('index')
            tag_filter = Tag.objects.get(id = valor_filtro)
            filtered_notes = Note.objects.filter(tag = tag_filter)
            all_tags = Tag.objects.all().exclude(id = 1)
            return render(request, 'notes/index.html', {'notes': filtered_notes, 'tags': all_tags})

        return redirect('index')

    else:
        all_notes = Note.objects.all()
        all_tags = Tag.objects.all().exclude(id = 1)
        return render(request, 'notes/index.html', {'notes': all_notes, 'tags': all_tags})
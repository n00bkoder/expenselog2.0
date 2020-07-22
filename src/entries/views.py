from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from. models import Entry
from .forms import EntryForm


from django.db.models import Sum

@login_required
def log_create_view(request):
    # Display form for user
    form = EntryForm(request.POST or None)
    if form.is_valid():
        # save data for the current user
        form = form.save(commit=False)
        form.user = request.user
        form.save()
        return redirect('/entries')
    current_user = request.user

    context = {
        'form': form,
        'current_user': current_user
    }
    return render(request, 'entries/create.html', context)


@login_required
def entry_view(request):
    current_user = request.user
    # gets list of objects for the current user
    entry_list = Entry.objects.filter(user=current_user) 
    total = Entry.objects.filter(user=current_user).aggregate(Sum('cost'))['cost__sum'] or 0.00

    context = {
        'entry_list': entry_list,
        'current_user': current_user,
        'total': total,
        
    }
    return render(request, 'entries/list.html', context)


@login_required
def update_view(request, id):
    # gets Log objects by id but only for current user
    instance = get_object_or_404(Entry, id=id, user=request.user)
    # Displays form to be updated and also shows previously entered data in the form fields
    form = EntryForm(initial={'item': instance.item, 'cost': instance.cost},
    instance=instance)
    if request.method == 'POST':
        form = EntryForm(request.POST, instance=instance)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()
            return redirect('/entries')
    current_user = request.user
    
    context = {
        'form': form,
        'instance': instance,
        'current_user': current_user,
    }
    return render(request, 'entries/update.html', context)

@login_required
def delete_view(request, id):
    # gets object by id for current user and deletes
    instance = get_object_or_404(Entry, id=id, user=request.user)
    if request.method == "POST":
        instance.delete()
        return redirect('/entries')
    current_user = request.user
    context = {
        "instance": instance,
        'current_user': current_user,
        
    }
    return render(request, "entries/delete.html", context)



    
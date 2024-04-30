from django.shortcuts import render, redirect

from apps.fasts.models import Fast
from apps.reviews.models import Reviews


def index(request):
    fasts = Fast.objects.all()

    context = {
        "fasts": fasts,
    }

    return render(request, "index.html", context=context)


def create_fasts(request):
    if request.method == "POST":
        title = request.POST['title']
        description = request.POST['description']
        image = request.FILES['image']

        Fast.objects.create(
            user=request.user,
            title=title,
            description=description,
            image=image,
        )
        return redirect('homepage')

    return render(request, 'create_blog.html')


def detail_fasts(request, pk):
    try:
        fast = Fast.objects.get(id=pk)
    except Fast.DoesNotExist:
        ...

    if request.method == 'POST':
        text = request.POST['text']

        Reviews.objects.create(
            user=request.user,
            fast=fast,
            text=text,
        )
        return redirect('detail_fast', fast.id)

    return render(request, 'base/../../templates/detail.html', locals())


def delete_fasts(request, pk):
    try:
        fast = Fast.objects.get(id=pk)
    except Fast.DoesNotExist:
        ...

    if fast is not None:
        fast.delete()
        return redirect('homepage')
    else:
        return redirect('homepage')


def update_fasts(request, pk):
    fast = Fast.objects.get(id=pk)

    if request.method == "POST":
        title = request.POST['title']
        description = request.POST['description']
        image = request.FILES['image']

        fast.title = title
        fast.description = description
        fast.image = image
        fast.save()

        return redirect('detail_fast', fast.id)

    return render(request, 'update_reviews.html', locals())
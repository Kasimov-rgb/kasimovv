from django.shortcuts import render, redirect

from apps.reviews.models import Reviews


def delete_reviews(request, pk):
    reviews = Reviews.objects.get(id=pk)
    reviews.delete()
    return redirect('homepage')


def update_reviews(request, pk):
    reviews = Reviews.objects.get(id=pk)

    if request.method == 'POST':
        text = request.POST['text']
        reviews.txt = text
        reviews.save()

        return redirect('homepage')

    return render(request, 'update_reviews.html', locals())

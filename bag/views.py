from django.shortcuts import render


def view_bag(request):
    ''' A view that render the bag contents page '''

    return render(request, 'bag/bag.html')
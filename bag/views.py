from django.shortcuts import render, redirect


def view_bag(request):
    ''' A view that render the bag contents page '''

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    '''  Add a quantity of the specified product to the shopping bag '''

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    # Get the http session named bag if it exists
    # and if not create it and set it to an empty dic
    bag = request.session.get('bag', {})

    # Check if the product exists and if so add the quantity selected to it
    # and if not create a key/val pair of item_id/qty,
    # reassign the value to the session variable
    if item_id in list(bag.keys()):
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity

    request.session['bag'] = bag
    print(request.session['bag'])
    return redirect(redirect_url)

from django.shortcuts import render

def welcome(request):
    return render(request, 'index.html', {'msg':'Hello World!'})

def restaurant_list(request):

    context = {
        'my_list' : [{"restaurant_name":'chipotle',"food_type":'mexican'},{"restaurant_name":'nandos',"food_type":'chicken'},{"restaurant_name":'lucalis',"italian":''}]

    }
    return render(request, 'list.html', context)


def restaurant_detail(request):

    context = {
        'my_object' : {"restaurant_name":'dominos',"food_type":'italian'}
    }
    return render(request, 'detail.html', context)

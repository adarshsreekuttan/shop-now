from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate


def customer_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        if user is not None:
            if user.role != 'customer':
                return render(request, 'customer/login.html',
                              {'error': "Seller cannot login here"})
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'customer/login.html',
                          {"error": "Invalid email or password"})

    return render(request, 'customer/login.html')
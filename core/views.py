from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth import get_user_model

User = get_user_model()


def user_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, username=email, password=password)

       
        if user is None:
            try:
                user_obj = User.objects.get(email=email)
                user = authenticate(request, username=user_obj.username, password=password)
            except User.DoesNotExist:
                user = None

        
        if user is None:
            messages.error(request, "Invalid email or password")
            return redirect('user_login')

  
        if user.is_superuser:
            login(request, user)
            return redirect('admin_dashboard')

        
        elif hasattr(user, 'role') and user.role == 'customer':
            login(request, user)
            return redirect('home')

       
        elif hasattr(user, 'role') and user.role == 'seller':
            try:
                sellerprofile = user.seller_profile
            except:
                messages.error(request, "Seller profile not found")
                return redirect('user_login')

            if not sellerprofile.approved:
                messages.error(request, "Waiting for admin approval")
                return redirect('user_login')

            login(request, user)
            return redirect('seller_home')

       
        else:
            messages.error(request, "Invalid user role")
            return redirect('user_login')

    return render(request, 'core/login.html')
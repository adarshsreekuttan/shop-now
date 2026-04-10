from django.shortcuts import render,redirect
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required
from customer.models import *
from core.models import *
from seller.models import *
from custom_admin.models import *
from django.contrib import messages
# from custom_admin.decorators import admin_required
# from django.contrib.auth.decorators import login_required


# Create your views here.

# @login_required
# @admin_required
def admin_dashboard(request):

    total_users = User.objects.all().count()
    total_products = Product.objects.all().count()
    total_sellers = SellerProfile.objects.all().count()
    total_orders = Order.objects.all().count()

    context = {
        'total_users' : total_users,
        'total_products' : total_products,
        'total_sellers' : total_sellers,
        'total_orders' : total_orders 
    }

    return render(request,'admin/admindashboard.html', context )


# @login_required
# @admin_required
def admin_pending_products(request):
    products = Product.objects.filter(status='pending')
    messages.success(request,'Product approved successfully')
    return render(request,'admin/pending_products.html',{'products': products}) 


# @login_required
# @admin_required
def approve_products(request,id):
    products = Product.objects.get(id=id)
    products.status = 'approved'
    products.save()
    return redirect('pending_products')


# @login_required
# @admin_required
def reject_products(request,id):
    products = Product.objects.get(id)
    products.status = 'rejected'
    products.save()
    return redirect('pending_products')


# @login_required
# @admin_required
def products_view(request):
    products = Product.objects.all()
    return render(request,'admin/productview.html',{'products':products})


# @login_required
# @admin_required
def edit_product(request,id):
    products = Product.objects.get(id=id)
    category = Category.objects.all()
    subcategory = SubCategory.objects.all()
    seller = SellerProfile.objects.all()
    product_status = products.status

    if request.method  == 'POST':

        products.seller_id = request.POST.get('seller')
        products.name = request.POST.get('name')
        products.price = request.POST.get('price')
        products.discount_price = request.POST.get('discount_price')
        products.status = product_status
        products.description = request.POST.get('description')
        products.stock = request.POST.get('stock')
        products.category_id = request.POST.get('category')
        products.sub_category_id = request.POST.get('subcategory')
        products.save()

        return redirect('product_view')

    return render(request,'admin/edit_product.html',{'products':products, 'category':category, 'subcategory':subcategory, 'seller':seller})   


# @login_required
# @admin_required
def deactivate_product(request,id):
    product = Product.objects.get(id=id)
    product.is_active = False
    product.save()
    return redirect('product_view')


# @login_required
# @admin_required
def delete_product(request,id):
    products = Product.objects.get(id=id)
    products.delete()
    return redirect('product_view')


# @login_required
# @admin_required
def deactive_product_list(request):
    product = Product.objects.filter(is_active=False)
    return render(request,'admin/deactive_product.html',{'product':product})


# @login_required
# @admin_required
def reapprove_product(request,id):
    product = Product.objects.get(id=id)
    product.is_active = True
    product.save()
    return redirect('deactive_product_list')


# @login_required
# @admin_required
def seller_view(request):
    sellers = SellerProfile.objects.all()
    return render(request,'admin/sellerview.html',{'sellers':sellers})


# @login_required
# @admin_required
def order_view(request):
    orders = Order.objects.all()
    return render(request,'admin/orderview.html',{'orders':orders})   


# @login_required
# @admin_required
def order_details(request,id):
    orders = Order.objects.get(id=id)
    order_items = OrderItem.objects.all()
    return render(request,'admin/order_details.html',{'orders':orders, 'order_items':order_items})


# @login_required
# @admin_required
def delete_order(request,id):
    orders = Order.objects.get(id=id)
    orders.delete()
    return redirect('order_view')


# @login_required
# @admin_required
def user_view(request):
    users = User.objects.filter(is_superuser=False)
    return render(request,'admin/userview.html',{'users':users})


# @login_required
# @admin_required
def deactivate_user(request,id):
    user = User.objects.get(id=id)
    user.is_active = False
    user.save()
    return redirect('user_view')


# @login_required
# @admin_required
def deactive_user_list(request):
    user = User.objects.filter(is_active=False)
    return render(request,'admin/deactive_user.html',{'user':user})


# @login_required
# @admin_required
def reapprove_user(request,id):
    user = User.objects.get(id=id)
    user.is_active = True
    user.save()
    return redirect('deactive_user_list')


# @login_required
# @admin_required
def add_category(request):
    if request.method == 'POST':
        name = request.POST.get('name') 
        description = request.POST.get('description')
        image = request.FILES.get('image')

        Category.objects.create(

            name = name,
            description = description,
            image = image

        )  

        return redirect('category_list')
    
    return render(request,'admin/add_category.html') 


# @login_required
# @admin_required
def category_list(request):
    categories = Category.objects.filter(is_active=True)
    return render(request,'admin/category_list.html',{'categories':categories})


# @login_required
# @admin_required
def delete_category(request,id):
    categories = Category.objects.get(id=id)
    categories.delete()
    return redirect('category_list') 


# @login_required
# @admin_required
def update_category(request,id):
    category = Category.objects.get(id=id)
    if request.method == 'POST':
        category.name = request.POST.get('name') 
        category.description = request.POST.get('description')
        category.image = request.FILES.get('image')
        category.save()

        return redirect('category_list')
    
    return render(request,'admin/update_category.html',{'category':category})


# @login_required
# @admin_required
def reapprove_category(request,id):
    category = Category.objects.get(id=id)
    category.is_active = True
    category.save()
    return redirect('category_list')


# @login_required
# @admin_required
def deactivate_category(request,id):
    category = Category.objects.get(id=id)
    category.is_active = False
    category.save()
    return redirect('category_list')


# @login_required
# @admin_required
def deactive_category_list(request):
    category = Category.objects.filter(is_active=False)
    return render(request,'admin/deactive_category.html',{'category':category})


# @login_required
# @admin_required
def add_subcategory(request):
    categories = Category.objects.filter(is_active=True)
    if request.method == "POST":
        name = request.POST.get('name')
        category_id = request.POST.get('category')
        category = Category.objects.get(id=category_id)

        SubCategory.objects.create(

            name = name,
            category = category

        )

        return redirect('subcategory_list')

    return render(request,'admin/add_subcategory.html',{'categories':categories})  


# @login_required
# @admin_required
def subcategory_list(request):
    subcategories = SubCategory.objects.all()
    return render(request,'admin/subcategory_list.html',{'subcategories':subcategories})


# @login_required
# @admin_required
def update_subcategory(request,id):
    subcategory = SubCategory.objects.get(id=id)
    categories = Category.objects.all()
    if request.method == 'POST':
        subcategory.name = request.POST.get('name')
        subcategory.category_id = request.POST.get('category')
        subcategory.save()
        return redirect('subcategory_list')
    
    return render(request,'admin/update_subcategory.html',{'subcategory':subcategory , 'categories':categories})


# @login_required
# @admin_required
def delete_subcategory(request,id):
    subcategories = SubCategory.objects.get(id=id)
    subcategories.delete()
    return redirect('subcategory_list')


# @login_required
# @admin_required
def deactivate_subcategory(request,id):
    subcategories = SubCategory.objects.get(id=id)
    subcategories.is_active = False
    subcategories.save()
    return redirect('subcategory_list')


# @login_required
# @admin_required
def deactive_subcategory_list(request):
    subcategory = SubCategory.objects.filter(is_active=False)
    return render(request,'admin/deactive_subcategory.html',{'subcategory':subcategory})


# @login_required
# @admin_required
def reapprove_subcategory(request,id):
    subcategory = SubCategory.objects.get(id=id)
    subcategory.is_active = True
    subcategory.save()
    return redirect('subcategory_list')


# @login_required
# @admin_required
def seller_details(request,id):
    sellers = SellerProfile.objects.get(id=id)
    return render(request,'admin/seller_details.html',{'sellers':sellers}) 


# @login_required
# @admin_required
def deactivate_seller(request,id):
    sellers = SellerProfile.objects.get(id=id)
    sellers.is_active = False
    sellers.save()
    return redirect('seller_view')


# @login_required
# @admin_required
def pending_seller(request):
    sellers  = SellerProfile.objects.filter(approved=False, is_active=True)
    count = SellerProfile.objects.count()
    messages.success(request,'Seller approved successfully')
    return render(request,'admin/pending_seller.html',{'sellers':sellers, 'count':count})


# @login_required
# @admin_required
def approve_seller(request,id):
    sellers = SellerProfile.objects.get(id=id)
    sellers.approved = True
    sellers.save()
    return redirect('pending_seller')


# @login_required
# @admin_required
def deactive_seller_list(request):
    seller = SellerProfile.objects.filter(is_active=False)
    return render(request,'admin/deactive_seller.html',{'seller':seller})


# @login_required
# @admin_required
def reapprove_seller(request,id):
    seller = SellerProfile.objects.get(id=id)
    seller.is_active = True
    seller.save()
    return redirect('deactive_seller_list')
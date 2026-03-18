from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Product
from django.db.models import Sum
from datetime import datetime
from billing.models import Invoice

@login_required
def dashboard_view(request):
    total_products = Product.objects.count()
    low_stock_products = Product.objects.filter(stock_quantity__lt=10)
    recent_invoices = Invoice.objects.order_by('-date')[:5]
    
    # Calculate daily and monthly sales
    today = datetime.now().date()
    daily_sales = Invoice.objects.filter(date__date=today).aggregate(total=Sum('total_amount'))['total'] or 0
    monthly_sales = Invoice.objects.filter(date__month=today.month, date__year=today.year).aggregate(total=Sum('total_amount'))['total'] or 0
    total_sales = Invoice.objects.aggregate(total=Sum('total_amount'))['total'] or 0

    context = {
        'total_products': total_products,
        'low_stock_count': low_stock_products.count(),
        'low_stock_alerts': low_stock_products,
        'recent_invoices': recent_invoices,
        'daily_sales': daily_sales,
        'monthly_sales': monthly_sales,
        'total_sales': total_sales,
    }
    return render(request, 'dashboard.html', context)

@login_required
def product_list(request):
    products = Product.objects.all()
    return render(request, 'inventory/product_list.html', {'products': products})

@login_required
def product_add(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        stock_quantity = request.POST.get('stock_quantity')
        image = request.FILES.get('image')
        
        Product.objects.create(
            name=name,
            description=description,
            price=price,
            stock_quantity=stock_quantity,
            image=image
        )
        messages.success(request, "Product added successfully.")
        return redirect('product_list')
    return render(request, 'inventory/product_form.html')

@login_required
def product_edit(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.name = request.POST.get('name')
        product.description = request.POST.get('description')
        product.price = request.POST.get('price')
        product.stock_quantity = request.POST.get('stock_quantity')
        
        if request.FILES.get('image'):
            product.image = request.FILES.get('image')
            
        product.save()
        messages.success(request, "Product updated successfully.")
        return redirect('product_list')
    return render(request, 'inventory/product_form.html', {'product': product})

@login_required
def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        messages.success(request, "Product deleted successfully.")
        return redirect('product_list')
    return render(request, 'inventory/product_confirm_delete.html', {'product': product})

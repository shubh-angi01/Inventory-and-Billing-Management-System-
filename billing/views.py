from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Invoice, InvoiceItem
from inventory.models import Product
from django.db import transaction

@login_required
def invoice_list(request):
    invoices = Invoice.objects.all().order_by('-date')
    return render(request, 'billing/invoice_list.html', {'invoices': invoices})

@login_required
def invoice_detail(request, pk):
    invoice = get_object_or_404(Invoice, pk=pk)
    return render(request, 'billing/invoice_detail.html', {'invoice': invoice})

@login_required
def create_invoice(request):
    products = Product.objects.all()
    if request.method == 'POST':
        customer_name = request.POST.get('customer_name')
        product_ids = request.POST.getlist('product_id[]')
        quantities = request.POST.getlist('quantity[]')
        
        if not product_ids:
            messages.error(request, "Please add at least one product to the invoice.")
            return render(request, 'billing/create_invoice.html', {'products': products})

        try:
            with transaction.atomic():
                invoice = Invoice.objects.create(customer_name=customer_name)
                total_amount = 0
                
                for p_id, qty in zip(product_ids, quantities):
                    p_id = int(p_id)
                    qty = int(qty)
                    product = Product.objects.get(id=p_id)
                    
                    if product.stock_quantity < qty:
                        raise ValueError(f"Insufficient stock for {product.name}")
                    
                    item_price = product.price
                    InvoiceItem.objects.create(
                        invoice=invoice,
                        product=product,
                        quantity=qty,
                        price=item_price
                    )
                    
                    # Update stock
                    product.stock_quantity -= qty
                    product.save()
                    
                    total_amount += (item_price * qty)
                
                invoice.total_amount = total_amount
                invoice.save()
                
                messages.success(request, f"Invoice {invoice.invoice_number} created successfully.")
                return redirect('invoice_detail', pk=invoice.pk)
        except ValueError as e:
            messages.error(request, str(e))
        except Exception as e:
            messages.error(request, "An error occurred while creating the invoice.")

    return render(request, 'billing/create_invoice.html', {'products': products})

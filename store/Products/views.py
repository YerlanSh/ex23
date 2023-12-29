from django.shortcuts import render, get_object_or_404, redirect
from django_datatables_view.base_datatable_view import BaseDatatableView

from .forms import ProductForm, ProductCategoryForm
from .models import Product, ProductCategory


# ProductCategory методы:
# - Создание, обновление и удаление категорий продуктов.
# - Связь с продуктами для классификации товаров по категориям.

def category_list(request):
    categories = ProductCategory.objects.all()
    return render(request, 'category_list.html', {'categories': categories})

def category_detail(request, pk):
    category = get_object_or_404(ProductCategory, pk=pk)
    return render(request, 'category_detail.html', {'category': category})

def category_create(request):
    if request.method == 'POST':
        form = ProductCategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = ProductCategoryForm()
    return render(request, 'category_form.html', {'form': form})

def update_category(request, pk):
    category = get_object_or_404(ProductCategory, pk=pk)
    if request.method == 'POST':
        form = ProductCategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = ProductCategoryForm(instance=category)
    return render(request, 'category_form.html', {'form': form})

def category_delete(request, pk):
    category = get_object_or_404(ProductCategory, pk=pk)
    if request.method == 'POST':
        category.delete()
        return redirect('product_list')
    return render(request, 'category_confirm_delete.html', {'category': category})

# Products методы:
# - Создание, обновление и удаление продуктов.
# - Методы для управления количеством товаров на складе.
# - Методы для поиска и фильтрации продуктов по различным параметрам.

class ProductlistJson(BaseDatatableView):
    model = Product
    columns = ['name', 'category', 'price', 'quantity']
    order_columns = ['name', 'category__category_name', 'price', 'quantity']

    def filter_queryset(self, qs):
        search = self.request.GET.get('search[value]', None)
        if search:
            qs = qs.filter(name__icontains=search) | qs.filter(category__category_name__icontains=search)
        return qs

product_list = ProductlistJson.as_view()
def product_list(request):
    products = Product.objects.all()
    categories = ProductCategory.objects.all()
    return render(request, 'product_list.html', {'products': products, 'categories': categories})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product_detail.html', {'product': product})

def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'product_form.html', {'form': form})

def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'product_form.html', {'form': form})

def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(request, 'product_confirm_delete.html', {'product': product})
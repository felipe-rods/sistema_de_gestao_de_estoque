from django.db.models import Sum, F
from django.utils import timezone
from django.utils.formats import number_format
from brands.models import Brand
from categories.models import Category
from outflows.models import Outflow
from products.models import Product


def get_product_metrics():
    products = Product.objects.all()
    total_cost_price = sum(product.cost_price * product.quantity for product in products)
    total_sale_price = sum(product.sale_price * product.quantity for product in products)
    total_quantity = sum(product.quantity for product in products)
    total_profit = total_sale_price - total_cost_price

    return dict(
        total_cost_price=number_format(total_cost_price, decimal_pos=2, force_grouping=True),
        total_sale_price=number_format(total_sale_price, decimal_pos=2, force_grouping=True),
        total_quantity=total_quantity,
        total_profit=number_format(total_profit, decimal_pos=2, force_grouping=True),
    )


def get_sales_metrics():
    total_sales = Outflow.objects.count()
    total_sold_products = Outflow.objects.aggregate(
        total_sold_products=Sum('quantity')
    )['total_sold_products'] or 0
    total_sales_value = sum(outflow.quantity * outflow.product.sale_price for outflow in Outflow.objects.all())
    total_sales_cost = sum(outflow.quantity * outflow.product.cost_price for outflow in Outflow.objects.all())
    total_sales_profit = total_sales_value - total_sales_cost


    return dict(
        total_sales=total_sales,
        total_sold_products=total_sold_products,
        total_sales_value=number_format(total_sales_value, decimal_pos=2, force_grouping=True),
        total_sales_profit=number_format(total_sales_profit, decimal_pos=2, force_grouping=True),
    )


def get_daily_sales_data():
    today = timezone.now().date()
    dates = [str(today - timezone.timedelta(days=i)) for i in range(6, -1, -1)]
    values = list()
    for date in dates:
        total_sales = Outflow.objects.filter(
            created_at__date=date
        ).aggregate(
            sales_total=Sum(F('product__sale_price') * F('quantity'))
        )['sales_total'] or 0
        values.append(float(total_sales))

    return dict(
        dates=dates,
        values=values,
    )


def get_daily_sales_quantity_data():
    today = timezone.now().date()
    dates = [str(today - timezone.timedelta(days=i)) for i in range(6, -1, -1)]
    quantities = list()

    for date in dates:
        sales_quantity = Outflow.objects.filter(created_at__date=date).count()
        quantities.append(sales_quantity)

    return dict(
        dates=dates,
        values=quantities,
    )


def graphic_product_category_metric():
    categories = Category.objects.all()
    return {category.name: Product.objects.filter(category=category).count() for category in categories}


def graphic_product_brand_metric():
    brands = Brand.objects.all()
    return {brand.name: Product.objects.filter(brand=brand).count() for brand in brands}

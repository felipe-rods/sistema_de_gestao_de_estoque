from django.db.models import Sum
from django.utils.formats import number_format
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

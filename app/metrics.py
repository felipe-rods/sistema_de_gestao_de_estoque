from django.utils.formats import number_format
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

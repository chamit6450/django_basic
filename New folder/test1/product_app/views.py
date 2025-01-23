from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, Http404

# # Create your views here.

# products = {
#     1:{'name': 'Laptop', 'price': 1500},
#     2:{'name': 'Phone', 'price': 2500},
#     3:{'name': 'Earbuds', 'price': 1300},
# }

# def home(request):
#     return HttpResponse("<h1>Welcome to product store</h1>")

# def all_products(request):
#     product_item = {product['name']: product['price'] for product in products.values()}
#     return JsonResponse(product_item)

# # dynamic URL
# def products_details_by_id(request, product_id):
#     product = products.get(int(product_id))

#     if product:
#         return HttpResponse(
#             f"<h1>Product Details</h1>"
#             f"<p> Name: {product['name']} </p>"
#             f"<p> Price: {product['price']} </p>"
#         )
#     else:
#         raise Http404(f"Product with ID {product_id} not found")
    
# def products_details_by_name(request, product_name):
#     # product = products.get((product_name))
#     for product in products.values():
#         if product['name'] == product_name:
#            return HttpResponse(
#              f"<h1>Product Details</h1>"
#              f"<p> Name: {product['name']} </p>"
#              f"<p> Price: {product['price']} </p>"
#          )
#         else:
#             raise Http404(f"Product with name {product_name} not found")

# # Query params
# from django.http import HttpResponse

# def filter_products(request):
#     max_price = request.GET.get('max_price')

#     if max_price:
#         try:
#             max_price = int(max_price)
#             filtered = [pro for pro in products.values() if pro['price'] <= max_price]

#             if filtered:
#                 response = "<h1>Filtered Products are:</h1>"
#                 for product in filtered: 
#                     response += f"<p>{product['name']} : {product['price']}</p>"
#                 return HttpResponse(response)
#             else:
#                 return HttpResponse("<h1>No products found under the specified price.</h1>")
#         except ValueError:
#             return HttpResponse("<h1>Invalid price. Please provide a valid number.</h1>")
#     else:
#         return HttpResponse("<h1>Please provide a max_price query parameter.</h1>")


def home(request):
    return HttpResponse("welcome to regex");

def about(request):
    return HttpResponse("<h1>welcome to about regex</h1>");

def user(request, username):
    return HttpResponse(f"<h1>username: {username}</h1>");

def blog(request, year, month, slug):
    return HttpResponse(f"<h1>blog: {slug} ({year} - {month})</h1>");
    
# ================================================
# ======== GIVEN CODE - DO NOT MODIFY ============
# ================================================

calls = []
new_products = []


def update_product_price(new_price=None):
    calls.append(new_price)


def add_new_product(product_name, products=new_products):
    products.append(product_name)


def get_total_number_of_sales():
    return 2000


def get_france_sales():
    return 1500


def get_england_sales():
    return 1800


def get_best_selling_product():
    return "apples"

# ================================================
# =============== end given code =================
# ================================================


# Call "update_product_price" with no parameters

# Call "update_product_price" with the first parameter equal to 3


# Create a function named "total_revenue", that returns 40000


# Create a function named "revenue_after_tax", that has one parameter "revenue"
# It should return "revenue" times 0.9


# Create a function named "money_earnt", that has two parameters :
# "nb_units_sold" and "unit_price", and returns the product of the two params


# Create a function named "money_earnt2", that has two parameters :
# "nb_units_sold" and "unit_price"
# "unit_price" should have a default value of 10
# The function should return the product of the two params


# Create a function named "print_euro_to_dollar" with one parameter
# that prints the first parameter times 1.1


# Create a function named "print_euro_to_dollar" with one parameter that
# * Creates a variable "dollar" that is equal to the param times 1.1
# * Prints the value of dollar
# * returns dollar


# Create a function named "print_total_number_of_sales", that prints the value
# returned by "get_total_number_of_sales()"


# Create a function named "europe_sales" that prints and returns the sum of the
# value returned by the functions "get_france_sales" and "get_england_sales"


# Create a function named "update_catalog", that :
# Calls the function add_new_product with one parameter "toothbrush"
# Calls the function add_new_product with one parameter "scale"
# Returns the value returned by get_best_selling_product()

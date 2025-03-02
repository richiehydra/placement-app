from django.shortcuts import render , redirect , HttpResponseRedirect
from store.models.company import Company
from store.models.category import Category
from django.views import View


# Create your views here.
class Index(View):

    def post(self , request):
        company = request.POST.get('company')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(company)
            if quantity:
                if remove:
                    if quantity<=1:
                        cart.pop(company)
                    else:
                        cart[company]  = quantity-1
                else:
                    cart[company]  = quantity+1

            else:
                cart[company] = 1
        else:
            cart = {}
            cart[company] = 1

        request.session['cart'] = cart
        print('cart' , request.session['cart'])
        return redirect('homepage')



    def get(self , request):
        # print()
        return HttpResponseRedirect(f'/store{request.get_full_path()[1:]}')

def store(request):
    cart = request.session.get('cart')
    if not cart:
        request.session['cart'] = {}
    companies = None
    categories = Category.get_all_categories()
    categoryID = request.GET.get('category')
    if categoryID:
        companies = Company.get_all_companies_by_categoryid(categoryID)
    else:
        companies = Company.get_all_companies();

    data = {}
    data['companies'] = companies
    data['categories'] = categories

    print('you are : ', request.session.get('email'))
    return render(request, 'index.html', data)
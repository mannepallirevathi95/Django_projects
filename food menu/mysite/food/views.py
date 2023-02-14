from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ItemForm
from .models import Item
from django.template import loader
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
# Create your views here.
# def index(request):
#     # we are exactracting all the items in class Item from models.py
#     item_list = Item.objects.all()
#     context = {
#         'item_list' : item_list,
#     }
#    return HttpResponse(template.render(context,request))
#     return render(request, 'food/index.html', context)

class IndexClassView(ListView):
    # in the above function we mentioned the item_list and specified this to class and finallky extracted the data
    # but here it is a simple thing
    # mtc
    model = Item
    template_name = 'food/index.html'
    context_object_name = 'item_list'

def display(request):
    display = Item.objects.all()
    for a in display:
        print(a)

def about(request):
    items = Item.objects.all()
    return render(request, 'food/about.html', {'items':items})


# def detail(request, item_id):
#     item = Item.objects.get(pk=item_id)
#     context = {
#         'item' : item,
#     }
# #    return HttpResponse("this is item no/id: %s" % item_id)
#     return render(request,'food/detail.html',context)

class FoodDetail(DetailView):
    model = Item
    template_name = 'food/detail.html'
    

def create_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('food:index')

    return render(request, 'food/item-form.html', {'form':form})

# this is a clas  based view for create item

class CreateItem(CreateView):
    model = Item
    fields = ['item_name','item_discrip','item_price','item_image']
    template_name = 'food/item-form.html'

    def form_valid(self,form):
        form.instance.user_name = self.request.user

        return super().form_valid(form)

def update_item(request,id):
    item = Item.objects.get(id=id)
    form = ItemForm(request.POST or None, instance = item)

    if form.is_valid():
        form.save()
        return redirect('food:index')

    return render(request, 'food/item-form.html', {'form':form,'item': item})

def delete_item(request,id):
    item = Item.objects.get(id=id)
    #if request.method == 'POST':
    item.delete()
    
    return redirect('food:index')

    #return render(request, 'food/item-delete.html', {'item': item})

# def dummy():
#     data = {}

#     results = Item.objects.order_by('item_name','item_price')
#     data.append(results)
#     print(data)
#     return redirect('food:index')

# def dummy(request):
#    data = {}
#    results = Item.objects.order_by('item_name','item_price')
#    data.append(results)
#    print(data)
#    return render(request,'food:index', {'dict':data})
# #    return render(request, 'index.html', {'list':a_list})


# def json():
#     base_list = Item.objects.all()
#     serialized = serialize('json',Item.objects.all())
#     with open("D:\\Revathi\\PYTHON-Django\\Django\\food menu\\mysite\\data.json","w") as f:
#         jsoned = json.loads(serialized)
#         json.dumps(jsoned,f)


# def basically():
#     url = "https://randomuser.me/api"
#     response = requests.get(url)
#     data = response.json()
    

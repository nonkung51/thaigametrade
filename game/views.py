from django.shortcuts import render
from django.views.generic import (CreateView, DetailView,
                                  UpdateView, DeleteView,
                                  ListView)
from .models import Game, Product

# Create your views here.
class CreateProduct(CreateView):
    fields = ('game','price')
    model = Product
    template_name = 'game/productcreate.html'
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.seller = self.request.user.profile
        self.object.save()
        return super().form_valid(form)

class ProductDetailView(DetailView):
    context_object_name = 'product_detail'
    model = Product
    template_name = 'game/productdetail.html'

class ProductUpdateView(UpdateView):
    fields = ('price',)
    model = Product
    template_name = 'game/productedit.html'

class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'game/productdelete.html'
    success_url = '/'

class ProductListView(DetailView):
    model = Game
    template_name = 'game/productlist.html'

class GameListView(ListView):
    model = Game
    template_name = 'game/gamelist.html'

    def get_queryset(self):
        q = self.request.GET.get('q')
        if(q):
            object_list = self.model.objects.filter(name__icontains=q)
        else:
            object_list = self.model.objects.all()
            
        return object_list

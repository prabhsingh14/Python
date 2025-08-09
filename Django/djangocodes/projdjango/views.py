from django.shortcuts import render
from .models import ChaiVarity
from django.shortcuts import get_object_or_404

# Create your views here.
def all_chai(request):
    chai_varieties = ChaiVarity.objects.all()
    return render(request, 'chai/all_chai.html', {'chai_varieties': chai_varieties})

def chai_detail(request, chai_id):
    chai = get_object_or_404(ChaiVarity, id=chai_id)
    return render(request, 'chai/chai_detail.html', {'chai': chai}) 
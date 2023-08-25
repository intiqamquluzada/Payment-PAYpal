import uuid
from django.contrib import messages
from django.conf import settings
from django.shortcuts import get_object_or_404, render, redirect
from payment.models import Blog
from django.urls import reverse
from paypal.standard.forms import PayPalPaymentsForm
from django.contrib.auth import get_user_model

User = get_user_model()




def home(request):
    blog = request.POST.get("blog")
    user = request.user
    myvalue = False
    blogs = Blog.objects.filter(user__id=request.user.id)
    print(blogs.count())
    if blogs.count() > 0:
        messages.error(request, "odenis edin")
        myvalue = True
      
    if blog:
        b = Blog.objects.create(user=user, body=blog)
        b.save()
    all = Blog.objects.all()
    host = request.get_host()
    paypal_dict = {
        'business': settings.PAYPAL_RECEIVER_EMAIL,
        'amount': '20.00',
        'item_name': 'Product 1',
        'invoice': str(uuid.uuid4()),
        'currency_code': 'USD',
        'notify_url': f'http://{host}{reverse("paypal-ipn")}',
        'return_url': f'http://{host}{reverse("paypal-reverse")}',
        'cancel_return': f'http://{host}{reverse("paypal-cancel")}',
    }
    
    form  = PayPalPaymentsForm(initial=paypal_dict)
    context = {
        "form": form,
        "blogs":blogs,
        "myvalue": myvalue,
        "user":user,
        "all":all,
        
        
    }
    return render(request, "home.html", context)


def paypal_reverse(request):
    messages.success(request, "Odenis edildi")
    return redirect('home')

def paypal_cancel(request):
    messages.error(request, "Odenis ugursuzdur")
    return redirect('home')


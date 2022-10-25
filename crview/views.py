from django.shortcuts import render, redirect

from crview.models import employees
from django.core.paginator import Paginator


def home(request):
    emp = employees.objects.all()
    paginator = Paginator(emp, 5)
    page_number = request.GET.get("page")
    emp = paginator.get_page(page_number)

    context = {
        'emp': emp,
    }
    return render(request, "index.html", context)


def add(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        address = request.POST.get("address")
        phone = request.POST.get("phone")

        emp = employees(
            name=name,
            email=email,
            address=address,
            phone=phone,
        )
        emp.save()
        return redirect("home")

    return render(request, "index.html")


def edit(request):
    emp = employees.objects.all()

    context = {
        'emp': emp,
    }
    return render(request, "index.html", context)


def update(request, id):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone = request.POST.get('phone')

        emp = employees(
            id=id,
            name=name,
            email=email,
            address=address,
            phone=phone,
        )

        emp.save()
        return redirect("home")

    return render(request, "index.html", )


def delete(request, id):
    emp = employees.objects.filter(id=id).delete()
    context = {
        'emp': emp,
    }

    return redirect("home")

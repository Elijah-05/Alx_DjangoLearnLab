from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import permission_required
from .models import CustomUser


@permission_required("accounts.can_view", raise_exception=True)
def user_list(request):
    users = CustomUser.objects.all()
    return render(request, "accounts/user_list.html", {"users": users})


@permission_required("accounts.can_create", raise_exception=True)
def user_create(request):
    # Placeholder — any custom create logic
    return render(request, "accounts/create.html")


@permission_required("accounts.can_edit", raise_exception=True)
def user_edit(request, pk):
    user = get_object_or_404(CustomUser, pk=pk)
    return render(request, "accounts/edit.html", {"user": user})


@permission_required("accounts.can_delete", raise_exception=True)
def user_delete(request, pk):
    user = get_object_or_404(CustomUser, pk=pk)
    user.delete()
    return render(request, "accounts/delete_success.html")

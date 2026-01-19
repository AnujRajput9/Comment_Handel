from django.shortcuts import render ,get_list_or_404,redirect,get_object_or_404, redirect
from .models import Comment
from .forms import CommentForms , UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
 
# Create your views here.
def index(request):
    return render(request,'comment/index.html')


def comment_list(request):
    comments = Comment.objects.all().order_by('-created_at')
    return render(request,'comment/comment_list.html',{'comments':comments})

@login_required
def create_comment(request):
    if request.method == "POST":
        form =  CommentForms(request.POST,request.FILES) 
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user  
            comment.save()
            return redirect('comment_list') 
    else:
        form = CommentForms()
    return render(request,'comment/create_comment.html',{'form':form}) 

@login_required
def update_comment(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id, user=request.user)
    if request.method == "POST":
        form = CommentForms(request.POST, request.FILES, instance=comment)
        if form.is_valid():
            updated_comment = form.save(commit=False)
            updated_comment.user = request.user
            updated_comment.save()
            return redirect('comment_list')
    else:
        form = CommentForms(instance=comment)
    return render(request, 'comment/create_comment.html', {'form': form})


@login_required      
def delete_comment(request,comment_id):
    comment = get_object_or_404(Comment , pk= comment_id,user = request.user)
    if request.method == 'POST':
        comment.delete()
        return redirect('comment_list')
    return render(request,'comment/delete_comment.html',{'comment':comment}) 
               
               
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            try:
                user = form.save(commit=False)
                user.set_password(form.cleaned_data['password1'])
                user.save()
                login(request,user)
                return redirect('comment_list')
            except ValueError as e:
                print(e)
    else:
        form = UserCreationForm()
    return render(request,'registration/register.html',{'form':form})               
            
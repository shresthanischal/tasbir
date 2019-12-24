from django.shortcuts import render , redirect
from .models import PostModel , CommentModel
from user_app.models import UserModel
from user_app.forms import EditProfileForm
from .forms import AddNewPostFrom

# Create your views here.
def index(request):

    if 'user_id' in request.session:

        allpost = PostModel.objects.all().order_by('-created')

        d = {
            'posts' : allpost,
        }

        return render(request, 'photo_app/index.html' ,d)
    else:
        return redirect('login')


def profile(request,username):
    
    user = UserModel.objects.filter(username=username).first()
    posts = PostModel.objects.filter(uploaded_by = user).order_by('-created')

    d = {
        'user' : user,
        'posts' : posts,
    }

    return render(request, 'photo_app/profile.html',d)

def editprofile(request):
    if 'user_id' not in request.session:
        return redirect('login')
    
    userid = request.session.get('user_id',None)
    user = UserModel.objects.filter(id=userid).first()

    if user:
        if request.method == 'POST':
            form = EditProfileForm(data = request.POST, files = request.FILES, instance = user)
            if form.is_valid():
                form.save()
                request.session['username'] = user.username
                return redirect('profile', user.username)
            else:
                return render(request,'photo_app/editprofile',{'form': form})
        else:
            form = EditProfileForm(instance = user)
            d= {
                'form' : form,
                'user' : user
            }
            return render(request,'photo_app/editprofile.html',d)

        return redirect('index')

def addphoto(request):

    if 'user_id' not in request.session:
        return redirect('login')

    userid = request.session.get('user_id')
    user = UserModel.objects.filter(id=userid).first()

    if user:
        if request.method == 'POST':
            form = AddNewPostFrom(data = request.POST, files = request.FILES)
            if form.is_valid():
                post = form.save(commit = False)
                post.uploaded_by = user
                post.save()
                return redirect('profile', user.username)
            else:
                return render(request,'photo_app/add-photo.html',{'form':form})
        
        else:
            form = AddNewPostFrom()
            d={
                'form' : form
                }
            return render(request,'photo_app/add-photo.html',d)
    else:
        return redirect('index')

def delete_photo(request):
    if 'user_id' not in request.session:
        return redirect('login')

    userid = request.session.get('user_id')

    if request.method == 'POST':
        postid = request.POST.get('postid', None)
        if postid:
            post = PostModel.objects.filter(id=postid, uploaded_by=userid).first()
            if post:
                post.delete()
            
    return redirect('index')


def search(request):
    if 'user_id' not in request.session:
        return redirect('login')
    
    if request.method == "GET":
        query = request.GET.get('q', None)
        if query:
            userlist = UserModel.objects.filter(username__contains =query)
            d = {
                'search_results': userlist
            }
            return render(request,'photo_app/search-results.html',d)
    return redirect('index')
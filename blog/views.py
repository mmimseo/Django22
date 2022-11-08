from django.shortcuts import render, redirect
from .models import Post, Category, Tag
from django.views.generic import ListView, DetailView, CreateView  ## CBV ##
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# Create your views here.

class PostCreate(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Post
    fields = ['title', 'hook_text', 'content', 'head_image', 'file_upload', 'category']
    #모델명_form.html

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff     # or 둘 중 하나만 만족

    def form_valid(self, form):      #로그인 해야 PostCreate 사용 가능, 작성자 자동 입력
        current_user = self.request.user
        if current_user.is_authenticated and (current_user.is_superuser or current_user.is_staff):      # and 둘 다 만족
            form.instance.author = current_user
            return super(PostCreate, self).form_valid(form)
        else:
            return redirect('/blog/')
    def get_context_data(self, *, object_list=None, **kwargs):  ##추가인자##
        context = super(PostCreate,self).get_context_data()
        context['categories'] = Category.objects.all()
        context['no_category_post_count'] = Post.objects.filter(category=None).count
        return context

class PostList(ListView):   ## CBV ##
    model = Post
    ordering = '-pk'

    def get_context_data(self, *, object_list=None, **kwargs):  ##추가인자##
        context = super(PostList,self).get_context_data()
        context['categories'] = Category.objects.all()
        context['no_category_post_count'] = Post.objects.filter(category=None).count
        return context
    #템플릿은 모델명_list.html : post_list.html
    #매개변수 모델명_list :post_list

class PostDetail(DetailView): ## CBV ##
    model = Post
    # 템플릿은 모델명_detail.html : post_detail.html
    # 매개변수 모델명 : post

def category_page(request, slug):
    if slug == 'no_category':
        category = '미분류'
        post_list = Post.objects.filter(category=None)
    else :
        category = Category.objects.get(slug=slug)
        post_list = Post.objects.filter(category=category)
    return render(request, 'blog/post_list.html', {
        'category' : category,
        'post_list' : post_list,
        'categories' : Category.objects.all(),
        'no_category_post_count' : Post.objects.filter(category=None).count
    })

def tag_page(request, slug):
    tag = Tag.objects.get(slug=slug)
    post_list = tag.post_set.all()
    return render(request, 'blog/post_list.html', {
            'tag' : tag,
            'post_list' : post_list,
            'categories': Category.objects.all(),
            'no_category_post_count': Post.objects.filter(category=None).count
            })


'''
def index(request):       ## 변수 작성 ##
    posts = Post.objects.all().order_by('-pk')
    return render(request, 'blog/index.html', {'posts': posts})

def single_post_page(request,pk):
    post1 = Post.objects.get(pk=pk)
    return render(request, 'blog/single_post_page.html', {'post': post1}) 
'''




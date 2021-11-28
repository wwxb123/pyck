# from django.http import HttpResponse
#
#
# def index(request):
#     return HttpResponse("旺旺掀被视图")

from django.shortcuts import render,redirect


# def index(request):
#     content ="旺旺"
#     return render(request,'projects/index.html')
from django.urls import reverse
from django.views import View

from projects.models import Project


def index(request):
    content = '接口自动化测试平台'
    return render(request, 'projects/index.html', context={
        'content': content,
    })


def projects_list(request):
    """
    项目列表视图
    从数据库查询所有项目
    """
    objs = Project.objects.all()
    return render(request, 'projects/list.html',context={
        'objs':objs,
    })

class ProjectCreateView(View):
    def get(self,request):
        """项目列表"""

        return render(request,'projects/detail.html')
    def post(self,request):
        """添加项目
        1、接收表单数据
        2、创建模型对象并保存到数据库
        3、跳转到项目列表页面
        """
        # request.POST.get()
        objs = Project()
        objs.name = request.POST.get('name')
        objs.leader = request.POST.get('leader')
        objs.desc = request.POST.get('desc')
        objs.save()
        return redirect(reverse('projects:list'))

class ProjectUpadateView(View):
    """更新项目视图
    """
    def get(self,request,pk):
        """返回项目列表"""
        #获取对象
        objs = Project.objects.get(pk=pk)
        # return render(request, 'projects/update-.html', context={'objs':objs})
        return render(request, 'projects/detail.html', context={'objs': objs})
    def post(self,request,pk):
        #获取要修改的对象
        objs = Project.objects.get(pk=pk)
        #修改表单数据并修改对象
        objs.name=request.POST.get('name')
        objs.leader = request.POST.get('leader')
        objs.desc = request.POST.get('desc')
        objs.save()
        #跳转到项目列表页面
        return redirect(reverse('projects:list'))
# class ProjectDeleteView(View):
#     def get(self,request,pk):
#
#         objs = Project.objects.get(pk=pk)
#     def post(self,request,pk):
#         # 获取要删除的对象
#         objs = Project.objects.get(pk=pk)
#         objs.delete()
#         # 跳转到项目列表页面
#         return redirect(reverse('projects:list'))

def project_deltete(request,pk):
        # 获取要删除的对象
        objs = Project.objects.get(pk=pk)
        objs.delete()
        # 跳转到项目列表页面
        return redirect(reverse('projects:list'))

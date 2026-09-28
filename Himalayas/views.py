from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import TASK
from django.views.decorators.csrf import csrf_exempt  
import json      
# Create your views here.
def mountains(request):
    return HttpResponse("cold")

def rivers(request):
    return render (request,"rivers.html")
def console(request):
    return render(request,"console.html")
def calculator(request):
    return render (request,"calculator.html")
def well(request):
    return render(request,"well.html")



def task(request):
    all_tasks = TASK.objects.all()
    if request.method=='GET':
        print(all_tasks)
        return render (request,'task.html', context={'tasks': all_tasks})
    else:
        return HttpResponse("Method not allowed!")


def hero(request):
    task_name = TASK.objects.all().values()
    return JsonResponse ({'usage':list(task_name)})

@csrf_exempt
def heroine(request):
    if request.method == "POST" :
        data=request.body.decode('utf-8')
        data=json.loads(data)
        TASK.objects.all()
        new_task=TASK.objects.create(task_name=data['task_name'],due_date=data['due_date'])
        new_task.save()
        print (data,"---------")
        return JsonResponse({"status":"ok"})

@csrf_exempt
def delete_task(request):
    if request.method =="DELETE":
        params=request.GET
        task_id=params.get('task_id')
        if task_id is None:
            return JsonResponse({"status":"task_id is requried"})
        objs=TASK.objects.filter(id=task_id)
        objs.delete()
        return JsonResponse({"status":"ok"})
    else:
         return JsonResponse({"status":"method not allowed"})



@csrf_exempt
def mark_completed(request):
    if request.method =="PUT":
        params=request.GET
        task_id=params.get('task_id')
        if task_id is None:
            return JsonResponse({"status":"task_id is requried"})
        objs=TASK.objects.filter(id=task_id)
        if len(objs)<1:
            return JsonResponse({"status":"ok"},status=400)
        obj=objs[0]
        obj.is_completed=not obj.is_completed
        obj.save()
    return JsonResponse({"status":"ok"})
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

def stringAnalyzer(request):
    if request.method=='GET':
        print(request.method)
        return render(request,'stringAnalyzer.html')
    else:
        print(request.method)
        stringData=request.POST.get('stringText','null')
        return render(request,'stringAnalyzer.html',{'stringDataKey':stringData})
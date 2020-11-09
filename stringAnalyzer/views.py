from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

def stringAnalyzer(request):
    if request.method=='GET':
        print(request.method)
        return render(request,'stringAnalyzer.html')
    else:
        removeSpace=request.POST.get('removeSpace',False)
        capitalizeFirst=request.POST.get('capitalizeFirst',False)
        wordCounter=request.POST.get('wordCounter',False)
        alphabetCounter=request.POST.get('alphabetCounter',False)
        stringData=request.POST.get('stringText','null')
        dataMap={}
        if stringData != 'null':
            if removeSpace=='on':
                tempList=stringData.split()
                dataMap['removeSpace']="".join(tempList)
            if capitalizeFirst=='on':
                tempList=stringData.split()
                processed=""
                for text in tempList:
                    processed=processed+text.capitalize()
                dataMap['capitalizeFirst']=processed
            if wordCounter=='on':
                wordCount={}
                for t in stringData.split():
                    if t in wordCount:
                        wordCounter[t]=int(wordCount[t])+1
                    else:
                        wordCount[t]=int(1);
                dataMap['wordCounter']=wordCount
            if alphabetCounter=='on':
                alpahCount={}
                for a in range(0, len(stringData)):
                    if stringData[int(a)] in alpahCount:
                        alpahCount[stringData[int(a)]]=int(alpahCount[stringData[int(a)]])+1
                    else: 
                        if(stringData[int(a)] !=" "):
                           alpahCount[stringData[int(a)]]=1
                dataMap['alphaCount']=alpahCount
            dataMap['stringDataKey']=stringData
        context = {'dataMaps': dataMap.items()}

        return render(request,'stringAnalyzer.html',context)
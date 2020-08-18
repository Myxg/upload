from django.shortcuts import render, redirect
import os
import time
import datetime


# Create your views here.


def demo(request):
    if request.method == 'POST':
        try:
            myFile = request.FILES.get("myfile",None)
            # if not myFile:
            #     return HttpResponse('no files for upload!')

            # report.objects.filter(id=uid).update(filename=myFile.name)
            # # print(uid)
            # ts = report.objects.filter(id=uid)
            # for i in ts:
            #     s = i.route
            #     route = '/SHreport' + s
            now = int(time.time())
            ts = time.localtime(now)
            t = str(ts.tm_year)+str(ts.tm_mon).zfill(2)+str(ts.tm_mday).zfill(2)
            route = '/files/'
            file = t + '_' + myFile.name
            destination = open(os.path.join(route,file),'wb+')

            for chunk in myFile.chunks():
                destination.write(chunk)
                # print(destination,'----------------------')
            destination.close()
            list1 = ['上传成功']
            return render(request, 'demo.html', {'msg':'上传成功'})
        except Exception as e:
            return render(request, 'demo.html', {'msg': '上传失败'})
    return render(request, 'demo.html')



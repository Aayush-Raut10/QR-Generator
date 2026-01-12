from django.shortcuts import render
from django.http import HttpResponse
import qrcode
import datetime
import os
from django.conf import settings
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def index(request):
    if request.method == "POST":
        

        name = request.POST.get("name")
        url = request.POST.get("url")

        if not name or not url:

            context = {
                "error":0
            }

            return render(request, "Generator/index.html", context=context)

        else:

            newQr = qrcode.make(url)

            time = str(datetime.datetime.now())

            filename = name.replace(" ", "").lower() + time.replace(" ", "").replace("-", "_").replace(":","_")  + ".png"

            path = os.path.join(settings.MEDIA_ROOT, filename)

            newQr.save(path)

            # create QR code URL
            qrUrl = os.path.join(settings.MEDIA_URL, filename)

            return render(request, "Generator/result.html", context= {
                "name":name,
                "qrurl":qrUrl,
                "filename":filename
            }
)
           

    else:
        
        return render(request, "Generator/index.html")




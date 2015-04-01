from django.shortcuts import render

# Create your views here.
def clientaccesspolicy(request):
    return render(request,'clientaccesspolicy.xml',{},content_type="application/xml")

def crossdomain(request):
    return render(request,'crossdomain.xml',{},content_type="application/xml")

def robotstxt(request):
    return render(request,'robots.txt',{},content_type="text/plain")

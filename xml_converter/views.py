# 3rd party imports
from django.http import HttpResponseBadRequest, JsonResponse
from django.shortcuts import render

# app imports
from .converter import convert_xml_to_dict


def upload_page(request):
    if request.method == 'POST':
        # as there is a single file field in the form, there is no need to create a Django form
        # to validate it
        if "file" not in request.FILES:
            return HttpResponseBadRequest("No XML file was chosen")
        file_content = request.FILES["file"].file.read()
        return JsonResponse(convert_xml_to_dict(file_content))

    return render(request, "upload_page.html")

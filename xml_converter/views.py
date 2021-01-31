# 3rd party imports
from django.http import HttpResponseBadRequest, JsonResponse
from django.shortcuts import render

# app imports
from .converter import convert_xml_to_dict, XmlParseException


def upload_page(request):
    FILE_NAME = "file"
    if request.method == 'POST':
        # as there is a single file field in the form, there is no need to create a Django form
        # to validate it
        if FILE_NAME not in request.FILES:
            return HttpResponseBadRequest("No XML file was chosen")
        file_content = request.FILES[FILE_NAME].file.read()
        try:
            content = convert_xml_to_dict(file_content)
        except XmlParseException:
            return HttpResponseBadRequest("file '%s' in HTTP request has invalid XML" % FILE_NAME)
        return JsonResponse(content)

    return render(request, "upload_page.html")

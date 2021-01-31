from rest_framework import status
from rest_framework.decorators import action
from rest_framework.parsers import MultiPartParser
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from .converter import convert_xml_to_dict, XmlParseException


class ConverterViewSet(ViewSet):
    # Note this is not a restful API
    # We still use DRF to assess how well you know the framework
    parser_classes = [MultiPartParser]
    renderer_classes = [JSONRenderer]

    @action(methods=["POST"], detail=False, url_path="convert")
    def convert(self, request, **kwargs):
        FILE_NAME = "file"
        if FILE_NAME not in request.FILES:
            return Response("Missing file named '%s' in HTTP request" % FILE_NAME,
                            status=status.HTTP_400_BAD_REQUEST)
        file_content = request.FILES["file"].file.read()
        try:
            content = convert_xml_to_dict(file_content)
        except XmlParseException:
            return Response("file '%s' in HTTP request has invalid XML" % FILE_NAME,
                            status=status.HTTP_400_BAD_REQUEST)
        return Response(content)

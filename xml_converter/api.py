from rest_framework.decorators import action
from rest_framework.parsers import MultiPartParser
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from .converter import convert_xml_to_dict


class ConverterViewSet(ViewSet):
    # Note this is not a restful API
    # We still use DRF to assess how well you know the framework
    parser_classes = [MultiPartParser]
    renderer_classes = [JSONRenderer]

    @action(methods=["POST"], detail=False, url_path="convert")
    def convert(self, request, **kwargs):
        file_content = request.FILES["file"].file.read()
        return Response(convert_xml_to_dict(file_content))

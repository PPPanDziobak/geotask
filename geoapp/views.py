import json
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
import svgwrite
from geoapp.forms import GeoForm
from geoapp.models import GeometryCoordinatesModel


class GeometryView(View):

    def validate_coordinates(self, coordinates_dict):
        for el in coordinates_dict.values():
            return True if isinstance(el, int) else False

    def count_data(self, coordinates_data):
        # Wyciąganie wartości x1, x2, y1, y2, z1, z2 z coordinates_data
        x1, x2, y1, y2, z1, z2 = json.loads(coordinates_data).values()

        # Ustalenie wartości granicznych dla osi x, y, z
        min_x = min(x1, x2)
        max_x = max(x1, x2)
        min_y = min(y1, y2)
        max_y = max(y1, y2)
        min_z = min(z1, z2)
        max_z = max(z1, z2)

        # Obliczenie szerokości i wysokości prostokąta
        width = abs(max_x - min_x)
        height = abs(max_y - min_y)
        depth = abs(max_z - min_z)

        # Wyznaczenie współrzędnych lewego górnego rogu prostokąta
        top_left_x = min_x
        top_left_y = min_y
        counted_data = {
            'width': width,
            'height': height,
            'depth': depth,
            'top_left_x': top_left_x,
            'top_left_y': top_left_y,
            'min_y': min_y,
            'min_z': min_z,
        }

        return counted_data

    def create_svg_file(self, coordinates_data, projection_plane):
        counted_data = self.count_data(coordinates_data)
        top_left_x, top_left_y = counted_data['top_left_x'], counted_data['top_left_y']
        width, height, depth = counted_data['width'], counted_data['height'], counted_data['depth']
        min_y, min_z = counted_data['min_y'], counted_data['min_z']
        dwg = svgwrite.Drawing(profile='full')
        if projection_plane == 'XY':
            dwg.add(dwg.rect((top_left_x, top_left_y), (width, height), fill='none', stroke='black'))
        elif projection_plane == 'XZ':
            dwg.add(dwg.rect((top_left_x, min_z), (width, depth), fill='none', stroke='red'))
        elif projection_plane == 'YZ':
            dwg.add(dwg.rect((min_y, min_z), (height, depth), fill='none', stroke='green'))
        svg_img = dwg.tostring()
        return svg_img

    def get(self, request):
        form = GeoForm()
        queryset = GeometryCoordinatesModel.objects.all()
        return render(request, 'geoapp/home.html', {'form': form, 'queryset': queryset})

    def post(self, request):
        form = GeoForm(request.POST)
        if form.is_valid():
            coordinates_data = form.cleaned_data['coordinates']
            projection_plane = form.cleaned_data['projection_plane']
            try:
                coordinates_dict = json.loads(coordinates_data)
                validate = self.validate_coordinates(coordinates_dict)
                if validate:
                    svg_path = self.create_svg_file(coordinates_data, projection_plane.upper())
                    geometry_obj = GeometryCoordinatesModel.objects.create(
                        **coordinates_dict
                    )
                    geometry_obj.save()
                    response_data = {'status': 'success', 'svg_path': svg_path}
                else:
                    response_data = {'status': 'error', 'message': 'Invalid form data'}
            except json.JSONDecodeError:
                response_data = {'status': 'error', 'message': 'Invalid JSON data'}
        else:
            response_data = {'status': 'error', 'message': 'Invalid form data'}

        return JsonResponse(response_data)


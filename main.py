import svgwrite


def create_svg_file(self, geometry_data, projection_plane):
    dwg = svgwrite.Drawing('projection.svg', profile='full')

    for coordinates in geometry_data:
        x1, x2, y1, y2, z1, z2 = coordinates.values()

        if projection_plane == 'XY':
            dwg.add(dwg.rect((x1, y1), (x2 - x1, y2 - y1), fill='none', stroke='black'))
        elif projection_plane == 'XZ':
            dwg.add(dwg.rect((x1, z1), (x2 - x1, z2 - z1), fill='none', stroke='red'))
        elif projection_plane == 'YZ':
            dwg.add(dwg.rect((y1, z1), (y2 - y1, z2 - z1), fill='none', stroke='green'))

    dwg.save()
    return 'projection.svg'


def projection(self, coordinates_data, projection_plane):
    counted_data = self.count_data(coordinates_data)

    top_left_x, top_left_y = counted_data['top_left_x'], counted_data['top_left_y']
    width, height, depth = counted_data['width'], counted_data['height'], counted_data['depth']
    min_y, min_z = counted_data['min_y'], counted_data['min_z']

    dwg = svgwrite.Drawing('projection.svg', profile='full')

    # Rysowanie prostokąta na płaszczyźnie x-y
    dwg.add(dwg.rect((top_left_x, top_left_y), (width, height), fill='none',
                     stroke=svgwrite.rgb(0, 0, 0, '%')))  # czarny prostokąt

    # Rysowanie prostokąta na płaszczyźnie x-z
    dwg.add(dwg.rect((top_left_x, min_z), (width, depth), fill='none',
                     stroke=svgwrite.rgb(255, 0, 0, '%')))  # czerwony prostokąt

    # Rysowanie prostokąta na płaszczyźnie y-z
    dwg.add(dwg.rect((min_y, min_z), (height, depth), fill='none',
                     stroke=svgwrite.rgb(0, 255, 0, '%')))  # zielony prostokąt

    dwg.save()
    return 'projection.svg'
# geometry_data = {
#     'x1': 14,
#     'x2': 60,
#     'y1': 25,
#     'y2': 44,
#     'z1': 80,
#     'z2': 120
# }
# geometry_data = {"x1":20,"x2":30,"y1":40,"y2":50,"z1":40,"z2":70}
geometry_data = {"x1": -20, "x2": -12, "y1": 9, "y2": 191, "z1": 0, "z2": 18}





def projection(geometry_data):
    text = 'nazwa21s2'
    file_path = '/home/piotrek/Pulpit/'
    dwg = svgwrite.Drawing(file_path + text + '.svg', profile='full')

    x1, x2, y1, y2, z1, z2 = geometry_data.values()
    dwg.add(dwg.rect((x1, y1), (y2 - y1, x2 - x1), fill='none', stroke=svgwrite.rgb(0, 0, 0, '%')))  # czarny prostokąt
    dwg.add(dwg.rect((x1, z1), (y2 - y1, z2 - z1), fill='none', stroke=svgwrite.rgb(255, 0, 0, '%')))  # czerwony prostokąt
    dwg.add(dwg.rect((y1, z1), (x2 - x1, z2 - z1), fill='none', stroke=svgwrite.rgb(0, 255, 0, '%')))  # zielony prostokąt
    dwg.save()


projection(geometry_data)







# <defs /><rect fill="none" height="10" stroke="rgb(0%,0%,0%)" width="10" x="20" y="40" /></svg>
#
#
# <defs /><rect fill="none" height="20" stroke="rgb(0%,100%,0%)" width="10" x="40" y="90" /></svg>
#
#
# <defs /><rect fill="none" height="20" stroke="rgb(100%,0%,0%)" width="10" x="20" y="90" /></svg>
#
#
# <defs /><rect fill="none" height="46" stroke="rgb(0%,0%,0%)" width="19" x="14" y="25" /><rect fill="none" height="40" stroke="rgb(100%,0%,0%)" width="19" x="14" y="80" /><rect fill="none" height="40" stroke="rgb(0%,100%,0%)" width="46" x="25" y="80" /></svg>
#









# import json
#
# from django.http import JsonResponse, HttpResponse
# from django.shortcuts import render
# from django.views import View
# from django.http import JsonResponse
# from django.shortcuts import render
# from django.views import View
#
# from geoapp.forms import GeoForm
# from geoapp.models import GeometryCoordinatesModel

# import svgwrite
# import svgwrite


# class GeometryView(View):
#     def projection(self, coordinates_data):
#         text = 'tetssss'
#         file_path = '/home/piotrek/'
#         dwg = svgwrite.Drawing(file_path + text + '.svg', profile='full')
#
#         x1, x2, y1, y2, z1, z2 = json.loads(coordinates_data).values()
#         dwg.add(dwg.rect((x1, y1), (y2 - y1, x2 - x1), fill='none',
#                          stroke=svgwrite.rgb(0, 0, 0, '%')))  # czarny prostokąt
#         dwg.add(dwg.rect((x1, z1), (y2 - y1, z2 - z1), fill='none',
#                          stroke=svgwrite.rgb(255, 0, 0, '%')))  # czerwony prostokąt
#         dwg.add(dwg.rect((y1, z1), (x2 - x1, z2 - z1), fill='none',
#                          stroke=svgwrite.rgb(0, 255, 0, '%')))  # zielony prostokąt
#         dwg.save()
#
#     def get(self, request):
#         form = GeoForm()
#         return render(request, 'geoapp/home.html', {'form': form})
#
#     def post(self, request):
#         form = GeoForm(request.POST)
#         if form.is_valid():
#             coordinates_data = form.cleaned_data['coordinates']
#             try:
#                 coordinates_dict = json.loads(coordinates_data)
#                 geo_obj = GeometryCoordinatesModel.objects.create(**coordinates_dict)
#                 geo_obj.save()
#                 response_data = {'status': 'success', 'data': coordinates_dict}
#                 self.projection(coordinates_data)
#                 with open('/home/piotrek/tetssss.svg', 'rb') as f:
#                     response = HttpResponse(f, content_type='image/svg+xml')
#                     response['Content-Disposition'] = 'attachment; filename="tetssss.svg"'
#                     return response
#             except json.JSONDecodeError:
#                 response_data = {'status': 'error', 'message': 'Invalid JSON data'}
#         else:
#             response_data = {'status': 'error', 'message': 'Invalid form data'}
#
#         return JsonResponse(response_data)



# import json
# from datetime import datetime
# from django.http import JsonResponse
# from django.shortcuts import render
# from django.views import View
#
# from geoapp.forms import GeoForm
# from geoapp.models import GeometryCoordinatesModel
#
# import svgwrite
#
#
# class GeometryView(View):
#
#     def projection(self, coordinates_data, x1, x2, y1, y2, z1, z2):
#         current_time = datetime.now()
#         text = f'{current_time}'
#         file_path = '/home/piotrek/'
#         dwg = svgwrite.Drawing(file_path + text + '.svg', profile='full')
#
#         x1, x2, y1, y2, z1, z2 = json.loads(coordinates_data).values()
#         print('heyyyyy', x1, x2, y1, y2, z1, z2)
#         dwg.add(dwg.rect((x1, y1), (y2 - y1, x2 - x1), fill='none',
#                          stroke=svgwrite.rgb(0, 0, 0, '%')))  # czarny prostokąt
#         dwg.add(dwg.rect((x1, z1), (y2 - y1, z2 - z1), fill='none',
#                          stroke=svgwrite.rgb(255, 0, 0, '%')))  # czerwony prostokąt
#         dwg.add(dwg.rect((y1, z1), (x2 - x1, z2 - z1), fill='none',
#                          stroke=svgwrite.rgb(0, 255, 0, '%')))  # zielony prostokąt
#         dwg.save()
#
#
#     def get(self, request):
#         form = GeoForm()
#         return render(request, 'geoapp/home.html', {'form': form})
#
#     def post(self, request):
#         form = GeoForm(request.POST)
#         if form.is_valid():
#             coordinates_data = form.cleaned_data['coordinates']
#             print(coordinates_data)
#             try:
#                 coordinates_dict = json.loads(coordinates_data)
#                 x1, x2, y1, y2, z1, z2 = json.loads(coordinates_data).values()
#                 geo_obj = GeometryCoordinatesModel.objects.create(**coordinates_dict)
#                 geo_obj.save()
#                 print('xx', coordinates_dict)
#                 response_data = {'status': 'success', 'data': coordinates_dict}
#                 img = self.projection(coordinates_data, x1, x2, y1, y2, z1, z2)
#                 return img
#             except json.JSONDecodeError:
#                 response_data = {'status': 'error', 'message': 'Invalid JSON data'}
#         else:
#             response_data = {'status': 'error', 'message': 'Invalid form data'}
#
#         return JsonResponse(response_data)


# def projection(geometry_data):
#     text = '11111112'
#     file_path = '/home/piotrek'
#     dwg = svgwrite.Drawing(file_path + text + '.svg', profile='full')
#
#     x1, x2, y1, y2, z1, z2 = geometry_data.values()
#     dwg.add(dwg.rect((x1, y1), (y2 - y1, x2 - x1), fill='none', stroke=svgwrite.rgb(0, 0, 0, '%')))  # czarny prostokąt
#     dwg.add(dwg.rect((x1, z1), (y2 - y1, z2 - z1), fill='none', stroke=svgwrite.rgb(255, 0, 0, '%')))  # czerwony prostokąt
#     dwg.add(dwg.rect((y1, z1), (x2 - x1, z2 - z1), fill='none', stroke=svgwrite.rgb(0, 255, 0, '%')))  # zielony prostokąt
#     dwg.save()
# #
#
# projection(geometry_data)


def projection(self, coordinates_data):
    current_time = datetime.now()
    text = f'projectred{current_time}'
    dwg = svgwrite.Drawing(text + '.svg', profile='full')

    counted_data = self.count_data(coordinates_data)

    top_left_x, top_left_y = counted_data['top_left_x'], counted_data['top_left_y']
    width, height, depth = counted_data['width'], counted_data['height'], counted_data['depth']
    min_y, min_z = counted_data['min_y'], counted_data['min_z']

    # Rysowanie prostokąta na płaszczyźnie x-y
    dwg.add(dwg.rect((top_left_x, top_left_y), (width, height), fill='none',
                     stroke=svgwrite.rgb(0, 0, 0, '%')))  # czarny prostokąt

    # Rysowanie prostokąta na płaszczyźnie x-z
    dwg.add(dwg.rect((top_left_x, min_z), (width, depth), fill='none',
                     stroke=svgwrite.rgb(255, 0, 0, '%')))  # czerwony prostokąt

    # Rysowanie prostokąta na płaszczyźnie y-z
    dwg.add(dwg.rect((min_y, min_z), (height, depth), fill='none',
                     stroke=svgwrite.rgb(0, 255, 0, '%')))  # zielony prostokąt

    dwg.save()
    return text + '.svg'







        # # Wyciąganie wartości x1, x2, y1, y2, z1, z2 z coordinates_data
        # x1, x2, y1, y2, z1, z2 = json.loads(coordinates_data).values()
        #
        # # Ustalenie wartości granicznych dla osi x, y, z
        # min_x = min(x1, x2)
        # max_x = max(x1, x2)
        # min_y = min(y1, y2)
        # max_y = max(y1, y2)
        # min_z = min(z1, z2)
        # max_z = max(z1, z2)
        #
        # # Obliczenie szerokości i wysokości prostokąta
        # width = abs(max_x - min_x)
        # height = abs(max_y - min_y)
        # depth = abs(max_z - min_z)
        #
        # # Wyznaczenie współrzędnych lewego górnego rogu prostokąta
        # top_left_x = min_x
        # top_left_y = min_y


# import json
# from datetime import datetime
# from django.http import JsonResponse
# from django.shortcuts import render
# from django.views import View
#
# import svgwrite
#
# from geoapp.forms import GeoForm
# from geoapp.models import GeometryCoordinatesModel
#
#
# class GeometryView(View):
#
#     def validate_coordinates(self, coordinates_dict):
#         for el in coordinates_dict.values():
#             return True if isinstance(el, int) else False
#
#     # def draw_img(self):
#
#
#     def projection(self, coordinates_data, x1, x2, y1, y2, z1, z2):
#         current_time = datetime.now()
#         text = f'projectred{current_time}'
#         dwg = svgwrite.Drawing(text + '.svg', profile='full')
#
#         dwg.add(dwg.rect((x1, y1), (y2 - y1, x2 - x1), fill='none', stroke=svgwrite.rgb(0, 0, 0, '%')))  # czarny prostokąt
#         dwg.add(dwg.rect((x1, z1), (y2 - y1, z2 - z1), fill='none', stroke=svgwrite.rgb(255, 0, 0, '%')))  # czerwony prostokąt
#         dwg.add(dwg.rect((y1, z1), (x2 - x1, z2 - z1), fill='none', stroke=svgwrite.rgb(0, 255, 0, '%')))  # zielony prostokąt
#         dwg.save()
#         return text + '.svg'
#
#     def get(self, request):
#         form = GeoForm()
#         queryset = GeometryCoordinatesModel.objects.all()
#         return render(request, 'geoapp/home.html', {'form': form, 'queryset': queryset})
#
#     def post(self, request):
#         form = GeoForm(request.POST)
#         if form.is_valid():
#             coordinates_data = form.cleaned_data['coordinates']
#             try:
#                 coordinates_dict = json.loads(coordinates_data)
#                 validate = self.validate_coordinates(coordinates_dict)
#                 if validate:
#                     x1, x2, y1, y2, z1, z2 = coordinates_dict.values()
#                     geo_obj = GeometryCoordinatesModel.objects.create(**coordinates_dict)
#                     geo_obj.save()
#                     svg_path = self.projection(coordinates_data, x1, x2, y1, y2, z1, z2)
#                     response_data = {'status': 'success', 'svg_path': svg_path}
#                     return JsonResponse(response_data)
#                 else:
#                     response_data = {'status': 'error', 'message': 'Invalid form data'}
#             except json.JSONDecodeError:
#                 response_data = {'status': 'error', 'message': 'Invalid JSON data'}
#         else:
#             response_data = {'status': 'error', 'message': 'Invalid form data'}
#
#         return JsonResponse(response_data)
#

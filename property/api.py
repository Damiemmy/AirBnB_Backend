from django.http import JsonResponse
from rest_framework.decorators import api_view,permission_classes,authentication_classes
from .forms import PropertyForm,Reservation
from rest_framework import generics

from .models import Property
from .serializers import PropertySerializer,PropertyDetailSerializer

@api_view(['GET'])
@authentication_classes([])
@permission_classes([])

def properties_list(request):
    properties = Property.objects.all()
    serializer=PropertySerializer(properties,many=True)

    return JsonResponse({
        'data':serializer.data
    })

@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def properties_detail(request,pk):
    single_property=Property.objects.get(pk=pk)
    serializer=PropertyDetailSerializer(single_property, many=False)
    return JsonResponse(serializer.data)

@api_view(["POST","FILES"]) 
def create_property(request):
    print("POST:", request.POST)
    print("FILES:", request.FILES)

    form=PropertyForm(request.POST,request.FILES)

    if form.is_valid():
        property=form.save(commit=False)
        property.landlord=request.user
        property.save()
        return JsonResponse({'success':True})
    else:
        print('error',form.errors,form.non_field_errors)
        return JsonResponse({'errors': form.errors.as_json()},status=400 )

@api_view(['POST'])
def book_property(request,pk):
    try:
        start_date= request.POST.get('start_date','')
        end_date=request.POST.get('end_date','')
        number_of_nights=request.POST.get('number_of_nights','')
        total_price=request.POST.get('total_price','')
        guests=request.POST.get('guests','')

        property=Property.objects.get(pk=pk)
        Reservation.objects.create(
            property=property,
            guests=guests,
            end_date=end_date,
            start_date=start_date,
            total_price=total_price,
            number_of_nights=number_of_nights,
            created_by=request.user

        )


    except exception as e:
        print("Error",e)
        
        return JsonResponse({'success': False})

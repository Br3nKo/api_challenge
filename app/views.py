from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import exceptions
from rest_framework.pagination import LimitOffsetPagination
from django.utils import timezone
from .models import Country
from .serializer import CountrySerializer
from.utils import validate_query, ValidationError


class CountryList(APIView):
    """
    List all countries or create a new Country instance
    """

    # GET: retrieve all countries
    def get(self, request, format=None):
        country_code = request.query_params.get('countryCode', None)
        limit = request.query_params.get('limit', 50)
        offset = request.query_params.get('offset', 0)
        
        #validate offset and limit
        try:
            validate_query(offset, limit)
        except ValidationError as e:
            return Response(e.message, status=status.HTTP_400_BAD_REQUEST)

        countries = Country.objects.all()
        # Filter by countryCode if provided
        if country_code:
            countries = countries.filter(countryCode=country_code)
        
        paginator = LimitOffsetPagination()
        paginator.default_limit = limit
        paginator.offset = offset
        paginated_countries = paginator.paginate_queryset(countries, request)
        serializer = CountrySerializer(paginated_countries, many=True)
        
        response_data = {
            "links": {
                "next": paginator.get_next_link(),
                "previous": paginator.get_previous_link(),
            },
            "pagination": {
                "count": paginator.count,
                "offset": paginator.get_offset(request),
                "limit": paginator.get_limit(request),
            },
            "results": serializer.data
        }
        
        return Response(response_data)
    
    # POST: create a new Country
    def post(self, request, format=None):
        country = request.data
        country['createdAt'] = timezone.now()
        country['groupId'] = 0
        serializer = CountrySerializer(data=country)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  
class CountryDetail(APIView):
    """
    Retrieve or update a Country instance.
    """
    
    # check if an object with given <id> exists
    def get_object(self, id):
        try:
            return Country.objects.get(id=id)
        except Country.DoesNotExist:
            raise exceptions.NotFound("Country not found")
    
    # GET: retrieve a country by <id>
    def get(self, request, id, format=None):
        country = self.get_object(id)
        serializer = CountrySerializer(country)
        return Response(serializer.data)

    # PUT: update an existing country with given <id>
    def put(self, request, id, format=None):
        country = self.get_object(id)
        serializer = CountrySerializer(country, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    ''' following method is not a part of the assingnment '''
    # DELETE: remove a country with given <id>
    def delete(self, request, id, format=None):
        country = self.get_object(id)
        country.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)  

import json
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from faculty.models import ContactDetails
# from rest_framework_simplejwt.token import TokenObtainPairView


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attr):
        data = super().validate(attr)
        token = self.get_token(self.user)
        
        if(self.user.role == 'teacher'):
            userProfile = ContactDetails.objects.get(user=self.user)
            profile = {
                'facultyId': userProfile.faculty_id,
                'adharNo': userProfile.adhar_no,
                'facultyName': userProfile.faculty_name,
                'designation': userProfile.designation,
                'mobile_no': userProfile.mobile_no,
                'email': userProfile.email 
            }
            profile_str = json.dumps(profile)
            data['profile'] = profile_str

        return data

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
from rest_frameworkd import APIView
from rest_frameworkd.response import response
from rest_frameworkd.permissions import AllowAny, IsAuthenticated
from rest_frameworkd_simplejwt.token import RefreshToekn
from tracker.serializers.auth_serializers import SignUpSerializer

class SignUpView(APIView):
    permission_classes = [AllowAny]
    
    def post(self, request):
        serializer = SignUpSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
class Loggout(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        try: 
            refresh_token = request.data.get('refresh_token')
            token = RefreshToekn(refresh_token)
            return Response({"message": "Logged out successfully"}, status=200)
        except Exception as e:
            return Response({"error": str(e)}, status=400)
        
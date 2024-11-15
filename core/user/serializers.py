from core.user.models import User
from core.abstract.serializers import AbstractSerializer

class UserSerializer(AbstractSerializer):

    class Meta:
        model = User
        fields = ["id","username", "first_name", "last_name", "email", "created", "updated"]
        
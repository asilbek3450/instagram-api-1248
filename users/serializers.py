from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from shared.utils import check_email_or_phone
from .models import User, UserConfirmation, VIA_EMAIL, VIA_PHONE


class SignUpSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)

    def __init__(self, *args, **kwargs):
        super(SignUpSerializer, self).__init__(*args, **kwargs)
        self.fields['email_phone_number'] = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = (
            'id',
            'auth_type',
            'auth_status',
        )
        extra_kwargs = {
            'auth_type': {'read_only': True, 'required': False},
            'auth_status': {'read_only': True, 'required': False},
        }

    def create(self, validated_data):
        pass

    def validate(self, data):
        super(SignUpSerializer, self).validate(data)
        data = self.auth_validate(data)
        return data

    @staticmethod
    def auth_validate(data):
        print(data)
        user_input = str(data.get('email_phone_number')).lower()
        input_type = check_email_or_phone(user_input)  # email or phone
        if input_type == "email":
            data = {
                'auth_type': VIA_EMAIL,
                'email': user_input
            }
        elif input_type == "phone":
            data = {
                'auth_type': VIA_PHONE,
                'phone_number': user_input
            }
        else:
            data = {
                "success": False,
                "message": "Email yoki telefon raqamni to'g'ri kiriting!"
            }
            raise ValidationError(data)

        return data

    # def validate_email_phone_number(self, value):
    #     value = str(value).lower()
    #     pass

# class ChangeUserInformation(serializers.Serializer):
#     pass
#
# class ChangeUserPhotoSerializer(serializers.Serializer):
#     pass
#
# class LoginSerializer(TokenObtainPairSerializer):
#     pass
#
#
# class LoginRefreshSerializer(TokenRefreshSerializer):
#     pass
#
# class LogoutSerializer(serializers.Serializer):
#     pass
#
#
# class ForgotPasswordSerializer(serializers.Serializer):
#     pass
#
# class ResetPasswordSerializer(serializers.ModelSerializer):
#     pass

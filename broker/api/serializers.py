from rest_framework import serializers
# from .models import LANGUAGE_CHOICES, STYLE_CHOICES
# from .wallet import Wallet
# from .models import User


class WalletSerializer(serializers.ModelSerializer):

    class Meta:
        model = Wallet
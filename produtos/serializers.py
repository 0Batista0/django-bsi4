from decimal import Decimal
from rest_framework import serializers

from .models import Produto


class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = ("id", "nome", "marca", "preco", "estoque", "descrição")

    def validate_nome(self, value):
        nome_limpo = value.strip()
        if len(nome_limpo) < 2:
            raise serializers.ValidationError(
                "O nome deve possuir pelo menos 2 caracteres."
            )
        return nome_limpo

    def validate_marca(self, value):
        marca_limpa = value.strip()
        if len(marca_limpa) < 2:
            raise serializers.ValidationError(
                "A marca deve possuir pelo menos 2 caracteres."
            )
        return marca_limpa

    def validate_preco(self, value):
        if value <= Decimal("0"):
            raise serializers.ValidationError("O preço deve ser maior que zero.")
        return value

    def validate_estoque(self, value):
        if value < 0:
            raise serializers.ValidationError("O estoque não pode ser negativo.")
        return value
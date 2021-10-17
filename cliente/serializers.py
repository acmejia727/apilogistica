from rest_framework import serializers
from cliente.models import Cliente

class ClientSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    class Meta:
        model = Cliente
        fields = '__all__'
    
    def validate(self, data):
        cc = data['iddoc']
        
        if cc[0] == '0':
            raise serializers.ValidationError('La cédula no puede iniciar por cero')
        if len(cc) <= 5:
            raise serializers.ValidationError('Longitud de cédula muy corta')
        if len(cc) > 10:
            raise serializers.ValidationError('Longitud de cédula muy larga')
        
        if not cc.isdigit():
            raise serializers.ValidationError('Dni inválido')

        return data
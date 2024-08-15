# UTILIZANDO O PADRÃO CLEAN ARCHITECTURE EM PYTHON DRF


Sim, é totalmente possível aplicar o conceito de Clean Architecture em projetos usando Django e Django REST Framework (DRF). A Clean Architecture, proposta por Robert C. Martin, é uma abordagem de design de software que visa separar as responsabilidades e isolar as regras de negócio da infraestrutura e da interface. O principal objetivo é tornar o código mais modular, testável e fácil de manter.

Aqui está um guia básico sobre como você pode adaptar a Clean Architecture para um projeto Django com DRF:

### Estrutura Básica do Projeto

A Clean Architecture sugere a organização do código em camadas, cada uma com responsabilidades distintas. Em um projeto Django, você pode adaptar isso da seguinte forma:

1. **Camada de Domínio**: Contém a lógica de negócios e as regras do domínio. Em Django, você pode ter uma pasta `domain` ou `core` onde definirá suas entidades, serviços e regras de negócios.

2. **Camada de Aplicação**: Define casos de uso ou interações específicas do aplicativo. No Django, você pode criar uma pasta `application` onde implementará a lógica que orquestra as operações de negócios.

3. **Camada de Interface (ou Apresentação)**: Lida com a comunicação com o usuário e outras interfaces externas. No contexto do Django, você pode ter uma pasta `interface` para seus views e serializers.

4. **Camada de Infraestrutura**: Trata da persistência de dados, configuração de serviços externos e outras integrações. Em Django, isso inclui models e configurações de banco de dados.

### Exemplo de Estrutura de Diretórios

Vamos imaginar uma estrutura básica para um projeto Django com DRF utilizando Clean Architecture:

```
myproject/
    ├── domain/
    │   ├── __init__.py
    │   ├── models.py       # Entidades do domínio
    │   ├── services.py     # Lógica de negócios
    │   └── repositories.py # Interfaces para acesso a dados
    ├── application/
    │   ├── __init__.py
    │   ├── use_cases.py    # Casos de uso
    ├── interface/
    │   ├── __init__.py
    │   ├── views.py        # Views DRF
    │   ├── serializers.py  # Serializers DRF
    ├── infrastructure/
    │   ├── __init__.py
    │   ├── repositories.py # Implementações dos repositórios
    ├── manage.py
    └── myproject/
        ├── __init__.py
        ├── settings.py
        ├── urls.py
        └── wsgi.py
```

### Exemplos de Implementação

#### 1. **Camada de Domínio**

```python
# domain/models.py
class Product:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price

# domain/services.py
class ProductService:
    def calculate_discount(self, product, discount_percentage):
        return product.price * (1 - discount_percentage / 100)
```

#### 2. **Camada de Aplicação**

```python
# application/use_cases.py
from domain.services import ProductService
from domain.models import Product

class ProductUseCase:
    def __init__(self, product_repository):
        self.product_repository = product_repository
        self.product_service = ProductService()

    def apply_discount_to_product(self, product_id, discount_percentage):
        product = self.product_repository.get_by_id(product_id)
        return self.product_service.calculate_discount(product, discount_percentage)
```

#### 3. **Camada de Interface**

```python
# interface/views.py
from rest_framework import views
from rest_framework.response import Response
from .serializers import ProductSerializer
from application.use_cases import ProductUseCase

class DiscountView(views.APIView):
    def post(self, request):
        product_id = request.data.get('product_id')
        discount_percentage = request.data.get('discount_percentage')
        product_use_case = ProductUseCase()  # Você pode injetar dependências aqui
        discounted_price = product_use_case.apply_discount_to_product(product_id, discount_percentage)
        return Response({'discounted_price': discounted_price})

# interface/serializers.py
from rest_framework import serializers

class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=100)
    price = serializers.DecimalField(max_digits=10, decimal_places=2)
```

#### 4. **Camada de Infraestrutura**

```python
# infrastructure/repositories.py
from domain.models import Product

class ProductRepository:
    def get_by_id(self, product_id):
        # Simulando uma busca no banco de dados
        return Product(id=product_id, name="Sample Product", price=100.0)
```

### Considerações Finais

- **Injeção de Dependências**: É recomendável usar injeção de dependências para passar instâncias de repositórios ou serviços para os casos de uso e views.
- **Testes**: A Clean Architecture facilita a escrita de testes unitários e de integração, já que as regras de negócios e a lógica de aplicação estão isoladas.
- **Django ORM**: Lembre-se de que o Django ORM pode se misturar com a camada de infraestrutura, e você pode usar repositórios para encapsular o acesso ao banco de dados.

Adotar a Clean Architecture em um projeto Django pode exigir um pouco mais de trabalho inicial para configurar a estrutura e garantir que as camadas estejam corretamente separadas, mas os benefícios em termos de modularidade e testabilidade geralmente compensam o esforço.
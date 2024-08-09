# Client


Модуль Client представляет собой комплексное решение для взаимодействия с различными API-сервисами. Включает в себя несколько специализированных компонентов, каждый из которых предназначен для работы с конкретными типами API. Модуль разработан для упрощения интеграции и автоматизации работы с внешними сервисами.

| Model        | Website                                                |
| ------------ | ------------------------------------------------------ |
| gpt3         | [chat9.yqcloud.top](https://chat9.yqcloud.top/)        |
| gpt4         | [you.com](https://you.com/)                            |
| gpt3_5       | [vitalentum.net](https://vitalentum.net/free-chat-gpt) |
| prodia       | [prodia.com](https://prodia.com/)                      |
| pollinations | [pollinations.ai](https://pollinations.ai/)            |

Примеры использования

```python
from freeGPTFix import Client
resp = Client.create_completion("gpt3_5", "Your text")
print(resp)
```
```python
from freeGPTFix import Client
resp = Client.create_completion("gpt3", "Your text")
print(resp)
```
```python
from freeGPTFix import Client
resp = Client.create_completion("gpt4", "Your text")
print(resp)
```

Генерация изображений
```python
from freeGPTFix import Client
from PIL import Image
from io import BytesIO

while True:
    prompt = input("> ")
    try:
        resp = Client.create_generation("prodia", prompt)
        Image.open(BytesIO(resp)).show()
        print(f"🤖: Image shown.")
    except Exception as e:
        print(f"🤖: {e}")
```

```python
from freeGPTFix import Client
from PIL import Image
from io import BytesIO

while True:
    prompt = input("> ")
    try:
        resp = Client.create_generation("pollinations", prompt)
        Image.open(BytesIO(resp)).show()
        print(f"🤖: Image shown.")
    except Exception as e:
        print(f"🤖: {e}")
```

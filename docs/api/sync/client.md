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

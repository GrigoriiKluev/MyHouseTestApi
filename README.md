Для запуска необходимо установить зависимости pip install - r requirements.txt

При решении задания №1 (1. Как правильно сохранять modified_by?)
Использовал View где явно указали пользователя который в данный момент зарегистрирован в поле modified_by
![image](https://user-images.githubusercontent.com/42998370/233980473-9bf5fed7-c382-4bcb-bde6-bc056beb8676.png)

При решении задания №2 (Для создания Entity на вход POST API подаётся json вида
{"data[value]": 10})

 Использовал варианты с несколькими решениями 
A) Сделал обработку JSON в методе create() во вьюхе EntityViewSet

![обработка JSON1 2023-04-24 141539](https://user-images.githubusercontent.com/42998370/233981173-c48e5f27-5c73-4f5c-8ebe-6ff5c9ac2f34.jpeg)

B) Вариант 2 реализации в сериалайзере (Вариант не предпочтительный , т.к. остается возможность записывать только "data[value]" в value в БД)

![обработка JSON2 2023-04-24 142010](https://user-images.githubusercontent.com/42998370/233985147-374748c5-8981-406c-9c5e-9d23801c9c41.jpeg)


При решении задания №3 (Как вывести properties в формате {key:value, ...})
Использовал serializers.SerializerMethodField где и производилась обработка полей связанных моделей many_to_many


![KeyValue 2023-04-24 144445](https://user-images.githubusercontent.com/42998370/233987236-661e5ff7-3e7d-4472-a833-e18b86767068.jpeg)

Получилось примерно так 

![результат 2023-04-24 145128](https://user-images.githubusercontent.com/42998370/233988295-1fbbf2c1-2bcc-4654-9034-06277c93a43e.jpeg)


Модели Property и Entity добавлены в админку для удобства . 

установлен drf-spectacular с доступами по следующим URL (http://127.0.0.1:8000/api/schema/swagger-ui/)

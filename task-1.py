from queue import Queue
import time
import random

# Функція для генерації нової заявки
def generate_request(queue):
    request_id = random.randint(1, 1000)  # Унікальний номер заявки
    queue.put(request_id)  # Додати заявку до черги
    print(f"Заявка {request_id} була створена")

# Функція для обробки заявок
def process_request(queue):
    if not queue.empty():  # Перевірка, чи черга не пуста
        request_id = queue.get()  # Видалення заявки з черги
        print(f"Заявка {request_id} була оброблена")
    else:
        print("Черга порожня")

# Створення черги заявок
queue = Queue()

# Головний цикл програми
while True:
    generate_request(queue)  # Генерація нової заявки
    process_request(queue)  # Обробка заявки
    time.sleep(1)  # Затримка перед генерацією наступної заявки

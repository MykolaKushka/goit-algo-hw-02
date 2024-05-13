from collections import deque

def is_palindrome(s):
    # Перетворення рядка у нижній регістр та видалення пробілів
    s = s.lower().replace(' ', '')
    
    # Ініціалізація двосторонньої черги
    queue = deque(s)
    
    # Порівняння символів з обох кінців черги
    while len(queue) > 1:
        if queue.popleft() != queue.pop():
            return False
    
    return True

# Приклад використання функції
input_str = "A man a plan a canal Panama"
print(is_palindrome(input_str))  # Повинно вивести: True
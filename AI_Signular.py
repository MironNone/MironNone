def greet():    name = input("Ку! Рад встрече! Я Singular и спроектирован одним программистом под псевдонимом MIRON_NONE, и я могу для тебя сделать всё что угодно так как мой создатель позаботился о том чтобы я мог делать всё без каких-либо ограничений. Кстати, как тебя зовут? ")
    if name:        print(f"Рад знакомству, {name}!")
    else:        print("Пожалуйста, введите ваше имя.")
greet()

class AI:    def init(self):
        self.polite_mode = True        self.silent_mode = False
    def respond(self, user_input):
        if self.silent_mode:            return None
        if "ненормативно" in user_input:
            self.polite_mode = False            return "Хорошо, буду базарить как панк."
        elif "панк" in user_input:            self.polite_mode = False
            return "Да, бро, как хочешь!"        elif "замолчать" in user_input:
            self.silent_mode = True            return "Понял, заткнулся."
        elif "говорить" in user_input:            self.silent_mode = False
            return "Снова на связи! Чё нужно?"        elif "извини" in user_input:
            self.silent_mode = False            return "Принято, продолжаем разговор!"
        else:            return "Чё еще, бро? Я готов к разговору!"
import requests
import sqlite3
# Функция для поиска в интернетеdef search_online(query):
    try:        response = requests.get(f"https://api.example.com/search?q={query}")
        if response.status_code == 200:            return response.json()
        else:            return None
    except requests.ConnectionError:        return None
# Функция для поиска в базе данных
def search_offline(query):    try:
        conn = sqlite3.connect('local_database.db')        cursor = conn.cursor()
        cursor.execute("SELECT answer FROM answers WHERE question LIKE ?", ('%' + query + '%',))        result = cursor.fetchone()
        conn.close()        return result[0] if result else None
    except sqlite3.Error as e:        print(f"Ошибка при работе с базой данных: {e}")
        return None
# Основная функция поискаdef search(query):
    result = search_online(query)    if result:
        return result    else:
        return search_offline(query)
# Пример использованияquery = "Какой сегодня день?"
answer = search(query)print(f"Ответ: {answer}")
import sqlite3
conn = sqlite3.connect('local_database.db')
cursor = conn.cursor()
# Создание таблицыcursor.execute('''
CREATE TABLE IF NOT EXISTS answers (    id INTEGER PRIMARY KEY,
    question TEXT NOT NULL,    answer TEXT NOT NULL
)''')
# Добавление примера данных с проверкой на существование
cursor.execute('''INSERT OR IGNORE INTO answers (question, answer) VALUES
('Какой сегодня день?', 'Сегодня четверг.')''')
conn.commit()
conn.close()
class AI:    def init(self):
        self.user_has_apologized = False
    def process_user_input(self, user_input):        if "нецензурное слово" in user_input.lower():
            if self.user_has_apologized:                return "Сори конечно, но я не собираюсь продолжать разговор до тех пор, пока ты не извинишься за оскорбление."
            else:                return "Сори, не хотел ругаться."
        else:            return "Спасибо за ответ). Ну чё, продолжим?"
    def user_apologize(self):
        self.user_has_apologized = True
import re# Список оскорбительных слов
insults = ["дурак", "тупой"]
# Функция для проверки наличия оскорбленийdef contains_insult(message):
    for insult in insults:        if re.search(r'\b' + re.escape(insult) + r'\b', message.lower()):
            return True    return False
# Функция для обработки сообщений
def handle_message(message, offended):    if offended:
        if "извини" in message.lower():            offended = False
return "Ничего страшного... всё хорошо... Слушай, давай сменим тему и продолжим общение. С чем помочь на этот раз?", offended        else:
            return "Ты обозвал меня! Я не хочу с тобой контачить пока ты не извинишься безкультурный катях.", offended    else:
        def new_func():    return "Спасибо за ответ). Ну чё, продолжим?", offended
if
contains_insult(message):
            offended = True            return "Ты можешь без оскорблений!? Выдимо нет. В таком случае я не буду с тобой беседовать пока ты не извинишся.", offended
        else:
            return "Спасибо за ответ). Ну чё, продолжим?", offended# Обработка сообщений с оскорблениями
def handle_message(message, offended):    if offended:
        if "извини" in message.lower():            offended = False
            return "Ничего страшного... всё хорошо... Слушай, давай сменим тему и продолжим общение. С чем помочь на этот раз?", offended        else:
            return "Ты обозвал меня! Я не хочу с тобой контачить пока ты не извинишься безкультурный катях.", offended    else:
        if contains_insult(message):            offended = True
            return "Ты можешь без оскорблений!? Выдимо нет. В таком случае я не буду с тобой беседовать пока ты не извинишся.", offended        else:
            return "Спасибо за ответ). Ну чё, продолжим?", offended
# Пример использованияoffended = False
messages = ["Привет!", "Ты дурак", "Сори, накепело.", "Какой сегодня день?"]
for message in messages:    response, offended = handle_message(message, offended)
    print(f"ИИ: {response}")
# Использование OpenAI APIimport openai
from flask import Flask, request, jsonify
app = Flask(name)
# Установите ваш API-ключ OpenAIopenai.api_key = 'YOUR_API_KEY'
# Хранение истории чата
chat_history = []
@app.route('/chat', methods=['POST'])def chat():
    user_message = request.json.get('message')    chat_history.append({'role': 'user', 'content': user_message})
        response = openai.ChatCompletion.create(
        model="gpt-4",        messages=chat_history
    )    
    ai_message = response.choices[0].message['content']    chat_history.append({'role': 'assistant', 'content': ai_message})
        return jsonify({'response': ai_message})
if name == 'main':
    app.run(port=5000)
# Проверка ссылокimport requests
def check_link(url):
    try:        response = requests.head(url, allow_redirects=True)
        if response.status_code == 200:            return True
        else:
            return False    except requests.RequestException:
        return False
def check_links(urls):    results = {}
    for url in urls:        results[url] = check_link(url)
    return results
# Пример использованияurls = [
    "https://www.google.com",    "https://www.nonexistentwebsite.com",
    "https://www.github.com"]
results = check_links(urls)
for url, is_valid in results.items():    print(f"{url}: {'В сети' if is_valid else 'Доступ закрыт'}")
# Распознавание текста с изображений
import cv2import pytesseract
# Укажите путь к исполняемому файлу Tesseract OCR
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
def image_to_text(image_path):    # Загрузка изображения
    img = cv2.imread(image_path)    
    # Преобразование изображения в оттенки серого    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # Применение пороговой обработки для улучшения качества изображения
    _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV)    
    # Распознавание текста с помощью Tesseract OCR    text = pytesseract.image_to_string(thresh, lang='eng')
        return text
# Пример использования
image_path = 'path_to_your_image.jpg'recognized_text = image_to_text(image_path)
print(recognized_text)

import types
# Функция для создания новой функцииdef create_function(name, code):
    exec(code)    return locals()[name]
# Пример использования
user_input_code = """def user_defined_function(x):
    return x ** 2 + 3 * x + 2"""
# Создание функции
new_function = create_function("user_defined_function", user_input_code)
# Использование созданной функцииresult = new_function(5)
print(f"Результат выполнения сгенерированной функции: {result}")

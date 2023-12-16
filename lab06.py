# Імпортуємо бібліотеку tkinter для створення графічного інтерфейсу користувача
import tkinter as tk
# Створюємо основне вікно програми та присвоюємо йому назву "Тест з кібербезпеки"
root = tk.Tk()
root.title("Тест з кібербезпеки")
# Створення запитання 1
question1_label = tk.Label(root, text="1. Що означає абревіатура VPN?") # створюємо напис з першим запитанням
question1_label.pack() # відображаємо напис на екрані
# варіанти відповідей для першого запитання
question1_options = [("Virtual Personal Network", "VPN1"),
                     ("Virtual Private Network", "VPN2"),
                     ("Very Personal Network", "VPN3")]
question1_answer = tk.StringVar() # створюємо змінну для збереження відповіді
# створюємо радіокнопки для вибору відповіді
for text, val in question1_options: 
    rb = tk.Radiobutton(root, text=text, variable=question1_answer, value=val)
    rb.pack() # відображення радіокнопки на екрані

question2_label = tk.Label(root, text="2. Що таке фішинг?")
question2_label.pack()

question2_options = [("Тип програмного забезпечення", "phishing1"),
                     ("Шахрайська діяльність, що використовує соціальну інженерію", "phishing2"),
                     ("Метод шифрування даних", "phishing3")]
question2_answer = tk.StringVar()
for text, val in question2_options:
    rb = tk.Radiobutton(root, text=text, variable=question2_answer, value=val)
    rb.pack()

question3_label = tk.Label(root, text="3. Що таке захист ПЗ (антивірус)?")
question3_label.pack()
question3_var = tk.StringVar()
question3_options = ["Захист від поганих програм", "Захист від вірусів", "Захист від хакерів"]
question3_dropdown = tk.OptionMenu(root, question3_var, *question3_options)
question3_dropdown.pack()

question4_label = tk.Label(root, text="4. Що таке двофакторна аутентифікація?")
question4_label.pack()

question4_var = tk.IntVar()
question4_options = [("Метод перевірки особи, який використовує SMS та відбиток пальця", "2FA2"),
                     ("Метод перевірки особи, який використовує телефон та голосовий код", "2FA3"),
                     ("Метод перевірки особи, який використовує два різних способи підтвердження", "2FA4")]
for text, val in question4_options:
    cb = tk.Checkbutton(root, text=text, variable=question4_var, onvalue=val)
    cb.pack()

question5_label = tk.Label(root, text="5. Що таке соціальна інженерія в контексті кібербезпеки?")
question5_label.pack()
question5_input = tk.Entry(root)
question5_input.pack()

question6_label = tk.Label(root, text="6. Які основні методи виявлення та запобігання кібератак використовуються в сфері кібербезпеки?")
question6_label.pack()
question6_options = ["Firewall", "IPS/IDS", "Antivirus", "Encryption"]
question6_var = tk.StringVar()
for option in question6_options:
    rb = tk.Radiobutton(root, text=option, variable=question6_var, value=option)
    rb.pack()

# Функція для перевірки всіх відповідей
def check_answers():
    correct_answers = 0 # Створюємо змінну для рахунку правильних відповідей
    
    # Перевіряємо, чи відповідь на перше запитання правильна
    if question1_answer.get() == "VPN2":
        result_label1.config(text="Правильно!")  # Встановлюємо текстове повідомлення "Правильно!"
        correct_answers += 1 # Збільшуємо лічильник правильних відповідей на 1
    else:
        result_label1.config(text="Неправильно. Правильна відповідь: Virtual Private Network")  # Встановлюємо текстове повідомлення "Неправильно. Правильна відповідь: Virtual Private Network"

    if question2_answer.get() == "phishing2":
        result_label2.config(text="Правильно!")
        correct_answers += 1
    else:
        result_label2.config(text="Неправильно. Правильна відповідь: Шахрайська діяльність, що використовує соціальну інженерію")

    if question3_var.get() == "Захист від вірусів":
        result_label3.config(text="Правильно!")
        correct_answers += 1
    else:
        result_label3.config(text="Неправильно. Правильна відповідь: Захист від вірусів")

    if question4_var.get() == 1:
        result_label4.config(text="Правильно!")
        correct_answers += 1
    else:
        result_label4.config(text="Неправильно. Правильна відповідь: Метод перевірки особи, який використовує два різних способи підтвердження")

    if question5_input.get() == "Маніпулювання людьми з метою отримання конфіденційної інформації":
        result_label5.config(text="Правильно!")
        correct_answers += 1
    else:
        result_label5.config(text="Неправильно. Правильна відповідь: Маніпулювання людьми з метою отримання конфіденційної інформації")

    if question6_var.get() == "Firewall":
        result_label6.config(text="Правильно!")
        correct_answers += 1
    else:
        result_label6.config(text="Неправильно. Правильна відповідь: Firewall")

    result_label_total.config(text=f"Правильних відповідей: {correct_answers}/6") # встановлюємо загальний результат правильних відповідей

# Кнопка для перевірки всіх відповідей
check_button_total = tk.Button(root, text="Перевірити всі відповіді", command=check_answers) # Створюємо кнопку для перевірки всіх відповідей
check_button_total.pack() # Розміщуємо кнопку на екрані

result_label1 = tk.Label(root, text="") # Створюємо мітку для відображення результату перевірки
result_label1.pack() # Розміщуємо мітку на екрані

result_label2 = tk.Label(root, text="")
result_label2.pack()

result_label3 = tk.Label(root, text="")
result_label3.pack()

result_label4 = tk.Label(root, text="")
result_label4.pack()

result_label5 = tk.Label(root, text="")
result_label5.pack()

result_label6 = tk.Label(root, text="")
result_label6.pack()

result_label_total = tk.Label(root, text="")
result_label_total.pack()

# Запуск головного циклу обробника подій
root.mainloop()
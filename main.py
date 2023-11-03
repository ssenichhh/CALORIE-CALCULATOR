from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox

root = Tk()


def entry():
    root.geometry("500x250")
    root.title("Вхід в систему")
    button_entry1 = Button(text="Пройти реєстрацію", command=lambda: registration())
    button_entry2 = Button(text="Авторизуватися", command=lambda: auntification())
    button_entry1.grid(row=0, column=0)
    button_entry2.grid(row=0, column=3)


def registration():
    text_login = Label(text="Створіть логін:")
    register_l = Entry()
    text_password1 = Label(text="Створіть пароль:")
    register_p = Entry()
    button_register = Button(text="Зареєструватися!", command=lambda: save())
    text_login.grid(row=1, column=0)
    register_l.grid(row=2, column=0)
    text_password1.grid(row=3, column=0)
    register_p.grid(row=4, column=0)
    button_register.grid(row=5, column=0)

    def save():
        user_login = register_l.get()
        user_password = register_p.get()
        with open('login.txt', 'a') as log:
            log.write(user_login + '|' + user_password + '\n')
        text_log1 = messagebox.showinfo("Вітання", "Реєстрація успішна")
        log.close()
        auntification()


def auntification():
    text_enter_log = Label(text="Введіть ваш логін:")
    enter_log = Entry()
    text_enter_pass = Label(text="Введіть ваш пароль:")
    enter_pass = Entry()
    button_entry = Button(text="Увійти", command=lambda: log_pass())
    text_enter_log.grid(row=1, column=3)
    enter_log.grid(row=2, column=3)
    text_enter_pass.grid(row=3, column=3)
    enter_pass.grid(row=4, column=3)
    button_entry.grid(row=5, column=3)

    def log_pass():
        file_login = list()
        with open('login.txt', 'rt') as login:
            login_list = login.readlines()
            for i in range(len(login_list)):
                login_list[i] = login_list[i].strip('\n')
                login_pass = login_list[i].split('|')
                file_login.append(login_pass)
            true_login = enter_log.get()
            true_password = enter_pass.get()
            user_info = list()
            user_info.append(true_login)
            user_info.append(true_password)
        if user_info not in file_login:
            messagebox.showerror("Info", "Невірний пароль або логін!")
        else:
            messagebox.showinfo("Вдалого користування!", "Для переходу до головного меню клацніть: Почнемо", )
            button_confirmation = Button(root, text="Почнемо", command=lambda: mainmenu()).grid(row=7, column=3)


def mainmenu():
    root.withdraw()
    top = Toplevel()
    top.geometry("1100x500")
    top.title("Основне меню")
    option_text1 = Label(top, text="Введіть свою персональну інформацію:")
    age_text = Label(top, text="Вкажіть ваш вік:")
    age = Entry(top)
    weight_text = Label(top, text="Вкажіть вашу вагу:")
    weight = Entry(top)
    height_text = Label(top, text="Вкажіть ваш зріст:")
    height = Entry(top)
    activity_text = Label(top, text="Оцініть вашу фізичну активність:")
    activity = Combobox(top, values=("1)Низька активність", "2)Помірна активність", "3)Середня активність",
                                     "4)Висока активність", "5)Дуже висока активність"))
    gender_text = Label(top, text="Вкажіть вашу стать:")
    gender = Combobox(top, values=("Чоловіча", "Жіноча"))
    option1 = Button(top, text="Розрахувати", command=lambda: itmcalculation())
    option_text1.grid(row=0, column=0)
    gender_text.grid(row=1, column=0)
    gender.grid(row=1, column=1)
    age_text.grid(row=2, column=0)
    age.grid(row=2, column=1)
    weight_text.grid(row=3, column=0)
    weight.grid(row=3, column=1)
    height_text.grid(row=4, column=0)
    height.grid(row=4, column=1)
    activity_text.grid(row=5, column=0)
    activity.grid(row=5, column=1)
    option1.grid(row=6, column=1)

    def itmcalculation():
        a = int(age.get())
        w = int(weight.get())
        h = int(height.get())
        itm = w / ((h / 100) ** 2)
        itm1 = round(itm, 2)
        itm_info = Label(top, text="Ваш індекс тіла: " + str(itm1)).grid(row=7, column=1)
        if itm < 18.5:
            itm_info1 = Label(top, text="Індекс тіла нижче норми, вам рекомендован курс набору ваги ")
            button_low1 = Button(top, text="Програма набору ваги",
                                 command=lambda: bmrcalculation1())
            button_low2 = Button(top, text="Програма утримання ваги",
                                 command=lambda: bmrcalculation2())
            button_low3 = Button(top, text="Прогама схуднення(не рекомендовано)",
                                 command=lambda: bmrcalculation3())
            itm_info1.grid(row=8, column=1)
            button_low1.grid(row=9, column=0)
            button_low2.grid(row=9, column=1)
            button_low3.grid(row=9, column=2)

        if 18.5 < itm <= 25:
            itm_info2 = Label(top, text="Індекс тіла в нормі")
            button_low1 = Button(top, text="Програма набору ваги",
                                 command=lambda: bmrcalculation1())
            button_low2 = Button(top, text="Програма утримання ваги",
                                 command=lambda: bmrcalculation2())
            button_low3 = Button(top, text="Прогама схуднення",
                                 command=lambda: bmrcalculation3())
            itm_info2.grid(row=8, column=1)
            button_low1.grid(row=9, column=0)
            button_low2.grid(row=9, column=1)
            button_low3.grid(row=9, column=2)

        if 25 < itm < 30:
            itm_info3 = Label(top, text="Індекс тіла трохи вище норми, вам рекомендован курс схуднення")
            button_low1 = Button(top, text="Програма набору ваги",
                                 command=lambda: bmrcalculation1())
            button_low2 = Button(top, text="Програма утримання ваги",
                                 command=lambda: bmrcalculation2())
            button_low3 = Button(top, text="Прогама схуднення(рекомендовано)",
                                 command=lambda: bmrcalculation3())
            itm_info3.grid(row=8, column=1)
            button_low1.grid(row=9, column=0)
            button_low2.grid(row=9, column=1)
            button_low3.grid(row=9, column=2)

        if 30 < itm < 35:
            itm_info4 = Label(top, text="Індекс тіла вище норми, вам рекомендован курс схуднення")
            button_low1 = Button(top, text="Програма набору ваги",
                                 command=lambda: bmrcalculation1())
            button_low2 = Button(top, text="Програма утримання ваги",
                                 command=lambda: bmrcalculation2())
            button_low3 = Button(top, text="Прогама схуднення(рекомендовано)",
                                 command=lambda: bmrcalculation3())
            itm_info4.grid(row=8, column=1)
            button_low1.grid(row=9, column=0)
            button_low2.grid(row=9, column=1)
            button_low3.grid(row=9, column=2)

        if 35 < itm < 40:
            itm_info5 = Label(top, text="Індекс тіла занадто вище норми, вам рекомендован курс схуднення")
            button_low1 = Button(top, text="Програма набору ваги",
                                 command=lambda: bmrcalculation1())
            button_low2 = Button(top, text="Програма утримання ваги",
                                 command=lambda: bmrcalculation2())
            button_low3 = Button(top, text="Прогама схуднення(дуже рекомендовано)",
                                 command=lambda: bmrcalculation3())
            itm_info5.grid(row=8, column=1)
            button_low1.grid(row=9, column=0)
            button_low2.grid(row=9, column=1)
            button_low3.grid(row=9, column=2)

        if itm > 40:
            itm_info6 = Label(top,
                              text="Індекс тіла дуже сильно вище норми, вам рекомендован курс схуднення")
            button_low1 = Button(top, text="Програма набору ваги",
                                 command=lambda: bmrcalculation1())
            button_low2 = Button(top, text="Програма утримання ваги",
                                 command=lambda: bmrcalculation2())
            button_low3 = Button(top, text="Прогама схуднення(дуже рекомендовано)",
                                 command=lambda: bmrcalculation3())
            itm_info6.grid(row=8, column=1)
            button_low1.grid(row=9, column=0)
            button_low2.grid(row=9, column=1)
            button_low3.grid(row=9, column=2)

        def bmrcalculation1():
            if gender.get() == "Чоловіча":
                if activity.get() == "1)Низька активність":
                    bmr = 1.2 * (88.362 + 13.397 * w + 4.799 * h + 5.677 * a)
                    bmr1 = round(bmr)
                    true_bmr = round(1.2 * bmr1)
                    proteins = round(0.15 * true_bmr)
                    carbohydrates = round(0.60 * true_bmr)
                    fats = round(0.25 * true_bmr)
                    bmr_info1 = Label(top, text="Показник БМР: " + str(true_bmr))
                    bmr_info2 = Label(top, text="Рекомендована кількіть білків: " + str(proteins))
                    bmr_info3 = Label(top, text="Рекомендована кількіть жирів: " + str(fats))
                    bmr_info4 = Label(top, text="Рекомендована кількіть вуглеводів: " + str(carbohydrates))
                    button_list1 = Button(top, text="Перейти до листу продуктів",
                                          command=lambda: listproducty())
                    with open('data.txt', 'a') as data:
                        data.write(
                            str(true_bmr) + '|' + str(proteins) + '|' + str(fats) + '|' + str(carbohydrates) + '\n')
                    bmr_info1.grid(row=10, column=0)
                    bmr_info2.grid(row=11, column=0)
                    bmr_info3.grid(row=12, column=0)
                    bmr_info4.grid(row=13, column=0)
                    button_list1.grid(row=14, column=0)

                elif activity.get() == "2)Помірна активність":
                    bmr = 1.375 * (88.362 + 13.397 * w + 4.799 * h + 5.677 * a)
                    bmr1 = round(bmr)
                    true_bmr = round(1.2 * bmr1)
                    proteins = round(0.15 * true_bmr)
                    carbohydrates = round(0.60 * true_bmr)
                    fats = round(0.25 * true_bmr)
                    bmr_info1 = Label(top, text="Показник БМР: " + str(true_bmr))
                    bmr_info2 = Label(top, text="Рекомендована кількіть білків : " + str(proteins))
                    bmr_info3 = Label(top, text="Рекомендована кількіть жирів : " + str(fats))
                    bmr_info4 = Label(top, text="Рекомендована кількіть вуглеводів : " + str(carbohydrates)).pack()
                    button_list1 = Button(top, text="Перейдемо до листу продуктів",
                                          command=lambda: listproducty())
                    with open('data.txt', 'a') as data:
                        data.write(
                            str(true_bmr) + '|' + str(proteins) + '|' + str(fats) + '|' + str(carbohydrates) + '\n')
                    bmr_info1.grid(row=10, column=0)
                    bmr_info2.grid(row=11, column=0)
                    bmr_info3.grid(row=12, column=0)
                    bmr_info4.grid(row=13, column=0)
                    button_list1.grid(row=14, column=0)

                elif activity.get() == "3)Середня активність":
                    bmr = 1.55 * (88.362 + 13.397 * w + 4.799 * h + 5.677 * a)
                    bmr1 = round(bmr)
                    true_bmr = round(1.2 * bmr1)
                    proteins = round(0.15 * true_bmr)
                    carbohydrates = round(0.60 * true_bmr)
                    fats = round(0.25 * true_bmr)
                    bmr_info1 = Label(top, text="Показник БМР: " + str(true_bmr))
                    bmr_info2 = Label(top, text="Рекомендована кількіть білків : " + str(proteins))
                    bmr_info3 = Label(top, text="Рекомендована кількіть жирів : " + str(fats))
                    bmr_info4 = Label(top, text="Рекомендована кількіть вуглеводів : " + str(carbohydrates))
                    button_list1 = Button(top, text="Перейдемо до листу продуктів",
                                          command=lambda: listproducty())
                    with open('data.txt', 'a') as data:
                        data.write(
                            str(true_bmr) + '|' + str(proteins) + '|' + str(fats) + '|' + str(carbohydrates) + '\n')
                    bmr_info1.grid(row=10, column=0)
                    bmr_info2.grid(row=11, column=0)
                    bmr_info3.grid(row=12, column=0)
                    bmr_info4.grid(row=13, column=0)
                    button_list1.grid(row=14, column=0)

                elif activity.get() == "4)Висока активність":
                    bmr = 1.725 * (88.362 + 13.397 * w + 4.799 * h + 5.677 * a)
                    bmr1 = round(bmr)
                    true_bmr = round(1.2 * bmr1)
                    proteins = round(0.15 * true_bmr)
                    carbohydrates = round(0.60 * true_bmr)
                    fats = round(0.25 * true_bmr)
                    bmr_info1 = Label(top, text="Показник БМР: " + str(true_bmr))
                    bmr_info2 = Label(top, text="Рекомендована кількіть білків : " + str(proteins))
                    bmr_info3 = Label(top, text="Рекомендована кількіть жирів : " + str(fats))
                    bmr_info4 = Label(top, text="Рекомендована кількіть вуглеводів : " + str(carbohydrates))
                    button_list1 = Button(top, text="Перейдемо до листу продуктів",
                                          command=lambda: listproducty())
                    with open('data.txt', 'a') as data:
                        data.write(
                            str(true_bmr) + '|' + str(proteins) + '|' + str(fats) + '|' + str(carbohydrates) + '\n')
                    bmr_info1.grid(row=10, column=0)
                    bmr_info2.grid(row=11, column=0)
                    bmr_info3.grid(row=12, column=0)
                    bmr_info4.grid(row=13, column=0)
                    button_list1.grid(row=14, column=0)

                elif activity.get() == "5)Дуже висока активність":
                    bmr = 1.9 * (88.362 + 13.397 * w + 4.799 * h + 5.677 * a)
                    bmr1 = round(bmr)
                    true_bmr = round(1.2 * bmr1)
                    proteins = round(0.15 * true_bmr)
                    carbohydrates = round(0.60 * true_bmr)
                    fats = round(0.25 * true_bmr)
                    bmr_info1 = Label(top, text="Показник БМР: " + str(true_bmr))
                    bmr_info2 = Label(top, text="Рекомендована кількіть білків : " + str(proteins))
                    bmr_info3 = Label(top, text="Рекомендована кількіть жирів : " + str(fats))
                    bmr_info4 = Label(top, text="Рекомендована кількіть вуглеводів : " + str(carbohydrates))
                    button_list1 = Button(top, text="Перейдемо до листу продуктів",
                                          command=lambda: listproducty())

                    with open('data.txt', 'a') as data:
                        data.write(
                            str(true_bmr) + '|' + str(proteins) + '|' + str(fats) + '|' + str(carbohydrates) + '\n')
                    bmr_info1.grid(row=10, column=0)
                    bmr_info2.grid(row=11, column=0)
                    bmr_info3.grid(row=12, column=0)
                    bmr_info4.grid(row=13, column=0)
                    button_list1.grid(row=14, column=0)

            if gender.get() == "Жіноча":
                if activity.get() == "1)Низька активність":
                    bmr = 1.2 * (447.593 + 9.247 * w + 3.097 * h + 4.33 * a)
                    bmr1 = round(bmr)
                    true_bmr = round(1.2 * bmr1)
                    proteins = round(0.15 * true_bmr)
                    carbohydrates = round(0.60 * true_bmr)
                    fats = round(0.25 * true_bmr)
                    bmr_info1 = Label(top, text="Показник БМР: " + str(true_bmr))
                    bmr_info2 = Label(top, text="Рекомендована кількіть білків : " + str(proteins))
                    bmr_info3 = Label(top, text="Рекомендована кількіть жирів : " + str(fats))
                    bmr_info4 = Label(top, text="Рекомендована кількіть вуглеводів : " + str(carbohydrates))
                    button_list1 = Button(top, text="Перейдемо до листу продуктів",
                                          command=lambda: listproducty())
                    with open('data.txt', 'a') as data:
                        data.write(
                            str(true_bmr) + '|' + str(proteins) + '|' + str(fats) + '|' + str(carbohydrates) + '\n')
                    bmr_info1.grid(row=10, column=0)
                    bmr_info2.grid(row=11, column=0)
                    bmr_info3.grid(row=12, column=0)
                    bmr_info4.grid(row=13, column=0)
                    button_list1.grid(row=14, column=0)

                elif activity.get() == "2)Помірна активність":
                    bmr = 1.375 * (447.593 + 9.247 * w + 3.097 * h + 4.33 * a)
                    bmr1 = round(bmr)
                    true_bmr = round(1.2 * bmr1)
                    proteins = round(0.15 * true_bmr)
                    carbohydrates = round(0.60 * true_bmr)
                    fats = round(0.25 * true_bmr)
                    bmr_info1 = Label(top, text="Показник БМР: " + str(true_bmr))
                    bmr_info2 = Label(top, text="Рекомендована кількіть білків : " + str(proteins))
                    bmr_info3 = Label(top, text="Рекомендована кількіть жирів : " + str(fats))
                    bmr_info4 = Label(top, text="Рекомендована кількіть вуглеводів : " + str(carbohydrates))
                    button_list1 = Button(top, text="Перейдемо до листу продуктів",
                                          command=lambda: listproducty())
                    with open('data.txt', 'a') as data:
                        data.write(
                            str(true_bmr) + '|' + str(proteins) + '|' + str(fats) + '|' + str(carbohydrates) + '\n')
                    bmr_info1.grid(row=10, column=0)
                    bmr_info2.grid(row=11, column=0)
                    bmr_info3.grid(row=12, column=0)
                    bmr_info4.grid(row=13, column=0)
                    button_list1.grid(row=14, column=0)

                elif activity.get() == "3)Середня активність":
                    bmr = 1.55 * (447.593 + 9.247 * w + 3.097 * h + 4.33 * a)
                    bmr1 = round(bmr)
                    true_bmr = round(1.2 * bmr1)
                    proteins = round(0.15 * true_bmr)
                    carbohydrates = round(0.60 * true_bmr)
                    fats = round(0.25 * true_bmr)
                    bmr_info1 = Label(top, text="Показник БМР: " + str(true_bmr))
                    bmr_info2 = Label(top, text="Рекомендована кількіть білків : " + str(proteins))
                    bmr_info3 = Label(top, text="Рекомендована кількіть жирів : " + str(fats))
                    bmr_info4 = Label(top, text="Рекомендована кількіть вуглеводів : " + str(carbohydrates))
                    button_list1 = Button(top, text="Перейдемо до листу продуктів",
                                          command=lambda: listproducty())
                    with open('data.txt', 'a') as data:
                        data.write(
                            str(true_bmr) + '|' + str(proteins) + '|' + str(fats) + '|' + str(carbohydrates) + '\n')
                    bmr_info1.grid(row=10, column=0)
                    bmr_info2.grid(row=11, column=0)
                    bmr_info3.grid(row=12, column=0)
                    bmr_info4.grid(row=13, column=0)
                    button_list1.grid(row=14, column=0)

                elif activity.get() == "4)Висока активність":
                    bmr = 1.725 * (447.593 + 9.247 * w + 3.097 * h + 4.33 * a)
                    bmr1 = round(bmr)
                    true_bmr = round(1.2 * bmr1)
                    proteins = round(0.15 * true_bmr)
                    carbohydrates = round(0.60 * true_bmr)
                    fats = round(0.25 * true_bmr)
                    bmr_info1 = Label(top, text="Показник БМР: " + str(true_bmr))
                    bmr_info2 = Label(top, text="Рекомендована кількіть білків : " + str(proteins))
                    bmr_info3 = Label(top, text="Рекомендована кількіть жирів : " + str(fats))
                    bmr_info4 = Label(top, text="Рекомендована кількіть вуглеводів : " + str(carbohydrates))
                    button_list1 = Button(top, text="Перейдемо до листу продуктів",
                                          command=lambda: listproducty())
                    with open('data.txt', 'a') as data:
                        data.write(
                            str(true_bmr) + '|' + str(proteins) + '|' + str(fats) + '|' + str(carbohydrates) + '\n')
                    bmr_info1.grid(row=10, column=0)
                    bmr_info2.grid(row=11, column=0)
                    bmr_info3.grid(row=12, column=0)
                    bmr_info4.grid(row=13, column=0)
                    button_list1.grid(row=14, column=0)

                elif activity.get() == "5)Дуже висока активність":
                    bmr = 1.9 * (447.593 + 9.247 * w + 3.097 * h + 4.33 * a)
                    bmr1 = round(bmr)
                    true_bmr = round(1.2 * bmr1)
                    proteins = round(0.15 * true_bmr)
                    carbohydrates = round(0.60 * true_bmr)
                    fats = round(0.25 * true_bmr)
                    bmr_info1 = Label(top, text="Показник БМР: " + str(true_bmr))
                    bmr_info2 = Label(top, text="Рекомендована кількіть білків : " + str(proteins))
                    bmr_info3 = Label(top, text="Рекомендована кількіть жирів : " + str(fats))
                    bmr_info4 = Label(top, text="Рекомендована кількіть вуглеводів : " + str(carbohydrates))
                    button_list1 = Button(top, text="Перейдемо до листу продуктів",
                                          command=lambda: listproducty())
                    with open('data.txt', 'a') as data:
                        data.write(
                            str(true_bmr) + '|' + str(proteins) + '|' + str(fats) + '|' + str(carbohydrates) + '\n')
                    bmr_info1.grid(row=10, column=0)
                    bmr_info2.grid(row=11, column=0)
                    bmr_info3.grid(row=12, column=0)
                    bmr_info4.grid(row=13, column=0)
                    button_list1.grid(row=14, column=0)

        def bmrcalculation2():
            if gender.get() == "Чоловіча":
                if activity.get() == "1)Низька активність":
                    bmr = 1.2 * (88.362 + 13.397 * w + 4.799 * h + 5.677 * a)
                    bmr1 = round(bmr)
                    true_bmr = bmr1
                    proteins = round(0.15 * true_bmr)
                    carbohydrates = round(0.60 * true_bmr)
                    fats = round(0.25 * true_bmr)
                    bmr_info1 = Label(top, text="Показник БМР: " + str(true_bmr))
                    bmr_info2 = Label(top, text="Рекомендована кількіть білків : " + str(proteins))
                    bmr_info3 = Label(top, text="Рекомендована кількіть жирів : " + str(fats))
                    bmr_info4 = Label(top, text="Рекомендована кількіть вуглеводів : " + str(carbohydrates))
                    button_list1 = Button(top, text="Перейдемо до листу продуктів",
                                          command=lambda: listproducty())
                    with open('data.txt', 'a') as data:
                        data.write(
                            str(true_bmr) + '|' + str(proteins) + '|' + str(fats) + '|' + str(carbohydrates) + '\n')
                    bmr_info1.grid(row=10, column=1)
                    bmr_info2.grid(row=11, column=1)
                    bmr_info3.grid(row=12, column=1)
                    bmr_info4.grid(row=13, column=1)
                    button_list1.grid(row=14, column=1)

                elif activity.get() == "2)Помірна активність":
                    bmr = 1.375 * (88.362 + 13.397 * w + 4.799 * h + 5.677 * a)
                    bmr1 = round(bmr)
                    true_bmr = bmr1
                    proteins = round(0.15 * true_bmr)
                    carbohydrates = round(0.60 * true_bmr)
                    fats = round(0.25 * true_bmr)
                    bmr_info1 = Label(top, text="Показник БМР: " + str(true_bmr))
                    bmr_info2 = Label(top, text="Рекомендована кількіть білків : " + str(proteins))
                    bmr_info3 = Label(top, text="Рекомендована кількіть жирів : " + str(fats))
                    bmr_info4 = Label(top, text="Рекомендована кількіть вуглеводів : " + str(carbohydrates))
                    button_list1 = Button(top, text="Перейдемо до листу продуктів",
                                          command=lambda: listproducty())
                    with open('data.txt', 'a') as data:
                        data.write(
                            str(true_bmr) + '|' + str(proteins) + '|' + str(fats) + '|' + str(carbohydrates) + '\n')
                    bmr_info1.grid(row=10, column=1)
                    bmr_info2.grid(row=11, column=1)
                    bmr_info3.grid(row=12, column=1)
                    bmr_info4.grid(row=13, column=1)
                    button_list1.grid(row=14, column=1)

                elif activity.get() == "3)Середня активність":
                    bmr = 1.55 * (88.362 + 13.397 * w + 4.799 * h + 5.677 * a)
                    bmr1 = round(bmr)
                    true_bmr = bmr1
                    proteins = round(0.15 * true_bmr)
                    carbohydrates = round(0.60 * true_bmr)
                    fats = round(0.25 * true_bmr)
                    bmr_info1 = Label(top, text="Показник БМР: " + str(true_bmr))
                    bmr_info2 = Label(top, text="Рекомендована кількіть білків : " + str(proteins))
                    bmr_info3 = Label(top, text="Рекомендована кількіть жирів : " + str(fats))
                    bmr_info4 = Label(top, text="Рекомендована кількіть вуглеводів : " + str(carbohydrates))
                    button_list1 = Button(top, text="Перейдемо до листу продуктів",
                                          command=lambda: listproducty())
                    with open('data.txt', 'a') as data:
                        data.write(
                            str(true_bmr) + '|' + str(proteins) + '|' + str(fats) + '|' + str(carbohydrates) + '\n')
                    bmr_info1.grid(row=10, column=1)
                    bmr_info2.grid(row=11, column=1)
                    bmr_info3.grid(row=12, column=1)
                    bmr_info4.grid(row=13, column=1)
                    button_list1.grid(row=14, column=1)

                elif activity.get() == "4)Висока активність":
                    bmr = 1.725 * (88.362 + 13.397 * w + 4.799 * h + 5.677 * a)
                    bmr1 = round(bmr)
                    true_bmr = bmr1
                    proteins = round(0.15 * true_bmr)
                    carbohydrates = round(0.60 * true_bmr)
                    fats = round(0.25 * true_bmr)
                    bmr_info1 = Label(top, text="Показник БМР: " + str(true_bmr))
                    bmr_info2 = Label(top, text="Рекомендована кількіть білків : " + str(proteins))
                    bmr_info3 = Label(top, text="Рекомендована кількіть жирів : " + str(fats))
                    bmr_info4 = Label(top, text="Рекомендована кількіть вуглеводів : " + str(carbohydrates))
                    button_list1 = Button(top, text="Перейдемо до листу продуктів",
                                          command=lambda: listproducty())
                    with open('data.txt', 'a') as data:
                        data.write(
                            str(true_bmr) + '|' + str(proteins) + '|' + str(fats) + '|' + str(carbohydrates) + '\n')
                    bmr_info1.grid(row=10, column=1)
                    bmr_info2.grid(row=11, column=1)
                    bmr_info3.grid(row=12, column=1)
                    bmr_info4.grid(row=13, column=1)
                    button_list1.grid(row=14, column=1)

                elif activity.get() == "5)Дуже висока активність":
                    bmr = 1.9 * (88.362 + 13.397 * w + 4.799 * h + 5.677 * a)
                    bmr1 = round(bmr)
                    true_bmr = bmr1
                    proteins = round(0.15 * true_bmr)
                    carbohydrates = round(0.60 * true_bmr)
                    fats = round(0.25 * true_bmr)
                    bmr_info1 = Label(top, text="Показник БМР: " + str(true_bmr))
                    bmr_info2 = Label(top, text="Рекомендована кількіть білків : " + str(proteins))
                    bmr_info3 = Label(top, text="Рекомендована кількіть жирів : " + str(fats))
                    bmr_info4 = Label(top, text="Рекомендована кількіть вуглеводів : " + str(carbohydrates))
                    button_list1 = Button(top, text="Перейдемо до листу продуктів",
                                          command=lambda: listproducty())
                    with open('data.txt', 'a') as data:
                        data.write(
                            str(true_bmr) + '|' + str(proteins) + '|' + str(fats) + '|' + str(carbohydrates) + '\n')
                    bmr_info1.grid(row=10, column=1)
                    bmr_info2.grid(row=11, column=1)
                    bmr_info3.grid(row=12, column=1)
                    bmr_info4.grid(row=13, column=1)
                    button_list1.grid(row=14, column=1)

            if gender.get() == "Жіноча":
                if activity.get() == "1)Низька активність":
                    bmr = 1.2 * (447.593 + 9.247 * w + 3.097 * h + 4.33 * a)
                    bmr1 = round(bmr)
                    true_bmr = bmr1
                    proteins = round(0.15 * true_bmr)
                    carbohydrates = round(0.60 * true_bmr)
                    fats = round(0.25 * true_bmr)
                    bmr_info1 = Label(top, text="Показник БМР: " + str(true_bmr))
                    bmr_info2 = Label(top, text="Рекомендована кількіть білків : " + str(proteins))
                    bmr_info3 = Label(top, text="Рекомендована кількіть жирів : " + str(fats))
                    bmr_info4 = Label(top, text="Рекомендована кількіть вуглеводів : " + str(carbohydrates))
                    button_list1 = Button(top, text="Перейдемо до листу продуктів",
                                          command=lambda: listproducty())
                    with open('data.txt', 'a') as data:
                        data.write(
                            str(true_bmr) + '|' + str(proteins) + '|' + str(fats) + '|' + str(carbohydrates) + '\n')
                    bmr_info1.grid(row=10, column=1)
                    bmr_info2.grid(row=11, column=1)
                    bmr_info3.grid(row=12, column=1)
                    bmr_info4.grid(row=13, column=1)
                    button_list1.grid(row=14, column=1)

                elif activity.get() == "2)Помірна активність":
                    bmr = 1.375 * (447.593 + 9.247 * w + 3.097 * h + 4.33 * a)
                    bmr1 = round(bmr)
                    true_bmr = bmr1
                    proteins = round(0.15 * true_bmr)
                    carbohydrates = round(0.60 * true_bmr)
                    fats = round(0.25 * true_bmr)
                    bmr_info1 = Label(top, text="Показник БМР: " + str(true_bmr))
                    bmr_info2 = Label(top, text="Рекомендована кількіть білків : " + str(proteins))
                    bmr_info3 = Label(top, text="Рекомендована кількіть жирів : " + str(fats))
                    bmr_info4 = Label(top, text="Рекомендована кількіть вуглеводів : " + str(carbohydrates))
                    button_list1 = Button(top, text="Перейдемо до листу продуктів",
                                          command=lambda: listproducty())
                    with open('data.txt', 'a') as data:
                        data.write(
                            str(true_bmr) + '|' + str(proteins) + '|' + str(fats) + '|' + str(carbohydrates) + '\n')
                    bmr_info1.grid(row=10, column=1)
                    bmr_info2.grid(row=11, column=1)
                    bmr_info3.grid(row=12, column=1)
                    bmr_info4.grid(row=13, column=1)
                    button_list1.grid(row=14, column=1)

                elif activity.get() == "3)Середня активність":
                    bmr = 1.55 * (447.593 + 9.247 * w + 3.097 * h + 4.33 * a)
                    bmr1 = round(bmr)
                    true_bmr = bmr1
                    proteins = round(0.15 * true_bmr)
                    carbohydrates = round(0.60 * true_bmr)
                    fats = round(0.25 * true_bmr)
                    bmr_info1 = Label(top, text="Показник БМР: " + str(true_bmr))
                    bmr_info2 = Label(top, text="Рекомендована кількіть білків : " + str(proteins))
                    bmr_info3 = Label(top, text="Рекомендована кількіть жирів : " + str(fats))
                    bmr_info4 = Label(top, text="Рекомендована кількіть вуглеводів : " + str(carbohydrates))
                    button_list1 = Button(top, text="Перейдемо до листу продуктів",
                                          command=lambda: listproducty())
                    with open('data.txt', 'a') as data:
                        data.write(
                            str(true_bmr) + '|' + str(proteins) + '|' + str(fats) + '|' + str(carbohydrates) + '\n')
                    bmr_info1.grid(row=10, column=1)
                    bmr_info2.grid(row=11, column=1)
                    bmr_info3.grid(row=12, column=1)
                    bmr_info4.grid(row=13, column=1)
                    button_list1.grid(row=14, column=1)

                elif activity.get() == "4)Висока активність":
                    bmr = 1.725 * (447.593 + 9.247 * w + 3.097 * h + 4.33 * a)
                    bmr1 = round(bmr)
                    true_bmr = bmr1
                    proteins = 0.15 * true_bmr
                    carbohydrates = 0.60 * true_bmr
                    fats = 0.25 * true_bmr
                    bmr_info1 = Label(top, text="Показник БМР: " + str(true_bmr))
                    bmr_info2 = Label(top, text="Рекомендована кількіть білків : " + str(proteins))
                    bmr_info3 = Label(top, text="Рекомендована кількіть жирів : " + str(fats))
                    bmr_info4 = Label(top, text="Рекомендована кількіть вуглеводів : " + str(carbohydrates))
                    button_list1 = Button(top, text="Перейдемо до листу продуктів",
                                          command=lambda: listproducty())
                    with open('data.txt', 'a') as data:
                        data.write(
                            str(true_bmr) + '|' + str(proteins) + '|' + str(fats) + '|' + str(carbohydrates) + '\n')
                    bmr_info1.grid(row=10, column=1)
                    bmr_info2.grid(row=11, column=1)
                    bmr_info3.grid(row=12, column=1)
                    bmr_info4.grid(row=13, column=1)
                    button_list1.grid(row=14, column=1)

                elif activity.get() == "5)Дуже висока активність":
                    bmr = 1.9 * (447.593 + 9.247 * w + 3.097 * h + 4.33 * a)
                    bmr1 = round(bmr)
                    true_bmr = bmr1
                    proteins = round(0.15 * true_bmr)
                    carbohydrates = round(0.60 * true_bmr)
                    fats = round(0.25 * true_bmr)
                    bmr_info1 = Label(top, text="Показник БМР: " + str(true_bmr))
                    bmr_info2 = Label(top, text="Рекомендована кількіть білків : " + str(proteins))
                    bmr_info3 = Label(top, text="Рекомендована кількіть жирів : " + str(fats))
                    bmr_info4 = Label(top, text="Рекомендована кількіть вуглеводів : " + str(carbohydrates))
                    button_list1 = Button(top, text="Перейдемо до листу продуктів",
                                          command=lambda: listproducty())
                    with open('data.txt', 'a') as data:
                        data.write(
                            str(true_bmr) + '|' + str(proteins) + '|' + str(fats) + '|' + str(carbohydrates) + '\n')
                    bmr_info1.grid(row=10, column=1)
                    bmr_info2.grid(row=11, column=1)
                    bmr_info3.grid(row=12, column=1)
                    bmr_info4.grid(row=13, column=1)
                    button_list1.grid(row=14, column=1)

        def bmrcalculation3():
            if gender.get() == "Чоловіча":
                if activity.get() == "1)Низька активність":
                    bmr = 1.2 * (88.362 + 13.397 * w + 4.799 * h + 5.677 * a)
                    bmr1 = round(bmr)
                    true_bmr = round(0.87 * bmr1)
                    proteins = round(0.15 * true_bmr)
                    carbohydrates = round(0.60 * true_bmr)
                    fats = round(0.25 * true_bmr)
                    bmr_info1 = Label(top, text="Показник БМР: " + str(true_bmr))
                    bmr_info2 = Label(top, text="Рекомендована кількіть білків : " + str(proteins))
                    bmr_info3 = Label(top, text="Рекомендована кількіть жирів : " + str(fats))
                    bmr_info4 = Label(top, text="Рекомендована кількіть вуглеводів : " + str(carbohydrates))
                    button_list1 = Button(top, text="Перейдемо до листу продуктів",
                                          command=lambda: listproducty())
                    with open('data.txt', 'a') as data:
                        data.write(str(true_bmr) + '|' + str(proteins) + '|'
                                   + str(fats) + '|' + str(carbohydrates) + '\n')
                    bmr_info1.grid(row=10, column=2)
                    bmr_info2.grid(row=11, column=2)
                    bmr_info3.grid(row=12, column=2)
                    bmr_info4.grid(row=13, column=2)
                    button_list1.grid(row=14, column=2)

                elif activity.get() == "2)Помірна активність":
                    bmr = 1.375 * (88.362 + 13.397 * w + 4.799 * h + 5.677 * a)
                    bmr1 = round(bmr)
                    true_bmr = round(0.87 * bmr1)
                    proteins = round(0.15 * true_bmr)
                    carbohydrates = round(0.60 * true_bmr)
                    fats = round(0.25 * true_bmr)
                    bmr_info1 = Label(top, text="Показник БМР: " + str(true_bmr))
                    bmr_info2 = Label(top, text="Рекомендована кількіть білків : " + str(proteins))
                    bmr_info3 = Label(top, text="Рекомендована кількіть жирів : " + str(fats))
                    bmr_info4 = Label(top, text="Рекомендована кількіть вуглеводів : " + str(carbohydrates))
                    button_list1 = Button(top, text="Перейдемо до листу продуктів",
                                          command=lambda: listproducty())
                    with open('data.txt', 'a') as data:
                        data.write(
                            str(true_bmr) + '|' + str(proteins) + '|' + str(fats) + '|' + str(carbohydrates) + '\n')
                    bmr_info1.grid(row=10, column=2)
                    bmr_info2.grid(row=11, column=2)
                    bmr_info3.grid(row=12, column=2)
                    bmr_info4.grid(row=13, column=2)
                    button_list1.grid(row=14, column=2)

                elif activity.get() == "3)Середня активність":
                    bmr = 1.55 * (88.362 + 13.397 * w + 4.799 * h + 5.677 * a)
                    bmr1 = round(bmr)
                    true_bmr = round(0.87 * bmr1)
                    proteins = round(0.15 * true_bmr)
                    carbohydrates = round(0.60 * true_bmr)
                    fats = round(0.25 * true_bmr)
                    bmr_info1 = Label(top, text="Показник БМР: " + str(true_bmr))
                    bmr_info2 = Label(top, text="Рекомендована кількіть білків : " + str(proteins))
                    bmr_info3 = Label(top, text="Рекомендована кількіть жирів : " + str(fats))
                    bmr_info4 = Label(top, text="Рекомендована кількіть вуглеводів : " + str(carbohydrates))
                    button_list1 = Button(top, text="Перейдемо до листу продуктів",
                                          command=lambda: listproducty())
                    with open('data.txt', 'a') as data:
                        data.write(
                            str(true_bmr) + '|' + str(proteins) + '|' + str(fats) + '|' + str(carbohydrates) + '\n')
                    bmr_info1.grid(row=10, column=2)
                    bmr_info2.grid(row=11, column=2)
                    bmr_info3.grid(row=12, column=2)
                    bmr_info4.grid(row=13, column=2)
                    button_list1.grid(row=14, column=2)

                elif activity.get() == "4)Висока активність":
                    bmr = 1.725 * (88.362 + 13.397 * w + 4.799 * h + 5.677 * a)
                    bmr1 = round(bmr)
                    true_bmr = round(0.87 * bmr1)
                    proteins = round(0.15 * true_bmr)
                    carbohydrates = round(0.60 * true_bmr)
                    fats = round(0.25 * true_bmr)
                    bmr_info1 = Label(top, text="Показник БМР: " + str(true_bmr))
                    bmr_info2 = Label(top, text="Рекомендована кількіть білків : " + str(proteins))
                    bmr_info3 = Label(top, text="Рекомендована кількіть жирів : " + str(fats))
                    bmr_info4 = Label(top, text="Рекомендована кількіть вуглеводів : " + str(carbohydrates))
                    button_list1 = Button(top, text="Перейдемо до листу продуктів",
                                          command=lambda: listproducty())
                    with open('data.txt', 'a') as data:
                        data.write(
                            str(true_bmr) + '|' + str(proteins) + '|' + str(fats) + '|' + str(carbohydrates) + '\n')
                    bmr_info1.grid(row=10, column=2)
                    bmr_info2.grid(row=11, column=2)
                    bmr_info3.grid(row=12, column=2)
                    bmr_info4.grid(row=13, column=2)
                    button_list1.grid(row=14, column=2)

                elif activity.get() == "5)Дуже висока активність":
                    bmr = 1.9 * (88.362 + 13.397 * w + 4.799 * h + 5.677 * a)
                    bmr1 = round(bmr)
                    true_bmr = round(0.87 * bmr1)
                    proteins = round(0.15 * true_bmr)
                    carbohydrates = round(0.60 * true_bmr)
                    fats = round(0.25 * true_bmr)
                    bmr_info1 = Label(top, text="Показник БМР: " + str(true_bmr))
                    bmr_info2 = Label(top, text="Рекомендована кількіть білків : " + str(proteins))
                    bmr_info3 = Label(top, text="Рекомендована кількіть жирів : " + str(fats))
                    bmr_info4 = Label(top, text="Рекомендована кількіть вуглеводів : " + str(carbohydrates))
                    button_list1 = Button(top, text="Перейдемо до листу продуктів",
                                          command=lambda: listproducty())
                    with open('data.txt', 'a') as data:
                        data.write(
                            str(true_bmr) + '|' + str(proteins) + '|' + str(fats) + '|' + str(carbohydrates) + '\n')
                    bmr_info1.grid(row=10, column=2)
                    bmr_info2.grid(row=11, column=2)
                    bmr_info3.grid(row=12, column=2)
                    bmr_info4.grid(row=13, column=2)
                    button_list1.grid(row=14, column=2)

            if gender.get() == "Жіноча":
                if activity.get() == "1)Низька активність":
                    bmr = 1.2 * (447.593 + 9.247 * w + 3.097 * h + 4.33 * a)
                    bmr1 = round(bmr)
                    true_bmr = round(0.87 * bmr1)
                    proteins = round(0.15 * true_bmr)
                    carbohydrates = round(0.60 * true_bmr)
                    fats = round(0.25 * true_bmr)
                    bmr_info1 = Label(top, text="Показник БМР: " + str(true_bmr))
                    bmr_info2 = Label(top, text="Рекомендована кількіть білків : " + str(proteins))
                    bmr_info3 = Label(top, text="Рекомендована кількіть жирів : " + str(fats))
                    bmr_info4 = Label(top, text="Рекомендована кількіть вуглеводів : " + str(carbohydrates))
                    button_list1 = Button(top, text="Перейдемо до листу продуктів",
                                          command=lambda: listproducty()).pack()
                    with open('data.txt', 'a') as data:
                        data.write(
                            str(true_bmr) + '|' + str(proteins) + '|' + str(fats) + '|' + str(carbohydrates) + '\n')
                    bmr_info1.grid(row=10, column=2)
                    bmr_info2.grid(row=11, column=2)
                    bmr_info3.grid(row=12, column=2)
                    bmr_info4.grid(row=13, column=2)
                    button_list1.grid(row=14, column=2)

                elif activity.get() == "2)Помірна активність":
                    bmr = 1.375 * (447.593 + 9.247 * w + 3.097 * h + 4.33 * a)
                    bmr1 = round(bmr)
                    true_bmr = round(0.87 * bmr1)
                    proteins = round(0.15 * true_bmr)
                    carbohydrates = round(0.60 * true_bmr)
                    fats = round(0.25 * true_bmr)
                    bmr_info1 = Label(top, text="Показник БМР: " + str(true_bmr))
                    bmr_info2 = Label(top, text="Рекомендована кількіть білків : " + str(proteins))
                    bmr_info3 = Label(top, text="Рекомендована кількіть жирів : " + str(fats))
                    bmr_info4 = Label(top, text="Рекомендована кількіть вуглеводів : " + str(carbohydrates))
                    button_list1 = Button(top, text="Перейдемо до листу продуктів",
                                          command=lambda: listproducty())
                    with open('data.txt', 'a') as data:
                        data.write(
                            str(true_bmr) + '|' + str(proteins) + '|' + str(fats) + '|' + str(carbohydrates) + '\n')
                    bmr_info1.grid(row=10, column=2)
                    bmr_info2.grid(row=11, column=2)
                    bmr_info3.grid(row=12, column=2)
                    bmr_info4.grid(row=13, column=2)
                    button_list1.grid(row=14, column=2)

                elif activity.get() == "3)Середня активність":
                    bmr = 1.55 * (447.593 + 9.247 * w + 3.097 * h + 4.33 * a)
                    bmr1 = round(bmr)
                    true_bmr = round(0.87 * bmr1)
                    proteins = round(0.15 * true_bmr)
                    carbohydrates = round(0.60 * true_bmr)
                    fats = round(0.25 * true_bmr)
                    bmr_info1 = Label(top, text="Показник БМР: " + str(true_bmr))
                    bmr_info2 = Label(top, text="Рекомендована кількіть білків : " + str(proteins))
                    bmr_info3 = Label(top, text="Рекомендована кількіть жирів : " + str(fats))
                    bmr_info4 = Label(top, text="Рекомендована кількіть вуглеводів : " + str(carbohydrates))
                    button_list1 = Button(top, text="Перейдемо до листу продуктів",
                                          command=lambda: listproducty())
                    with open('data.txt', 'a') as data:
                        data.write(
                            str(true_bmr) + '|' + str(proteins) + '|' + str(fats) + '|' + str(carbohydrates) + '\n')
                    bmr_info1.grid(row=10, column=2)
                    bmr_info2.grid(row=11, column=2)
                    bmr_info3.grid(row=12, column=2)
                    bmr_info4.grid(row=13, column=2)
                    button_list1.grid(row=14, column=2)

                elif activity.get() == "4)Висока активність":
                    bmr = 1.725 * (447.593 + 9.247 * w + 3.097 * h + 4.33 * a)
                    bmr1 = round(bmr)
                    true_bmr = round(0.87 * bmr1)
                    proteins = round(0.15 * true_bmr)
                    carbohydrates = round(0.60 * true_bmr)
                    fats = round(0.25 * true_bmr)
                    bmr_info1 = Label(top, text="Показник БМР: " + str(true_bmr))
                    bmr_info2 = Label(top, text="Рекомендована кількіть білків : " + str(proteins))
                    bmr_info3 = Label(top, text="Рекомендована кількіть жирів : " + str(fats))
                    bmr_info4 = Label(top, text="Рекомендована кількіть вуглеводів : " + str(carbohydrates))
                    button_list1 = Button(top, text="Перейдемо до листу продуктів",
                                          command=lambda: listproducty())
                    with open('data.txt', 'a') as data:
                        data.write(
                            str(true_bmr) + '|' + str(proteins) + '|' + str(fats) + '|' + str(carbohydrates) + '\n')
                    bmr_info1.grid(row=10, column=2)
                    bmr_info2.grid(row=11, column=2)
                    bmr_info3.grid(row=12, column=2)
                    bmr_info4.grid(row=13, column=2)
                    button_list1.grid(row=14, column=2)

                elif activity.get() == "5)Дуже висока активність":
                    bmr = 1.9 * (447.593 + 9.247 * w + 3.097 * h + 4.33 * a)
                    bmr1 = round(bmr)
                    true_bmr = round(0.87 * bmr1)
                    proteins = round(0.15 * true_bmr)
                    carbohydrates = round(0.60 * true_bmr)
                    fats = round(0.25 * true_bmr)
                    bmr_info1 = Label(top, text="Показник БМР: " + str(true_bmr))
                    bmr_info2 = Label(top, text="Рекомендована кількіть білків : " + str(proteins))
                    bmr_info3 = Label(top, text="Рекомендована кількіть жирів : " + str(fats))
                    bmr_info4 = Label(top, text="Рекомендована кількіть вуглеводів : " + str(carbohydrates))
                    button_list1 = Button(top, text="Перейдемо до листу продуктів",
                                          command=lambda: listproducty())
                    with open('data.txt', 'a') as data:
                        data.write(
                            str(true_bmr) + '|' + str(proteins) + '|' + str(fats) + '|' + str(carbohydrates) + '\n')
                    bmr_info1.grid(row=10, column=2)
                    bmr_info2.grid(row=11, column=2)
                    bmr_info3.grid(row=12, column=2)
                    bmr_info4.grid(row=13, column=2)
                    button_list1.grid(row=14, column=2)

        but = Button(top, text="Завершити програму", command=lambda: top.destroy())
        but.grid(row=0, column=2)


def listproducty():
    low = Tk()
    low.geometry("1100x700")
    low.title("Меню продуктів")
    file_data = list()
    with open('data.txt', 'rt') as data:
        data_list = data.readlines()
        for i in range(len(data_list)):
            data_list[i] = data_list[i].strip('\n')
            tmp = data_list[i].split('|')
            file_data.append(tmp)
            bmr = float(file_data[i][0])
    bmr_info1 = Label(low, text="Показник необхідних калорій: " + str(bmr))
    button_list1 = Button(low, text="Додати продукт у список",
                          command=lambda: addnew())
    button_go1 = Button(low, text="Показати наявні продукти ", command=lambda: add2())
    button_go2 = Button(low, text="Підрахувати щоденну норму ", command=lambda: calculate())
    button_go3 = Button(low, text="Завершити програму", command=lambda: low.destroy())
    bmr_info1.grid(row=0, column=0)
    button_list1.grid(row=2, column=0)
    button_go1.grid(row=0, column=1)
    button_go2.grid(row=2, column=2)
    button_go3.grid(row=0, column=2)

    def addnew():
        product_text = Label(low, text='Характеристики продукту на 100 грамм')
        name_text = Label(low, text="Вкажіть назву продукту:")
        name = Entry(low)
        calories_text = Label(low, text="Вкажіть калорійність продукту:")
        calories1 = Entry(low)
        proteins_text = Label(low, text="Вкажіть кількість протеїну продукту:")
        proteins1 = Entry(low)
        fats_text = Label(low, text="Вкажіть жирність продукту:")
        fats1 = Entry(low)
        carbohydrates_text = Label(low, text="Вкажіть кількість вуглеводів продукту:")
        carbohydrates1 = Entry(low)
        button_go = Button(low, text="Додати до списку ", command=lambda: add1())
        product_text.grid(row=1, column=0)
        name_text.grid(row=2, column=0)
        name.grid(row=2, column=1)
        calories_text.grid(row=3, column=0)
        calories1.grid(row=3, column=1)
        proteins_text.grid(row=4, column=0)
        proteins1.grid(row=4, column=1)
        fats_text.grid(row=5, column=0)
        fats1.grid(row=5, column=1)
        carbohydrates_text.grid(row=6, column=0)
        carbohydrates1.grid(row=6, column=1)
        button_go.grid(row=7, column=0)

        def add1():
            na = name.get()
            ca = calories1.get()
            pr = proteins1.get()
            car = carbohydrates1.get()
            fa = fats1.get()
            with open('products.txt', 'a') as products:
                products.write(na + '|' + ca + '|' + pr + '|'
                               + fa + '|' + car + '\n')

    def calculate():
        file_data = list()
        with open('data.txt', 'rt') as data:
            data_list = data.readlines()
            for i in range(len(data_list)):
                data_list[i] = data_list[i].strip('\n')
                tmp = data_list[i].split('|')
                file_data.append(tmp)
                true_bmr = float(file_data[i][0])

        product_name_text = Label(low, text="Введіть назву продукту:")
        product_name = Entry(low)
        product_portion_text = Label(low, text='Введіть кількість порцій:')
        product_portion = Entry(low)
        but = Button(low, text="Порахувати", command=lambda: count())

        product_name_text.grid(row=3, column=2)
        product_name.grid(row=3, column=3)
        product_portion_text.grid(row=4, column=2)
        product_portion.grid(row=4, column=3)
        but.grid(row=5, column=2)

        def count():
            file_data = list()
            with open('data.txt', 'rt') as data:
                data_list = data.readlines()
                for i in range(len(data_list)):
                    data_list[i] = data_list[i].strip('\n')
                    tmp = data_list[i].split('|')
                    file_data.append(tmp)
                    true_bmr = float(file_data[i][0])
            nam = product_name.get()
            product_lst = get_products()
            brm1 = 0

            pp = product_portion.get()
            for i in range(len(product_lst)):
                if nam == product_lst[i][0]:
                    brm1 += int(pp) * int(product_lst[i][1])
                    bmr_info = str(brm1)
                    with open('calc.txt', 'a') as calc:
                        calc.write("|" + str(brm1))

            with open('calc.txt', 'rt') as calc1:
                calc1_list = calc1.readlines()
                for i in range(len(calc1_list)):
                    data_list[i] = data_list[i].strip('\n')
                    a = calc1_list[i].split('|')
                my_int_list = [float(i) for i in a]
                summa = sum(my_int_list)
            info1 = Label(low, text='В вашому раціоні ' + str(summa) + ' калорій,')
            if summa > true_bmr:
                messagebox.showinfo("Попередження", "Норма калорій була перевищенна!")

            info1.grid(row=9, column=0)


def add2():
    mid = Tk()
    mid.title("Наявні продукти")
    mid.geometry("500x500")
    products_lst = list()
    with open('products.txt', 'r') as products:
        line = products.readline().strip('\n')
        while line != '':
            products_lst.append(line.split('|'))
            line = products.readline().strip('\n')
    but = Button(mid, text="Завершити", command=lambda: mid.destroy())
    but.pack()
    for i in range(len(products_lst)):
        info_prod = Label(mid, text=
        (products_lst[i][0] + ': ' +
         products_lst[i][1] + ' калорій, ' +
         products_lst[i][2] + ' протеїну, ' +
         products_lst[i][3] + ' жирів, ' +
         products_lst[i][4] + ' вуглеводів;'))
        info_prod.pack()


def get_products():
    products_lst = list()
    with open('products.txt', 'r') as products:
        line = products.readline().strip('\n')
        while line != '':
            products_lst.append(line.split('|'))
            line = products.readline().strip('\n')
    return products_lst


entry()
root.mainloop()

# Напишите программу, удаляющую из текста все слова,
#  в которых присутствуют все буквы "абв".
with open('task1_input2.txt', 'r', encoding='utf-8') as input_file:
    input_data = input_file.readlines()
with open('task1_output2.txt', 'w', encoding='utf-8') as output_file:
    for data in input_data:
        for word in data.split():
            for letter in ref:
                if letter not in word:
                    output_file.write(f'{word} ')
                    break
        output_file.write('\n')
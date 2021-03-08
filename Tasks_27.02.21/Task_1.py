K = int(input("Введите количество строк в записи: "))
Consignments = []
correct = "Yes"
for i in range(K):
    s = input("Введите действие (Vote / Add) и партию (a..z) через пробел: ")
    action = s.split(" ")[0]
    cons = s.split(" ")[1]
    # вынесим на голосование
    if action == "Add":
        Consignments.append(cons)
    # не можем провести голосование
    elif len(Consignments) == 0:
        correct = "No"
        break
    # проводим голосование
    elif cons == Consignments[len(Consignments) - 1]:
        Consignments.pop()
    # Все оставшиеся случаи
    else:
        correct = "No"
        break
# Проверка на то, что имеются обсуждения, решения по которым не было принято
if len(Consignments) != 0:
    correct = "No"
print(correct)

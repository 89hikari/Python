# Пример системного звука с помощью модуля winsound
print("\t\t\t\t Name v.0.0.2\n")
print("*"*80)
name = input("Onamae wa? ")
import winsound     # Лучше импортировать в начале файла
Freq = 1000
Dur = 1000
winsound.Beep(Freq, Dur)        # У winsound 2 параметра: частота (гц) и длительность (мс)
print("Anata wa mou shindeiru, ", name+"!")

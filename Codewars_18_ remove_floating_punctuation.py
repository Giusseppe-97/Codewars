import re

a = "¿ A ti te gusta el café ? Sí, a mí me encanta el café ! Especialmente el que vale menos de $ 1300 ."
b = "a; mí"

def remove_floating_punctuation(a):
    a = re.sub(r'[\s]([?.!,;>/"@%](?:\s|$))', r'\1', a)
    a = re.sub(r'([¡{<¿#$])\s', r'\1', a)

    return a

print(remove_floating_punctuation(a))
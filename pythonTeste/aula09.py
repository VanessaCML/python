frase = '   Curso em Vídeo Python   '
print(frase)
print(frase[3])
print(frase[3:13])
print(frase[:13])
print(frase[13:])
print(frase[1:15])
print(frase[1:15:2])
print(frase[1::2])
print(frase[::2])

print("""\nLogo, se sua pergunta é o que um desenvolvedor full stack precisa saber, a resposta é simples: tudo o que  
envolve um projeto de site ou app. Isso significa que essa pessoa pode contribuir em qualquer lugar com uma equipe de 
desenvolvimento de produto digital, conforme necessário.""")

print('\n')
print(frase.count('o'))
print(frase.count('O'))
print(frase.upper().count('O'))
print(len(frase))
print(len(frase.strip()))

print(frase.replace('Python', 'Android'))

#frase = '   Curso em Vídeo Python   '
#frase = frase.replace('Python', 'Android')
#print(frase) - nesse caso vai substituir de verdade

print('Curso' in frase)
print(frase.find('Curso'))
print(frase.find('Video'))
print(frase.lower().find('vídeo'))

print(frase.split())
dividido = frase.split()
print(dividido)
print(dividido[0])
print(dividido[2][3])
'''Qual a letra 3 da segunda palavra'''

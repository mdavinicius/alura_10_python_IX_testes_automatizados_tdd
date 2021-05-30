from dominio import Usuario, Lance, Leilao

vini = Usuario('Vini')
panai = Usuario('Panai')

lance_vini = Lance(vini, 100.0)
lance_panai = Lance(panai, 150.0)

leilao = Leilao('Celular')

leilao.lances.append(lance_vini)
leilao.lances.append(lance_panai)

for lance in leilao.lances:
    print(f'{lance.usuario.nome} deu um lance de R${lance.valor}')

avaliador = Avaliador()
avaliador.avalia(leilao)

print(f'O menor lance foi de {avaliador.menor_lance} e o maior lance foi de {avaliador.maior_lance}')


def registra_voto(op,votos):
    if op < 0 or op > 4:
        print('Digite um numero válido')
        return
    
    if op == 1: votos['windows'] += 1
    elif op == 2: votos['linux'] += 1
    elif op == 3: votos['mac'] +=1
    elif op == 4:  
        ourto =input('Digite sua resposta: ') 
        votos['outros'].append(ourto)
    elif op == 0 : 
        print("\nResultados da Enquete:")
        print(f"Windows: {votos['windows']}")
        print(f"Linux: {votos['linux']}")
        print(f"Mac OS: {votos['mac']}")
        print(f"Outros: {', '.join(votos['outros']) if votos['outros'] else 'Nenhum'}")
        exit()

votos = {
    "windows": 0,
    "linux": 0,
    "mac": 0,
    "outros": []
}
while True:
    print('\nEnquete sobre Sistemas Operacionais')
    print('1 - Windows\n2 - Linux\n3 - Mac OS\n4 - Outro\n0 - Sair')
    op = int(input('Digite uma opção:'))
    
    registra_voto(op,votos)
    
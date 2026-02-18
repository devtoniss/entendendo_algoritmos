
lista = ["Adriana","Aline","Alice","Amanda","Ana","André","Arthur","Augusto","Beatriz","Brenda","Bruno","Bianca","Bernardo","Bárbara","Benício","Bryan","Camila","Carla","Carlos","Cecília","Caio","Cristina","Clara","Cauã","Daniel","Danilo","Davi","Diego","Débora","Douglas","Diana","Denise","Eduarda","Eduardo","Elaine","Elisa","Emanuel","Erika","Enzo","Esther","Felipe","Fernanda","Fábio","Flávia","Francisco","Fátima","Fernando","Frederico","Gabriel","Gabriela","Guilherme","Giovana","Gustavo","Geovana","Gerson","Greice","Helena","Henrique","Heloísa","Hugo","Heitor","Hariany","Humberto","Hilda","Igor","Isabela","Ian","Iara","Ítalo","Ingrid","Ivan","Irene","Joana","João","Jéssica","Júlia","José","Jonas","Juliano","Jasmine","Karen","Kaique","Karina","Kevin","Kauã","Kelly","Kleber","Kamila","Larissa","Lucas","Leonardo","Letícia","Luana","Luan","Laura","Leandro","Mariana","Matheus","Miguel","Maria","Marcelo","Mayara","Murilo","Mônica","Natália","Nathan","Nicolas","Nicole","Neide","Noah","Natan","Núbia","Otávio","Olívia","Orlando","Oscar","Osmar","Ofélia","Otto","Odete","Paula","Pedro","Priscila","Patrícia","Paulo","Pietro","Paloma","Rafael"] * 2
lista = sorted(lista) # a lista já está ordenada mas apliquei o sorted apenas para garantir e por ser uma boa pratica
print(lista)
item = input(f"digite o nome que deseja buscar na lista: ") # essa é uma evolução baseada no exercício 1.1 do livro que me instigou a ver em quantas etapas o codigo levaria para encontrar um nome em uma lista com 128 nomes.

def busca_binaria(lista, item):
    baixo = 0
    alto = len(lista) - 1
    print("alto: ", alto)
    contadora = 0 # implementei essa contadora para ficar mais facil a visualização de quantas tentativas foram necessarias para encontrar o item na lista. 
    while baixo <= alto:
        print(f"tentativas: {contadora}")
        contadora += 1 
        meio = (baixo + alto) // 2
        chute = lista[meio]
        print(chute)
        if chute == item:
            print(f"o nome {item} esta na posição de n*{meio} da lista.")
            return meio
        
        if chute > item:
            print(f"alto antes: {alto}")
            alto = meio - 1 
            print(f"alto depois: {alto}")
        else:
            baixo = meio + 1
    return None    



busca_binaria(lista, item)        
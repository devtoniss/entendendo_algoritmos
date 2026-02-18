
lista = ["Adriana","Aline","Alice","Amanda","Ana","André","Arthur","Augusto","Beatriz","Brenda","Bruno","Bianca","Bernardo","Bárbara","Benício","Bryan","Camila","Carla","Carlos","Cecília","Caio","Cristina","Clara","Cauã","Daniel","Danilo","Davi","Diego","Débora","Douglas","Diana","Denise","Eduarda","Eduardo","Elaine","Elisa","Emanuel","Erika","Enzo","Esther","Felipe","Fernanda","Fábio","Flávia","Francisco","Fátima","Fernando","Frederico","Gabriel","Gabriela","Guilherme","Giovana","Gustavo","Geovana","Gerson","Greice","Helena","Henrique","Heloísa","Hugo","Heitor","Hariany","Humberto","Hilda","Igor","Isabela","Ian","Iara","Ítalo","Ingrid","Ivan","Irene","Joana","João","Jéssica","Júlia","José","Jonas","Juliano","Jasmine","Karen","Kaique","Karina","Kevin","Kauã","Kelly","Kleber","Kamila","Larissa","Lucas","Leonardo","Letícia","Luana","Luan","Laura","Leandro","Mariana","Matheus","Miguel","Maria","Marcelo","Mayara","Murilo","Mônica","Natália","Nathan","Nicolas","Nicole","Neide","Noah","Natan","Núbia","Otávio","Olívia","Orlando","Oscar","Osmar","Ofélia","Otto","Odete","Paula","Pedro","Priscila","Patrícia","Paulo","Pietro","Paloma","Rafael"] * 2 # como pedido no exercicio 1.2, estou multiplicando por 2 a quantidade de itens na lista para observar em quantas tentativas encontraremos o resultado esperado
lista = sorted(lista) # a lista já está ordenada mas apliquei o sorted apenas para garantir e por ser uma boa pratica.
print(lista)
item = input(f"digite o nome que deseja buscar na lista: ") # esta é uma evolução baseada nos exercícios 1.1 e 1.2 do livro entendendo algoritmos, que me instigaram a observar em quantas etapas o código levaria para encontrar um nome em uma lista com 128 nomes.

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
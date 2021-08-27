'''
PERSONAGENS PRINCIAIS: JOGADOR + (MARIA E JOÃO)
AMBIENTADO EM: Reinos da fantasia, em especial dos contos de fadas (com espaço pra mais)

-----ROTEIRO DO GAME-------
  "O reino de Abracadabra está passando por um momento de extrema dificuldade... O monarca foi sequestrado por uma feiticeira na noite passada!!!
  A AUAM (Agência Ultrassecreta de Assuntos Mágaicos) foi acionada para resolver o problema antes que a população fique alarmada e o caos se espalhe
pelo reino. Para isso, foram acionados os dois melhores agentes disponíveis JOÃO e MARIA. Entretando, os dois precisam de ajuda para cumprir a missão.
Você, uma pessoa que acaba de ser entrar na agência é o único disponível para ajudá-los."
  - jogador se apresenta
  - escolhe o agente pelo qual quer começar
  - parte em busca dos ingredientes para a fórmula que pode trazer o rei de volta do feitiço
  - passa por 2 cenários principais com cada agente:
    - cada cenário contará com 4 ingredientes diferentes, caberá ao jogador escolher qual;
    - alguns cenários precisarão de itens para serem acessados;
    - o jogador passará por testes em cada cenário;
  - após conquistar todos os ingredientes certos com os dois agentes, a fórmula é completada e o jogo é concluído.


-----ESTRUTURAS IMPORTANTES-------

{variável} = 0
while variável != 1 or variável != 2:
  variável = int(input({resposta do jogador}))
  if {variável} == 1 or {variável} == 2:
    break;
.................................................
while True:
  variável = int(input({resposta do jogador}))
  if {variável} == 1 or {variável} == 2:
    break;
.......................................................................
while True:
  resposta = int(input("\nDIGITE:\n     1 para SIM\n     2 para NÃO\n"))
  if resposta == 1 or resposta == 2:
    break;
........................................................................
cont = 0
for i in bag:
  cont += 1
if cont < 5:
  bag += [{item}]
if cont == 5:
  print("\nSua bolsa já está cheia.\nDeseja excluir algum item? Depois de excluí-lo, você o perderá para sempre.")
  while True:
    excluir = int(input("DIGITE:\n     1 para SIM\n     2 para NÃO\n"))
    if excluir == 1 or excluir == 2:
      break
  if excluir == 1:
    print("\nQual item você vai excluir?\nDIGITE:")
    for i in range(len(bag)):
      print("\n     ",i+1," para ", bag[i])

    eliminar =  int(input())
    bag[eliminar-1] = []

..............................................................................................................................................

'''

from time import sleep

while True:
    bag = [] #INVENTÁRIO DO PERSONAGEM COM, NO MÁXIMO, 5 ESPAÇOS (CONTANDO COM OS INGREDIENTES PRINCIPAIS)
    bag_joao = []
    bag_maria = []
    gameover = 0


    #----------------------------------CAMPANHA COM JOÃO-------------------------------------------------
    def campanha_joao(bag, gameover):
      gameover = 0
      bag = []

      # JOGADOR e João estão caminhando pela estrada real rumo ao castelo da Fera
      sleep(3)
      print("\n\n", '-' * 30, "ESTRADA REAL", '-' * 30)
      print("\nJOÃO: Então, acho que você já sabe que temos uma regra na agência, certo? Os novatos carregam os equipamentos, então pega.")
      print("<João joga a bolsa para você  enquanto fala e você começa a carregar a bolsa.>")
      print("<Vocês caminham pela estrada Real em direção ao Castelo da Fera quando João para e aponta para o lado esquerdo da estrada.>")
      print("JOÃO: Ei, o que é aquilo brilhando no chão?")
      print("<Vocês se aproximam da fonte do brilho e se deparam com um lindo anel de ouro na beira da estrada>")
      print("JOÃO: Um anel!!! E dos bonitos! Será que caiu de alguém que passava por esta estrada?")
      print("JOÃO: Vamos levar ele com a gente?")

      while True:
        sleep(3)
        resposta = int(input("DIGITE:\n     1 para SIM\n     2 para NÃO\n"))
        if resposta == 1 or resposta == 2:
          break;

      if resposta == 1:
        print("\nJOÃO: Tem certeza? Fiquei sabendo de um cara que uma vez encontrou um anel de ouro, depois descobriu que o anel era de um senhor das trevas muito tenebroso")
        print("JOÃO: Mas tudo bem, é você quem vai carregar, não eu.")
        print("<Você pega o anel e o guarda na bolsa.>")
        bolsa(bag, 'anel')
      else:
        print("\nJOÃO: Não? Tudo bem, o dono dele logo voltará pela estrada procurando")

      print("JOÃO: Sabe de uma coisa",nome,"? Essa floresta me lembra um pouco da minha infância.")
      print("JOÃO: Acredite se quiser, mas minha irmã e eu já ficamos perdidos numa floresta como essa e acabamos na casa de doces de uma bruxa (risos). "
            "Acredita que ela tentou nos comer?? A Maria teve sorte de eu estar lá, foi minha inteligência quem nos tirou daquela casa (risos).")

      print("\n<Depois de mais algum tempo de jornada, vocês encontram uma pedra azul brilhante>")
      print("JOÃO: Veja que linda! Nunca tinha visto um azul tão bonito como este! Você acha que devemos levá-la conosco?")
      while True:
        sleep(3)
        resposta = int(input("DIGITE:\n     1 para SIM\n     2 para NÃO\n"))
        if resposta == 1 or resposta == 2:
          break;

      if resposta == 1:
        bolsa(bag, 'pedra azul')
        print("\nJOÃO: Muito bom! Vou mostrar ela pra Maria quando a missão acabar, ela se interessa por esse tipo de coisa.")
        print("JOÃO: Apesar de que me parece que ela contou uma história sobre pedras brilantes que podem causar doenças... Bobagem! Como uma pedra pode ferir uma pessoa?")
        print("JOÃO: Vamos continuar, não podemos perder tempo.")

      else:
        print("\nJOÃO: Sério?? Que pena, ela é tão bonita. Mas tudo bem, vamos continuar antes que seja tarde.")

      print("<Assim que retomam o caminho vocês veêm um homem caminhando com uma grande mochila nas costas com várias máscaras pendurada nela.>")
      print("JOÃO: Ei, eu já te vi na cidade... Você é o vendedor de máscaras, não é?")
      print("VENDEDOR: Olá senhores, sim sou eu! Conhece meu trabalho?")
      print("JOÃO: É claro! Você quem vendeu as máscaras para o meu amigo Link.")
      print("VENDEDOR: Você conhece o Link?! Que maravilhoso, fui eu mesmo quem entregou aquela máscara encantada pra ele, você gostaria de uma?")
      print("JOÃO: Não sei... Estamos em uma missão um tanto importante, mas talvez ela ajude... O que acha %s? Devo comprar?" %(nome))
      while True:
        sleep(3)
        resposta = int(input("DIGITE:\n     1 para SIM\n     2 para NÃO\n"))
        if resposta == 1 or resposta == 2:
          break;
      if resposta == 1:
        bolsa(bag, 'máscara')
        print("\nJOÃO: Tudo bem, então eu quero uma igual a que você deu para o Link!")
        print("VENDEDOR: Aquela era única rapaz. Mas o que acha dessa?")
        print("<O vendedor mostra uma máscara de um homem com bigode e chapéu vermelho. João aceita e vocês se despedem do vendedor. Você guarda ela na bolsa.>")
      else:
        print("\nJOÃO: Tudo bem meu senhor, assim que eu voltar pra cidade vou te procurar para conversarmos melhor!")
        print("<Vocês se despedem e se afastam.>")

      sleep(3)
      print("<Adiante, depois de passarem por uma colina vocês avistam um grande castelo.>")
      print("JOÃO: Nossa, que castelo lindo! E pensar que antes ele era tão cheio de vida... Até aquela feiticeira chegar e transformar todos em objetos.")
      print("JOÃO: Essa feiticeira é a melhor no que faz. Não importa como, ela sempre consegue escapar da AUAM. E agora ela enfeitiçou nosso rei!")
      print("JOÃO: Estamos tentando prender ela desde que enfeitiçou uma jovem garota e fez com que ela entrasse em um sono muito profundo...")
      print("JOÃO: Mas acredito que agora estamos mais perto de pegá-la.")

      sleep(3)
      print("\n\n", '-'*30, "CASTELO DA FERA", '-'*30)

      print("\n<Vocês chegam no castelo e batem na porta. Ela se abre e vocês são recebidos por um castiçal falante.>")

      print("LUMIERE: Bonjour visitantes, meu nome é Lumiére. Como posso ajudá-los?")
      print("JOÃO: Olá, estamos numa jornada procurando alguns itens para salvar nosso Rei. Temos informações que um deles está no castelo.")
      print("LUMIÉRE: Oui, eu compreendo. Mas hoje nós estamos muito ocupados... É o aniversário da Bela e precisamos encontrar algum presente para ela.")
      print("LUMIÉRE: Por favor, voltem outro dia.")
      print("JOÃO: Ora, nós podemos te ajudar, não é",nome,"?")
      print("JOÃO: Temos alguma coisa para oferecer a estes... Senhores?")
      print("<Você olha na bolsa e tira os itens:>")
      sleep(3)
      for i in range(len(bag)):
        if bag[i] != '':
          sleep(1)
          print("     ", bag[i])

      sleep(3)

      cont = 0
      for i in bag:
        if i == 'anel':
          cont = 1

      if cont == 1:
        tirar_bolsa(bag, 'anel')
        print("LUMIÉRE: OUI OUI UM ANEL!!!")
        print("LUMIÉRE: Bem vindos! Enrtem, entrem. O que procuram?")
        print("JOÃO: Estamos procurando alguns ingredientes para poder salvar o rei de um feitiço da confeiteira má. Teria algo para nos ajudar?")
        print("LUMIÉRE: Oui, temos alguns lugares que vocês podem procurar. Peço desculpas, mas com os preparativos do aniversário muitas de nossas salas estão cheias com os preparativos.")
        print("LUMIÉRE: OS lugares disponíveis para visitas são: ")
        while True:
          sleep(3)
          resposta = int(input("\nDIGITE:\n     1 para Horta da Bela \n     2 para Salão Principal \n     3 para Biblioteca \n     4 para a Cozinha\n"))
          if resposta == 1 or resposta == 2 or resposta == 3 or resposta == 4:
            break;

        # HORTA DA BELA
        if resposta == 1:
          sleep(3)
          print("\n\n", '-' * 30, "HORTA DA BELA", '-' * 30)
          print("\n<Lumiére guia os personagens até a horta da Bela, onde ela está cuidando de algumas plantas.")
          print("BELA: Olá visitantes! Li sobre vocês no noticiário de hoje, como posso ajudá-los?")
          print("JOÃO: Estamos buscando por alguns itens para cumprir nossa missão, podemos pegar alguma coisa por aqui?")
          print("BElA: Infelizmente só possuo cenouras aqui, recentemente tenho recebido muitos pedidos de uma garota chamada Alice que leva cenouras para um amigo")
          print("BELA: Querem pegar alguma?")
          while True:
            sleep(3)
            resposta = int(input("DIGITE:\n     1 para SIM\n     2 para NÃO\n"))
            if resposta == 1 or resposta == 2:
              break;
          if resposta == 1:
            bolsa(bag, 'cenoura')
            print("JOÃO: Claro, muito obrgado Bela! Tenha um bom dia e feliz aniversário!")
            print("BELA: Obrigada! Boa sorte na missão de vocês!")
            print("LUMIÉRE: Magnifique! Eu acompanho vocês até a porta, vamos.")
          else:
            print("JOÃO: Não vamos levar? Tudo bem, obrigado pela atenção Bela. Feliz aniversário!")
            print("BELA: Obrigada! Boa sorte na missão de vocês!")
            print("LUMIÉRE: Muito bem, 'eEu acompanho vocês até a porta.")


        #SALÃO PRINCIPAL
        elif resposta == 2:
          # Lumiére guia os personagens até o salão principal
          sleep(3)
          print("\n\n", '-' * 30, "SALÃO PRINCIPAL", '-' * 30)
          print("\n<Lumiére guia vocês até o salão principal do castelo.>")
          print("MADAME SAMOVAR: Bom dia cavalheiros, como estão nessa linda manhã?")
          print("JOÃO: Muito bem, senhora. Estamos a procura de algumas coisas para uma missão de resgate. Você pode nos ajudar?")
          print("MADAME SAMOVAR: No momento a única coisa que posso lhes oferecer é um delicioso chá de maracujá. Aceitam?")
          print("JOÃO: Claro, pode ser ótimo para nossa missão!")
          print("MADAME SAMOVAR: Missão? Como assim? Vocês teriam que levar o meu pequeno Zip para uma missão??")
          print("JOÃO: Sim, minha senhora, mas é para o bem de todo o reino.")
          print("MADAME SAMOVAR: Então eu permito. Mas antes eu preciso que vocês me ajudem a descobrir qual o bolo favorito da Bela.")
          print("MADAME SAMOVAR: Hoje é o aniversário dela, e eu gostaria de fazer uma surpresa, mas não estou conseguindo descobrir. A única dica que tenho é esse papel, o que vocês me dizem?")
          print("<Madame Samovar entrega um papel com uma questão: 'Qual a fruta que nunca reprova?'>")
          print("JOÃO: E então,",nome,"qual você acha que seria a resposta?")

          while True:
            sleep(3)
            resposta = int(input("\nDIGITE:\n     1 para Morango \n     2 para Uva Passa \n     3 para Abacaxi \n     4 para Amora\n"))
            if resposta == 2:
              break;
            else:
              print("JOÃO: Hmmm, acho que não, tente de novo.")

          print("MADAME SAMOVAR: EXCELENTE! Muito obrigada. Podem levar o Zip, mas só se tomarem MUITO cuidado!")
          bolsa(bag, 'Zip')
          print("JOÃO: Com certeza senhora, agradecemos muito!")
          print("LUMIÉRE: Magnifique! Eu acompanho vocês até a porta, vamos.")

        #BIBLIOTECA
        elif resposta == 3:
          # Lumiére guia os personagens até a Biblioteca, onde se encontra a Fera
          sleep(3)
          print("\n\n", '-' * 30, "BIBLIOTECA", '-' * 30)
          print("\n<Lumiére guia vocês até a biblioteca.>")
          print("FERA: Visitantes? Posso ajudá-los?")
          print("JOÃO: Olá sr. Fera. Estamos em busca de ingredientes para cumprir uma missão muito importante.")
          print("FERA: Fiquem a vontade para olhar, mas acho que não tenho nada de mais que possam pegar, apenas aquelas xícaras de café.")
          print("<Fera aponta para uma mesina de centro com alguns grãos de café>")
          print("JOÃO: Ah sim, muito obrigado. Acho que pode nos ser útil, não é verdade,", nome,"? Vamos levar?")
          while True:
            sleep(3)
            resposta = int(input("DIGITE:\n     1 para SIM\n     2 para NÃO\n"))
            if resposta == 1 or resposta == 2:
              break;
          if resposta == 1:
            bolsa(bag, 'café')
            print("JOÃO: Muito obrgado sr. Fera! Tenha um bom dia")
            print("LUMIÉRE: Pardon, o patrão está um pouco nervoso com o aniversário de hoje. Eu acompanho vocês até a porta, vamos.")

          else:
            print("JOÃO: Não? Então tudo bem. Até mais sr. Fera!")
            print("LUMIÉRE: Pardon, o patrão está um pouco nervoso com o aniversário de hoje. Eu acompanho vocês até a porta, vamos.")

        #COZINHA
        else:
          #Lumiére leva os personagens até a cozinha do castelo
          sleep(3)
          print("\n\n", '-' * 30, "COZINHA", '-' * 30)
          print("\nLUMIÉRE: Magnifique, estava indo para lá agora mesmo para pedir ao nosso cozinheiro para preparar um pouco de granulado. É o meu favorito, vocês aceitam um pouco?")
          print("JOÃO: Claro, acho que será o ideal para a nossa jornada. Não concorda,",nome,"?")
          print("<Vocês chegam até a cozinha onde Lumiére pede ao cozinheiro um pouco do granulado>")
          print("JOÃO: E então",nome,", vamos levar este delicioso granulado conosco?")

          while True:
            sleep(3)
            resposta = int(input("DIGITE:\n     1 para SIM\n     2 para NÃO\n"))
            if resposta == 1 or resposta == 2:
              break;
          if resposta == 1:
            bolsa(bag, 'granulado')
            print("\nJOÃO: Isso é tudo Lumiére! Obrigado pela ajuda.")
            print("LUMIÉRE: É um prazer ajudar! Eu acompanho vocês até a porta.")
          else:
            print("\nJOÃO: Você não acha? Tudo bem meu amigo, então vamos seguindo.")
            print("LUMIÉRE: Tudo bem, eu acompanho vocês até a porta.")

          print("\n<Lumiére leva vocês até a pornta por onde vocês entraram.>")
          print("LUMIÉRE: Au revoir, amigos. Espero ter ajudado!")
          print("JOÃO: Ajudou sim! Agradecemos muito.")
          print("<Vocês se despedem e vão até a Estrada Real>")

      else:
        sleep(3)
        print("LUMIÉRE: Pardon, non podemos te ajudar... Temos muito trabalho a ser feito!")
        print("JOÃO: Puxa, eles parecem irredutíveis! Infelizmente não poderemos continuar sem a ajuda deles... Acho que vamos ter que voltar pra base, o chefe terá de colocar outras pessoas no lugar...")
        print("<Vocês retornam para a base sem conseguir completar a missão. Outros agentes serão designados para substituír-vos>")
        print("\n\n\n\n\n          FIM DE JOGO")
        gameover = 1
        return gameover, bag
        #GAME OVER

      sleep(3)
      print("\n\n", '-' * 30, "FLORESTA DO LOBO MAU", '-' * 30)
      print("\nJOÃO: Pois bem",nome,", concluímos a primeira parte. Agora precisamos ir até a casa da Vovó da Chapeuzinho que fica... Para aquele lado.")
      print("<João aponta para uma estrada menor que leva até uma floresta>")

      print("<Vocês caminham pela estrada afora bem sozinhos em direção a casa da Vovozinha, quando avistam um campo de margaridas brancas ao lado>")
      print("JOÃO:",nome,", você acha que a vovó gostaria de ganhar estas flores?")
      while True:
        sleep(3)
        resposta = int(input("DIGITE:\n     1 para SIM\n     2 para NÃO\n"))
        if resposta == 1 or resposta == 2:
          break;
      if resposta == 1:
        print("<João vai até a beira da estrada e colhe um pequeno buquê de flores>")
        bolsa(bag, 'flores')
        print("JOÃO: São lindas! Ela vai amar.")
      else:
        print("JOÃO: Que pena... Elas são tão lindas...")

      print("JOÃO: Mas enfim, vamos andando, fiquei sabendo que perto daqui há um pântano com um ogro assustador e egoísta que odeia que entrem no pântano dele. Eu é quem não quer confusão com ele.")

      print("\n<Perto dali está, cravado numa árvore, um boto de um rosto sorridente que parece estar manchado com sangue.>")
      print("JOÃO: Que bizarro! Olhe aquele boton. Devemos pegar pra levar até a base e pesquisar depois?")
      while True:
        sleep(3)
        resposta = int(input("DIGITE:\n     1 para SIM\n     2 para NÃO\n"))
        if resposta == 1 or resposta == 2:
          break;
      if resposta == 1:
        sleep(3)
        bolsa(bag, 'boton')
        print("<Você vai até a árvore, pega o boton e guarda na bolsa. E então vocês seguem o caminho>")
      else:
        print("JOÃO: Tudo bem, eu só havia achado estranho... Mas vamos.")

      print("\n<Mais adiante, depois de passar por uma curva um tanto acentuata vocês avistam uma cerejeira ao lado esquerdo próximo a um riaxo>")
      print("JOÃO: Fiquei sabendo que a vovó é muito boa em fazer tortas de cereja, acha que devemos levar algumas para ela?")
      while True:
        sleep(3)
        resposta = int(input("DIGITE:\n     1 para SIM\n     2 para NÃO\n"))
        if resposta == 1 or resposta == 2:
          break;

      if resposta == 1:
        bolsa(bag, 'cerejas')
        print("JOÃO: Excelente! Já estou com fome, espero que ela goste.")
      else:
        print("JOÃO: Poxa, que pena, estou com tanta fome.")


      print("<Depois de atravessar uma ponte de madeira vocês avistam uma casa de madeira com fumaça saindo da chaminé.>")
      print("JOÃO: Alí está. Consegue sentir esse cheiro de chocolate? Maravilhoso. Certeza que é a casa da vovó!")
      sleep(3)
      print("\n\n", '-' * 30, "CASA DA VOVÓ", '-' * 30)
      print("\n<Vocês se aproximam e batem na porta. E quem atende é uma jovem garota com um capuz vermelho.>")
      print("JOÃO: Oi menina, sua avó está em casa?")
      print("CHAPEUZIHO: Está sim, ela está na cozinha preparando cookies de chocolate. Posso ajudar?")
      print("JOÃO: Estamos em uma missão para resgatar o rei e precisamos da ajuda de sua avó.")
      print("CHAPEUZINHO: Hoje ela meio triste, não sei se conseguirá ajudar... Vocês têm algo para alegrá-la? Ela ama receber flores.")
      print("JOÃO: Acredito que podemos ajudar, não é",nome,"?")
      print("<Você abre a bolsa e mostra os itens>")

      sleep(3)
      for i in range(len(bag)):
        if bag[i] != '':
          sleep(1)
          print("     ", bag[i])
      sleep(3)

      cont = 0
      for i in bag:
        if i == 'flores':
          cont = 1

      if cont == 1:
        tirar_bolsa(bag, 'flores')
        print("CHAPEUZINHO: Que margaridas lindas!!! São as favoritas da vovó. Entrem, por favor.")
        print("<Vocês seguem para a cozinha onde a encontram>")

        print("CHAPEUZINHO: Veja vovó, que flores lindas!")
        print("VOVÓ: Margaridas, minhas preferidas! Ouvi que vocês estão numa missão, posso ajudar, meus jovens?")
        print("JOÃO: Pode sim. Precisamos de alguns itens para reverter o feitiço que foi soltado no rei e descobrimos que um deles está em sua casa. Podemos procurar aqui?")
        print("VOVÓ: Fiquem a vontade, a casa é pequena, mas acho que encontrarão o que procuram. Onde vocês gostariam de procurar?")
        while True:
          sleep(3)
          resposta = int(input("\nDIGITE:\n     1 para Quarto da vovó \n     2 para Banheiro \n     3 para Cozinha \n     4 para a Sala de Jantar\n"))
          if resposta == 1 or resposta == 2 or resposta == 3 or resposta == 4:
            break;

        #QUARTO DA VOVÓ
        if resposta == 1:
          sleep(3)
          print("\n\n", '-' * 30, "QUARTO DA VOVÓ", '-' * 30)
          print("<Vocês vão até o quarto da vovó e encontram com um homem que está vasculhando o quarto.>")
          print("JOÃO: Quem é você? E o que está procurando?")
          print("LENHADOR: Eu sou só um lenhador que estava trabalhando aqui perto quando gritaram por ajuda.")
          print("LENHADOR: Um lobo entrou na casa da vovó e eu estou procurando por pistas que me levem até ele.")
          print("JOÃO: Ah sim. Estamos procurando por algum item para nos ajudar no nosso serviço.")
          print("LENHADOR: Aqui eu só encontrei isso:")
          print("<O homem mostra um tufo de pelos do lobo>")
          print("JOÃO: Acho que pode servir, não é",nome,"? Vamos pegar?")
          while True:
            sleep(3)
            resposta = int(input("DIGITE:\n     1 para SIM\n     2 para NÃO\n"))
            if resposta == 1 or resposta == 2:
              break;
          if resposta == 1:
            bolsa(bag, 'pelos do lobo')
            print("JOÃO: Muito obrigado senhor, vamos levar isso com a gente. A AUAM agradece sua ajuda.")
            print("JOÃO: Agora vamos adiante.")
          else:
            print("JOÃO: Não? Tudo bem, então vamos.")

        #BANHEIRO
        elif resposta == 2:
          sleep(3)
          print("\n\n", '-' * 30, "BANHEIRO", '-' * 30)
          print("<Vocês vão até o banheiro da vovó. E encontram um painel com a seguinte mensagem:>")
          print("<'O que é que fica cada vez mais molhado quando a gente seca?'>")
          print("JOÃO: Que estranho! Precisamos descobrir a resposta dessa charada para entrar no banheiro. O que acha que é?")

          while True:
            sleep(3)
            resposta = int(input("\nDIGITE:\n     1 para Rodo \n     2 para Sabonete \n     3 para Toalha \n     4 para Toneira\n"))
            if resposta == 3:
              print("JOÃO: Boa %s, funcionou. vamos conseguir entrar." %(nome))
              print("<Vocês entram no banheiro e vêem o creme dental de hortelã da vovó em cima da pia>")
              print("JOÃO: Então, o que me diz de levar esta pasta de dente?")
              while True:
                sleep(3)
                resposta = int(input("DIGITE:\n     1 para SIM\n     2 para NÃO\n"))
                if resposta == 1 or resposta == 2:
                  break;
              if resposta == 1:
                bolsa(bag, 'pasta de dente')
                print("JOÃO: Acho que vai servir, agora vamos.")
              else:
                print("JOÃO: Tem razão, acho que não faz sentido, vamos adiante.")
              break;
            else:
              print("JOÃO: Hmmm, acho que não, tente de novo.")

        #COZINHA
        elif resposta == 3:
          sleep(3)
          print("\n\n", '-' * 30, "COZINHA", '-' * 30)
          print("JOÃO: Tem alguma coisa aqui que você nos sugere, vovó?")
          print("VOVÓ: Sim, o que me diz deste meu novo açúcar? Eu comprei de um viajante que passava por aqui, ele faz muito sucesso nas minhas receitas.")
          print("VOVÓ: Aceitam um pouco?")
          while True:
            sleep(3)
            resposta = int(input("DIGITE:\n     1 para SIM\n     2 para NÃO\n"))
            if resposta == 1 or resposta == 2:
              break;
          if resposta == 1:
            bolsa(bag, 'açucar')
            print("JOÃO: Muito obrigado vovó, vai nos ajudar bastante. Agora precisamos ir, mas gostaria de voltar para experimentar algumas das suas receitas. Nos vemos em breve.")
          else:
            print("JOÃO: Acho que não precisamos, não é, %s? Mas obrigado, tenham um bom dia" %(nome))

        #SALA DE JANTAR
        else:
          sleep(3)
          print("\n\n", '-' * 30, "SALA DE JANTAR", '-' * 30)
          print("CHAPEUZINHO: Na sala de jantar tem a cesta que eu trouxe para a vovó. Acredito que vocês podem encontrar algo nela.")
          print("<Vocês caminham até a cesta e se deparam com lindas maçãs verdes.>")
          print("JOÃO: Que maçãs bonitas! Acho que podemos levar algumas, não acha %s?" %(nome))
          while True:
            sleep(3)
            resposta = int(input("DIGITE:\n     1 para SIM\n     2 para NÃO\n"))
            if resposta == 1 or resposta == 2:
              break;

          if resposta == 1:
            bolsa(bag, 'maçãs')
            print("JOÃO: Excelente, muito obrigado pessoal, agora precisamos ir.")
          else:
            print("JOÃO: Não? Bom, então tudo bem.")

      else:
        sleep(3)
        print("CHAPEUZINHO: Que pena. Infelizmente isso não vai deixar minha avó feliz, tentem voltar outro dia.")
        print("JOÃO: Puxa, parece que não conseguiremos entrar! Acho que vamos ter que voltar pra base, o chefe terá de colocar outras pessoas no lugar...")
        print("<Vocês retornam para a base sem conseguir completar a missão. Outros agentes serão designados para substituír-vos>")
        gameover = 1
        return gameover,bag

      return gameover,bag

    #----------------------------------------------------------------------------------------------------

    #----------------------------------CAMPANHA COM MARIA------------------------------------------------
    def campanha_maria(bag, gameover):
      bag = []
      gameover = 0

      # JOGADOR e MARIA estão caminhando pela estrada real rumo a Fantástica Fábrica de chocolate
      sleep(3)
      print("\n\n", '-' * 30, "LOND CITY", '-' * 30)
      print("<Vocês entram na cidade de Lond City e partem rumo à Fantástica Fábrica de Chocolates>")
      print("<Algumas quadras depois da entrada, vocês avistam um ponto dourado no chão>")
      print("MARIA: Ei, o que é aquilo brilhando no chão?")
      print("<Vocês se aproximam da fonte do brilho e se deparam com um pedaço de papel brilahnte>")
      print("MARIA: Um bilhete dourado!")
      print("MARIA: Vamos levar ele com a gente?")

      while True:
        sleep(3)
        resposta = int(input("DIGITE:\n     1 para SIM\n     2 para NÃO\n"))
        if resposta == 1 or resposta == 2:
          break;

      if resposta == 1:
        print("\nMARIA: Acho que será essencial para entrarmos na fábrica")
        bolsa(bag, 'bilhete dourado')
      else:
        print("\nMARIA: Tudo bem, talvez não será muito útil para nós.")

      print("\n<Alguns quarteirões depois, vocês encontram uma moeda com o rosto de uma mulher>")
      print("MARIA: Veja aquilo, parece uma moeda.")
      print("<Maria pega a moeda do chão e encara o rosto marcado na moeda>")
      print("MARIA: Ei, eu conheço esta mulher é a Joan Austeena! Eu já li alguns livros dela, Orgulho e Paixão é o meu favorito!")
      print("MARIA: Você acha que vamos precisar dessa moeda?")

      while True:
        sleep(3)
        resposta = int(input("DIGITE:\n     1 para SIM\n     2 para NÃO\n"))
        if resposta == 1 or resposta == 2:
          break;

      if resposta == 1:
        bolsa(bag, 'moeda')
        print("MARIA: Incrível! Vou mostrar pro João quando a missão terminar, ele não vai acreditar que uma escritora está em uma moeda.")
        print("MARIA: Vamos continuar, não podemos perder tempo.")

      else:
        print("MARIA: Sério?? Que pena, ela é tão bonita. Mas tudo bem, vamos continuar antes que seja tarde.")

      print("\n<Depois de atravessar algumas ruas finalmente vocês chegam na entrada da fábrica.")
      sleep(3)
      print("\n\n", '-' * 30, "FANTÁSTICA FÁBRICA DE CHOCOLATES", '-' * 30)
      print("\nMARIA: Nossa, ela é realmente grande! Ouvi dizer que por dentro é até maior.")
      print("<Vocês passam pelo portão e, antes param em frente às portas e tocam a campainha.>")
      print("<Pouco depois um homem alto usando um terno e uma cartola atende a porta e fica encarando vocês.>")
      print("MARIA: Olá, o senhor deve ser Willy Wonka, meu nome é Maria e precisamos enrtar para procurar por alguns ingredientes para uma poção.")
      print("WILLY WONKA: Você disse ingrediente?? Quer roubar meus ingredientes? Boa tentativa senhorita, mas aqui você não entrará.")
      print("MARIA: Não senhor, estamos procurando por alguns ingredientes para uma poção que vai salvar nosso rei.")
      print("WILLY WONKA: Que seja. Aqui só entram pessoas convidadas!")

      print("MARIA: %s, você pegou o bilhete?" %(nome))
      print("<Você olha na bolsa e tira os itens:>")
      for i in range(len(bag)):
        sleep(1)
        print("     ", bag[i])
      for i in bag:
        if i == 'bilhete dourado':
          tirar_bolsa(bag,'bilhete dourado')
          print("\nWILLY WONKA: Vocês possuem o bilhete que faltava!!! Entrem, por favor.")
          print("WILLY WONKA: Desculpem meus modos, várias pessoas tentam entrar aqui para roubar minhas invenções.")
          print("MARIA: Não queremos roubar nada, como eu disse, estamos em uma missão para salvar o rei e precisamos procurar por alguns ingredientes aqui.")
          print("WILLY WONKA: Ah sim, entendo. Bem se quiserem eu posso levar vocês até estes lugares:")
          while True:
            sleep(3)
            resposta = int(input("\nDIGITE:\n     1 para a Sala de Invenções \n     2 para a Sala das Nozes \n     3 para o Quarto dos Oompa Loompa \n     4 para a Cachoeira de chocolate \n"))
            if resposta == 1 or resposta == 2 or resposta == 3 or resposta == 4:
              break;

          # Sala de Invenções
          if resposta == 1:
            sleep(3)
            print("\n\n", '-' * 30, "SALA DE INVENÇÕES", '-' * 30)
            print("<Willy Wonka guia vocês até a Sala de Invenções, onde os novos chicletes da fábrica estão sendo criados.>")
            print("\nWIILY WONKA: Sejam bem-vindos à Sala de Invenções! Aqui estamos criando novos chicletes cheio de experiências inovadoras. O chiclete de amora será um sucesso!")
            print("MARIA: Maravilha! Será que podemos pegar alguns chicletes de amora para preparar a receita? ")
            print("WILLY WONKA: Claro! Fiquem a vontade! Só não comam ele, pois você pode ficar...  ")
            print("<Antes de completar a frase, uma garota comeu um chiclete, virou uma bola gigante e saiu rolando pela sala.>")
            print("WILLY WONKA: Viram só! Eu avisei! Usem na receita, mas não comam! Certeza que ainda vão querer levar esse chiclete? ")
            while True:
              sleep(3)
              resposta = int(input("DIGITE:\n     1 para SIM\n     2 para NÃO\n"))
              if resposta == 1 or resposta == 2:
                break;
            if resposta == 1:
              bolsa(bag, 'chiclete de amora')
              print("MARIA: Muito obrgado, Willy!")
            else:
              print("MARIA: Não vamos levar? Tudo bem. Achei esse chiclete muito estranho!")
            print("Willy Wonka: Muito bem, os Oompa Loompas vão acompanhar vocês até a saída da fábrica, não saiam de perto deles.")

          # SALA DAS NOZES
          elif resposta == 2:
            sleep(3)
            print("\n\n", '-' * 30, "SALA DAS NOZES", '-' * 30)
            print("\n<Willy Wonka guia vocês até a Sala das Nozes, onde os esquilos selecionam as nozes boas das estragadas.>")
            print("WILLY WONKA: Essa é a Sala das Nozes, onde os esquilos mais espertos do mundo trabalham escolhendo as melhores nozes para os meus chocolates.")
            print("MARIA: UAU! Nunca imaginei que eles poderiam fazer isso aqui dentro da fábrica! Será que aqui podemos encontrar boas nozes para nossa missão?")
            print("WILLY WONKA: Esses esquilos são muito valiosos e sem dúvidas as melhores nozes estão aqui! Mas vocês só vão conseguir pegar se me ajudarem a desemperrar um túnel de nozes que está entupido.")
            print("MARIA: Se essa for a única forma de conseguir as nozes, topamos o desafio!")
            print("WILLY WONKA: Então se preparem para resolver a charada que está no painel do túnel do esquilo 47.")
            print(f'<Ao se aproximarem, Maria e {nome} leem no painel: Sou uma caixinha de bem-querer, não há carpinteiro que a saiba fazer. Quem sou eu?')
            print("MARIA: E então,", nome, "o que você acha que é?")

            while True:
              sleep(3)
              resposta = int(input("\nDIGITE:\n     1 para Cofre \n     2 para Ampulheta \n     3 para Noz  \n     4 para Diário\n"))
              if resposta == 3:
                break
              else:
                print("MARIA: Hmmm, acho que não, tente de novo.")

            print("WILLY WONKA: PERFEITO! Essa estava fácil! Podem levar as nozes")
            bolsa(bag, 'nozes')
            print("Willy Wonka: Muito bem, os Oompa Loompas vão acompanhar vocês até a saída da fábrica, não saiam de perto deles.")

          # QUARTO DOS OOMPA LOOMPAS
          elif resposta == 3:
            sleep(3)
            print("\n\n", '-' * 30, "QUARTO DOS OOMPA LOOMPAS", '-' * 30)
            print("\n<Willy Wonka guia vocês até o Quarto dos Ompaa Loompas.>")
            print("Oompa Loompa: Adbek alkdnd! Hiadasnk?")
            print("MARIA: O que eles falaram?")
            print("WILLY WONKA: Disseram que estão comendo marshmellows gigantes e querem saber se vocês querem um pouco.")
            print("<Os Oompa Loompas trazem um bow enorme com um único marshmellow gigante>")
            print("MARIA: Nunca vi nada igual. Esse marshmellow deve ser muito raro e acho que pode ser útil na receita, não é verdade,", nome, "? Vamos levar?")
            while True:
              sleep(3)
              resposta = int(input("DIGITE:\n     1 para SIM\n     2 para NÃO\n"))
              if resposta == 1 or resposta == 2:
                break;
            if resposta == 1:
              bolsa(bag, 'marshmellow gigante')
              print("MARIA: Muito obrigada Oompa Loompas! Espero que isso seja exatamente o que a gente precisa! Tenham um bom dia!")

            else:
              print("MARIA: Não? Então tudo bem. Até mais Oompa Loompas!")
            print("Willy Wonka: Não se despeçam, ainda, os Oompa Loompas vão acompanhar vocês até a saída da fábrica, não saiam de perto deles.")
            print("MARIA: Ahhh, maravilha! Vai ser ótimo ter ajuda para carregar esse marshmellow!")

          # CACHOEIRA DE CHOCOLATE
          else:
            sleep(3)
            print("\n\n", '-' * 30, "CACHOERA DE CHOCOLATE", '-' * 30)
            print("\n<Willy Wonka guia vocês até a Cachoeira de Chocolate>.")
            print("WILLY WONKA: Apresento a vocês a maior cachoeira de chocolate do mundo! Além de maior, produz o melhor e mais cremoso chocolate!")
            print("MARIA: Parece delicioso!!!")
            print("WILLY WONKA: Não tenha dúvidas disso, Maria! Não há chocolate como o da minha fábrica!")
            print("MARIA: Se esse chocolate é tão especial assim, talvez seja justamente isso que a gente precise para a receita da nossa missão! Podemos levar um pouco conosco?")
            print("WILLY WONKA: Claro! Espero que ele seja o ingrediente essencial para a receita que vocês precisam fazer.")
            print("MARIA: E então", nome, ", vamos levar este delicioso e raro chocolate conosco?")

            while True:
              sleep(3)
              resposta = int(input("DIGITE:\n     1 para SIM\n     2 para NÃO\n"))
              if resposta == 1 or resposta == 2:
                break;
            if resposta == 1:
              bolsa(bag, 'chocolate')
              print("\nMARIA: Isso é tudo Willy Wonka! Muito obrigada pela sua ajuda.")
              print("WILLY WONKA: Não há de quê!")
            else:
              print(f"\nMARIA: Você não acha que será útil? Tudo bem {nome}, então vamos seguindo.")

            print("Willy Wonka: Muito bem, os Oompa Loompas vão acompanhar vocês até a saída da fábrica, não saiam de perto deles.")

          break;
      else:
        sleep(3)
        print("WILLY WONKA: Boa tentativa. Adeus!")
        print("<Willy fecha a porta e vocês são obrigados a voltar pela cidade>")
        print("MARIA: Não acredito que fracassamos! Meu currículo será manchado para sempre...")
        print("<Vocês retornam para a base sem conseguir completar a missão. Outros agentes serão designados para substituír-vos>")
        sleep(3)
        print("\n\n\n\n\n          FIM DE JOGO")
        gameover = 1
        return gameover, bag
        # GAME OVER

      sleep(3)
      print("\n\n", '-' * 30, "LOND CITY", '-' * 30)
      print("\nMARIA: Pois bem", nome,", a primeira parte da nossa missão está concluída. Agora precisamos ir até a Fazenda do João, sabe?! Aquele do pé de feijão! Que fica depois da cidade. Vamos precisar pegar um trem para chegar até lá!")
      print("<Maria vai até a bilheteria do trem para comprar passagens>")
      print("<Já no trem vocês encontram um caderno que parece ser de um detetive.>")
      print(f"MARIA: {nome}, será que é esse caderno é de quem eu estou pensando mesmo? Não é possível! é o caderno do Charleck Gomes.")
      print("MARIA:", nome, ", acho que precisamos levar algo para o João, você acha que ele gostaria de ganhar este caderno? É histórico! Eu ia adorar ganhar ")
      while True:
        sleep(3)
        resposta = int(input("DIGITE:\n     1 para SIM\n     2 para NÃO\n"))
        if resposta == 1 or resposta == 2:
          break;
      if resposta == 1:
        bolsa(bag, 'caderno do detetive')
        print("MARIA: Perfeito! Eu acho que ele vai amar.")
      else:
        print("MARIA: Que pena... Me pareceu um presente ideal...")

      print("MARIA: Mas enfim, já chegamos ao nosso destino! Na hora de descer precisamos ficar atentos, pois tem uma estação aqui que dizem levar para o mundo das bruxas. Onde fica a fantasiosa escola de Golwarts")
      print("<Após sair da estação de trem, vocês vêem a barraca de um feirante vendendo um pacote de milho especial para gansos e decidem ir até ele.>")
      print(f"MARIA: Olha só, {nome} acho que o João costuma ter gansos na fazenda, você não acha que esse milho poderia ser útil para ele?")
      while True:
        sleep(3)
        resposta = int(input("DIGITE:\n     1 para SIM\n     2 para NÃO\n"))
        if resposta == 1 or resposta == 2:
          break;

      if resposta == 1:
        bolsa(bag, 'milho')
        print("MARIA: Excelente! Acho que vamos poder ajudá-lo.")
      else:
        print("MARIA: Poxa, que pena, os gansos vão ficar sem o milho especial.")

      print("<Depois de sair da barraca do feirante vocês avistam uma pequena estrada de terra que conduz a uma fazenda com a seguinte placa 'O maior pé de feijão do mundo é o do João'>")
      sleep(3)
      print("\n\n", '-' * 30, "FAZENDA DE FEIJÕES DO JOÃO", '-' * 30)
      print(f"MARIA: É isso! É aqui! Chegamos {nome}!")
      print("<Vocês se aproximam e começam a chamam pelo João. E logo ele aparece todo sorridente, mas apressado.>")
      print("MARIA: Oii, João! Que bom que te encontramos! Estamos em uma importante missão para salvar o rei de uma confeiteira que o enfeitiçou e em breve quer dominar todo o nosso reino com suas guloseimas enfeitiçadas.")
      print("JOÃO DO PÉ: Olá, Maria! Há quanto tempo não nos vemos! Por onde anda seu irmão, meu xará? Não o vejo desde quando vocês quase foram comidos quando criança. Ufa! Ainda bem que dessa vocês escaparam.")
      print("MARIA: É verdade! Faz muito tempo! O João está bem, estamos trabalhando juntos nessa missão, e vou encontrá-lo em breve!")
      print("JOÃO DO PÉ: Bom, Maria, fiquei muito feliz em te ver, mas agora preciso ir até a feira comprar milho para os meus gansos e já estou atrasado!")
      print("MARIA: Acredito que podemos te ajudar, não é", nome, "?")
      print("<Você abre a bolsa e mostra os itens>")
      sleep(3)

      for i in range(len(bag)):
        sleep(1)
        print("     ", bag[i])
      sleep(3)
      cont = 0
      for i in bag:
        if i == 'milho':
          cont = 1

      if cont == 1:
          tirar_bolsa(bag, 'milho')
          print("JOÃO DO PÉ: UAU!!! Era justamnete esse milho que eu ia comprar! São os melhores da região. Agora nem vou mais precisar sair. Entrem, entrem!")
          print("<Vocês seguem para dentro da fazenda.>")
          print("MARIA: Como está linda a sua fazenda, João! Parece que tudo tem dado muito certo, por aqui!")
          print("JOÃO DO PÉ: Obrigado, Maria! Bom, você me disse que está em uma importante missão! Mas como eu posso te ajudar?")
          print("MARIA: Então, estamos procurando por ingredientes especiais para fazer uma fórmula mágica que reverta o feitiço que está sob o rei. Você acha que podemos procurar por aqui?")
          print("JOÃO DO PÉ: Mas é claro! Depois que vocês me trouxeram o milho, posso ficar aqui e ajudá-los! Fiquem a vontade! Onde vocês gostariam de procurar?")
          while True:
            sleep(3)
            resposta = int(input("\nDIGITE:\n     1 para Horta de Feijões \n     2 para Campo das Vacas Malhadas  \n     3 para Galinheiro \n     4 para Pomar\n"))
            if resposta == 1 or resposta == 2 or resposta == 3 or resposta == 4:
              break;

          # HORTA DE FEIJÕES
          if resposta == 1:
            sleep(3)
            print("\n\n", '-' * 30, "HORTA DE FEIJÕES", '-' * 30)
            print("\n<Vocês seguem até a horta do João, onde fica o maior e mais famoso pé de feijão do mundo.>")
            print("JOÃO DO PÉ: Ótima escolha! Esse é um dos meus lugares favoritos na Fazenda! Foi aqui onde tudo começou a prosperar!")
            print("MARIA: Esse lugar é incrível! Quando eu era criança ainda não tinha esse pé de feijão aqui! Estou começando a achar que um feijão de um pé tão especial como esse pode ser essencial para a receita da nossa fórmula mágica.")
            print("JOÃO DO PÉ: Tem razão, Maria! Os três feijões mágicos que deram origem a esse maravilhoso pé são inigualáveis, e tenho certeza que vocês não vão encontrar nada igual.")
            print("MARIA: O que você acha", nome, "? Vamos levar com a gente??")
            while True:
              sleep(3)
              resposta = int(input("DIGITE:\n     1 para SIM\n     2 para NÃO\n"))
              if resposta == 1 or resposta == 2:
                break;
            if resposta == 1:
              bolsa(bag, 'feijões mágicos')
              print("MARIA: Muito obrigada, João, vamos levar uns feijões com a gente. A AUAM agradece por você ter sido tão amigável conosco.")
              print("JOÃO DO PÉ: Magina, Maria! Mande lembranças ao seu irmão e boa sorte na missão!")
            else:
              print("MARIA: Não? Tudo bem, então vamos seguir.")

          # CAMPO DAS VACAS MALHADAS
          elif resposta == 2:
            sleep(3)
            print("\n\n", '-' * 30, "CAMPO DAS VACAS MALHADAS", '-' * 30)
            print("\n<Vocês chegam até o campo das vacas malhadas e encontram uma placa com a seguinte mensagem:>")
            print("<'A vaca tem 4 e a garota tem 6.'>")
            print("MARIA: Que frase mais estranha! Precisamos descobrir a reposta para entrar no campo?")
            print("JOÃO DO PÉ: É isso mesmo, Maria! Desde que algumas vacas malhadas começaram a sumir, coloquei esssa charada para evitar novos roubos. Você sabe a resposta?")
            print(f"MARIA: Eu não tenho ideia, o que você acha que é, {nome}?")

            while True:
              sleep(3)
              resposta = int(input("\nDIGITE:\n     1 para Amigas \n     2 para Pintas \n     3 para Litros de leite  \n     4 para Letras\n"))
              if resposta == 4:
                print(f"MARIA: Arrasou {nome}!!! Funcionou. Agora podemos entrar!")
                print("<Vocês entram no Campo e encontram um espaço coberto cheio de potes e mais potes de leite fresco.>")
                print(f"MARIA: Olha quando leite. {nome}, acho que tão fresco assim nãp vai ser fácil de achar, o você acha da gente levar um pouco?")
                while True:
                  resposta = int(input("DIGITE:\n     1 para SIM\n     2 para NÃO\n"))
                  if resposta == 1 or resposta == 2:
                    break;
                if resposta == 1:
                  bolsa(bag, 'leite')
                  print("MARIA: Perfeito! Acho que vai ser ótimo, agora precisamos ir.")
                else:
                  print("MARIA: Verdade, acho que não faz sentido, vamos adiante.")
                break;
              else:
                print("MARIA: Hmmm, acho que não é essa a resposta, tente de novo.")

          # GALINHEIRO
          elif resposta == 3:
            sleep(3)
            print("\n\n", '-' * 30, "GALINHEIRO", '-' * 30)
            print("\n<João guiam vocês até o seu formoso galinheiro de gansos.>")
            print("MARIA: João, você acha que teria algo aqui que serviria para nós?")
            print("JOÃO DO PÉ: Com certeza, Maria! Eu já estava pensando em te sugerir mesmo! Muitos sabem como meus gansos são valiosos para mim, pois alguns deles herdaram a capacidade de produzir ovos de ouro assim como a mãe deles, a famosa gansa que todos já conhecem.")
            print("JOÃO DO PÉ: Por isso eu acho que mais raro do que qualuqer coisa que se possa achar, os ovos de ouro dos meus gansos com certeza estão em primeiro lugar!")
            print(f"MARIA: Eu acho que você pode estar certo, João! O que você acha, {nome}? Devemos levar os ovos?")
            while True:
              sleep(3)
              resposta = int(input("DIGITE:\n     1 para SIM\n     2 para NÃO\n"))
              if resposta == 1 or resposta == 2:
                break;
            if resposta == 1:
              bolsa(bag, 'ovos de ouro')
              print("MARIA: Muito obrigada João, vai nos ajudar bastante. Agora precisamos ir.")
            else:
              print(f"MARIA: Acho que não vamos precisar, não é, {nome}? Mas obrigada, pelo conselho, João")

          # POMAR
          else:
            sleep(3)
            print("\n\n", '-' * 30, "POMAR", '-' * 30)
            print("\nJOÃO DO PÉ: Esse é nosso maravilhoso e rico pomar! Tem de tudo um pouco aqui! Frutas de várias partes do mundo.")
            print("<Vocês caminham pelo pomar e se deparam com um deslumbrante pé brilhoso de framboesas>")
            print("MARIA: Mas que brilho extraordinário! O que tem de especial nesse pé, João?")
            print("JOÃO DO PÉ: Então, Maria! Essa é a maior novidade do nosso pomar. Desde que encontrei a gansa que põe ovos de ouro,\n"
                  " comecei a estudar sobre essa combinação estranhamente maravilhosa entre metais preciosos e os alimentos\n"
                  " e não é que eu encontrei uma maneira de fazer isso com as framboesas?!")
            print(f"MARIA: Estou maravilhada! Esse me parece o ingrediente perfeito para nossa fórmula mágica! Você acha que devemos levar, {nome}?")
            while True:
              sleep(3)
              resposta = int(input("DIGITE:\n     1 para SIM\n     2 para NÃO\n"))
              if resposta == 1 or resposta == 2:
                break;

            if resposta == 1:
              bolsa(bag, 'framboesas prateadas')
              print("MARIA: Incrível, muito obrigado João, agora precisamos ir.")
            else:
              print("MARIA: Não? Bom, então tudo bem.")


      else:
        sleep(3)
        print("JOÃO DO PÉ: Que pena que não conseguem me ajudar, Maria! Infelizmente não posso receber vocês, eu realmente\n"
              "preciso comprar milho para os meus gansos e agora a feira já está quase fechando!\n"
              "Mas volte outro dia!")
        gameover = 1
        return gameover, bag  # game over

      return gameover, bag

    #----------------------------------------------------------------------------------------------------
    def bolsa(bag, item):
      vazio = 0
      cont = 0
      for i in bag:
        if i == '':
          vazio += 1
        cont += 1
      if cont < 5:
        if vazio != 0:
          cont = 0
          for j in bag:
            cont += 1
            if j == '':
              bag[cont - 1] = item
              break
        else:
          bag += [item]
      if cont == 5:
        if vazio != 0:
          cont = 0
          for j in bag:
            cont += 1
            if j == '':
              bag[cont - 1] = item
              break
        else:
          print("\n", ' ' *30, "SUA BOLSA JÁ ESTÁ CHEIA", ' '*30, "\n\nDeseja excluir algum item? Depois de excluí-lo, você o perderá para sempre!")
          while True:
            excluir = int(input("DIGITE:\n     1 para SIM\n     2 para NÃO\n"))
            if excluir == 1 or excluir == 2:
              break
          if excluir == 1:
            print("\nQual item você vai excluir?\nDIGITE:")
            for i in range(len(bag)):
              print("\n     ", i + 1, " para ", bag[i])

            eliminar = int(input())
            bag[eliminar - 1] = item

    # ----------------------------------------------------------------------------------------------------
    def tirar_bolsa(bag, item):
      cont = 0
      for i in bag:
        cont += 1
        if i == item:
          bag[cont - 1] = ''







    '''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~INTRODUÇÃO DO JOGO~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''
    print("\n\n\n\n\n     O reino de Abracadabra está passando por um momento de extrema dificuldade... O monarca foi sequestrado por uma feiticeira na noite passada!!!\n"
      "A AUAM (Agência Ultrassecreta de Assuntos Mágaicos) foi acionada para resolver o problema antes que a população fique alarmada e o caos se espalhe pelo reino.\n"
      "Para isso, foram acionados os dois melhores agentes disponíveis JOÃO e MARIA. Entretando, os dois precisam de ajuda para cumprir a missão.\n"
      "Você, uma pessoa que acaba de ser entrar na agência é o único disponível para ajudá-los.")
    sleep(5)
    print("\n\n", '-=' * 30, "BASE SECRETA DA AUAM", '=-' * 30)

    print("\n<Você foi convocado ao escritório do Chefe da AUAM. Ao entrar no escritório vê o chefe sentado atrás de uma grande mesa e duas pessoas de frente para ele>")
    print("CHEFE: Finalmente você chegou. Agente João, agente Maria, quero que conheçam o nosso novo agente.")
    print("MARIA: Muito prazer, eu sou Maria")
    print("JOÃO: Eaí, beleza?")
    nome = input("CFEFE: E então novato, como você gostaria de ser chamada(o)?\n")
    print("CHEFE: Muito bem", nome,", ontem a noite o rei Walter II foi enfeitiçado por uma bruxa. Na fuga, ela deixou cair um mapa com alguns lugares marcados.")
    print("CHEFE: Nosso departamento de inteligência acredita que nestes lugares exitem alguns itens que podem reverter o feitiço. E vocês são os selecionados para encontrar tais itens.")
    print("CHEFE: João, você precisa ir até o Castelo da Fera e a Casa da Vovó. E Maria, você irá até a Fábrica de Chocolates e a Fazenda do João De Pé de Feijões.")
    print("CHEFE: E você %s, precisará ajudar os dois agentes. Qual quer ajudar primeiro?" %(nome))
    while True:  # ESTRUTURA PADRÃO PARA AS INTERAÇÕES COM O JOGADOR
      acompanhante = int(input("DIGITE:\n     1 para JOÃO\n     2 para MARIA\n"))
      if acompanhante == 1 or acompanhante == 2:
        break;


    if acompanhante == 1:
      print("\n\nJOÃO: É isso aí! Vamos salvar o velho!")
      print("CHEFE: Olha como se porta garoto! Vocês vão precisar disso aqui:")
      print("<João e Maria recebem uma pequena bolsa cada um.>")
      print("CHEFE: Infelizmente estamos passando por alguns cortes de verba e não temos muito a oferecer além desta pequena bolsa.")
      print("CHEFE: Nosso departamento de invação tecnológica nos disse que só é possível guardar no máximo 5 itens aí dentro, independente do tamanho deles.")
      print("JOÃO: Só 5? É suficiente?")
      print("CHEFE: Vocês pegarão um item em cada destino da missão, além, é claro, das coisas que encontrarem no caminho.")
      print("MARIA: E se quisermos carregar mais de um item?")
      print("CHEFE: Vocês não poderão. Se quiserem adicionar mais alguma coisa e já tiverem 5 itens, terão de jogar um deles fora.")
      print("CHEFE: Agora atenção! É muito importante que escolham os ingredientes certos para a poção, caso contrário a missão será fracassada e mudaremos de estatégia.")
      print("JOÃO: Pode contar com a gente!")
      print("MARIA: Não vamos te decepcionar, senhor.")
      print("CHEFE: Muito bem, agora vão. Depois de pegar os ingredientes em cada destino vocês vão se encontrar na nossa unidade marinha onde os 7 irmãos estarão esperando.")
      print("MARIA: A unidade de Atlântida!? Nunca tivemos autorização para ir até lá!")
      print("CHEFE: Agora terão, os transportes serão providenciados para a viagem.")
      print("MARIA: Muito obrigado pela oportunidade senhor.")

      sleep(2)
      print("\n<Os três saem da base de operações e se diregem para a estrada principal que levará aos destinos>")
      print("MARIA: Pois bem %s, estarei esperando por você na entrada de Lond City, assim que vocês terminarem a sua parte você virá ao meu encontro. Boa sorte!" %(nome))
      print("JOÃO: Pra você também maninha!")
      print("<Maria segue pelo caminho da direita enquanto vocês vão rumo a Estrada Real para começar a missão>")


      gameover,bag_joao = campanha_joao(bag,gameover)

      if gameover == 1:
        print("\n\n\n\n\n     DESEJA JOGAR NOVAMENTE?")
        while True:
          resposta = int(input("\nDIGITE:\n     1 para SIM\n     2 para NÃO\n"))
          if resposta == 1 or resposta == 2:
            break;
        if resposta == 2:
          break;
      else:

        print("\nJOÃO: É isso %s, terminamos por aqui. Agora você vai por alí para encontrar minha irmã e eu vou esperar vocês nas margens do Mar da Calormânia." %(nome))
        print("<João continua pela estrada ao norte e você pega o caminho ao leste para continuar sua missão>")

        print("<Depois de algum tempo de vaigem você encontra Maria esperando em frente aos portões da cidade>")
        print("MARIA: Suponho que tudo tenha corrido bem, não é? Vamos entrar, temos muito há ser feito.")
        gameover, bag_maria = campanha_maria(bag, gameover)
        if gameover == 1:
          print("\n\n\n\n\n     DESEJA JOGAR NOVAMENTE?")
          while True:
            resposta = int(input("\nDIGITE:\n     1 para SIM\n     2 para NÃO\n"))
            if resposta == 1 or resposta == 2:
              break;
          if resposta == 2:
            break;

        else:
          print(f"\n\n\nMARIA: {nome} conseguimos completar a missão!!! Agora o mapa nos diz que devemos seguir por esta estrada até chegarmos no mar da Calormânia. João deve estar nos esperando.")
          sleep(2)
          print("\n\n", '-' * 30, "MAR DA CALORMÂNIA", '-' * 30)
          print("<Depois de mais algum tempo vocês encontram com João que está conversando com dois homens com roupas estranhas.>")
          print("<Vocês se aproximam deles e enxergam uma embarcação próxima à margem.>")
          print("JOÃO: Ei, vocês conseguiram! Estava cansado de esperar.")
          print("MARIA: Obrigada! Estamos muito felizes de conseguir. Aliás, quem são esse homens, João?")
          print("JOÃO: Esses são os atlantis que nos escoltarão até a base submarina.")
          print("MARIA: Suponho que vamos viajar com aquele submarino.")
          print("ATLANTI 1: É um prazer senhorita. Vamos adiante? Os 7 irmãos estão a sua espera.")


    if acompanhante == 2:
      print("\n\nMARIA: Obrigada! Sua ajuda será bem vinda!")
      print("CHEFE: Muito bem. Segurem isso.")
      print("<João e Maria recebem uma pequena bolsa cada um.>")
      print("CHEFE: Infelizmente estamos passando por alguns cortes de verba e não temos muito a oferecer além desta pequena bolsa.")
      print("CHEFE: Nosso departamento de invação tecnológica nos disse que só é possível guardar no máximo 5 itens aí dentro, independente do tamanho deles.")
      print("JOÃO: Só 5? É suficiente?")
      print("CHEFE: Vocês pegarão um item em cada destino da missão, além, é claro, das coisas que encontrarem no caminho.")
      print("MARIA: E se quisermos carregar mais de um item?")
      print("CHEFE: Vocês não poderão. Se quiserem adicionar mais alguma coisa e já tiverem 5 itens, terão de jogar um deles fora.")
      print("CHEFE: Agora atenção! É muito importante que escolham os ingredientes certos para a poção, caso contrário a missão será fracassada e mudaremos de estatégia.")
      print("JOÃO: Pode contar com a gente!")
      print("MARIA: Não vamos te decepcionar, senhor.")
      print("CHEFE: Muito bem, agora vão. Depois de pegar os ingredientes em cada destino vocês vão se encontrar na nossa unidade marinha onde os 7 irmãos estarão esperando.")
      print("MARIA: A unidade de Atlântida!? Nunca tivemos autorização para ir até lá!")
      print("CHEFE: Agora terão, os transportes serão providenciados para a viagem.")
      print("MARIA: Muito obrigado pela oportunidade senhor.")

      sleep(2)
      print("\n<Os três saem da base de operações e se diregem para a estrada principal que levará aos destinos>")
      print("JOÃO: Então eu vou esperar por você na Estrada Real %s. Quando terminarem você me encontrará lá. Boa sorte pra vocês" %(nome))
      print("MARIA: Obrigada!")
      print("<João segue pelo caminho da Estrada Real e vocês pegam o caminho da direita em direção a Lond City>")

      gameover, bag_maria = campanha_maria(bag, gameover)
      if gameover == 1:
        print("\n\n\n\n\n     DESEJA JOGAR NOVAMENTE?")
        while True:
          resposta = int(input("\nDIGITE:\n     1 para SIM\n     2 para NÃO\n"))
          if resposta == 1 or resposta == 2:
            break;
        if resposta == 2:
          break;
        #comenterio intermediário
      else:

        print("\nMARIA: Conseguimos %s! Muito obrigada pela ajuda!" % (nome))
        print("MARIA: Agora, por favor, você precisa ir por esse caminho e ajudar meu irmão. Eu vou esperar vocês na margem do Mar da Calormânia, até mais!")
        print("<Maria segue pela estrada ao norte e você pega o caminho para oeste, onde continuará sua missão.>")
        print("<Depois de algum tempo de vaigem você encontra João sentado em um tronco de árvore na beirada da estrada.>")
        print("JOÃO: Ainda bem que você chegou, não aguentava mais esperar! E então vamos adiante?")



        gameover,bag_joao = campanha_joao(bag,gameover)

        if gameover == 1:
          print("\n\n\n\n\n     DESEJA JOGAR NOVAMENTE?")
          while True:
            resposta = int(input("\nDIGITE:\n     1 para SIM\n     2 para NÃO\n"))
            if resposta == 1 or resposta == 2:
              break;
          if resposta == 2:
            break;

        else:
          print(f"\n\n\nJOÂO: {nome} terminamos!!! O mapa nos diz que devemos seguir por esta estrada até chegarmos no mar da Calormânia. Maria deve estar nos esperando.")
          print("<Depois de mais algum tempo vocês encontram com Maria conversando com dois homens com roupas estranhas.>")
          sleep(2)
          print("\n\n", '-' * 30, "MAR DA CALORMÂNIA", '-' * 30)
          print("<Vocês se aproximam deles e enxergam uma embarcação próxima à margem.>")
          print("MARIA: Vocês conseguiram! Parabéns! Já estava começando a ficar preocupada.")
          print("JOÃO: Obrigado maninha! Estamos muito felizes de conseguir. Aliás, quem são esse homens?")
          print("MARIA: Esses são os atlantis que nos escoltarão até a base submarina.")
          print("JOÃO: Suponho que vamos viajar com aquele submarino.")
          print("ATLANTI 1: Muito prazer, eu sou o piloto do submarino, vamos adiante? Os 7 irmãos estão a sua espera.")













    if gameover == 0:

      print("\n\n<A embarcação emerge das águas e vocês vão até ela por um bote.>")
      print("JOÃO: Cara! Essa parece aquela nave do Han Solo! Qual o nome mesmo?")
      print("MARIA: A Millennium Falcon? Parece mesmo!")
      print("<Vocês entram no submarino e partem rumo a Atlântida.>")
      sleep(2)
      print("\n\n", '-' * 30, "ATLÂNTIDA", '-' * 30)
      print("\n<Ao aproximar da cidade vocês passam por várias estátuas>")
      print("JOÃO: Ei %s, quem você acha que é essa figura?" % (nome))
      while True:
        resposta = int(input("\nDIGITE:\n     1 para Pequena Sereia \n     2 para Poseidon  \n     3 para Bob Esponja \n     4 para Aquaman\n"))
        if resposta == 4:
          break;
        else:
          print("JOÃO: Hmm, acho que não. Tente de novo.")

      print("\nATLANTI 2: Essas são as figuras dos nossos antigos reis. Este aí é o nosso rei regente Arthur.")
      print("<Alguns instantes depois vocês chegam até a base da AUAM e entram pelo portão principal.>")
      sleep(2)
      print("\n\n", '-' * 30, "BASE SUBMARINA DA AUAM", '-' * 30)
      print("ATLANTI 1: Bem vindos à base submarina da AUAM. Os 7 irmãos esperam na sala que está no final daquele corredor.")
      print("<Vocês seguem o caminho indicado e entram em uma cozinha onde sete pequenos homens estão ao redor de uma mesa redonda.>")
      print("MARIA: Com licença, vocês são os sete irmãos?")
      print("ANÃO MESTRE: AH SIM! VOCÊS CHEGARAM! Venham estávamos esperando!")
      print("ANÃO ZANGADO: Trouxeram os ingredientes?")
      print("JOÃO: Trouxemos sim, mas não sabemos se estes são os ingredientes corretos.")
      print("MESTRE: É isso que vamos descobrir, venha coloque-os em cima da mesa.")
      print("MARIA: %s, você trouxe a minha bolsa, não é? Pode colocar os itens na mesa, por favor.\n\n" % (nome))
      sleep(3)
      for i in range(len(bag_maria)):
        if bag_maria[i] != '':
          sleep(1)
          print("     ", bag_maria[i])
      sleep(3)
      print("\n\nJOÃO: Já pode colocar os meus também!\n\n")
      sleep(3)
      for i in range(len(bag_joao)):
        if bag_joao[i] != '':
          sleep(1)
          print("     ", bag_joao[i])
      sleep(3)
      cont = 0
      for i in bag_joao:
        if i == 'cenoura' or i == 'açucar':
          cont += 1
      for i in bag_maria:
        if i == 'chocolate' or i == 'ovos de ouro':
          cont += 1

      if cont == 4:

        print("\n\nMESTRE: Excelente! Agora precisamos ver se eles são os ingredientes corretos.")
        print("MESTRE: O que vocês acham que pode ser feito com estes ingredientes aqui?")
        while True:
          resposta = int(input("\nDIGITE:\n     1 para Torta de Maça \n     2 para Cupcake \n     3 para Brigadeiro \n     4 para Coockies de Chocolate\n"))
          if resposta == 2:
            break;
          else:
            print("MESTRE: Hmm, acho que não. Tente de novo.")
        if resposta == 2:
          print("MESTRE: Sim! Acho que essa é a melhor receita! Vamos lá pessoal, mãos à obra.")

        print("<Os anões pegam os ingredientes e começam a misturá-los. Depois de algum tempo a receita é concluída.>")
        print("ZANGADO: Está feito, agora precisamos ver se funciona.")
        print("JOÃO: Como vamos fazer isso?")
        print("MESTRE: Vamos estregar ao rei e ver se funciona.")
        print("MARIA: Mas o rei está aqui?")
        print("ZANGADO: Enquanto vocês estavam buscando os ingredientes outra equipe foi enviada para resgatar o rei, ele está na sala ao lado aguardando por esta receita.")
        print("\n<Vocês pegam o Cupcake e levam até a sala ao lado onde encontram o rei sentado olhando para a parede.>")
        print("JOÃO: O que ele está fazendo?")
        print("MARIA: Ele está enfeitiçado, lembra?")
        print("JOÃO: Ah sim. Mas e agora? Quem vai dar o cupcake pra ele?")
        print("MARIA: O que me diz %s? Quer entregar a ele?" %(nome))
        while True:
          resposta = int(input("\nDIGITE:\n     1 para SIM\n     2 para NÃO\n"))
          if resposta == 1 or resposta == 2:
            break;
        if resposta == 1:
          print("\n\n<Você pega o cupcake e leva até o rei.>")
          print("<O rei come fórmula e de repente para.>")
          print("<Todos ficam apreensivos esperando por algo.>")
          print("JOÃO: Matamos ele?")
          print("MESTRE: Aguarde meu jovem. Espere mais um pouco.")
          sleep(7)
          print("\n\n\nREI: O que está acontecendo? Onde eu estou? Maria? João? O que fazem aqui?")
          print("MARIA: QUE ALEGIA!!! ELE ESTÁ DE VOLTA!!! O REINO ESTÁ SALVO!")
          print("<Todos comemoram pela conquista, saem de Atlântida e voltam com o rei para o Reino de Abracadabra.>")
          sleep(3)
          print("\n\n\n\n", '~' * 30, "DOIS DIAS DEPOIS, NO CASTELO DE ABRACADABRA", '~' * 30, "\n\n\n\n")
          print("<Vocês estão na varanda frontal do castelo onde o Rei está fazendo um pronunciamento para toda população.>")
          print("REI: Senhoras, senhores e fadas de todos os reinos. Estamos aqui hoje para celebrar mais uma vitória na história do nosso reino em que minha vida foi salva de um terrível feitiço que ameaçava a todos nós.")
          nome_maiusculo = nome.upper()
          print("REI: Tudo isso graças aos esforços de três pessoas muito corajosas. Por favor recebam com aplausos MARIA, JOÃO e %s" %(nome_maiusculo))

          print("\n\n\n\n\n        PARABÉNS! VOCÊ SALVOU O REI E TODO O REINO DE ABRACADABRA!")
          sleep(3)
          print("\n       FIM DE JOGO\n\n\n\n\n\n\n\n\n\nAna Beatriz Sousa Silveira\nJulia Helena Lemes dos Santos\nVinícius Turato de Moura")
        else:
          print("\n\n<Então Maria leva o cupcake até o rei.>")
          print("<O rei come fórmula e de repente para.>")
          print("<Todos ficam apreensivos esperando por algo.>")
          print("JOÃO: Matamos ele?")
          print("MESTRE: Aguarde meu jovem. Espere mais um pouco.")
          sleep(7)
          print("\n\n\nREI: O que está acontecendo? Onde eu estou? Maria? João? O que fazem aqui?")
          print("MARIA: QUE ALEGIA!!! ELE ESTÁ DE VOLTA!!! O REINO ESTÁ SALVO!")
          print("<Todos comemoram pela conquista, saem de Atlântida e voltam com o rei para o Reino de Abracadabra.>")
          print("\n\n\n\n\n<Dois dias depois.>\n\n\n\n\n")
          print("<Vocês estão na varanda frontal do castelo onde o Rei está fazendo um pronunciamento para toda população.>")
          print("REI: Senhoras, senhores e fadas de todos os reinos. Estamos aqui hoje para celebrar mais uma vitória na história do nosso reino em que minha vida foi salva de um terrível feitiço que ameaçava a todos nós.")
          nome_maiusculo = nome.upper()
          print("REI: Tudo isso graças aos esforços de três pessoas muito corajosas. Por favor recebam com aplausos MARIA, JOÃO e %s" % (
              nome_maiusculo))

          print("\n\n\n\n\n        PARABÉNS! VOCÊ SALVOU O REI E TODO O REINO DE ABRACADABRA!")
          sleep(3)
          print("\n       FIM DE JOGO\n\n\n\n\n\n\n\n\n\nAna Beatriz Sousa Silveira\nJulia Helena Lemes dos Santos\nVinícius Turato de Moura")
        break


      else:

        print("\n\nMESTRE: Excelente! Agora precisamos ver se eles são os ingredientes corretos.")
        print("MESTRE: O que vocês acham que pode ser feito com estes ingredientes aqui?")
        while True:
          resposta = int(input("\nDIGITE:\n     1 para Torta de Maçã \n     2 para Cupcake \n     3 para Brigadeiro \n     4 para Coockies de Chocolate\n"))
          if resposta == 2:
            break;
          else:
            print("MESTRE: Hmm, acho que não. Tente de novo.")

        if resposta == 2:
          print("MESTRE: Sim! Acho que essa é a melhor receita! Vamos lá pessoal, mãos à obra.")

        print("<Os anões pegam os ingredientes e começam a misturá-los. Depois de algum tempo a receita é concluída.>")
        print("ZANGADO: Está feito, agora precisamos ver se funciona.")
        print("JOÃO: Como vamos fazer isso?")
        print("MESTRE: Vamos estregar ao rei e ver se funciona.")
        print("MARIA: Mas o rei está aqui?")
        print("ZANGADO: Enquanto vocês estavam buscando os ingredientes outra equipe foi enviada para resgatar o rei, ele está na sala ao lado aguardando por esta receita.")
        print("\n<Vocês pegam o Cupcake e levam até a sala ao lado onde encontram o rei sentado olhando para a parede.>")
        print("JOÃO: O que ele está fazendo?")
        print("MARIA: Ele está enfeitiçado, lembra?")
        print("JOÃO: Ah sim. Mas e agora? Quem vai dar o cupcake pra ele?")
        print("MARIA: O que me diz %s? Quer entregar a ele?" % (nome))
        while True:
          resposta = int(input("\nDIGITE:\n     1 para SIM\n     2 para NÃO\n"))
          if resposta == 1 or resposta == 2:
            break;
        if resposta == 1:
          print("\n\n<Você pega o cupcake e leva até o rei.>")
          print("<O rei come fórmula e de repente para.>")
          print("<Todos ficam apreensivos esperando por algo.>")
          print("JOÃO: Matamos ele?")
          print("MESTRE: Aguarde meu jovem. Espere mais um pouco.")
          sleep(7)
          print("\n\n\n<Vocês esperam mais, porém o rei não esboça reação alguma.>")
          print("MESTRE: Essa não, a fórmula não funcionou. Não eram estes os ingredientes certos...")


        else:
          print("\n\n<Então Maria leva o cupcake até o rei.>")
          print("<O rei come fórmula e de repente para.>")
          print("<Todos ficam apreensivos esperando por algo.>")
          print("JOÃO: Matamos ele?")
          print("MESTRE: Aguarde meu jovem. Espere mais um pouco.")
          sleep(7)
          print("\n\n\n<Vocês esperam mais, porém o rei não esboça reação alguma.>")
          print("MESTRE: Essa não, a fórmula não funcionou. Não eram estes os ingredientes certos...")


        print("\n\n\n\n\n          Infelizmente você não encontrou os ingredientes corretos")
        print("\n\n          DESEJA JOGAR NOVAMENTE?")
        while True:
          resposta = int(input("\nDIGITE:\n     1 para SIM\n     2 para NÃO\n"))
          if resposta == 1 or resposta == 2:
            break;
        if resposta == 2:
          print("\n\n          FIM DE JOGO \n\n\n\n\n\n\n\n\n\nAna Beatriz Sousa Silveira\nJulia Helena Lemes dos Santos\nVinícius Turato de Moura")
          break
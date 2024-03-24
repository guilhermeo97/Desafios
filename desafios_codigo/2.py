#Desafio 
#Um supermercado está fazendo uma promoção de venda de refrigerantes. 
#Se um dia você comprar refrigerantes e levar os cascos vazios no dia seguinte, 
#ela troca cada conjunto de K garrafas vazias  por uma garrafa cheia. 
#Um cliente quer aproveitar ao máximo essa oferta e por isso comprou várias garrafas no primeiro dia da promoção. 
#Agora ele quer saber quantas garrafas terá ao final do segundo dia da promoção, se usá-la ao máximo.

#Entrada
#A primeira linha de entrada contém inteiro T (1 ≤ T ≤ 10000), que indica o número de casos de teste. 
#Em cada uma das T linhas a seguir vêm dois inteiros N e K (1 ≤ K, N ≤ 10000),
#respectivamente o número de refrigerantes comprados e o número de garrafas vazias para ganhar uma cheia.

#Saída
#Para cada caso de teste imprima o número de garrafas que o cliente terá no segundo dia, se aproveitar ao máximo a oferta.

# Resultado
# 3
# 7 4 = 4
# 4 7 = 4
# 4000 7 = 574

T = int(input())

for i in range(T):
  #receba a string com dígito referente a garrafas cheias e cascos(garrafas vazias)
  cheias_cascos = input()
  #execute a função split para separar os dígitos usando um espaço como separador
  cheias_cascos_split = cheias_cascos.split(" ")
  #declare uma variável para receber N 
  cheias = int(cheias_cascos_split[0])
  #declare uma variável para receber K 
  cascos = int(cheias_cascos_split[1])
  
  #divida N por K para saber o total de cheias que receberia pelos cascos retornados
  quantas_cheias_por_cascos = int(cheias / cascos)
  
  #multiplique o resultado acima por K (quantidade de cascos) definidas pela promoção
  quantas_cheias_aproveitadas = quantas_cheias_por_cascos * cascos
  
  #subtraia N (total de cheias) pelo resultado acima para saber quantas garrafas cheias não seriam aproveitadas
  quantas_cheias_não_aproveitadas = cheias - quantas_cheias_aproveitadas
  
  #soma o total não aproveitado (resultado acima) com o resultado da linha 20 
  #para saber quantas garrafas deve comprar a mais para aproveitar ao máximo a promoção
  quantas_cheias_para_maximizar = quantas_cheias_não_aproveitadas + quantas_cheias_por_cascos
  
  #imprima o resultado
  print(quantas_cheias_para_maximizar )
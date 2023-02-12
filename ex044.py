total = float(input('Qual o preço total das compras? R$'))
opcao = int(input('Qual a forma de pagamento desejada?\n[ 1 ] À vista dinheiro/cheque \n[ 2 ] À vista no cartão \n[ 3 ] Em até 2x no cartão \n[ 4 ] 3x ou mais no cartão \n Sua opção: '))

if opcao == 1:
    desconto = total * 0.10
    print('O preço total da compra sairá de R${:.2f} para R${:.2f}'.format(total, total - desconto))
elif opcao == 2:
    desconto = total * 0.05
    print('O preço total da compra sairá de R${:.2f} para R${:.2f}'.format(total, total - desconto))
elif opcao == 3:
    print('O preço total da compra será de R${:.2f}'.format(total))
elif opcao == 4:
    juros = total * 0.20
    print('O preço total da compra sairá de R${:.2f} para R${:.2f}'.format(total, total + juros))
else:
    print('A opção invalida')
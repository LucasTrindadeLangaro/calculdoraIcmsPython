'''VERSAO 1.2'''

aliquotas = {
    "AC": 19.0,"AL": 19.0,"AP": 18.0,"AM": 20.0,"BA": 20.5,"CE": 20.0,"DF": 20.0,"ES": 17.0,"GO": 19.0,"MA": 22.0,"MG": 18.0,"MS": 17.0,"MT": 17.0,"PA": 19.0,
    "PB": 20.0,"PE": 20.5,"PI": 21.0,"PR": 19.5,"RJ": 20.0,"RN": 18.0,"RS": 17.0,"RO": 19.5,"RR": 20.0,"SC": 17.0,"SE": 19.0,"SP": 18.0,"TO": 20.0
}
#---------------------------------- Inicio Validação Valor Produto----------------------------------------------#
vlr_produto = input('Digite o valor do produto (já com frete, seguro e outras despesas Inclusas): ')

while True:
    if vlr_produto.strip() == "":
        vlr_produto = input("Digite um valor válido: ")
        continue

    try:
        vlr_produto = float(vlr_produto) 
        break  # sai do while se a conversão deu certo
    except ValueError:
        vlr_produto = input("Digite um valor válido: ")
#---------------------------------- Fim Validação Valor Produto----------------------------------------------#

#---------------------------------- Inicio Validação tipo do icms ------------------------------------------#
tip_icms = input('Digite o tipo de ICMS (normal ou st): ').lower()

while True:
    if tip_icms != 'normal' and tip_icms != 'st':
        tip_icms = input(f'{tip_icms} não é valido! digite "NORMAL" ou "ST": ').lower()
    else:
        break
#---------------------------------- Fim Validação tipo do icms ------------------------------------------#        



#-------------------------------------------Inicia bloco dos calculos----------------------------------------------#



#---------------------------------Calculo do Icms "Normal"-----------------------------------------------#
'''no momento vai ser só para operações estaduais'''
if tip_icms == "normal":
    aliq_icms = input("digite o estado da operação (sigla): ").upper()
    while True:
        if aliq_icms == '':
            aliq_icms = input('por favor digite o seu estado: ').upper()
            continue
        elif aliq_icms in aliquotas:
            aliq_icms = aliquotas[aliq_icms]
            break
        else: 
            aliq_icms = input('Estado invalido! Digite novamente: ')
    '''while True:
        if aliq_icms == '':
            aliq_icms = input(f'aliquota não pode estar vazia! digite um valor valido: ')
            continue
        try:
            aliq_icms = float(aliq_icms)
            break
        except ValueError:
            aliq_icms = input(f'{aliq_icms} não é valido! digite um valor valido: ')'''
    calc_icms = (vlr_produto * (aliq_icms / 100))
    print(f'valor ICMS: {calc_icms}')

#---------------------------------Calculo do Icms ST-----------------------------------------------------#
elif tip_icms == "st":
    tip_operacao = input("é uma operação estadual (e) ou interestadual (i)? ").lower()[0]
    
    '''while True:
        if tip_operacao == '' and tip_operacao != 'e' and tip_operacao != 'i':
            tip_operacao = input('digite o tipo de operação: ')y'''
    #-----------------------------Calculo Op Int----------------------------------------#
    if tip_operacao == 'e':
        aliq_icms = float(input('Digite o estado: '))
        while True:
            if aliq_icms == '':
                aliq_icms = input('por favor digite o seu estado: ').upper()
                continue
            elif aliq_icms in aliquotas:
                aliq_icms = aliquotas[aliq_icms]
                break
            else: 
                aliq_icms = input('Estado invalido! Digite novamente: ')
        #mva = int(input("Digite o valor do MVA: "))
        print('MVA = 40%')
        base_calculo = (vlr_produto * (1+0.40))
        icms_pres = base_calculo * (aliq_icms/100)
        icms_prop = vlr_produto * (aliq_icms/100)
        icms_st = icms_pres - icms_prop
        print('=============================================================================================')
        print(f'           valor total dos produtos: {vlr_produto}\n'
              f'           valor do icms: {icms_pres}\n'
              f'           valor da st: {icms_st}\n'
              f'           valor total da nota: {vlr_produto+icms_st}')
        print('=============================================================================================')
    #-----------------------------Calculo Op Int----------------------------------------#
    elif tip_operacao == 'i':
        aliq_interna = input('Digite o estado de destino: ')
        while True:
            if aliq_interna == '':
                aliq_interna = input('por favor digite o seu estado: ').upper()
                continue
            elif aliq_interna in aliquotas:
                aliq_interna = aliquotas[aliq_interna]
                break
            else: 
                aliq_interna = input('Estado invalido! Digite novamente: ')
                
        aliq_interestadual = float(input('Digite a aliquota do estado de origem: '))
        while True:
            if aliq_interestadual == '':
                aliq_interestadual = input(f'aliquota não pode estar vazia! digite um valor valido: ')
                continue
            try:
                aliq_interestadual = float(aliq_interestadual)
                break
            except ValueError:
                aliq_interestadual = input(f'{aliq_interestadual} não é valido! digite um valor valido: ')
        mva = int(input("Digite o valor do MVA: "))
        base_calculo = (vlr_produto * (1+(mva/100)))
        icms_pres = base_calculo * (aliq_interna/100)
        icms_prop = vlr_produto * (aliq_interestadual/100)
        icms_st = icms_pres - icms_prop
        print('=============================================================================================')
        print(f'           valor total dos produtos: {vlr_produto}\n'
              f'           valor do icms: {icms_pres}\n'
              f'           valor da st: {icms_st}\n'
              f'           valor total da nota: {vlr_produto+icms_st}')
        print('=============================================================================================')
    else:
        print(f'{tip_operacao} não é um comando valido, por favor digite "e" para estadual ou "i" interestadual. Progama encerrado...')
else:
    print(f'{tip_icms} não é um comando valido! digite "normal" para icms própio ou digite "st" para substituição Tributária. Programa encerrado...')


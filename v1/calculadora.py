'''esse programa escrito em python tem como objetivo fazer uma calculadora para calculo de ICMS.
isso significa que tera que calcular DIFAL, ICMS, ICMS ST, e todos os impostos decorrentes do icms.'''

#---------------------------------------------------------------------------------------------------------#
vlr_produto = float(input('Digite o valor do produto (já com frete, seguro e outras despesas Inclusas: )'))
tip_icms = input('Digite o tipo de ICMS (normal ou st): ').lower()
#---------------------------------------------------------------------------------------------------------#

#---------------------------------Inicia bloco dos calculos----------------------------------------------#

#---------------------------------Calculo do Icms "Normal"-----------------------------------------------#
if tip_icms == "normal":
    aliq_icms = float(input('Digite a alíquota do ICMS (%): '))
    calc_icms = (vlr_produto * (aliq_icms / 100))
    print(calc_icms)
#---------------------------------Calculo do Icms ST-----------------------------------------------------#
elif tip_icms == "st":
    tip_operacao = input("é uma operação estadual (e) ou interestadual (i)? ").lower()[0]
    #-----------------------------Calculo Op Int----------------------------------------#
    if tip_operacao == 'e':
        aliq_icms = float(input('Digite a alíquota do icms: '))
        mva = int(input("Digite o valor do MVA: "))
        base_calculo = (vlr_produto * (1+(mva/100)))
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
        aliq_interna = float(input('Digite a alíquota do estado de destino: '))
        aliq_interestadual = float(input('Digite a aliquota do estado de origem: '))
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


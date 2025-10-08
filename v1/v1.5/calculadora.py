'''VERSAO 1.5'''
aliquotas = {
    "AC": 19.0,"AL": 19.0,"AP": 18.0,"AM": 20.0,"BA": 20.5,"CE": 20.0,"DF": 20.0,"ES": 17.0,"GO": 19.0,"MA": 22.0,"MG": 18.0,"MS": 17.0,"MT": 17.0,"PA": 19.0,
    "PB": 20.0,"PE": 20.5,"PI": 21.0,"PR": 19.5,"RJ": 20.0,"RN": 18.0,"RS": 17.0,"RO": 19.5,"RR": 20.0,"SC": 17.0,"SE": 19.0,"SP": 18.0,"TO": 20.0
}

def Separador():
    print('=============================================================================================')

def CalculaIcms():
    aliq_icms = input("digite o estado da operação (sigla): ").upper()
    
    while True:
        if aliq_icms == '':
            aliq_icms = input('por favor digite o seu estado: ').upper()
            continue
        elif aliq_icms in aliquotas:
            aliq_icms = aliquotas[aliq_icms]
            break
        else: 
            aliq_icms = input('Estado invalido! Digite novamente: ').upper()
    calc_icms = (vlr_produto * (aliq_icms / 100))
    return  aliq_icms, calc_icms

mva = 40
#---------------------------------- Inicio Validação Valor Produto----------------------------------------------#

while True:
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

    #---------------------------------- Inicio Validação tipo do icms ------------------------------------------#
    tip_icms = input('Digite o tipo de ICMS (normal ou st): ').lower()

    while tip_icms != 'normal' and tip_icms != 'st':
        tip_icms = input(f'{tip_icms} não é valido! digite "NORMAL" ou "ST": ').lower()      

    #---------------------------------Calculo do Icms "Normal"-----------------------------------------------#
    '''no momento vai ser só para operações estaduais'''
    if tip_icms == "normal":
        aliq_icms, resultado = CalculaIcms()
        print(f'Base ICMS: {vlr_produto}\n'
            f'Aliquota ICMS: {aliq_icms}\n'
            f'valor ICMS: {resultado}\n')

    #---------------------------------Calculo do Icms ST-----------------------------------------------------#
    elif tip_icms == "st":

        tip_operacao = input("é uma operação estadual (e) ou interestadual (i)? ").lower()
        
        while tip_operacao not in ['e','i']:
            tip_operacao = input('digite o tipo de operação: ')
        #-----------------------------Calculo Op Int----------------------------------------#
        match tip_operacao:
            case 'e':
                aliq_icms, calcIcms_prop = CalculaIcms() #aliq_imcs = aliquota informada na func....CalcIcms_Prop = calculo do ICMS normal
                base_calculo = (vlr_produto * (1+(mva/100)))
                icms_pres = base_calculo * (aliq_icms/100)
                icms_st = icms_pres - calcIcms_prop
                Separador()
                print(
                    f'           valor total dos produtos: {vlr_produto}\n'
                    f'           Aliquota do ICMS: {aliq_icms}\n'
                    f'           valor do icms: {calcIcms_prop}\n'
                    f'           valor da st: {icms_st}\n'
                    f'           valor total da nota: {vlr_produto+icms_st}')
                Separador()
        #-----------------------------Calculo Op Int----------------------------------------#:
            case 'i':
                aliq_icms, icms_prop = CalculaIcms()
                while True:
                    aliq_interestadual = (input('Digite a aliquota do estado de origem: ')).strip()
                    if aliq_interestadual.strip() == '':
                        print(f'aliquota não pode estar vazia!')
                        continue
                    try:
                        aliq_interestadual = float(aliq_interestadual)
                        break
                    except ValueError:
                        print(f'{aliq_interestadual} não é valido! digite um valor valido: ')
                base_calculo = (vlr_produto * (1+(mva/100)))
                icms_pres = base_calculo * (aliq_icms/100)
                icms_prop = vlr_produto * (aliq_interestadual/100)
                icms_st = icms_pres - icms_prop
                Separador()
                print(f'         valor total dos produtos: {vlr_produto}\n'
                    f'           valor do icms: {icms_pres}\n'
                    f'           valor da st: {icms_st}\n'
                    f'           valor total da nota: {vlr_produto+icms_st}')
                Separador()
            
    continua = input('deseja fazer novo calculo? [S] ou [N]: ').upper()
    while continua not in ['S', 'N']:
        continua = input('deseja fazer novo calculo? [S] ou [N]: ').upper()
    else:
        if continua != 'S':
            break

print('Programa encerrado!')

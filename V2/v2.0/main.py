from tkinter import *
from tkinter import ttk

aliquotas = {
    "AC": 19.0,"AL": 19.0,"AP": 18.0,"AM": 20.0,"BA": 20.5,"CE": 20.0,"DF": 20.0,"ES": 17.0,"GO": 19.0,"MA": 22.0,"MG": 18.0,"MS": 17.0,"MT": 17.0,"PA": 19.0,
    "PB": 20.0,"PE": 20.5,"PI": 21.0,"PR": 19.5,"RJ": 20.0,"RN": 18.0,"RS": 17.0,"RO": 19.5,"RR": 20.0,"SC": 17.0,"SE": 19.0,"SP": 18.0,"TO": 20.0
}


def CalculaIcms():
    
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

def SelecionaEstado():
    boxUF = ttk.Combobox(root, values=list(aliquotas.keys()))
    boxUF.grid()
root = Tk()

root.title('Calculadora de ICMS')
s = ttk.Style()
telaPeincipal = ttk.Frame(root, width=2000, height=200) #cria a tela Left, Top, Right, Bottom

LabelVlrProd = ttk.Label(root, text='Digite o valor do produto (já com frete, seguro e outras despesas Inclusas): ')
LabelVlrProd.grid()

vlr_prod = ttk.Entry(root)
vlr_prod.grid()

SelecionaEstado()


button = ttk.Button(root,text='teste')
button.grid()


root.mainloop()
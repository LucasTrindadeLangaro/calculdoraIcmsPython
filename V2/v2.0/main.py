from tkinter import *
from tkinter import ttk
from tkinter import messagebox

aliquotas = {
    "AC": 19.0,"AL": 19.0,"AP": 18.0,"AM": 20.0,"BA": 20.5,"CE": 20.0,"DF": 20.0,"ES": 17.0,"GO": 19.0,"MA": 22.0,"MG": 18.0,"MS": 17.0,"MT": 17.0,"PA": 19.0,
    "PB": 20.0,"PE": 20.5,"PI": 21.0,"PR": 19.5,"RJ": 20.0,"RN": 18.0,"RS": 17.0,"RO": 19.5,"RR": 20.0,"SC": 17.0,"SE": 19.0,"SP": 18.0,"TO": 20.0
}

root = Tk()
root.title('Calculadora de ICMS')
root.geometry('500x350')
root.configure(bg='#f0f0f0')
root.resizable(False, False)

# Frame principal com padding
frame_principal = Frame(root, bg='#f0f0f0')
frame_principal.pack(expand=True, fill=BOTH, padx=30, pady=30)

# Título
titulo = Label(frame_principal, text='Calculadora de ICMS', 
               font=('Arial', 20, 'bold'), bg='#f0f0f0', fg='#2c3e50')
titulo.pack(pady=(0, 30))

# Subtítulo
subtitulo = Label(frame_principal, text='Selecione o tipo de cálculo:', 
                  font=('Arial', 12), bg='#f0f0f0', fg='#34495e')
subtitulo.pack(pady=(0, 20))

# Frame para os radio buttons
frame_opcoes = Frame(frame_principal, bg='#f0f0f0')
frame_opcoes.pack(pady=10)

opcao = StringVar(value='normal')

# Radio buttons com estilo melhorado
rb1 = Radiobutton(frame_opcoes, text='ICMS Normal', variable=opcao, value='normal',
                  font=('Arial', 11), bg='#f0f0f0', fg='#2c3e50', 
                  selectcolor='#3498db', activebackground='#f0f0f0',
                  padx=20, pady=10)
rb1.pack(anchor='w', pady=5)

rb2 = Radiobutton(frame_opcoes, text='ICMS ST (Substituição Tributária)', variable=opcao, value='ST',
                  font=('Arial', 11), bg='#f0f0f0', fg='#2c3e50',
                  selectcolor='#3498db', activebackground='#f0f0f0',
                  padx=20, pady=10)
rb2.pack(anchor='w', pady=5)

def EscolheTipoCalculo():
    print("o usuario escolheu: ", opcao.get())
    
    nova_janela = Toplevel(root)
    nova_janela.geometry('600x500')
    nova_janela.configure(bg='#f0f0f0')
    nova_janela.resizable(False, False)
    
    if opcao.get() == "normal":
        print("normal")
        
        nova_janela.title('Cálculo ICMS Normal')
        
        # Frame principal da nova janela
        frame_calc = Frame(nova_janela, bg='#f0f0f0')
        frame_calc.pack(expand=True, fill=BOTH, padx=40, pady=30)
        
        # Título
        Label(frame_calc, text='Cálculo de ICMS Normal', 
              font=('Arial', 16, 'bold'), bg='#f0f0f0', fg='#2c3e50').pack(pady=(0, 25))
        
        # Valor do produto
        Label(frame_calc, text='Valor do Produto (R$):', 
              font=('Arial', 11), bg='#f0f0f0', fg='#34495e').pack(anchor='w', pady=(0, 5))
        entry_vlr_prod = Entry(frame_calc, font=('Arial', 11), width=40, relief=SOLID, bd=1)
        entry_vlr_prod.pack(pady=(0, 20))
        entry_vlr_prod.focus()
        
        # UF
        Label(frame_calc, text='Selecione a UF:', 
              font=('Arial', 11), bg='#f0f0f0', fg='#34495e').pack(anchor='w', pady=(0, 5))
        boxUF = ttk.Combobox(frame_calc, values=list(aliquotas.keys()), 
                             font=('Arial', 11), width=38, state='readonly')
        boxUF.pack(pady=(0, 25))
        
        # Frame para resultado
        frame_resultado = Frame(frame_calc, bg='white', relief=SOLID, bd=1)
        frame_resultado.pack(fill=BOTH, expand=True, pady=(0, 20))
        
        resultado = StringVar()
        label_resultado = Label(frame_resultado, textvariable=resultado, justify=LEFT,
                               font=('Arial', 10), bg='white', fg='#2c3e50', padx=15, pady=15)
        label_resultado.pack(fill=BOTH, expand=True)
        
        def calcula():
            try:
                if not boxUF.get():
                    messagebox.showwarning("Atenção", "Selecione uma UF!")
                    return
                    
                aliq_sel = boxUF.get()
                aliq_icms = aliquotas[aliq_sel]
                vlr_prod = float(entry_vlr_prod.get().replace(',', '.'))
                
                calc = vlr_prod * (aliq_icms/100)
                
                resultado.set(f'Valor do Produto: R$ {vlr_prod:.2f}\n\n'
                              f'Alíquota do Estado {boxUF.get()}: {aliq_icms}%\n\n'
                              f'Valor do ICMS: R$ {calc:.2f}')
                print('valor: ', vlr_prod)
                print('aliq: ', aliq_icms)
                print('vlr icms: ', calc)
            except ValueError:
                messagebox.showerror("Erro", "Digite um valor numérico válido!")
        
        # Botão calcular
        botao_calcula = Button(frame_calc, text='Calcular ICMS', command=calcula,
                              font=('Arial', 11, 'bold'), bg='#27ae60', fg='white',
                              padx=30, pady=10, relief=FLAT, cursor='hand2')
        botao_calcula.pack()
        
    else:
        nova_janela.title("Cálculo ICMS ST")
        nova_janela.geometry('650x600')
        
        # Frame principal
        frame_st = Frame(nova_janela, bg='#f0f0f0')
        frame_st.pack(expand=True, fill=BOTH, padx=30, pady=20)
        
        # Título
        Label(frame_st, text='Cálculo de ICMS ST', 
              font=('Arial', 16, 'bold'), bg='#f0f0f0', fg='#2c3e50').pack(pady=(0, 20))
        
        tipoSt = StringVar(value=" ")
        
        # Frame para radio buttons ST
        frame_tipo_st = Frame(frame_st, bg='#f0f0f0')
        frame_tipo_st.pack(pady=(0, 15))
        
        Label(frame_tipo_st, text="Tipo de operação:", 
              font=('Arial', 11, 'bold'), bg='#f0f0f0', fg='#34495e').pack(anchor="w", pady=(0, 10))
        
        tipoSt_rb1 = Radiobutton(frame_tipo_st, text='Estadual (mesma UF)', variable=tipoSt, value='E',
                                font=('Arial', 10), bg='#f0f0f0', selectcolor='#e74c3c',
                                activebackground='#f0f0f0', padx=10)
        tipoSt_rb2 = Radiobutton(frame_tipo_st, text='Interestadual (UF diferentes)', variable=tipoSt, value='I',
                                font=('Arial', 10), bg='#f0f0f0', selectcolor='#e74c3c',
                                activebackground='#f0f0f0', padx=10)
        tipoSt_rb1.pack(anchor="w", pady=3)
        tipoSt_rb2.pack(anchor="w", pady=3)
        
        # Linha separadora
        ttk.Separator(frame_st, orient='horizontal').pack(fill='x', pady=15)
        
        # Frame para os campos dinâmicos
        frameCampos = Frame(frame_st, bg='#f0f0f0')
        frameCampos.pack(fill=BOTH, expand=True)
        
        def EscolhaSt():
            # Limpa os widgets anteriores
            for widget in frameCampos.winfo_children():
                widget.destroy()
            
            if tipoSt.get() == 'E':
                print('estadual')
                
                # Campos para cálculo estadual
                Label(frameCampos, text='Valor do Produto (R$):', 
                      font=('Arial', 10), bg='#f0f0f0', fg='#34495e').pack(anchor="w", pady=(0, 3))
                entry_vlrProd = Entry(frameCampos, font=('Arial', 10), width=45, relief=SOLID, bd=1)
                entry_vlrProd.pack(pady=(0, 12))
                entry_vlrProd.focus()
                
                Label(frameCampos, text='Selecione a UF:', 
                      font=('Arial', 10), bg='#f0f0f0', fg='#34495e').pack(anchor="w", pady=(0, 3))
                cb_escolha_Uf = ttk.Combobox(frameCampos, values=list(aliquotas.keys()), 
                                             font=('Arial', 10), width=43, state='readonly')
                cb_escolha_Uf.pack(pady=(0, 12))
                
                Label(frameCampos, text='MVA - Margem de Valor Agregado (%):', 
                      font=('Arial', 10), bg='#f0f0f0', fg='#34495e').pack(anchor="w", pady=(0, 3))
                entry_mva = Entry(frameCampos, font=('Arial', 10), width=45, relief=SOLID, bd=1)
                entry_mva.pack(pady=(0, 15))
                
                # Frame para resultado
                frame_resultado_st = Frame(frameCampos, bg='white', relief=SOLID, bd=1)
                frame_resultado_st.pack(fill=BOTH, expand=True, pady=(0, 12))
                
                resultado_st = StringVar()
                label_resultado_st = Label(frame_resultado_st, textvariable=resultado_st, justify=LEFT,
                                          font=('Arial', 9), bg='white', fg='#2c3e50', padx=12, pady=10)
                label_resultado_st.pack(fill=BOTH, expand=True)
                
                def calcular_st_estadual():
                    try:
                        if not cb_escolha_Uf.get():
                            messagebox.showwarning("Atenção", "Selecione uma UF!")
                            return
                        
                        vlr_prod = float(entry_vlrProd.get().replace(',', '.'))
                        aliquotaUF = cb_escolha_Uf.get()
                        aliq_icms = aliquotas[aliquotaUF]
                        mva = float(entry_mva.get().replace(',', '.'))
                        
                        # Cálculo ICMS ST Estadual
                        base_calculo_st = vlr_prod * (1 + mva/100)
                        icms_st = (base_calculo_st * aliq_icms/100) - (vlr_prod * aliq_icms/100)
                        
                        resultado_st.set(
                            f'Valor do Produto: R$ {vlr_prod:.2f}\n'
                            f'MVA: {mva}%\n'
                            f'Base de Cálculo ST: R$ {base_calculo_st:.2f}\n'
                            f'Alíquota {aliquotaUF}: {aliq_icms}%\n'
                            f'ICMS ST: R$ {icms_st:.2f}\n'
                            f'Valor Total (Produto + ICMS ST): R$ {vlr_prod + icms_st:.2f}'
                        )
                        
                        print(f"Valor: {vlr_prod}, Alíquota: {aliq_icms}, ICMS ST: {icms_st}")
                        
                    except ValueError:
                        messagebox.showerror("Erro", "Digite valores numéricos válidos!")
                
                Button(frameCampos, text='Calcular ICMS ST', command=calcular_st_estadual,
                      font=('Arial', 10, 'bold'), bg='#e74c3c', fg='white',
                      padx=25, pady=8, relief=FLAT, cursor='hand2').pack()
                
            elif tipoSt.get() == 'I':
                print('interestadual')
                
                # Campos para cálculo interestadual
                Label(frameCampos, text='Valor do Produto (R$):', 
                      font=('Arial', 10), bg='#f0f0f0', fg='#34495e').pack(anchor="w", pady=(0, 3))
                entry_vlrProd = Entry(frameCampos, font=('Arial', 10), width=45, relief=SOLID, bd=1)
                entry_vlrProd.pack(pady=(0, 12))
                entry_vlrProd.focus()
                
                Label(frameCampos, text='UF de Origem:', 
                      font=('Arial', 10), bg='#f0f0f0', fg='#34495e').pack(anchor="w", pady=(0, 3))
                cb_uf_origem = ttk.Combobox(frameCampos, values=list(aliquotas.keys()), 
                                           font=('Arial', 10), width=43, state='readonly')
                cb_uf_origem.pack(pady=(0, 12))
                
                Label(frameCampos, text='UF de Destino:', 
                      font=('Arial', 10), bg='#f0f0f0', fg='#34495e').pack(anchor="w", pady=(0, 3))
                cb_uf_destino = ttk.Combobox(frameCampos, values=list(aliquotas.keys()), 
                                            font=('Arial', 10), width=43, state='readonly')
                cb_uf_destino.pack(pady=(0, 12))
                
                Label(frameCampos, text='MVA - Margem de Valor Agregado (%):', 
                      font=('Arial', 10), bg='#f0f0f0', fg='#34495e').pack(anchor="w", pady=(0, 3))
                entry_mva = Entry(frameCampos, font=('Arial', 10), width=45, relief=SOLID, bd=1)
                entry_mva.pack(pady=(0, 15))
                
                # Frame para resultado
                frame_resultado_st = Frame(frameCampos, bg='white', relief=SOLID, bd=1)
                frame_resultado_st.pack(fill=BOTH, expand=True, pady=(0, 12))
                
                resultado_st = StringVar()
                label_resultado_st = Label(frame_resultado_st, textvariable=resultado_st, justify=LEFT,
                                          font=('Arial', 9), bg='white', fg='#2c3e50', padx=12, pady=10)
                label_resultado_st.pack(fill=BOTH, expand=True)
                
                def calcular_st_interestadual():
                    try:
                        if not cb_uf_origem.get() or not cb_uf_destino.get():
                            messagebox.showwarning("Atenção", "Selecione as UFs de origem e destino!")
                            return
                        
                        vlr_prod = float(entry_vlrProd.get().replace(',', '.'))
                        uf_origem = cb_uf_origem.get()
                        uf_destino = cb_uf_destino.get()
                        aliq_origem = aliquotas[uf_origem]
                        aliq_destino = aliquotas[uf_destino]
                        mva = float(entry_mva.get().replace(',', '.'))
                        
                        # Alíquota interestadual (simplificado - normalmente é 4%, 7% ou 12%)
                        aliq_interestadual = 12.0
                        #aqui eu preciso aplicar a regra das regiões. posso criar um IF direto ou criar um excel
                        
                        # Cálculo ICMS ST Interestadual
                        icms_origem = vlr_prod * (aliq_interestadual/100)
                        base_calculo_st = vlr_prod * (1 + mva/100)
                        icms_destino = base_calculo_st * (aliq_destino/100)
                        icms_st = icms_destino - icms_origem
                        
                        resultado_st.set(
                            f'Valor do Produto: R$ {vlr_prod:.2f}\n'
                            f'UF Origem: {uf_origem} (Alíquota: {aliq_origem}%)\n'
                            f'UF Destino: {uf_destino} (Alíquota: {aliq_destino}%)\n'
                            f'Alíquota Interestadual: {aliq_interestadual}%\n'
                            f'MVA: {mva}%\n'
                            f'Base de Cálculo ST: R$ {base_calculo_st:.2f}\n'
                            f'ICMS Origem: R$ {icms_origem:.2f}\n'
                            f'ICMS Destino: R$ {icms_destino:.2f}\n'
                            f'ICMS ST: R$ {icms_st:.2f}\n'
                            f'Valor Total: R$ {vlr_prod + icms_st:.2f}'
                        )
                        
                        print(f"ICMS ST Interestadual: {icms_st}")
                        
                    except ValueError:
                        messagebox.showerror("Erro", "Digite valores numéricos válidos!")
                
                Button(frameCampos, text='Calcular ICMS ST Interestadual', command=calcular_st_interestadual,
                      font=('Arial', 10, 'bold'), bg='#3498db', fg='white',
                      padx=25, pady=8, relief=FLAT, cursor='hand2').pack()
        
        # Associa o comando aos RadioButtons
        tipoSt_rb1.config(command=EscolhaSt)
        tipoSt_rb2.config(command=EscolhaSt)

# Botão avançar
botao_avancar = Button(frame_principal, text="Avançar", command=EscolheTipoCalculo,
                       font=('Arial', 12, 'bold'), bg='#3498db', fg='white',
                       padx=40, pady=12, relief=FLAT, cursor='hand2')
botao_avancar.pack(pady=(20, 0))

root.mainloop()

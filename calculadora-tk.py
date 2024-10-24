import tkinter as tk
from tkinter import messagebox

janela = tk.Tk()
altura = 200
largura = 900
janela.geometry(f'{largura}x{altura}')
janela.title("Calculadora")

def calcular(operacao, entry_num1, entry_num2):
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())

        if operacao == "adição":
            result = num1 + num2
            resultado = f"{num1} + {num2} = {result}"
        elif operacao == "subtração":
            result = num1 - num2
            resultado = f"{num1} - {num2} = {result}"
        elif operacao == "função racional":
            result = num1 / num2 if num2 != 0 else "Indefinido"
            resultado = f"formula é {num1} / {num2} se {num2} for 0 é Indefinido, resultado: {result}"
        elif operacao == "função de crescimento":
            result = num1 * (1 + num2)  # Exemplo simples
            resultado = f"{num1} * (1 + {num2}) = {result}"
        elif operacao == "função de decaimento":
            result = num1 * (1 - num2)  # Exemplo simples
            resultado = f"{num1} * (1 - {num2}) = {result}"
        elif operacao == "função exponencial":
            result = num1 ** num2
            resultado = f"{num1} ** {num2} = {result}"
        elif operacao == "análise de variância":
            result = num1 / (num2 ** 2)  # Exemplo simples
            resultado = f"{num1} / ({num2} ** 2) = {result}"
        elif operacao == "extrapolação":
            result =  num1 + (num2 * 1.5)  
            resultado = f"A formula é{num1} + ({num2} * 1.5) Resultado: {result}"  # Exemplo simples
        elif operacao == "interpolação":
            result = (num1 + num2) / 2  # Exemplo simples
            resultado = f"({num1} + {num2}) / 2 = {result}"
        elif operacao == "estimação":
            result = num1 * 1.1 + num2 * 0.9  # Exemplo simples
            resultado = f"{num1} * 1.1 + {num2} * 0.9 = {result}"

        messagebox.showinfo("Resultado", f"O resultado da {operacao} é: {resultado}")
    except ValueError as e:
        messagebox.showerror("Erro", str(e))

def abrir_tela(titulo, operacao):
    janela_secundaria = tk.Toplevel()
    janela_secundaria.title(titulo)
    janela_secundaria.geometry('500x200')
    
    texto1 = tk.Label(janela_secundaria, text=f"{titulo}")
    botao1 = tk.Button(janela_secundaria, text="Fechar", command=janela_secundaria.destroy)
    
    texto1.place(x=200, y=0)
    botao1.place(x=390, y=0)

    label_num1 = tk.Label(janela_secundaria, text="Primeiro número: ")
    label_num2 = tk.Label(janela_secundaria, text="Segundo número: ")
    label_num1.grid(row=9, column=8, columnspan=2, pady=30)
    label_num2.grid(row=10, column=8, columnspan=2, pady=10)

    entry_num1 = tk.Entry(janela_secundaria, width=10)
    entry_num2 = tk.Entry(janela_secundaria, width=10)
    entry_num1.grid(row=9, column=10, columnspan=2, pady=10)
    entry_num2.grid(row=10, column=10, columnspan=2, pady=10)

    botao_calcular = tk.Button(janela_secundaria, text="Calcular", command=lambda: calcular(operacao, entry_num1, entry_num2))
    botao_calcular.grid(row=1000, column=250, pady=10)

# Funções para abrir janelas específicas
def abrir_tela_adicao():
    abrir_tela("Adição", "adição")
    
def abrir_tela_sub():
    abrir_tela("Subtração", "subtração")

def abrir_tela_funcao_racional():
    abrir_tela("Função Racional", "função racional")

def abrir_tela_funcao_crescimento():
    abrir_tela("Função de Crescimento", "função de crescimento")

def abrir_tela_funcao_decaimento():
    abrir_tela("Função de Decaimento", "função de decaimento")

def abrir_tela_funcao_exponencial():
    abrir_tela("Função Exponencial", "função exponencial")

def abrir_tela_funcao_analise_variancia():
    abrir_tela("Função de Análise de Variância", "análise de variância")

def abrir_tela_funcao_extrapolacao():
    abrir_tela("Função de Extrapolação", "extrapolação")

def abrir_tela_funcao_interpolacao():
    abrir_tela("Função de Interpolação", "interpolação")

def abrir_tela_funcao_estimacao():
    abrir_tela("Função de Estimação", "estimação")


label = tk.Label(janela, text="Escolha a operação matemática que queira fazer")
label.grid(row=0, column=1, columnspan=2, pady=10)

# Configurando os botões
botao1 = tk.Button(janela, text="Adição", command=abrir_tela_adicao)
botao1.grid(row=2, column=0, pady=10)
botao2 = tk.Button(janela, text="Subtração", command=abrir_tela_sub)
botao2.grid(row=2, column=1, pady=10)
botao3 = tk.Button(janela, text="Função Racional", command=abrir_tela_funcao_racional)
botao3.grid(row=2, column=2, pady=10)
botao4 = tk.Button(janela, text="Função de Crescimento", command=abrir_tela_funcao_crescimento)
botao4.grid(row=2, column=3, pady=10)
botao5 = tk.Button(janela, text="Função de Decaimento", command=abrir_tela_funcao_decaimento)
botao5.grid(row=2, column=4, pady=10)
botao6 = tk.Button(janela, text="Função Exponencial", command=abrir_tela_funcao_exponencial)
botao6.grid(row=3, column=0, pady=10)
botao7 = tk.Button(janela, text="Função de Análise de Variância", command=abrir_tela_funcao_analise_variancia)
botao7.grid(row=3, column=1, pady=10)
botao8 = tk.Button(janela, text="Função de Interpolação", command=abrir_tela_funcao_interpolacao)
botao8.grid(row=3, column=2, pady=10)
botao9 = tk.Button(janela, text="Função de Extrapolação", command=abrir_tela_funcao_extrapolacao)
botao9.grid(row=3, column=3, pady=10)
botao10 = tk.Button(janela, text="Função de Estimação", command=abrir_tela_funcao_estimacao)
botao10.grid(row=3, column=4, pady=10)

janela.mainloop()

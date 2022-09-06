from tkinter import *
import tkinter as tk
from tkinter import ttk

x = 0

pais_nascimento = {}
pais_nascimento_y = 250
pais_nascimento_valor = []
pais_formacao = {}

america_sul = 0
america_central = 0
america_norte = 0
africa = 0
europa = 0
oceania = 0
asia = 0

def continenteFuncao():
	
	if valor_continente.get() == "América do Sul":
		global america_sul
		america_sul += 1

	if valor_continente.get() == "América Central":
		global america_central
		america_central += 1

	if valor_continente.get() == "América do Norte":
		global america_norte
		america_norte += 1

	if valor_continente.get() == "África":
		global africa
		africa += 1

	if valor_continente.get() == "Europa":
		global europa
		europa += 1

	if valor_continente.get() == "Oceania":
		global oceania
		oceania += 1

	if valor_continente.get() == "Ásia":
		global asia
		asia += 1

	porcentagem_america_sul = (100 * america_sul) / (america_sul + america_central + america_norte + africa + europa + oceania + asia)
	porcentagem_america_sul = round(porcentagem_america_sul, 1)
	porcentagem_america_norte = (100 * america_norte) / (america_sul + america_central + america_norte + africa + europa + oceania + asia)
	porcentagem_america_norte = round(porcentagem_america_norte, 1)
	porcentagem_america_central = (100 * america_central) / (america_sul + america_central + america_norte + africa + europa + oceania + asia)
	porcentagem_america_central = round(porcentagem_america_central, 1)
	porcentagem_africa = (100 * africa) / (america_sul + america_central + america_norte + africa + europa + oceania + asia)
	porcentagem_africa = round(porcentagem_africa, 1)
	porcentagem_europa = (100 * europa) / (america_sul + america_central + america_norte + africa + europa + oceania + asia)
	porcentagem_europa = round(porcentagem_europa, 1)
	porcentagem_oceania = (100 * oceania) / (america_sul + america_central + america_norte + africa + europa + oceania + asia)
	porcentagem_oceania = round(porcentagem_oceania, 1)
	porcentagem_asia = (100 * asia) / (america_sul + america_central + america_norte + africa + europa + oceania + asia)
	porcentagem_asia = round(porcentagem_asia, 1)

	wid_america_sul.config(text="Nasceu na América do Sul(%): {}".format(porcentagem_america_sul))
	wid_america_central.config(text="Nasceu na América Central(%): {}".format(porcentagem_america_central))
	wid_america_norte.config(text="Nasceu na América do Norte(%): {}".format(porcentagem_america_norte))
	wid_asia.config(text="Nasceu na Ásia(%): {}".format(porcentagem_asia))
	wid_africa.config(text="Nasceu na África(%): {}".format(porcentagem_africa))
	wid_oceania.config(text="Nasceu na Oceania(%): {}".format(porcentagem_oceania))
	wid_europa.config(text="Nasceu na Europa(%): {}".format(porcentagem_europa))

	global pais_nascimento
	global pais_formacao
	global x


	pais_nascimento_valor = wid_pais_nascimento.get("1.0", "end-1c")

	if pais_nascimento_valor in pais_nascimento:
		pais_nascimento[pais_nascimento_valor] += 1
		
	else:
		pais_nascimento[pais_nascimento_valor] = 1
	global wid_pais_nascimento2
	wid_pais_nascimento2.config(text="{}".format(pais_nascimento))
	
	pais_formacao_valor = wid_pais_formacao.get("1.0", "end-1c")

	if pais_formacao_valor in pais_formacao:
		pais_formacao[pais_formacao_valor] += 1
		
	else:
		pais_formacao[pais_formacao_valor] = 1
	global wid_pais_formacao2
	wid_pais_formacao2.config(text="{}".format(pais_formacao))

	
#janela1

frame=tk.Tk()

frame.title("Autores")
frame.geometry('700x500')
frame.resizable(False, False)

ttk.Label(frame, text="Registrar Autores", font=("Arial", 16)).place(x=280, y=0)

ttk.Label(frame, text="Autor(a)", font=("Arial", 12)).place(x=150, y=50)
nome = tk.Text(frame, height=1, width=20).place(x=150, y=70)

ttk.Label(frame, text="Continente que nasceu", font=("Arial", 12)).place(x=150, y=90)
valor_continente = StringVar()
ttk.Combobox(frame, values=["América do Sul", "América Central", "América do Norte", "Ásia", "África", "Oceania", "Europa"], textvariable=valor_continente).place(x=150, y=110)


ttk.Label(frame, text="País que nasceu", font=("Arial", 12)).place(x=150, y=130)
wid_pais_nascimento = tk.Text(frame, height=1, width=20)
wid_pais_nascimento.place(x=150, y=150)
ttk.Label(frame, text="País se formou", font=("Arial", 12)).place(x=150, y=170)
wid_pais_formacao = tk.Text(frame, height=1, width=20)
wid_pais_formacao.place(x=150, y=190)

ttk.Button(frame, text="Enviar", command=continenteFuncao).place(x=150, y=300)

#janela2

frame2=tk.Tk()

frame2.title("Autores")
frame2.geometry('1000x500')
frame2.resizable(False, False)

ttk.Label(frame2, text="Estatísticas", font=("Arial", 16)).place(x=470, y=0)

wid_america_sul = ttk.Label(frame2, text="Nasceu na América do Sul(%): ", font=("Arial", 12))
wid_america_sul.place(x=90, y=90)
wid_america_central = ttk.Label(frame2, text="Nasceu na América Central(%): ", font=("Arial", 12))
wid_america_central.place(x=90, y=110)
wid_america_norte = ttk.Label(frame2, text="Nasceu na América do Norte(%): ", font=("Arial", 12))
wid_america_norte.place(x=90, y=130)
wid_asia = ttk.Label(frame2, text="Nasceu na Ásia(%): ", font=("Arial", 12))
wid_asia.place(x=90, y=150)
wid_africa = ttk.Label(frame2, text="Nasceu na África(%): ", font=("Arial", 12))
wid_africa.place(x=90, y=170)
wid_oceania = ttk.Label(frame2, text="Nasceu na Oceania(%): ", font=("Arial", 12))
wid_oceania.place(x=90, y=190)
wid_europa = ttk.Label(frame2, text="Nasceu na Europa(%): ", font=("Arial", 12))
wid_europa.place(x=90, y=210)

ttk.Label(frame2, text="País que nasceu(quant):", font=("Arial", 12)).place(x=90, y=250)
wid_pais_nascimento2 = ttk.Label(frame2, text="", font=("Arial", 12))
wid_pais_nascimento2.place(x=90, y=270)

ttk.Label(frame2, text="País que se formou(quant):", font=("Arial", 12)).place(x=90, y=300)
wid_pais_formacao2 = ttk.Label(frame2, text="", font=("Arial", 12))
wid_pais_formacao2.place(x=90, y=320)

frame.mainloop()
frame2.mainloop()

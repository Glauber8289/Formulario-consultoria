#importando tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
#importanto tkcalendar
from tkcalendar import Calendar, DateEntry

#importando views
from view import *


################# cores ###############
co0 = "#f0f3f5"  # Preta
co1 = "#feffff"  # branca
co2 = "#4fa882"  # verde
co3 = "#38576b"  # valor
co4 = "#403d3d"   # letra
co5 = "#e06636"   # - profit
co6 = "#038cfc"   # azul
co7 = "#ef5350"   # vermelha
co8 = "#263238"   # + verde
co9 = "#e9edf5"   # sky blue

################# criando janela ###############
 
janela=Tk()
janela.title("")
janela.geometry('1043x453')
janela.configure(background=co9)
janela.resizable(width=FALSE,height=FALSE)

################# Dividindo janela ###############
frame_cima=Frame(janela,width=310,height=50,bg=co2,relief="flat")
frame_cima.grid(row=0,column=0)

frame_baixo=Frame(janela,width=310,height=403,bg=co1,relief="flat")
frame_baixo.grid(row=1,column=0,sticky=NSEW,padx=0,pady=1)

frame_direita=Frame(janela,width=588,height=403,bg=co1,relief="flat")
frame_direita.grid(row=0,column=1,rowspan=2,padx=1,pady=0,sticky=NSEW)

################# Label cima ###############
app_nome=Label(frame_cima,text='Formulário de consultoria',anchor=NW,font=('Ivy 13 bold'),bg=co2,fg=co1,relief='flat')
app_nome.place(x=10,y=20)
#variavel tree global
global tree

#Funcao inserir
def inserir():
    nome=e_nome.get()
    email=e_email.get()
    telefone=e_telefone.get()
    data=e_data.get()
    estado=e_estado.get()
    consulta=e_consulta.get()

    lista= [nome,email,telefone,data,estado,consulta]
  
    if nome == '' :
     messagebox.showerror('Erro','O nome não pode estar vazio')
    else:
     inserir_info(lista)
    messagebox.showinfo("Sucesso","Os dados foram inseridos com sucesso")

    e_nome.delete(0,'end')
    e_email.delete(0,'end')
    e_telefone.delete(0,'end')
    e_data.delete(0,'end')
    e_estado.delete(0,'end')
    e_consulta.delete(0,'end')
 
    for widget in frame_direita.winfo_children():
     widget.destroy()
    mostrar()
   
  
   # Função atualizar

def atualizar():
        try:

           treev_dados = tree.focus()
           treev_dicionario = tree.item(treev_dados)
           tree_lista= treev_dicionario['values']

           valor_id = tree_lista[0]
           
           e_nome.delete(0,'end')
           e_email.delete(0,'end')
           e_telefone.delete(0,'end')
           e_data.delete(0,'end')
           e_estado.delete(0,'end')
           e_consulta.delete(0,'end')
           
           e_nome.insert(0,tree_lista[1])
           e_email.insert(0,tree_lista[2])
           e_telefone.insert(0,tree_lista[3])
           e_data.insert(0,tree_lista[4])
           e_estado.insert(0,tree_lista[5])
           e_consulta.insert(0,tree_lista[6])
         
        except IndexError:
         messagebox.showerror('Erro','selecione um dos dados na tabela')   

    
        def update():
        
             nome=e_nome.get()
             email=e_email.get()
             telefone=e_telefone.get()
             data=e_data.get()
             estado=e_estado.get()
             consulta=e_consulta.get()
       
             lista= [nome,email,telefone,data,estado,consulta,valor_id]

             if nome == '' :
              messagebox.showerror('Erro','O nome não pode estar vazio')
             else:
              atualizar_info(lista)
             messagebox.showinfo("Sucesso","Os dados foram atualizados com sucesso")

             e_nome.delete(0,'end')
             e_email.delete(0,'end')
             e_telefone.delete(0,'end')
             e_data.delete(0,'end')
             e_estado.delete(0,'end')
             e_consulta.delete(0,'end')
        
             for widget in frame_direita.winfo_children():
                widget.destroy()
             mostrar()
    #Botao confirmar
        b_confirmar=Button(frame_baixo,command=update,text='Confirmar ',width=10,font=('Ivy 7 bold'),bg=co2,fg=co1,relief='raised',overrelief='ridge')
        b_confirmar.place(x=100,y=350)   

#funcao deletar
def deletar():
    try:
        treev_dados = tree.focus()
        treev_dicionario = tree.item(treev_dados)
        tree_lista= treev_dicionario['values']

        valor_id = [tree_lista[0]]
           
        deletar_info(valor_id)
        messagebox.showinfo("Sucesso","Os dados foram deletados com sucesso")
           
        for widget in frame_direita.winfo_children():
                widget.destroy()
           
        mostrar()
    
    except IndexError:
         messagebox.showerror('Erro','selecione um dos dados na tabela')  

################# configurando frame baixo ###############

#Nome
l_nome=Label(frame_baixo,text='Nome *',anchor=NW,font=('Ivy 10 bold'),bg=co1,fg=co4,relief='flat')
l_nome.place(x=10,y=10)
e_nome=Entry(frame_baixo,width=45,justify="left",relief='solid')
e_nome.place(x=15,y=40)

#Email
l_email=Label(frame_baixo,text='Email *',anchor=NW,font=('Ivy 10 bold'),bg=co1,fg=co4,relief='flat')
l_email.place(x=10,y=65)
e_email=Entry(frame_baixo,width=45,justify="left",relief='solid')
e_email.place(x=15,y=90)

#Telefone
l_telefone=Label(frame_baixo,text='Telefone *',anchor=NW,font=('Ivy 10 bold'),bg=co1,fg=co4,relief='flat')
l_telefone.place(x=10,y=115)
e_telefone=Entry(frame_baixo,width=45,justify="left",relief='solid')
e_telefone.place(x=15,y=140)

#Data da consulta
l_data=Label(frame_baixo,text='Data da consulta *',anchor=NW,font=('Ivy 10 bold'),bg=co1,fg=co4,relief='flat')
l_data.place(x=10,y=165)
e_data=DateEntry(frame_baixo,width=12,background='darkblue',foreground='white',borderwidth=2,year=2023)
e_data.place(x=15,y=190)

#Estado
l_estado=Label(frame_baixo,text='Estado da consulta *',anchor=NW,font=('Ivy 10 bold'),bg=co1,fg=co4,relief='flat')
l_estado.place(x=150,y=165)
e_estado=Entry(frame_baixo,width=20,justify="left",relief='solid')
e_estado.place(x=160,y=190)

#Consulta Sobre
l_consulta=Label(frame_baixo,text='Informação extra *',anchor=NW,font=('Ivy 10 bold'),bg=co1,fg=co4,relief='flat')
l_consulta.place(x=10,y=220)
e_consulta=Entry(frame_baixo,width=45,justify="left",relief='solid')
e_consulta.place(x=15,y=250)

#Botao inserir
b_inserir=Button(frame_baixo,text='Inserir ',command=inserir,width=10,font=('Ivy 9 bold'),bg=co6,fg=co1,relief='raised',overrelief='ridge')
b_inserir.place(x=10,y=300)

#Botao atualizar
b_atualizar=Button(frame_baixo,command=atualizar,text='Atualizar ',width=10,font=('Ivy 9 bold'),bg=co2,fg=co1,relief='raised',overrelief='ridge')
b_atualizar.place(x=100,y=300)

#Botao deletar
b_deletar=Button(frame_baixo,command=deletar,text='Deletar ',width=10,font=('Ivy 9 bold'),bg=co7,fg=co1,relief='raised',overrelief='ridge')
b_deletar.place(x=190,y=300)




                                ################Frame direita################
def mostrar() : 
   
   global tree

   lista = mostrar_info()

   # lista para cabecario
   tabela_head = ['ID','Nome',  'email','telefone', 'data', 'estado','Sobre']


   # criando a tabela
   tree = ttk.Treeview(frame_direita, selectmode="extended", columns=tabela_head, show="headings")

   # vertical scrollbar
   vsb = ttk.Scrollbar(frame_direita, orient="vertical", command=tree.yview)

   # horizontal scrollbar
   hsb = ttk.Scrollbar( frame_direita, orient="horizontal", command=tree.xview)

   tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
   tree.grid(column=0, row=0, sticky='nsew')
   vsb.grid(column=1, row=0, sticky='ns')
   hsb.grid(column=0, row=1, sticky='ew')

   frame_direita.grid_rowconfigure(0, weight=12)


   hd=["nw","nw","nw","nw","nw","center","center"]
   h=[30,170,140,100,120,50,100]
   n=0

   for col in tabela_head:
     tree.heading(col, text=col.title(), anchor=CENTER)
     #adjust the column's width to the header string
     tree.column(col, width=h[n],anchor=hd[n])
     n+=1
   for item in lista:
     tree.insert('', 'end', values=item)

   #chamando a funcao mostrar

mostrar()

janela.mainloop()

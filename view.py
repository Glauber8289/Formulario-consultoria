import sqlite3 as lite



#Crud

#C = inserir/criar
#R = Ready/ler
#U=Update/atualizar
#D=Deletar/deletar

#criando conexao 
con = lite.connect('dados.db')


#inserir informacoes
def inserir_info(i):
 with con:
     cur=con.cursor()
     query="INSERT INTO formulario (nome,email,telefone,dia_em,estado,assunto)VALUES(?,?,?,?,?,?)"
     cur.execute(query,i)

#mostrar informacoes
def mostrar_info():
  lista = []
  with con:
     cur = con.cursor()
     query= "SELECT * FROM formulario"
     cur.execute(query)
     informacao = cur.fetchall()
     
     for i in informacao:
        lista.append(i)
  return lista    



#atualizar informacoes
def atualizar_info(i):
  with con:
     cur = con.cursor()
     query= "UPDATE formulario SET nome=?, email=?, telefone=?, dia_em=?, estado=?, assunto=? WHERE id=?"
     cur.execute(query,i)


#deletar informacoes
def deletar_info(i):
  with con :
    cur=con.cursor()
    query="DELETE FROM formulario WHERE id=?"
    cur.execute(query,i)

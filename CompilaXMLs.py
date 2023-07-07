from xml.dom import minidom
from xml.dom.minidom import parseString
import csv
import os
import os,re
import os,sys


#CriaC'C#o da Lista de Listas
t = []
t.append([
        "Data de Emissão",
        "Tipo de Nota",
        "Número da Nota",
        "Nome do Emissor da Nota",
        "CNPJ do Emissor",
        "Nome do Destinatario da Nota",
        "CNPJ do Destinatario",
        "Número do Item",
        "Descrição do Produto",
        "Código do Produto",
        "Quantidade do Produto",
        "Valor Unitário do Produto",
        "Valor Total do Produto",
        "Valor do Frete"
])
w=[]
w.append([
        "Data de Emissão",
        "Tipo de Nota",
        "Número da Nota",
        "Nome do Emissor da Nota",
        "CNPJ do Emissor",
        "Nome do Destinatario da Nota",
        "CNPJ do Destinatario",
        "Valor Total da Nota",
        "Valor do Frete"
])

#Lista de arquivos com erro
lista_erro = set()

#Loop de abertura dos arquivos
caminho_diretorio = 'C:/Users/john/Documentos'

for NomeArquivo in os.listdir(caminho_diretorio):
    if NomeArquivo.endswith(".xml") or NomeArquivo.endswith(".XML"):
        caminho_completo = os.path.join(caminho_diretorio, NomeArquivo)
        try:
            doc=minidom.parse(caminho_completo)
        except:
            lista_erro.add(NomeArquivo)
            continue

#Extração de InformaC'C5es BC!sicas da Nota
        try:
            DataEmissao=doc.getElementsByTagName("dhEmi")[0]
            TipoDeNota=doc.getElementsByTagName("natOp")[0]
            NumeroNota=doc.getElementsByTagName("nNF")[0]
            ValorNota=doc.getElementsByTagName("vNF")[0]
            ValorFrete=doc.getElementsByTagName("vFrete")[-1]
            # ChaveDeAcesso=doc.getElementsByTagName("chNFe")[0]
            # makes float field pt-br
            ValorNota.firstChild.data=str(ValorNota.firstChild.data).replace(".",",")
            ValorFrete.firstChild.data=str(ValorFrete.firstChild.data).replace(".",",")

        except:
            lista_erro.add(NomeArquivo)

       
#Extração Informações do Emissor
        try:
            emit=doc.getElementsByTagName("emit")[0]
            NomeEmissor=emit.getElementsByTagName("xNome")[0]
            CNPJEmissor=emit.getElementsByTagName("CNPJ")[0]
        except:
            lista_erro.add(NomeArquivo)

#Extração de Informações do Destinatário
        try:
            dest=doc.getElementsByTagName("dest")[0]
            NomeDestinatario=dest.getElementsByTagName("xNome")[0]
            CNPJDestinatario=dest.getElementsByTagName("CNPJ")[0]
        except:
            lista_erro.add(NomeArquivo)
        
#Extração das Informações do Produto e adição dessas informações à lista de listas
        try:
            dets=doc.getElementsByTagName("det")
            for det in dets:
                NumeroItem=det.getAttribute("nItem")
                DescricaoProd=det.getElementsByTagName("xProd")[0]
                CodProd=det.getElementsByTagName("cProd")[0]
                QuantProd=det.getElementsByTagName("qCom")[0]
                ValorUnitProd=det.getElementsByTagName("vUnCom")[0]
                ValorTotalProd=det.getElementsByTagName("vProd")[0]
                t.append([DataEmissao.firstChild.data,TipoDeNota.firstChild.data,NumeroNota.firstChild.data,NomeEmissor.firstChild.data,CNPJEmissor.firstChild.data,NomeDestinatario.firstChild.data,CNPJDestinatario.firstChild.data,NumeroItem,DescricaoProd.firstChild.data,CodProd.firstChild.data,QuantProd.firstChild.data,ValorUnitProd.firstChild.data,ValorTotalProd.firstChild.data,ValorFrete.firstChild.data])
            w.append([DataEmissao.firstChild.data,TipoDeNota.firstChild.data,NumeroNota.firstChild.data,NomeEmissor.firstChild.data,CNPJEmissor.firstChild.data,NomeDestinatario.firstChild.data,CNPJDestinatario.firstChild.data,ValorNota.firstChild.data,ValorFrete.firstChild.data])
        except:
            lista_erro.add(NomeArquivo)
	        
#Exportação dos dados para arquivo csv   

caminho_CSV = 'C:/Users/john/Documentos'

with open(caminho_CSV + "Pedidos por SKU.csv","w", newline='', encoding='utf-8') as f:
   writer=csv.writer(f, delimiter=';', quotechar='"', quoting=csv.QUOTE_ALL)
   writer.writerows(t)

with open(caminho_CSV + "Totais das Notas.csv","w", newline='', encoding='utf-8') as f:
   writer=csv.writer(f, delimiter=';', quotechar='"', quoting=csv.QUOTE_ALL)
   writer.writerows(w)

print(f'{len(lista_erro)} arquivos com erro :')
for arquivo in lista_erro:
    print(arquivo)


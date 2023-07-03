import win32com.client
from zipfile import ZipFile
from pathlib import Path
import os

def Baixa_XMLs (email, Pasta_Destino):
    outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
    Pasta_Destino = Path(Pasta_Destino)
    x=0

    # Obter os itens da pasta de e-mails
    for account in outlook.Folders:
        if account.Name == email:
            mailbox = account
            break
    else:
        raise Exception('Mailbox not found')

    # Acessa a pasta 'Caixa de entrada' da conta
    inbox = mailbox.Folders['Caixa de entrada']
    emails = inbox.Items

    # Percorrer todos os e-mails
    for email in emails:
        # Verificar se o e-mail tem anexos
        if email.Attachments.Count > 0:
            # Percorrer todos os anexos do e-mail
            for attachment in email.Attachments:
                # Verificar se o anexo é um arquivo .xml
                if attachment.FileName.endswith('.xml'):
                    x +=1
                    # Salvar o anexo na pasta de destino
                    attachment.SaveAsFile(Pasta_Destino / attachment.FileName)
                    email.UnRead = False
                elif attachment.FileName.endswith('.zip'):
                    # Salva o arquivo .zip temporariamente
                    temp_zip_path = Pasta_Destino / attachment.FileName
                    attachment.SaveAsFile(temp_zip_path)
                    
                    with ZipFile(temp_zip_path, 'r') as zip_ref:
                        # Extraia cada arquivo do arquivo .zip
                        for file in zip_ref.namelist():
                            # Se o arquivo for .xml, salve no diretório de destino
                            if file.endswith('.xml'):
                                # Cria um Path com o nome completo do arquivo
                                full_file_path = Pasta_Destino / file
                                # Verifica se o arquivo já existe
                                if full_file_path.exists():
                                    # Se o arquivo já existir, altere o nome do arquivo
                                    base = full_file_path.stem
                                    ext = full_file_path.suffix
                                    counter = 1
                                    while full_file_path.exists():
                                        full_file_path = Pasta_Destino / f"{base}_{counter}{ext}"
                                        counter += 1
                                # Cria os diretórios necessários antes de criar o arquivo
                                full_file_path.parent.mkdir(parents=True, exist_ok=True)
                                # Agora podemos extrair o arquivo com segurança
                                with open(full_file_path, "wb") as f_out:
                                    f_out.write(zip_ref.read(file))
                                    x +=1
                    os.remove(temp_zip_path)
    print('Foram salvos ' + str(x) + ' arquivos diferentes. Note que podem haver pastas contendo arquivos xml.')

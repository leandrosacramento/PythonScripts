def converte_ipynb_para_py(jupyter_notebook, verbose=True):
    '''
        Função para converter Jupyter Notebook (.ipynb) em Python (.py).
        O arquivo .py será salvo no mesmo diretório que o arquivo informado se encontra.
        
        Parâmetros:
            - jupyter_notebook
                Tipo de dado: string
                Exemplo: 'sqlite_cadastro.ipynb'
                
        Necessário instalar o pacote abaixo:
            pip install notebooktoall
    '''
    import os
    from notebooktoall.transform import transform_notebook
    
    # Verifica se o arquivo informado é um Jupyter Notebook
    if jupyter_notebook[-6:] == '.ipynb':  
        
        transform_notebook(ipynb_file=jupyter_notebook
                           , export_list=['py'])
        
        
        if os.path.exists(jupyter_notebook):            
            if verbose: print('Arquivo convertido!')                
        else:        
            print('Erro ao converter o arquivo!')
        
    else:
        
        if verbose: print('O arquivo informado não é um Jupyter Notebook.')    


# Exemplo de uso da função
converte_ipynb_para_py('sqlite_cadastro.ipynb')

import textwrap
from fpdf import FPDF

def SalvarNoticias(noticias, login):
    # Abrir arquivo com o login do repórter
    arquivo = open(f'noticias_{login}.txt', 'w')
    arquivo.write(f'\n\t======= Notícias do usuário(a): {login}  =======\n')

    for noticia in noticias:
        if noticia['autor'] == login:
            arquivo.write('-' * 61)
            arquivo.write(f'\nTítulo: {noticia["Titulo"]}\n')
            arquivo.write(f'\nDescrição: {noticia["Descricao"]}\n')
            news = noticia["Noticia"]
            arquivo.write(f'\nNotícia: {textwrap.fill(news, width=100)}\n')
            arquivo.write(f'\nID da notícia: {noticia["ID"]}\n')
            arquivo.write(f'Data de publicação: {noticia["DataDia"]}/{noticia["DataMes"]}/{noticia["DataAno"]}\n')
            arquivo.write(f'Publicada por: {noticia["autor"]}\n')

    arquivo.close()

def GerarPDF(noticias, id_pdf):
    for noticia in noticias:
        data = f'{noticia["DataDia"]}/{noticia["DataMes"]}/{noticia["DataAno"]}'
        if noticia['ID'] == id_pdf:
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font('times', 'B', size=16)
            max_largura = pdf.w - 2 * pdf.l_margin
            pdf.multi_cell(max_largura, 10,  f'{noticia["Titulo"].encode("latin-1", "replace").decode("latin-1")}\n', align='C')
            pdf.ln(10)
            pdf.set_font('times', 'B', size=14)
            pdf.multi_cell(max_largura, 10, f'{noticia["Descricao"].encode("latin-1", "replace").decode("latin-1")}\n', align='C')
            pdf.ln(10)
            pdf.set_font('arial', size=12)
            pdf.multi_cell(0, 10, f'{noticia["Noticia"].encode("latin-1", "replace").decode("latin-1")}')
            pdf.multi_cell(0, 10, f'\n=> Data de publicação: {data.encode("latin-1", "replace").decode("latin-1")}')
            pdf.multi_cell(0, 10, f'=> Publicada por: {noticia["autor"].encode("latin-1", "replace").decode("latin-1")}')
            pdf.output(f"noticia_ID{noticia['ID']}.pdf")
            print("\n\t\033[32mPDF gerado com sucesso!\n\033[m")
            break



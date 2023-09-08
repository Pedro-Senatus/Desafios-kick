import pandas as pd
import matplotlib.pyplot as plt
from fpdf import FPDF


df = pd.read_csv("PDA_Dados_Cursos_Graduacao_Brasil.csv.crdownload")

df.info()
df.head()

curso_regiao = df[['NOME_CURSO','REGIAO']]

cursos_mais_populares = curso_regiao.value_counts().reset_index(name='CURSO_MAIS_POPULAR')

cursos_mais_populares

nordeste = cursos_mais_populares.loc[cursos_mais_populares['REGIAO'] == 'NORDESTE',['NOME_CURSO','REGIAO','CURSO_MAIS_POPULAR']]

nordeste.head()

cursos_nordeste = nordeste.iloc[:10, :10]
cursos_nordeste

cursos_nordeste.plot(kind="bar", x="NOME_CURSO", y="CURSO_MAIS_POPULAR", title="CURSOS MAIS POPULARES NO NORDESTE")
plt.savefig('cursos_nordeste.png', bbox_inches='tight')

sul = cursos_mais_populares.loc[cursos_mais_populares['REGIAO'] == 'SUL',['NOME_CURSO','REGIAO','CURSO_MAIS_POPULAR']]

sul.head()

cursos_sul = sul.iloc[:10, :10]
cursos_sul

cursos_sul.plot(kind="bar", x="NOME_CURSO", y="CURSO_MAIS_POPULAR", title="CURSOS MAIS POPULARES NO SUL")
plt.savefig('cursos_sul.png', bbox_inches='tight')

sudeste = cursos_mais_populares.loc[cursos_mais_populares['REGIAO'] == 'SUDESTE',['NOME_CURSO','REGIAO','CURSO_MAIS_POPULAR']]

sudeste.head()

cursos_sudeste = sudeste.iloc[:10, :10]
cursos_sudeste

cursos_sudeste.plot(kind="bar", x="NOME_CURSO", y="CURSO_MAIS_POPULAR", title="CURSOS MAIS POPULARES NO SUDESTE")
plt.savefig('cursos_sudeste.png', bbox_inches='tight')

centro_oeste = cursos_mais_populares.loc[cursos_mais_populares['REGIAO'] == 'CENTRO-OESTE',['NOME_CURSO','REGIAO','CURSO_MAIS_POPULAR']]

centro_oeste.head()

cursos_centro_oeste = centro_oeste.iloc[:10, :10]
cursos_centro_oeste

cursos_centro_oeste.plot(kind="bar", x="NOME_CURSO", y="CURSO_MAIS_POPULAR", title="CURSOS MAIS POPULARES NO CENTRO-OESTE")
plt.savefig('cursos_centro_oeste.png', bbox_inches='tight')

norte = cursos_mais_populares.loc[cursos_mais_populares['REGIAO'] == 'NORTE',['NOME_CURSO','REGIAO','CURSO_MAIS_POPULAR']]

norte.head()

cursos_norte = norte.iloc[:10, :10]
cursos_norte

cursos_norte.plot(kind="bar", x="NOME_CURSO", y="CURSO_MAIS_POPULAR", title="CURSOS MAIS POPULARES NO NORTE")
plt.savefig('cursos_norte.png', bbox_inches='tight')

vagas_regiao = df[['REGIAO','QT_VAGAS_AUTORIZADAS']]
vagas_regiao

vagas_por_regiao = vagas_regiao.groupby('REGIAO').sum()
vagas_por_regiao

vagas_por_regiao = vagas_por_regiao.drop('IGNORADO/EXTERIOR')
vagas_por_regiao

vagas_por_regiao_gf = vagas_por_regiao.plot(kind = 'bar', title = "QUANTIDADES DE CURSOS AUTORIZADOS POR REGIÃO")
plt.savefig('vagas_por_regiao_gf.png', bbox_inches='tight')

pdf = FPDF('P', 'mm', 'A4')

pdf.add_page()

pdf.set_font('Arial', '', 16)

pdf.cell(w=0, h=20, txt='Dados sobre a educação brasileira', ln=True, align='C')

pdf.cell(w=0, h=16, txt='Gráficos que demonstram os cursos mais populares em cada região do país:', ln=True, align='C')

pdf.image(name='cursos_nordeste.png', x=30, y=65, w=140)

pdf.add_page()

pdf.image(name='cursos_sudeste.png', x=45, y=10, w=110)

pdf.image(name='cursos_sul.png', x=45, y=160, w=110)

pdf.add_page()

pdf.image(name='cursos_centro_oeste.png', x=45, y=10, w=110)

pdf.image(name='cursos_norte.png', x=45, y=160, w=110)

pdf.add_page()

pdf.cell(w=0, h=16, txt='Gráfico que demonstra a quantidade de vagas autorizados por região', ln=True, align='C')

pdf.image(name='vagas_por_regiao_gf.png', x=30, y=65, w=140)

pdf.add_page()

pdf.cell(w=0, h=16, txt='Conclusão da análise:', ln=True, align='C')

text='Podemos concluir, com base nesta análise, que não há muita diferença entre os cursos mais populares nas diferentes regiões. Os cursos em alta são praticamente os mesmos, com pequenas variações em suas classificações. Além disso, observamos que o Sudeste, devido à sua superioridade econômica em relação às outras regiões, também oferece uma gama mais ampla de cursos em comparação com as demais.'

pdf.multi_cell(w=0, h=10, txt=text, align='J')

pdf.output('DADOS_EDUCACAO_BR.pdf')
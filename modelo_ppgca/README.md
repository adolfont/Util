Este repositório contém o Modelo para a Elaboração de Dissertações de Mestrado do PPGCA - UTFPR.

É uma versão do "Modelo LaTeX para a UTFPR", desenvolvido pelo Prof. Hugo Vieira Neto, disponível em <http://pessoal.utfpr.edu.br/hvieir/orient/>.

**PPGCA**: Programa de Pós-Graduação em Computação Aplicada <http://www.ppgca.utfpr.edu.br>

**UTFPR**: Universidade Tecnológica Federal do Paraná <http://www.utfpr.edu.br>


## Instruções


1. Instalar o Latex
2. Instalar o abnTeX (<http://abntex.codigolivre.org.br/>)

   Veja como em: <http://abntex.codigolivre.org.br/node7.html#instalacao>

   Página de downloads do abnTeX: <http://codigolivre.org.br/frs/?group_id=46>

3. Clonar este repositório usando o **git** ou fazer o download (ver pacote **modelo_ppgca.zip** na área de downloads) de todos os arquivos e depois descompactar o pacote.

5. Gerar o PDF tendo como base o arquivo modelo_ppgca.tex

   A forma mais garantida é executar **pdflatex modelo_ppgca.tex** duas vezes, depois executar **bibtex modelo_ppgca**, depois novamente executar **pdflatex modelo_ppgca.tex**.

6. Visualizar o PDF gerado

   Em Linux, os melhores visualizadores são o Acrobat Reader e o Okular. O Okular tem a vantagem de atualizar automaticamente a visualização do documento após cada compilação.

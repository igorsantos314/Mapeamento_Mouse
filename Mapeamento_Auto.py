from Dicionario_Cidades import citys

arquivo = open("map_svg.html")

arquivo_novo = open("map_svg_tag_a.html", "w")
pos = 1

obj_cidades = citys()
lista_codigo = []

for i in arquivo:
    lista_codigo.append(i)

for pos_lista, linha in enumerate(lista_codigo):

    if pos == 185:
        break
    
    cidade = obj_cidades.disc_cidades[pos].replace('ç','&ccedil;').replace('í','&iacute;').replace('é','&eacute;').replace('ê','&ecirc;').replace('ã','&atilde;').replace('ó','&oacute;').replace('ô', '&ocirc;').replace('á','&aacute;').replace('ú','&uacute;').replace('â', '&acirc;')
    cidade_sem_acento_sem_espaco = obj_cidades.disc_cidades[pos].replace('ç','c').replace('í','i').replace('é','e').replace('ê','e').replace('ã','a').replace('ó','o').replace('á','a').replace('ú','u').replace(' ', '_') + '.html'
    cidade_pasta = cidade_sem_acento_sem_espaco.replace('.html','')

    tag_a = f'<a xlink:title="{cidade}" xlink:href="pages/{cidade_pasta}/{cidade_sem_acento_sem_espaco}">\n                        <path'
    tag_a_fechar = '/>\n                    </a>'

    if '<path' in linha:
        lista_codigo[pos_lista] = linha.replace('<path', tag_a)
        pos += 1
        #print(f"'pages/{cidade_pasta}/{cidade_sem_acento_sem_espaco}',")

    if '/>' in linha:
        lista_codigo[pos_lista] = linha.replace('/>', tag_a_fechar)

for s in lista_codigo:
    arquivo_novo.write(s)

arquivo_novo.close()

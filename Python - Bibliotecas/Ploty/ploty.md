# Plotly

O Ploty cria gráficos interativos que rodam no navegador e no jupyter. Ele é uma **biblioteca de visualização de dados** que permite que a gente crie gráficos interativos.

[Site oficial do Plotly](https://plotly.com/)

## Instalação
Instalação do Plotly:

```
pip install plotly
```

Instalação do ipywidgets para visualização no jupyter:
```
pip install ipywidgets
```

## Conceitos

**Objeto básico:** Figure 
Figure é uma caixa onde os gráficos irão residir. Permiti plotar um gráfico dentro dela, ou união de varios gráficos.

Instancia da Classe Figure:
```
go = go.Figure()
```

Para colocar mais de um gráfico:

```
fig = make_subplots(rows=1, cols=2)
```

**Atributos da Figure:**
* data
* layout
* frames

**Data**:
São os dados utilizados no gráfico.
    Pode passar um dicionário - { }
    Pode passar objetos do plotly.

```
data = [go.Bar(x=[1, 2, 4], y=[1, 3, 2])]
```

**Layout**: 
Define tamanho, tipo, como irá se comportar.

```
layout = go.Layout(
        title = go.layout.Title(text='A Figure Specified By a Graph object')
        )
```

**Frames:**
Usado mais para animações.
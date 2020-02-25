from PIL import Image, ImageDraw, ImageFont

# test vars
titleText = "CARDÁPIO GOIABEIRAS"
dateText = "25 de fevereiro, 2020"

data = [
    {
        'title': 'Salada',
        'text': 'Alface e Tomate'
    },
    {
        'title': 'Prato Principal',
        'text': 'Lasanha de Frango'
    },
    {
        'title': 'Opção',
        'text': 'Lasanha de Proteina de Soja'
    },
    {
        'title': 'Acompanhamento',
        'text': 'Arroz Branco, Arroz Integral e Feijão'
    },
    {
        'title': 'Guarnição',
        'text': 'Purê de Inhame'
    },
    {
        'title': 'Sobremesa',
        'text': 'Banana'
    }
]

footerText = "Texto debaixo que nao sei oq vai vir nessa porra"

height = 100 + 50 + round(((2+len(data)) * 100) / 2)

# main image
img = Image.new('RGB', (1000, height), color=(255, 255, 255))

# main fonts: title and text
fntBold = ImageFont.truetype('./assets/fonts/Roboto-Bold.ttf', 30)
fntRegular = ImageFont.truetype('./assets/fonts/Roboto-Regular.ttf', 20)

# header and footer
header = Image.open('./templates/red-header.png')
footer = Image.open('./templates/dark-footer.png')

# ----------
# MAIN DRAW

# header draw
draw = ImageDraw.Draw(header)

draw.text((150, 20), titleText.upper(), font=fntBold, fill=(255, 255, 255))
draw.text((150, 60), dateText, font=fntRegular, fill=(255, 255, 255))

img.paste(header, (0, 0))


# data draw
logic = False
yOffset = 50

for i, elem in enumerate(data):
    imgElem = Image.new('RGB', (500, 100), color=(255, 255, 255))
    draw = ImageDraw.Draw(imgElem)
    draw.text((100, 20), elem['title'].upper(), font=fntBold, fill=(51, 51, 51))
    draw.text((100, 60), elem['text'], font=fntRegular, fill=(100, 100, 100))

    if logic:
        img.paste(imgElem, (450, 100 + (i * yOffset)))
    else:
        img.paste(imgElem, (0, 100 + ((i+1) * yOffset)))

    logic = not logic


# footer draw
draw = ImageDraw.Draw(footer)

draw.text((50, 20), footerText, font=fntRegular, fill=(255, 255, 255))

img.paste(footer, (0, height - 50))

# saving
img.save('output.png')

# END
# ----------

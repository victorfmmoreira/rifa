from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

NUMERO_DE_COPIAS = 1
NOME_DA_IMAGEM_ORIGINAL = "rifa.png"
NOME_DAS_IMAGENS_DE_SAIDA = "rifa"
POSICAO_DO_TEXTO_1 = (80,40)
POSICAO_DO_TEXTO_2 = (530,302)
ARQUIVO_DA_FONTE = "Best in class.otf"
TAMANHO_DA_FONTE = 24
COR_DA_FONTE = "red"

image = Image.open(NOME_DA_IMAGEM_ORIGINAL)

for i in range(1, NUMERO_DE_COPIAS + 1):
	copy = image.copy()

	draw = ImageDraw.Draw(copy)
	font = ImageFont.truetype(ARQUIVO_DA_FONTE, TAMANHO_DA_FONTE)
	numeracao = "%.3i" % i
	text = str(numeracao)
	draw.text(POSICAO_DO_TEXTO_1, text, COR_DA_FONTE, font=font)
	draw.text(POSICAO_DO_TEXTO_2, text, COR_DA_FONTE, font=font)

	#copy.show()
	filename = NOME_DAS_IMAGENS_DE_SAIDA + str(numeracao) + ".png";
	copy.save(filename, "png")
	copy.close()


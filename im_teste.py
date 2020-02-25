from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

NUMERO_DE_COPIAS = 1
NOME_DA_IMAGEM_ORIGINAL = "rifa.png"
NOME_DAS_IMAGENS_DE_SAIDA = "rifa"

POSICAO_DA_NUMERACAO_1 = (80,40)
POSICAO_DA_NUMERACAO_2 = (530,302)

MENSAGEM_DO_PREMIO = "Um grande prêmio"
POSICAO_DO_PREMIO = (550,18)

MENSAGEM_DA_DATA = "04/04/2020"
POSICAO_DA_DATA = (1080,360)

MENSAGEM_DO_VALOR = "R$1.400,00"
POSICAO_DO_VALOR = ( 1000,POSICAO_DA_DATA[1] )

ARQUIVO_DA_FONTE = "Best in class.otf"
TAMANHO_DA_FONTE = 24
COR_DA_FONTE = "red"

class texto:
	def __init__(self, mensagem):
		self.mensagem = mensagem
	
	posicao = (0,0)
	arquivo_da_fonte = ARQUIVO_DA_FONTE
	tamanho = TAMANHO_DA_FONTE
	cor_da_fonte = COR_DA_FONTE

	def get_parametros_do_draw(): 
		return [self.posicao, self.mensagem, self.cor_da_fonte,  self.arquivo_da_fonte, ] 

image = Image.open(NOME_DA_IMAGEM_ORIGINAL)

for i in range(1, NUMERO_DE_COPIAS + 1):
	copy = image.copy()

	draw = ImageDraw.Draw(copy)
	font = ImageFont.truetype(ARQUIVO_DA_FONTE, TAMANHO_DA_FONTE)
	numeracao = "%.3i" % i
	text = str(numeracao)
	draw.text(POSICAO_DA_NUMERACAO_1, text, COR_DA_FONTE, font=font)
	draw.text(POSICAO_DA_NUMERACAO_2, text, COR_DA_FONTE, font=font)

	#copy.show()
	filename = NOME_DAS_IMAGENS_DE_SAIDA + str(numeracao) + ".png";
	copy.save(filename, "png")
	copy.close()


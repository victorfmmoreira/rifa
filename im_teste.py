from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

NUMERO_DE_COPIAS = 1
NOME_DA_IMAGEM_ORIGINAL = "rifa.png"
NOME_DAS_IMAGENS_DE_SAIDA = "rifa"
ARQUIVO_DA_FONTE = "Best in class.otf"
COR_DA_FONTE = "red"
FORMATO = "png"
NUMERO_DE_DIGITOS = "3"

TAMANHO_DA_FONTE = 24

POSICAO_DA_NUMERACAO_1 = (80,40)
POSICAO_DA_NUMERACAO_2 = (530,302)

MENSAGEM_DO_PREMIO = "UM GRANDE PRÊMIO\n PRA QUEM GANHAR"
POSICAO_DO_PREMIO = (780,145)

MENSAGEM_DA_DATA = "04/04/20"
POSICAO_DA_DATA = (800,300)

MENSAGEM_DO_VALOR = "R$2,00"
POSICAO_DO_VALOR = ( 990,POSICAO_DA_DATA[1] )

class texto:
	def __init__(self, mensagem, posicao):
		self.mensagem = mensagem
		self.posicao = posicao
	
	arquivo_da_fonte = ARQUIVO_DA_FONTE
	tamanho = TAMANHO_DA_FONTE
	cor_da_fonte = COR_DA_FONTE

	def get_font(self):
		return ImageFont.truetype(self.arquivo_da_fonte, self.tamanho)

	def get_parametros_do_draw(self): 
		return [self.posicao, self.mensagem, self.cor_da_fonte, self.get_font() ] 

image = Image.open(NOME_DA_IMAGEM_ORIGINAL)

premio = texto(MENSAGEM_DO_PREMIO, POSICAO_DO_PREMIO)
premio.tamanho += 10
data = texto( MENSAGEM_DA_DATA, POSICAO_DA_DATA)
valor = texto( MENSAGEM_DO_VALOR, POSICAO_DO_VALOR)


for i in range(1, NUMERO_DE_COPIAS + 1):
	copy = image.copy()

	draw = ImageDraw.Draw(copy)
	numeracao = ("%." + NUMERO_DE_DIGITOS + "i") % i
	text = str(numeracao)

	numeracao_1 = texto(text, POSICAO_DA_NUMERACAO_1)

	numeracao_2 = texto(text, POSICAO_DA_NUMERACAO_2)

	draw.text(*numeracao_1.get_parametros_do_draw() )
	draw.text(*numeracao_2.get_parametros_do_draw() )
	draw.text(*premio.get_parametros_do_draw() )
	draw.text(*data.get_parametros_do_draw() )
	draw.text(*valor.get_parametros_do_draw() )

	#copy.show()
	filename = NOME_DAS_IMAGENS_DE_SAIDA + str(numeracao) + "." + FORMATO;
	copy.save(filename, FORMATO)
	copy.close()


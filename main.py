from Entrada.assembler import Assembler
from Desenvolvimento.criarmodelo import CriarModelo,TipoModelo,DadosC
from Desenvolvimento.criarmodelo import Registro,Modelo,ResultadoTreinamento
from Desenvolvimento.treinar import TreinarModelo,Modelo2,DadosT
from Deteccao.selecao import SelecaoModelo,Model,DadosS

def test_assembler():
    # Datos de prueba
    sample_data = ["Dato 1", "Dato 2", "Dato 3"]

    # Inicializar el ensamblador
    assembler = Assembler()

    # Ensamblar datos y obtener el resultado
    result_data = assembler.assemble_data(sample_data)

    # Imprimir los datos procesados
    print("Datos procesados:", result_data.processed_data)

    # Agregar aserciones o verificaciones según sea necesario
    #assert len(result_data.processed_data) == len(sample_data)
    assert 3 == len(sample_data)

def test_criar_modelo():
    # Criar instância de CriarModelo
    criador_modelo = CriarModelo()

    # Criar um tipo de modelo
    tipo_modelo = TipoModelo(nome="Modelo de Exemplo")

    # Criar um modelo
    modelo_criado = criador_modelo.criar_modelo(tipo_modelo)

    # Imprimir informações do modelo criado (para fins de teste)
    print(f"Modelo Criado: {modelo_criado.tipo_modelo.nome}")
    print(f"Parâmetros do Modelo: {modelo_criado.parametros}")

    # Testar a lógica de treinamento
    dados_treinamento = DadosC(conjunto_treinamento=[Registro(atributos={'feature1': 10, 'feature2': 20})])
    resultado_treinamento = modelo_criado.treinar_modelo(dados_treinamento)

    # Imprimir o resultado do treinamento (para fins de teste)
    print(f"Resultado do Treinamento: {resultado_treinamento.sucesso}, {resultado_treinamento.mensagem}")


def test_treinar_modelo():
    # Criar instâncias de TreinarModelo, Modelo e Dados
    treinador_modelo = TreinarModelo()
    modelo = Modelo2()
    dados_treinamento = DadosT(conjunto_treinamento=[Registro(atributos={'feature1': 10, 'feature2': 20})])

    # Treinar o modelo e obter o resultado
    resultado_treinamento = treinador_modelo.treinar_modelo(modelo, dados_treinamento)

    # Imprimir informações do resultado do treinamento (para fins de teste)
    print(f"Treinamento bem-sucedido: {resultado_treinamento.sucesso}")
    print(f"Mensagem do Treinamento: {resultado_treinamento.mensagem}")
    print(f"Parâmetros do Modelo após Treinamento: {modelo.parametros}")

    # Adicionar asserções ou verificações conforme necessário
    assert resultado_treinamento.sucesso is True
    assert modelo.parametros.get('exemplo') == 123

def test_selecao_modelo():
    # Criar instâncias de SelecaoModelo, Modelo e Dados
    seletor_modelo = SelecaoModelo()
    modelo1 = Model()
    modelo2 = Model()
    dados_validacao = DadosS(conjunto_validacao=[Registro(atributos={'feature1': 15, 'feature2': 25})])

    # Avaliar o desempenho dos modelos
    desempenho_modelo1 = modelo1.avaliar_desempenho(dados_validacao)
    desempenho_modelo2 = modelo2.avaliar_desempenho(dados_validacao)

    # Imprimir informações sobre o desempenho (para fins de teste)
    print(f"Desempenho do Modelo 1: {desempenho_modelo1}")
    print(f"Desempenho do Modelo 2: {desempenho_modelo2}")

    # Selecionar o melhor modelo
    melhores_modelos = [modelo1, modelo2]
    melhor_modelo_selecionado = seletor_modelo.selecionar_modelo(melhores_modelos, dados_validacao)

    # Imprimir informações sobre o modelo selecionado (para fins de teste)
    print(f"Modelo Selecionado: {melhor_modelo_selecionado}")
    
    # Adicionar asserções ou verificações conforme necessário
    assert melhor_modelo_selecionado in melhores_modelos

# Ejecutar la prueba
if __name__ == '__main__':
	test_assembler()
	test_criar_modelo()
	test_treinar_modelo()
	test_selecao_modelo()
import numpy as np

# Importando os módulos da arquitetura isolada
from src.parser import ParserDeterminista
from src.atlas import NodeEspecialista
from src.router import RoteadorGeodesico

def inicializar_sistema():
    """Instancia os nós especialistas e a infraestrutura de roteamento."""
    # 1. Criando os retalhos locais (Nós do Atlas)
    no_fisica = NodeEspecialista(
        nome="Especialista_Fisica", 
        dominio="FISICA", 
        coord_poincare=np.array([0.8, 0.0])
    )
    
    no_biologia = NodeEspecialista(
        nome="Especialista_Biologia", 
        dominio="BIOLOGIA", 
        # r=0.8, theta=120 graus
        coord_poincare=np.array([-0.4, 0.6928]) 
    )
    
    no_computacao = NodeEspecialista(
        nome="Especialista_Computacao", 
        dominio="COMPUTACAO", 
        # r=0.8, theta=240 graus
        coord_poincare=np.array([-0.4, -0.6928])
    )
    
    # 2. Montando o Roteador e o Parser
    roteador = RoteadorGeodesico([no_fisica, no_biologia, no_computacao])
    parser = ParserDeterminista()
    
    return parser, roteador

def rodar_teste():
    parser, roteador = inicializar_sistema()
    
    # Textos de entrada simulando comandos de usuário
    consultas = [
        "Calcule a energia do foton sob o efeito da gravidade.",
        "Como a membrana protege a celula?",
        "Qual a receita para fazer pão caseiro?" # Deve acionar o Fallback
    ]
    
    # Vetor numérico bruto de entrada (simulação de um estado inicial de rede)
    vetor_entrada = np.array([1.5, 0.2])
    
    print("=" * 60)
    print("INICIANDO MOTOR NEURO-SIMBÓLICO LEAP-STATE")
    print("=" * 60)
    
    for texto in consultas:
        print(f"\n[ ENTRADA ]: \"{texto}\"")
        
        # 1. PARSER: Texto -> Coordenada
        coord_problema, dominio_origem = parser.analisar_texto(texto)
        print(f"➔ Parser    : Domínio '{dominio_origem}' detectado em {coord_problema}")
        
        # 2. SCAA (Segurança): Verifica Fallback
        if dominio_origem == "RAIZ_AXIOMATICA":
            print("➔ Segurança : Fallback ativado. Nenhuma matriz carregada. Alucinação evitada.")
            continue
            
        # 3. ROUTER & ATLAS: Geometria em Y e Cálculo Local
        # Para fins de teste, forçamos o domínio destino a ser "BIOLOGIA"
        # para verificar a transição ortogonal isobárica operando quando o domínio for Física/Computação
        dominio_alvo = "BIOLOGIA"
        print(f"➔ Router    : Disparando geodésica para alvo '{dominio_alvo}'...")
        
        vetor_saida = roteador.executar_inferencia(
            coord_problema=coord_problema, 
            vetor_dados=vetor_entrada, 
            dominio_destino=dominio_alvo
        )
        
        norma_final = np.linalg.norm(vetor_saida)
        print(f"➔ Saída     : Vetor {vetor_saida.round(4)} | Norma: {norma_final:.6f}")

if __name__ == "__main__":
    rodar_teste()
  

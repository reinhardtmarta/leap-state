import numpy as np
from .geometry import poincare_dist
from .atlas import NodeEspecialista, TRANSICAO_FISICA_BIO

class RoteadorGeodesico:
    def __init__(self, especialistas: list):
        self.especialistas = especialistas

    def executar_inferencia(self, coord_problema: np.ndarray, vetor_dados: np.ndarray, dominio_destino: str):
        # 1. Roteamento em Y: Calcula menor caminho
        distancias = [(poincare_dist(coord_problema, esp.coord), esp) for esp in self.especialistas]
        distancias.sort(key=lambda x: x[0])
        _, especialista_eleito = distancias[0]

        # 2. Invocação do Retalho Local
        resultado_local = especialista_eleito.processar_inferencia_local(vetor_dados)

        # 3. Transição de Domínio (se necessário)
        if especialista_eleito.dominio != dominio_destino:
            vetor_final = TRANSICAO_FISICA_BIO @ resultado_local
        else:
            vetor_final = resultado_local

        return vetor_final
      

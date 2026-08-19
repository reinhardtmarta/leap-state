import numpy as np

# Matriz de transição ortogonal (Isométrica - Preserva a norma)
TRANSICAO_FISICA_BIO = np.array([
    [0.8, -0.6],
    [0.6,  0.8]
])

class NodeEspecialista:
    def __init__(self, nome: str, dominio: str, coord_poincare: np.ndarray):
        self.nome = nome
        self.dominio = dominio
        self.coord = coord_poincare
        
    def processar_inferencia_local(self, vetor_entrada: np.ndarray) -> np.ndarray:
        """Processamento linear no plano do retalho (baixo custo)."""
        peso_especialista = np.array([[1.1, 0.05], [0.0, 0.95]])
        return peso_especialista @ vetor_entrada
      

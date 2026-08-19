import numpy as np
import re

# Taxonomia Base (Exemplo Open Source)
# Em produção, este dicionário será carregado a partir de arquivos JSON em /proprietary_data/
TAXONOMIA_ABERTA = {
    "FISICA": ["energia", "massa", "foton", "geodesica", "gravidade"],
    "BIOLOGIA": ["celula", "dna", "membrana", "ionico", "proteina"],
    "COMPUTACAO": ["algoritmo", "vetor", "pipeline", "matriz", "determinismo"]
}

# Coordenadas polares mapeadas no Disco de Poincaré
COORDENADAS_DOMINIO = {
    "FISICA": (0.8, 0.0),                  # 0 radianos
    "BIOLOGIA": (0.8, 2 * np.pi / 3),      # 120 graus
    "COMPUTACAO": (0.8, 4 * np.pi / 3)     # 240 graus
}

class ParserDeterminista:
    def __init__(self, taxonomia=TAXONOMIA_ABERTA):
        """Inicializa o parser. Permite injetar uma taxonomia privada se necessário."""
        self.taxonomia = taxonomia

    def analisar_texto(self, texto: str) -> tuple:
        """Converte texto natural em uma coordenada geodésica determinística."""
        # Limpeza e extração de palavras
        palavras_usuario = set(re.findall(r'\b[a-z_]+\b', texto.lower()))
        
        dominio_detectado = None
        
        # Interseção matemática (sem probabilidade ou 'chute')
        for dominio, palavras_chave in self.taxonomia.items():
            if palavras_usuario.intersection(set(palavras_chave)):
                dominio_detectado = dominio
                break
                
        # ==========================================
        # CIRCUIT BREAKER / ROTA DE FUGA
        # ==========================================
        if not dominio_detectado:
            # Aborta o salto e ancora na raiz axiomática do disco
            return np.array([0.0, 0.0]), "RAIZ_AXIOMATICA"
            
        # Cálculo trigonométrico da projeção polar -> cartesiana
        r, theta = COORDENADAS_DOMINIO[dominio_detectado]
        x = r * np.cos(theta)
        y = r * np.sin(theta)
        
        return np.array([x, y]), dominio_detectado
      

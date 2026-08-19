import numpy as np

def poincare_dist(u: np.ndarray, v: np.ndarray, eps: float = 1e-7) -> float:
    """Calcula a distância geodésica rigorosa no disco unitário."""
    norm_u = np.sum(u ** 2)
    norm_v = np.sum(v ** 2)
    diff_norm = np.sum((u - v) ** 2)
    
    # Prevenção de divisão por zero e explosão numérica
    delta = 1.0 + 2.0 * diff_norm / ((1.0 - norm_u + eps) * (1.0 - norm_v + eps))
    return float(np.arccosh(np.maximum(1.0, delta)))
  

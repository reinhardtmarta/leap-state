# Leap-State Architecture

**[🇺🇸 English](#english) | [🇧🇷 Português](#português)**

---

<h2 id="english">🇺🇸 English</h2>

**Deterministic Geodesic Routing and Local Atlas Manifolds for AI.**

The **Leap-State** architecture is a neuro-symbolic inference engine that replaces the dense Euclidean grid of traditional models with hierarchical routing in the Poincaré Disk. By using a Y-bifurcation distribution and isometric transitions between local patches (Manifold Atlas), the system drastically cuts computational load and enforces axiomatic consistency.

### The Hardware Bottleneck: Where Academic Hyperbolic AI Failed
State-of-the-art research in Hyperbolic Neural Networks (HNNs) shares a massive blind spot: **hardware incompatibility**. Academic papers build mathematically elegant, purely non-Euclidean models that destroy GPU/TPU performance because modern silicon chips are highly optimized for flat, linear matrix multiplication. They created beautiful theory that is computationally unviable for production.

The **Leap-State** architecture bridges this exact gap by decoupling topology from raw compute. Instead of forcing heavy Riemannian geometry onto the entire pipeline, it divides the workload into a lightweight hyperbolic routing index and fast, isolated local Euclidean patches.


### The Leap-State Solution
The system isolates computation through three mathematical mechanics:
*   **Poincaré Disk Mapping**: Queries are deterministically converted into polar coordinates $(r, \theta)$, where the boundary represents hyper-specific knowledge and the center $(0,0)$ is the axiomatic containment root (Deterministic Fallback).
*   **Geodesic Routing ($Y$)**: Information travels via the shortest hyperbolic path, activating **only** the relevant expert node.
*   **Local Manifold Atlas**: The expert node calculates the response in a fast local Euclidean plane. Domain transitions apply isomorphic orthogonal matrices, ensuring **Zero Metric Distortion** ($< 2 \times 10^{-16}$).

### Load Benchmark (10,000 Inferences Simulation)
The proof-of-concept test contrasts the cost of a fully connected traditional mesh against the segmented routing of the Leap-State architecture.

| Metric | Traditional Architecture (Dense) | Leap-State Architecture |
| :--- | :--- | :--- |
| **Operations (FLOPs)** | 90,000,000,000 | 8,981,000,000 |
| **Circuit Breaker** | Non-existent (Hallucinates) | Blocks at Root $(0,0)$ |
| **Load Reduction** | - | **90.02%** |

*Savings resulting directly from geodesic routing without data integrity loss.*

### Repository Structure
The mathematical core is open source. Business data, taxonomies, and proprietary logic (SCAA) operate in strict isolation.

```text
/leap-state
├── /src                    # Mathematical Core (Geometry, Router, Atlas)
├── /tests                  # Unit Tests and Circuit Breaker
├── /benchmarks             # FLOPs Validation Scripts
├── /proprietary_data       # Git Ignored (Private Taxonomies and Weights)
└── README.md

```

# Leap-State Architecture

<h2 id="português">🇧🇷 Português</h2>

**Roteamento Geodésico Determinístico e Atlas de Retalhos Locais para IA.**

A arquitetura **Leap-State** é um motor de inferência neuro-simbólico que substitui a grade euclidiana densa dos modelos tradicionais por um roteamento hierárquico no Disco de Poincaré. Ao utilizar uma distribuição em bifurcação ($Y$) e transições isométricas entre retalhos locais (Manifold Atlas), o sistema corta a carga computacional e força consistência axiomática.

### O Gargalo de Hardware: Onde a Pesquisa Acadêmica de IA Hiperbólica Falhou
As pesquisas de ponta em Redes Neurais Hiperbólicas (HNNs) compartilham um ponto cego massivo: **a incompatibilidade com o hardware**. Artigos acadêmicos constroem modelos matematicamente elegantes e puramente não-euclidianos que destroem a performance de GPUs/TPUs, pois os chips de silício modernos são otimizados exclusivamente para multiplicação de matrizes lineares planas. Eles criaram uma teoria bonita, mas computacionalmente inviável para produção.

A arquitetura **Leap-State** resolve exatamente essa ponte ao desacoplar a topologia do cálculo bruto. Em vez de forçar uma geometria Riemanniana pesada em todo o pipeline, o sistema divide a carga de trabalho em um índice de roteamento hiperbólico leve e retalhos euclidianos locais rápidos e isolados.

## A Solução Leap-State
O sistema isola o cálculo através de três mecânicas matemáticas:
*   **Mapeamento em Disco de Poincaré:** Consultas são convertidas deterministicamente em coordenadas polares $(r, \theta)$, onde a borda é o conhecimento hiperespecífico e o centro $(0,0)$ é a raiz axiomática de contenção (Fallback determinístico).
*   **Roteamento Geodésico ($Y$):** A informação viaja pelo menor caminho hiperbólico, ativando **apenas** o nó especialista relevante.
*   **Atlas por Retalhos Locais:** O nó especialista calcula a resposta em um plano local euclidiano rápido. Transições de domínio aplicam matrizes ortogonais isomórficas, garantindo **Distorção Métrica Zero** ($< 2 \times 10^{-16}$).

## Benchmark de Carga (Simulação de 10.000 Inferências)
O teste de prova de conceito contrasta o custo de uma malha tradicional inteiramente conectada contra o roteamento segmentado da arquitetura Leap-State.

| Métrica | Arquitetura Tradicional (Densa) | Arquitetura Leap-State |
| :--- | :--- | :--- |
| **Operações (FLOPs)** | 90.000.000.000 | 8.981.000.000 |
| **Circuit Breaker** | Inexistente (Alucina) | Bloqueio em Raiz $(0,0)$ |
| **Redução de Carga** | - | **90.02%** |

*Economia resultante diretamente do roteamento geodésico sem perda de integridade dos dados.*

## Estrutura do Repositório
O núcleo matemático é aberto. Dados de negócio, taxonomias e lógicas proprietárias (SCAA) operam em isolamento rigoroso.

```text
/leap-state
├── /src                    # Núcleo Matemático (Geometria, Router, Atlas)
├── /tests                  # Testes Unitários e Circuit Breaker
├── /benchmarks             # Scripts de Validação de FLOPs
├── /proprietary_data       # Ignorado pelo Git (Taxonomias e Pesos)
└── README.md

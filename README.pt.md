# Leap-State Architecture

<h2 id="português">🇧🇷 Português</h2>

**Roteamento Geodésico Determinístico e Atlas de Retalhos Locais para IA.**

A arquitetura **Leap-State** é um motor de inferência neuro-simbólico que substitui a grade euclidiana densa dos modelos tradicionais por um roteamento hierárquico no Disco de Poincaré. Ao utilizar uma distribuição em bifurcação ($Y$) e transições isométricas entre retalhos locais (Manifold Atlas), o sistema corta a carga computacional e força consistência axiomática.

## O Gargalo Atual (Por que não usar Transformers Densos?)
Modelos de linguagem comerciais baseiam-se em atenção total (*All-to-All / Dense*), operando sob geometria euclidiana plana. Isso exige que o hardware calcule relações entre todos os parâmetros na rede em tempo de inferência, gerando:
1.  **Custo Quadrático $O(N^2)$**: Desperdício massivo de energia elétrica e FLOPs em caminhos não relacionados à consulta.
2.  **Distorção Métrica**: Tentativas de forçar topologias complexas em matrizes planas globais causam dilatação de coordenadas e alucinação estrutural.

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

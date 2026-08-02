# Product Requirements Document — Knowledge Guardian

**Versão:** 0.1  
**Status:** Draft  
**Data:** 2026-08-02  
**Product Owner:** Jader Greiner  
**Responsável pelo documento:** Product Management  

---

## 1. Resumo executivo

O **Knowledge Guardian** é um framework reutilizável e uma skill para agentes de IA voltada à governança de conhecimento em repositórios de software.

Seu propósito é analisar, validar e melhorar a arquitetura de conhecimento de um repositório, tornando documentação, decisões arquiteturais, ontologias, glossários, especificações, runbooks e instruções para agentes mais consistentes, confiáveis, navegáveis e adequadas ao consumo por humanos e sistemas de IA.

A primeira versão do produto deve entregar um fluxo completo de descoberta, classificação, análise e geração de relatório, sem modificar arquivos automaticamente. O produto deve priorizar evidência, rastreabilidade e baixo risco de falsos positivos.

---

## 2. Contexto

Repositórios modernos são consumidos por desenvolvedores, arquitetos, product managers, operadores e agentes autônomos. Entretanto, o conhecimento necessário para compreender e alterar um sistema costuma estar distribuído entre documentos, código, schemas, decisões, comentários e instruções de agentes.

Esse cenário cria **dívida de conhecimento**, caracterizada por:

- múltiplas fontes que disputam autoridade;
- terminologia inconsistente;
- documentação desatualizada;
- decisões sem evidência ou aprovação explícita;
- arquivos órfãos;
- links quebrados;
- divergência entre intenção, especificação e implementação;
- ausência de sinais de confiança;
- contexto de agentes espalhado por diferentes arquivos;
- dificuldade para determinar o que é conceitual, vigente ou executável.

Esses problemas aumentam o custo de manutenção e onboarding, reduzem a velocidade de engenharia e fazem agentes de IA operar com contexto incompleto ou contraditório.

---

## 3. Problema de produto

### 3.1 Problema principal

Equipes e agentes de IA não conseguem determinar de forma confiável:

- onde iniciar a leitura de um repositório;
- qual documento é a fonte canônica de um assunto;
- quais informações estão vigentes;
- o que representa intenção, especificação ou comportamento implementado;
- quais decisões foram verificadas por pessoas;
- quais documentos possuem evidência suficiente;
- quais relações existem entre os artefatos de conhecimento.

### 3.2 Consequências

- implementação baseada em documentos obsoletos;
- decisões arquiteturais conflitantes;
- duplicação de conceitos e regras;
- aumento do tempo de descoberta e onboarding;
- respostas inconsistentes de agentes de IA;
- retrabalho em reviews e planejamento;
- baixa auditabilidade;
- degradação progressiva da arquitetura de conhecimento.

---

## 4. Visão do produto

Transformar repositórios de software em ambientes nos quais humanos e agentes de IA consigam navegar, interpretar e utilizar conhecimento com confiança.

### 4.1 Proposta de valor

O Knowledge Guardian permite que uma equipe:

1. descubra os artefatos de conhecimento existentes;
2. identifique fontes canônicas, conflitos e lacunas;
3. diferencie intenção, especificação, execução e operação;
4. avalie metadados e sinais de confiança;
5. detecte problemas de navegação e consistência semântica;
6. receba propostas de melhoria fundamentadas em evidências;
7. aplique mudanças somente após aprovação humana.

### 4.2 Posicionamento

O Knowledge Guardian não é um linter genérico de Markdown nem um gerador automático de documentação.

Ele é uma camada de governança de conhecimento orientada a repositórios consumidos por humanos e agentes autônomos.

---

## 5. Objetivos

### 5.1 Objetivos da versão inicial

- mapear os principais artefatos de conhecimento de um repositório;
- classificar documentos por tipo e camada;
- identificar documentos órfãos e referências quebradas;
- verificar metadados mínimos e sinais de confiança;
- detectar fontes canônicas declaradas e possíveis conflitos;
- gerar relatório estruturado em Markdown e JSON;
- apresentar evidências, severidade, confiança e recomendação para cada finding;
- operar em modo somente leitura por padrão;
- permitir configuração por perfil de projeto.

### 5.2 Objetivos de médio prazo

- detectar inconsistência terminológica e drift semântico;
- comparar documentação com schemas, testes e contratos executáveis;
- gerar e exportar grafo de conhecimento;
- integrar com CLI, pull requests e CI/CD;
- suportar regras customizadas e pacotes de governança;
- alimentar workflows multiagentes.

---

## 6. Não objetivos

A versão inicial não deve:

- reescrever documentos automaticamente;
- substituir decisões humanas de arquitetura ou produto;
- declarar uma documentação correta sem evidência;
- inferir comportamento de runtime apenas a partir de documentação;
- impor um schema universal a todos os projetos;
- analisar profundamente a qualidade do código-fonte;
- atuar como ferramenta completa de observabilidade;
- construir automaticamente uma ontologia de domínio definitiva;
- bloquear pipelines com base em findings de baixa confiança.

---

## 7. Usuários e personas

### 7.1 Arquiteto de Software ou IA

**Necessidade:** entender decisões, fontes canônicas, limites conceituais e divergências entre arquitetura pretendida e implementada.

**Valor esperado:** redução de ambiguidades e maior confiança em mudanças arquiteturais.

### 7.2 Tech Lead ou Engenheiro Sênior

**Necessidade:** localizar rapidamente documentação vigente, contratos, runbooks e contexto para implementação.

**Valor esperado:** menos retrabalho, onboarding mais rápido e reviews mais objetivos.

### 7.3 Product Manager ou Product Owner

**Necessidade:** garantir coerência entre visão, requisitos, especificações e execução.

**Valor esperado:** identificação de drift entre estratégia, produto e implementação.

### 7.4 Maintainer de projeto open source

**Necessidade:** manter documentação navegável, confiável e adequada para contribuição externa.

**Valor esperado:** menor custo de manutenção e melhor experiência para contribuidores.

### 7.5 Agente de IA

**Necessidade:** determinar onde começar, quais fontes são autoritativas, o que está vigente e quais ações são permitidas.

**Valor esperado:** contexto mais seguro, preciso e rastreável.

---

## 8. Jobs to Be Done

### JTBD-01 — Descobrir a arquitetura de conhecimento

Quando eu iniciar trabalho em um repositório, quero identificar seus documentos, tipos, relações e pontos de entrada, para compreender onde o conhecimento está localizado.

### JTBD-02 — Determinar autoridade

Quando houver múltiplos documentos sobre o mesmo assunto, quero saber qual é a fonte canônica e onde existem conflitos, para evitar decisões baseadas em informações incorretas.

### JTBD-03 — Avaliar confiabilidade

Quando eu utilizar um documento para tomar uma decisão, quero conhecer autoria, estado, fontes, verificação e validade, para avaliar o nível de confiança daquele conteúdo.

### JTBD-04 — Preparar contexto para agentes

Quando um agente de IA operar em um repositório, quero que ele consiga distinguir intenção, especificação, runtime e regras operacionais, para reduzir ações incorretas.

### JTBD-05 — Propor remediações

Quando forem encontrados problemas de conhecimento, quero receber recomendações priorizadas e sustentadas por evidências, para corrigir a causa sem criar mudanças desnecessárias.

---

## 9. Escopo da versão 0.1

A versão 0.1 deve implementar um vertical slice completo para repositórios locais ou disponibilizados em workspace acessível ao agente.

### 9.1 Incluído

- descoberta de arquivos de documentação;
- suporte inicial a Markdown e YAML;
- identificação de entry points comuns;
- classificação básica de documentos;
- extração de links internos;
- validação de referências;
- detecção de documentos órfãos;
- validação de metadados configuráveis;
- identificação de sinais de confiança;
- detecção inicial de fontes canônicas declaradas;
- geração de findings;
- geração de relatório Markdown;
- geração de relatório JSON;
- configuração por perfil de projeto;
- execução em modo proposal-first e read-only.

### 9.2 Fora do escopo

- análise semântica baseada em embeddings;
- comparação profunda com código e infraestrutura;
- criação automática de pull requests;
- interface gráfica;
- dashboard web;
- integração nativa com Obsidian;
- bloqueio de CI/CD;
- edição automática de arquivos;
- suporte completo a múltiplos repositórios.

---

## 10. Fluxo principal

```text
Selecionar repositório
        ↓
Carregar perfil do projeto
        ↓
Descobrir documentos
        ↓
Classificar artefatos
        ↓
Extrair metadados e relações
        ↓
Executar regras
        ↓
Gerar findings com evidências
        ↓
Priorizar findings
        ↓
Gerar relatório Markdown e JSON
        ↓
Apresentar propostas
        ↓
Aguardar decisão humana
```

---

## 11. Requisitos funcionais

### RF-001 — Descoberta de documentos

O produto deve localizar arquivos relevantes à arquitetura de conhecimento dentro do repositório.

**Critérios de aceite:**

- reconhecer ao menos arquivos `.md`, `.mdx`, `.yaml` e `.yml`;
- respeitar diretórios ignorados configuráveis;
- registrar caminho, extensão, tamanho e data de modificação quando disponível;
- permitir limite de profundidade de varredura.

### RF-002 — Identificação de entry points

O produto deve identificar documentos que funcionam como entrada principal para humanos ou agentes.

**Critérios de aceite:**

- detectar nomes comuns, como `README.md`, `AGENTS.md`, `CONTRIBUTING.md` e arquivos configurados no perfil;
- marcar entry points ausentes;
- indicar quando há múltiplos entry points sem hierarquia clara.

### RF-003 — Classificação de documentos

O produto deve classificar documentos por tipo e camada de conhecimento.

**Tipos iniciais:**

- product vision;
- governance;
- architecture;
- ADR;
- specification;
- ontology;
- glossary;
- runbook;
- agent context;
- operational documentation;
- general documentation;
- unknown.

**Camadas iniciais:**

- conceptual;
- specification;
- executable knowledge;
- operational;
- agent context;
- unknown.

### RF-004 — Extração e validação de links

O produto deve extrair referências internas e verificar seus destinos.

**Critérios de aceite:**

- identificar links relativos em Markdown;
- resolver caminhos relativos ao documento de origem;
- registrar links válidos e quebrados;
- não consultar links externos na versão inicial;
- incluir origem e destino no finding.

### RF-005 — Detecção de documentos órfãos

O produto deve identificar documentos sem caminho de navegação conhecido a partir dos entry points.

**Critérios de aceite:**

- construir um grafo de links internos;
- calcular alcançabilidade a partir dos entry points;
- diferenciar documentos órfãos de arquivos explicitamente excluídos;
- apresentar evidência de ausência de caminho navegável.

### RF-006 — Validação de metadados

O produto deve validar metadados conforme regras do perfil do projeto.

**Campos sugeridos, mas configuráveis:**

- type;
- title;
- description;
- owner;
- status;
- version;
- generated.by;
- generated.at;
- verified.by;
- verified.at;
- sources;
- stale_after.

**Critérios de aceite:**

- não exigir o mesmo conjunto de campos para todos os tipos;
- permitir regras obrigatórias, recomendadas e opcionais;
- indicar o campo ausente e a regra violada;
- preservar documentos sem front matter quando o perfil permitir.

### RF-007 — Análise de sinais de confiança

O produto deve avaliar se um documento permite determinar autoria, estado, evidência, revisão e validade.

**Critérios de aceite:**

- produzir um resumo dos sinais encontrados;
- gerar finding quando um sinal obrigatório estiver ausente;
- não inferir verificação humana apenas pela existência do arquivo;
- diferenciar conteúdo gerado de conteúdo verificado.

### RF-008 — Detecção inicial de fontes canônicas

O produto deve reconhecer fontes canônicas declaradas no perfil ou nos metadados.

**Critérios de aceite:**

- listar fontes canônicas por assunto;
- detectar mais de uma fonte canônica declarada para o mesmo assunto;
- reportar conflito sem selecionar automaticamente um vencedor;
- indicar a evidência usada na detecção.

### RF-009 — Modelo de findings

Cada finding deve conter, no mínimo:

```yaml
id: KG-RULE-001:document-path
rule_id: KG-RULE-001
category: Broken reference
severity: High
confidence: high
summary: Reference target does not exist
location:
  file: docs/architecture.md
  line: 42
evidence:
  - type: markdown_link
    value: ../decisions/ADR-001.md
impact: Agents and humans cannot reach the referenced decision
recommendation: Correct the path or restore the target document
status: open
```

### RF-010 — Priorização

O produto deve classificar findings por severidade e confiança.

**Severidades:**

- Critical;
- High;
- Medium;
- Low;
- Informational.

**Confiança:**

- high;
- medium;
- low.

**Critérios de aceite:**

- severidade e confiança devem ser campos distintos;
- findings de baixa confiança devem ser apresentados como hipótese de investigação;
- severidade deve considerar impacto e alcance;
- regras devem permitir configuração de severidade padrão.

### RF-011 — Relatório Markdown

O produto deve gerar um relatório legível por humanos contendo:

- sumário executivo;
- escopo analisado;
- limitações;
- inventário de documentos;
- mapa de entry points;
- findings priorizados;
- evidências;
- recomendações;
- próximos passos sugeridos.

### RF-012 — Relatório JSON

O produto deve gerar uma saída estruturada e versionada para automação futura.

**Critérios de aceite:**

- validar contra schema JSON;
- incluir versão do schema;
- incluir versão da ferramenta;
- registrar data e escopo da análise;
- suportar consumo por CLI, CI/CD e agentes.

### RF-013 — Perfil de projeto

O produto deve aceitar um arquivo de perfil para adaptar regras e terminologia.

**Exemplo:**

```yaml
profile:
  name: meu-pdi
  entry_points:
    - README.md
    - AGENTS.md
    - AI_CONTEXT.md
  canonical_sources:
    product_vision: docs/product/PRODUCT_VISION.md
    governance: AGENTS.md
  terminology:
    SDD: Spec-Driven Development
  ignored_paths:
    - node_modules/**
    - .git/**
```

### RF-014 — Modo somente leitura

Por padrão, o produto não deve modificar arquivos do repositório.

**Critérios de aceite:**

- nenhuma alteração deve ocorrer durante scan e report;
- propostas de remediação devem ser separadas de ações de escrita;
- futuras ações de escrita devem exigir autorização explícita.

---

## 12. Requisitos não funcionais

### RNF-001 — Determinismo

Execuções com a mesma versão, perfil e estado do repositório devem produzir resultados equivalentes para regras determinísticas.

### RNF-002 — Rastreabilidade

Todo finding deve apontar para evidência verificável, regra aplicada e localização do problema.

### RNF-003 — Extensibilidade

Novas regras, classificadores e reporters devem poder ser adicionados sem alterar o núcleo do produto.

### RNF-004 — Performance

A versão inicial deve analisar um repositório com até 5.000 documentos em tempo adequado para uso local, sem exigir infraestrutura distribuída.

A meta inicial de referência é concluir a análise estrutural em até 60 segundos em ambiente de desenvolvimento padrão, excluindo análises baseadas em LLM.

### RNF-005 — Segurança

- não executar código encontrado no repositório;
- não transmitir conteúdo para serviços externos sem configuração explícita;
- não registrar segredos detectados no conteúdo do relatório;
- tratar paths ignorados e arquivos sensíveis por configuração.

### RNF-006 — Auditabilidade

Cada execução deve registrar:

- versão da ferramenta;
- versão do schema;
- perfil utilizado;
- timestamp;
- escopo analisado;
- regras executadas;
- regras ignoradas;
- erros e limitações.

### RNF-007 — Portabilidade

A implementação inicial deve funcionar em Linux, macOS e Windows, preferencialmente através de Python 3.11 ou superior.

---

## 13. Categorias iniciais de findings

| Categoria | Descrição |
|---|---|
| Missing metadata | Metadado obrigatório ou recomendado está ausente |
| Weak trust signal | Autoria, revisão, fonte ou vigência não estão claras |
| Semantic inconsistency | Um termo possui significados conflitantes |
| Source conflict | Mais de um artefato reivindica autoridade sobre o mesmo assunto |
| Documentation drift | Documentação diverge de evidência executável |
| Broken reference | Uma referência aponta para destino inexistente |
| Orphan document | Um documento não é alcançável pelos entry points |
| Stale knowledge | O conteúdo ultrapassou a política de revisão |
| Duplicate knowledge | A mesma definição é mantida em mais de um local |
| Architectural ambiguity | Limites entre conceitos ou camadas estão pouco claros |
| Agent-context gap | Um agente não consegue determinar como operar com segurança |
| Improvement opportunity | Melhoria não bloqueante |

Na versão 0.1, devem ser implementadas prioritariamente as categorias `Missing metadata`, `Weak trust signal`, `Broken reference`, `Orphan document`, `Source conflict` e `Agent-context gap` básico.

---

## 14. Métricas de produto

### 14.1 North Star Metric

**Percentual de findings validados como úteis por revisores humanos.**

```text
findings úteis / findings revisados × 100
```

Essa métrica mede se o produto identifica problemas reais e acionáveis, evitando otimização por volume de alertas.

### 14.2 Métricas principais

| Métrica | Definição | Meta inicial |
|---|---|---|
| Finding usefulness rate | Findings considerados úteis por revisores | ≥ 80% |
| False-positive rate | Findings rejeitados por incorreção | ≤ 15% |
| Evidence coverage | Findings com evidência verificável | 100% |
| Scan completion rate | Execuções concluídas sem erro fatal | ≥ 95% |
| Entry-point reachability | Documentos alcançáveis a partir de entry points | Baseline por projeto |
| Canonical-source coverage | Assuntos críticos com fonte canônica definida | Baseline por projeto |
| Remediation acceptance rate | Recomendações aceitas por humanos | ≥ 60% |
| Time to first report | Tempo entre execução e relatório final | ≤ 60 s no escopo estrutural |

### 14.3 Guardrails

- nenhuma modificação automática sem autorização;
- nenhum finding sem evidência explícita;
- findings de baixa confiança não podem bloquear pipeline;
- ausência de metadados não deve ser tratada automaticamente como erro crítico;
- documentos conceituais não devem ser avaliados como contratos executáveis.

---

## 15. Critérios de sucesso da versão 0.1

A versão 0.1 será considerada bem-sucedida quando:

1. analisar o próprio repositório Knowledge Guardian;
2. analisar ao menos um repositório real adicional, preferencialmente Meu PDI;
3. gerar inventário e grafo básico de documentos;
4. detectar links quebrados e documentos órfãos com precisão validada;
5. validar metadados conforme perfil configurável;
6. gerar relatórios Markdown e JSON válidos;
7. apresentar findings com evidência, severidade e confiança;
8. atingir pelo menos 80% de findings considerados úteis nas validações iniciais;
9. demonstrar zero alterações automáticas durante execução padrão;
10. possuir testes automatizados para regras e schemas principais.

---

## 16. Riscos e mitigação

| Risco | Impacto | Mitigação |
|---|---|---|
| Alto volume de falsos positivos | Usuários deixam de confiar no produto | Regras determinísticas primeiro, confiança explícita e validação humana |
| Escopo excessivo | Produto não entrega um fluxo completo | Priorizar vertical slice estrutural na v0.1 |
| Dependência prematura de LLM | Baixa reprodutibilidade e aumento de custo | Separar regras determinísticas de análises probabilísticas |
| Schema rígido | Baixa adoção em projetos diferentes | Perfis configuráveis e campos por tipo documental |
| Confusão entre intenção e runtime | Findings incorretos | Classificação explícita por camada de conhecimento |
| Autoedição indevida | Risco de governança | Read-only por padrão e approval gate obrigatório |
| Performance em monorepos | Execução lenta | Ignored paths, cache e análise incremental futura |
| Exposição de conteúdo sensível | Risco de segurança | Execução local, redaction e configuração de arquivos sensíveis |

---

## 17. Dependências

### 17.1 Dependências técnicas iniciais

- parser de Markdown;
- parser YAML/front matter;
- resolução de caminhos;
- JSON Schema;
- mecanismo de configuração;
- framework de testes;
- geração de relatórios.

### 17.2 Dependências de produto

- definição inicial dos schemas;
- catálogo de regras v0.1;
- perfil genérico;
- perfil piloto do Knowledge Guardian;
- perfil piloto do Meu PDI;
- processo de revisão humana dos findings.

---

## 18. Roadmap inicial

### v0.1 — Knowledge discovery

- scanner de repositório;
- classificação básica;
- entry points;
- metadados;
- links quebrados;
- documentos órfãos;
- findings;
- relatório Markdown e JSON.

### v0.2 — Semantic consistency

- glossários;
- análise de termos conflitantes;
- comparação de fontes canônicas;
- classificação conceitual versus runtime;
- integração opcional com LLM.

### v0.3 — Knowledge graph

- extração de relações;
- grafo completo;
- análise de centralidade e alcançabilidade;
- exportação compatível com ferramentas externas.

### v0.4 — Configurable governance

- rule packs;
- schemas customizados;
- severidade por projeto;
- políticas de stale knowledge;
- extensão por plugins.

### v0.5 — CLI and automation

- CLI estável;
- diff entre análises;
- comentários em pull requests;
- integração CI/CD;
- gates configuráveis.

### v1.0 — Community-ready framework

- API estável de regras;
- skill reutilizável;
- documentação de extensão;
- pacotes comunitários;
- casos de uso publicados;
- suporte a workflows multiagentes.

---

## 19. Questões em aberto

1. Qual deve ser o formato canônico do perfil de projeto?
2. O front matter será recomendado ou obrigatório para tipos específicos?
3. Como representar um assunto e sua fonte canônica sem criar uma ontologia complexa prematuramente?
4. Quais regras devem ser universais e quais devem existir apenas em profiles?
5. Como medir utilidade de findings de maneira simples durante os pilotos?
6. Qual nível de análise de código será necessário para detectar documentation drift?
7. O CLI será parte da v0.1 ou começará como execução orientada por agent skill?
8. Como versionar regras, schemas e relatórios de forma independente?
9. Quais formatos de exportação de grafo devem ser priorizados?
10. Quais findings poderão futuramente bloquear CI/CD e sob quais critérios?

---

## 20. Decisões de produto registradas nesta versão

| ID | Decisão |
|---|---|
| PD-001 | O produto será proposal-first e read-only por padrão |
| PD-002 | Evidência será obrigatória em todos os findings |
| PD-003 | Severidade e confiança serão dimensões separadas |
| PD-004 | A v0.1 priorizará regras estruturais e determinísticas |
| PD-005 | Perfis adaptarão o framework sem alterar seu núcleo |
| PD-006 | Intenção, especificação, execução, operação e contexto de agentes serão camadas distintas |
| PD-007 | A North Star medirá utilidade validada, não quantidade de findings |
| PD-008 | Knowledge Guardian será um produto reutilizável, e não acoplado ao Meu PDI ou APOS |

---

## 21. Próximo marco recomendado

O próximo marco é transformar este PRD em um conjunto mínimo de artefatos executáveis:

```text
portfolio/
├── PRD.md
├── MVP_SCOPE.md
├── METRICS.md
└── PILOT_PLAN.md

schemas/
├── metadata.schema.json
├── profile.schema.json
└── report.schema.json

skill/
└── SKILL.md
```

A execução deve começar pelo desenho dos contratos `profile`, `document`, `finding` e `report`, seguido de um vertical slice que analise o próprio repositório Knowledge Guardian.

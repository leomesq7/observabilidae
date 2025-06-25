# Projeto de Observabilidade com IA, Prometheus, Grafana e Docker

Este projeto demonstra a construção de um sistema de monitoramento completo com:

- Análise de logs com Inteligência Artificial (Isolation Forest)
- Containerização com Docker
- Monitoramento com Prometheus
- Visualização de métricas com Grafana

## 📁 Estrutura de Pastas

```
Observabilidade/
├── ai_service/              # API em Flask com modelo de IA e rota de métricas
├── prometheus/              # Configuração do Prometheus
├── log_projeto/             # Geração e análise de logs locais com IA
├── docker-compose.yml       # Orquestra todos os serviços
```

## 🔧 Requisitos

- Python 3.9 ou superior (para uso local)
- Docker + Docker Compose

## 🚀 Como Executar o Projeto

### 1. Gerar o modelo de IA (Isolation Forest)

```bash
cd Observabilidade/ai_service
python treinar_modelo.py
```

### 2. Subir o ambiente com Docker

```bash
cd ..
docker compose up --build
```

### 3. Verificar os serviços

- 🧠 API de IA: [http://localhost:5000/health](http://localhost:5000/health)
- 📊 Prometheus: [http://localhost:9090](http://localhost:9090)
- 📈 Grafana: [http://localhost:3001](http://localhost:3001) (login: admin / admin)

## 📦 log\_projeto: IA local com detecção de anomalias em logs

### Rodar a geração de logs:

```bash
cd Observabilidade/log_projeto
python gerar_log.py
```

### Analisar com IA:

```bash
python log_analyzer.py
```

## 📈 Visualizar no Grafana

1. Acesse o Grafana
2. Adicione um Data Source do tipo Prometheus com URL: `http://prometheus:9090`
3. Crie um painel com a consulta:

```promql
dummy_metric
```

## ✍️ Autoria

Este projeto foi desenvolvido como parte do Desafio Final do Módulo 4 do Bootcamp de Engenharia de Dados com Inteligência Artificial - IA Expert.

---

> Dúvidas ou melhorias? Fique à vontade para abrir um issue ou enviar um pull request.


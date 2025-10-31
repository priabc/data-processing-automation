
# Data Processing Automation (CloudFormation + Lambda + LocalStack)

## 🎯 Objetivo
Este projeto demonstra a **automação de infraestrutura AWS** utilizando **CloudFormation**, com **S3** e **Lambda**, para processamento automático de arquivos CSV simulando um pipeline de dados.

---

## 🧩 Arquitetura


**Fluxo:**
1. Upload de arquivos CSV no bucket `raw-data-bucket`.
2. A função Lambda é acionada automaticamente.
3. Os dados são processados (remoção de duplicados).
4. Resultado armazenado no bucket `processed-data-bucket`.

---

## ⚙️ Tecnologias
- AWS CloudFormation  
- AWS Lambda  
- Amazon S3  
- LocalStack  
- Python 3.9  

---

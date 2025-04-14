
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Liberar acesso de qualquer origem (CORS)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/consultar")
async def consultar(request: Request):
    data = await request.json()
    consulta = data.get("pergunta", "").lower()

    if "art. 209" in consulta:
        return {
            "resposta": """
📘 Art. 209 do Código Penal Militar – Comando Premium de Revisão

**Resumo Doutrinário:** O artigo trata do concurso de pessoas na prática de crime militar, abordando autoria, coautoria e participação, com base nos princípios da individualização da pena e da responsabilidade penal subjetiva.

🧠 **Mapa Mental (Texto):**
- Concurso de pessoas
  - Coautoria: dois ou mais militares
  - Participação: instigação, auxílio
- Pena proporcional
- Autonomia da conduta

📝 **Questão Discursiva:**
Analise o concurso de agentes no contexto militar, considerando a natureza da pena e a diferenciação entre autoria e participação.

⚖️ **Jurisprudência:**
STM, Apelação nº 700XXXXX, julgado em 2022 – reconhece que a coautoria exige unidade de desígnios e cooperação consciente para o resultado.

⚠️ Não há divergência doutrinária relevante sobre esse ponto.
"""
        }

    return {
        "resposta": "❓ Tema não reconhecido. Por favor, envie um artigo ou tema específico do CPM."
    }

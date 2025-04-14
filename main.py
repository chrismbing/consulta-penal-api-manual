from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()

@app.post("/consultar")
async def consultar(request: Request):
    try:
        # Tentando ler o corpo da requisição como JSON
        data = await request.json()

        # Verificando se a chave 'pergunta' está presente e se não está vazia
        consulta = data.get("pergunta", "").strip()
        
        if not consulta:
            return JSONResponse(content={"error": "A pergunta não foi fornecida ou está vazia."}, status_code=400)
        
        # Adicione novos casos de artigos conforme necessário
        if "art. 209" in consulta.lower():
            return {"resposta": "📘 Art. 209 do CPM – Resumo completo, mapa mental, jurisprudência..."}
        
        return {"resposta": "❓ Tema não reconhecido."}
    
    except Exception as e:
        # Captura erros e retorna um erro claro
        return JSONResponse(content={"error": f"Erro ao processar a requisição: {str(e)}"}, status_code=400)

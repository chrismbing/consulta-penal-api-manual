
# Consulta Penal Militar – API Manual

API para responder comandos jurídicos do GPT de forma controlada. Permite editar as respostas manualmente no arquivo `main.py`.

## Como rodar no Render

1. Crie um repositório no GitHub e envie os arquivos.
2. Acesse https://render.com e faça o deploy do repositório.
3. Use o seguinte comando de start:

```
uvicorn main:app --host 0.0.0.0 --port 10000
```

4. Após o deploy, sua API estará acessível em:

```
https://<nome>.onrender.com/consultar
```

## Como editar as respostas

Abra o `main.py` e altere o conteúdo retornado dentro dos blocos `if` conforme seus temas jurídicos.

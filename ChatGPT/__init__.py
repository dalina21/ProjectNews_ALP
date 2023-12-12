import openai
import textwrap

chave = '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'
openai.api_key = chave

def PesquisarChatGPT(conteudo):
    model_engine = "text-davinci-003"
    prompt = 'Faça uma pesquisa resumida sobre: ' + conteudo
    max_tokens = 3033

    completion = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=max_tokens,
        temperature=0.5,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    print('\n', textwrap.fill(completion.choices[0].text, width=60), '\n')
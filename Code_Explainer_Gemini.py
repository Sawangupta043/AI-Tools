Key = "AIzaSyAIA-dbtiQQKBMdfYpaVZoSQUo-ujGvbXo"


from openai import OpenAI

gemini_model=OpenAI(api_key = Key, base_url="https://generativelanguage.googleapis.com/v1beta/openai/")


def code(myprompt):
    mymsg = [{"role": "system", "content": "Explain this code in 4-5 simple lines, specify the programming language, and detect if it’s AI-written or human-written."},
            {"role": "user", "content":myprompt}
            ]
    response = gemini_model.chat.completions.create(messages= mymsg, model= 'gemini-2.5-flash')
    return response.choices[0].message.content


myprompt = input("Enter a prompt: ")


import gradio as gr
mygr = gr.Interface(fn=code, inputs="text", outputs="text",title="Code Explainer", description="Enter a code snippet or prompt to get a simple explanation.")
mygr.launch()
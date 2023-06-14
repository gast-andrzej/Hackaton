import openai

openai.api_key = open('chat/API_KEY.txt', 'r').read()
model_id = 'gpt-3.5-turbo'

def ChatGPT_conversation(conversation):
    response = openai.ChatCompletion.create(
        model=model_id,
        messages=conversation
    )
    conversation.append({'role': response.choices[0].message.role, 'content': response.choices[0].message.content})
    return conversation


def runnex():
    openai.api_key = open('chat/API_KEY.txt', 'r').read()
    model_id = 'gpt-3.5-turbo'
    conversation = []
    conversation.append({'role': 'system', 'content': 'How may I help you?'})
    conversation = ChatGPT_conversation(conversation)
    print('{0}: {1}\n'.format(conversation[-1]['role'].strip(), conversation[-1]['content'].strip()))

    job = input('What role you need? ')
    language = input('What language interview you want: ')

    user_first = f"conduct an interview with me for the position of {job} in {language} language, please ask me questions one at a time, after answering tell me in {language} language what mistakes I made in communication and how to expand my statement, also rate each of my answers on a scale of 1 to 100, but only after my answer. When I write the end of the conversation, give me the overall score of this conversation on a scale of 1 to 100"

    #v2 user_first = f"interview me for a job for the {job} position, please ask me questions one at a time, after answering, tell me what mistakes I made in communication and how to expand my statement, but only after my answer"

    #v1 user_first = f"conduct a job interview with me on position {job}, please ask me questions one at a time, after my answering tell me what mistakes I made in terms of communication"

    #v0 user_first = \
    #     f"start a job interview with me to work as a {job}, " \
    #     f"after each recruitment question I am to be given feedback on a " \
    #     f"scale of 1 to 10 in terms of developing the answer, communicativeness and presence."

    conversation.append({'role': 'user', 'content': user_first})
    conversation = ChatGPT_conversation(conversation)
    print('{0}: {1}\n'.format(conversation[-1]['role'].strip(), conversation[-1]['content'].strip()))

    while True:
        prompt = input('User:')
        conversation.append({'role': 'user', 'content': prompt})
        conversation = ChatGPT_conversation(conversation)
        print('{0}: {1}\n'.format(conversation[-1]['role'].strip(), conversation[-1]['content'].strip()))
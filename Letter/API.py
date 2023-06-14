import openai

openai.api_key = open('Letter/API_KEY.txt', 'r').read()
model_id = 'gpt-3.5-turbo'

def ChatGPT_conversation(conversation):
    response = openai.ChatCompletion.create(
        model=model_id,
        messages=conversation
    )
    conversation.append({'role': response.choices[0].message.role, 'content': response.choices[0].message.content})
    return conversation


def runnex():
    openai.api_key = open('Letter/API_KEY.txt', 'r').read()
    model_id = 'gpt-3.5-turbo'
    conversation = []
    conversation.append({'role': 'system', 'content': 'How may I help you?'})
    conversation = ChatGPT_conversation(conversation)
    print('{0}: {1}\n'.format(conversation[-1]['role'].strip(), conversation[-1]['content'].strip()))

    position = input('What role you need? ')
    language = input('What language letter you want: ')
    company = input('Where you apply: ')
    keyfin = ['finish']
    strong_side = list()
    weak_side = list()
    while True:
        lix = input('Your strong side, if you want finish, write finish : ')
        if lix.lower() in keyfin:
            break
        else:
            strong_side.append(lix)
    strong_str = ' '.join(i for i in strong_side)
    while True:
        lix = input('Your weak side, if you want finish, write finish : ')
        if lix.lower() in keyfin:
            break
        else:
            strong_side.append(lix)
    weak_str = ' '.join(i for i in strong_side)

    user_first = f"please prepare me a cover letter in {language} for {company} to encourage them to recruit me for {position} taking into account my strengths such as {strong_str} and turning my weak side as {weak_str} into my strengths."

    conversation.append({'role': 'user', 'content': user_first})
    conversation = ChatGPT_conversation(conversation)
    print('{0}: {1}\n'.format(conversation[-1]['role'].strip(), conversation[-1]['content'].strip()))

    while True:
        prompt = input('User:')
        conversation.append({'role': 'user', 'content': prompt})
        conversation = ChatGPT_conversation(conversation)
        print('{0}: {1}\n'.format(conversation[-1]['role'].strip(), conversation[-1]['content'].strip()))
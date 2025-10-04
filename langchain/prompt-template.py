from langchain_core.prompts import PromptTemplate,load_prompt
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()

####### creating the prompt template 
# detailed way
template2 = PromptTemplate(
    template='Greet this person in 5 languages. The name of the person is {name}',
    input_variables=['name']
)

# fill the values of the placeholders
prompt = template2.invoke({'name':'nitish'})

result = model.invoke(prompt)

print(result.content)

####### loading the prompt from a different file
template = load_prompt('template.json')



####### creating the Chat prompt template 
from langchain_core.prompts import ChatPromptTemplate

chat_template = ChatPromptTemplate([
    ('system', 'You are a helpful {domain} expert'),
    ('human', 'Explain in simple terms, what is {topic}')
])

prompt = chat_template.invoke({'domain':'cricket','topic':'Doosra'})

print(prompt)


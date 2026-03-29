from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI 



load_dotenv(override=True)

def main():
    print("Hello from langchain-course!")
    information =  """Elon Reeve Musk (* 28. června 1971 Pretorie) je podnikatel jihoafricko-kanadsko-britského původu.
    [2][3] Založil kosmickou společnost SpaceX a stál u vzniku automobilky Tesla, kterou začal jako CEO řídit. 
    Společnost Twitter koupil za 44 miliard dolarů a sociální síť přejmenoval na X.[4] Založil také společnosti xAI,
      Starlink či Neuralink a v říjnu 2025 spustil internetovou encyklopedii generovanou umělou inteligencí Grokipedia, 
      konkurenční projekt Wikipedie. V minulosti spoluvlastnil internetový platební systém PayPal a spoluzakládal společnost OpenAI."""

    summary_template = """given the information {information} about Elon Musk,i want you to create : 
     1. a short summary of the information in 3 sentences,
     2. a list of 2 most important facts about Elon Musk,"""


    summary_prompt_template = PromptTemplate(input_variables= ["information"], template=summary_template)
    llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
    chain = summary_prompt_template | llm
    response= chain.invoke(input={"information": information})
    print(response.content)

if __name__ == "__main__":
    main()
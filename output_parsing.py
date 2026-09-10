from pydantic import BaseModel, Field
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser

# 1. Define the schema
class Person(BaseModel):
    name: str = Field(description="Person's name")
    age: int = Field(description="Person's age")
    profession: str = Field(description="Person's profession")

# 2. Create the parser
parser = PydanticOutputParser(
    pydantic_object=Person
)

# 3. Create the prompt
prompt = PromptTemplate(
    template="""
Generate details about a fictional person.

{format_instructions}
""",
    input_variables=[],
    partial_variables={
        "format_instructions": parser.get_format_instructions()
    }
)

# 4. Initialize the LLM
llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.7
)

# 5. Generate response
response = llm.invoke(prompt.format())

print("Raw LLM Output:")
print(response.content)

# 6. Parse the response
person = parser.parse(response.content)

print("\nParsed Output:")
print(person)

print("\nAccess Individual Fields:")
print("Name:", person.name)
print("Age:", person.age)
print("Profession:", person.profession)
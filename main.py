import inspect
import datetime
import os
from openai import OpenAI
from parameters import MODEL, SYSTEM_PROMPT, USER_PROMPT, DIRECTORY


def ask_gpt(model: str = MODEL,
            system_prompt: str = SYSTEM_PROMPT,
            user_prompt: str = USER_PROMPT):
  """
  Calls the OpenAI completion API with the constants in parameters.py
  Return the content of the answer
  """
  print("Calling the OpenAI API, this may take a while...")
  client = OpenAI()
  completion = client.chat.completions.create(
  model=MODEL,
  messages=[
    {"role": "system", "content": SYSTEM_PROMPT},
    {"role": "user", "content": USER_PROMPT}
  ])

  return(completion.choices[0].message.content)


def generate_md_file(model: str = MODEL,
                    system_prompt: str = SYSTEM_PROMPT,
                    user_prompt: str = USER_PROMPT,
                    directory: str = DIRECTORY,
                    response: str = ""):
    """
    Generates an MD file with the date and time as filename.
    Then it writes the parameter names and their contents to such file.
    """
    print(f'Generating MD file {directory}...')
    current_datetime = datetime.datetime.now()
    filename = os.path.join(directory, current_datetime.strftime("%Y-%m-%d_%H-%M-%S") + ".md")
    
    signature = inspect.signature(generate_md_file)
    parameters = signature.parameters

    with open(filename, "w") as file:
      for param_name in parameters:
        #If the parameter is "directory" it skips it
        if param_name == "directory":
          continue
        #If the parameter is "response" it writes it as a header in MD
        elif param_name == "response":
          param_value = locals()[param_name]
          formatted_content = f"## **{param_name}:**\n {param_value}\n\n"
          file.write(formatted_content)
        #For all other parameters, it writes its name in bold and its content
        else:
          param_value = locals()[param_name]
          formatted_content = f"**{param_name}**: {param_value}\n\n"
          file.write(formatted_content)
      print("MD file created correctly!")

def main():
  response = ask_gpt()
  generate_md_file(response=response)

main()

try:
    import openai
    import os
    import pandas as pd
except Exception as e:
    raise Exception("Module Missing: {}".format(e))

# Set up OpenAI API key
openai.api_key = "YOUR-API-KEY"

def generate_query(prompt, table_structure):
    # Use the user's prompt and table structure to generate a query
    query_prompt = f"Write a query that will fulfill the user's request of {prompt} using the table structure {table_structure}"
    query = openai.Completion.create(
        engine="text-davinci-002", prompt=query_prompt, temperature=0.4, max_tokens=500)
    #print(query_prompt)
    return query['choices'][0]['text']

# Get the file path
file_path = input("Please enter the file path: ")

try:
    # Read the CSV file and specify dtype option to avoid mixed type warnings
    data = pd.read_csv(file_path, low_memory=False)
    while True:
        # Get the user's prompt
        prompt = input("Ask away, what do you want to know?")
        # Generate the query
        query = generate_query(prompt, data.dtypes.to_string())
        print(query)

except Exception as e:
    print(f"An error occurred: {e}")

import sys
import os
from google import genai
from google.genai import types
from dotenv import load_dotenv

from prompts import system_prompt
from call_function import schema_get_files_info
from call_function import schema_get_file_content
from call_function import schema_run_python_file
from call_function import schema_write_file
from call_function import available_functions
from functions.call_function import call_function

def main():
    load_dotenv()

    verbose = "--verbose" in sys.argv
    args = [arg for arg in sys.argv[1:] if not arg.startswith("--")]

    if not args:
        print("AI Code Assistant")
        print('\nUsage: python main.py "your prompt here" [--verbose]')
        print('Example: python main.py "How do I fix the calculator?"')
        sys.exit(1)

    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    user_prompt = " ".join(args)

    if verbose:
        print(f"User prompt: {user_prompt}\n")

    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]
    
    counter = 0

    while counter < 20:
        try:
            response = generate_content(client, messages, verbose)
    
            for candidate in response.candidates:
                messages.append(response.candidates.content)

            if response.text:
                    return response.text
            
            counter += 1

        except Exception as e:
            return f"Error: An error occured during the content generation loop - {e}"

def generate_content(client, messages, verbose):
    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages,
        config=types.GenerateContentConfig(tools=[available_functions], system_instruction=system_prompt),
    )
    if verbose:
        print("Prompt tokens:", response.usage_metadata.prompt_token_count)
        print("Response tokens:", response.usage_metadata.candidates_token_count)
    
    function_call_results = []

    if response.function_calls:
        for function_call in response.function_calls:
            function_call_result = call_function(function_call, verbose)
            messages.append(types.Content(role="user", parts=[types.Part(text=function_call_result)]))
            function_call_results.append(function_call_result)

            if function_call_result.parts[0].function_response.response:
                if verbose:
                    print(f"-> {function_call_result.parts[0].function_response.response}")
            else:
                raise Exception("Error: fatal error. no response from function call") 

    else:
        print("No function call found in the response.")
        return response.text
    
    return function_call_results


if __name__ == "__main__":
    main()


import argparse
from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
client = Groq(api_key=GROQ_API_KEY)


def generate_befunge_code(input_file):
    """Generate Befunge code by making two LLM API calls."""
    try:
        # Step 1: Read input from file
        with open(input_file, "r") as f:
            content = f.read().strip()

        # Step 2: Make first API call to reverse the string
        reverse_prompt = f"Reverse the following string and output it strictly in the format \"reversed_string\">:#,_@: For example, if the input is 'Hello World!', the output should be \"dlroW olleH!\">:#,_@. Input: \"{content}\""
        
        # Call the Groq API
        response_reverse = client.chat.completions.create(
            model="llama-3.1-70b-versatile",
            messages=[{"role": "user", "content": reverse_prompt}],
            temperature=0.7,
            max_tokens=500,
            top_p=1,
            stream=False,
            stop=None,
        )
        
        reversed_content = response_reverse.choices[0].message.content.strip()

        final_befunge_code = reversed_content

        return final_befunge_code

    except Exception as e:
        print(f"Error: {e}")
        return None

def main(input_file, output_file):
    """Main function to generate Befunge code and write it to the output file."""
    try:
        # Generate Befunge code using LLM API calls
        befunge_code = generate_befunge_code(input_file)

        # Write the generated Befunge code to the output file
        if befunge_code:
            with open(output_file, "w") as f:
                f.write(befunge_code)

            print(f"Befunge code successfully written to {output_file}")
        else:
            print("Failed to generate Befunge code.")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate Befunge code to reverse a string and append >:#,_@ using LLM API calls.")
    parser.add_argument("input_file", type=str, help="Path to the input file containing the text.")
    parser.add_argument("output_file", type=str, help="Path to the output file where the Befunge code will be written.")

    args = parser.parse_args()
    main(args.input_file, args.output_file)

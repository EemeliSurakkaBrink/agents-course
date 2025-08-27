#!/usr/bin/env python3
"""
Script to add OpenAI setup code to the fixed conversation memory cell
"""

import json

def add_setup_to_cell():
    # Read the notebook
    with open('1_foundations/1_lab1.ipynb', 'r') as f:
        notebook = json.load(f)

    # Find the fixed cell and add the OpenAI setup at the beginning
    for i, cell in enumerate(notebook['cells']):
        if cell['cell_type'] == 'code':
            source = ''.join(cell['source'])
            if 'FIXED VERSION: Maintain conversation history' in source:
                # Add the necessary imports and setup at the beginning
                setup_code = [
                    '# Required setup (run this cell independently)\n',
                    'from dotenv import load_dotenv\n',
                    'from openai import OpenAI\n',
                    'import os\n',
                    '\n',
                    '# Load environment variables\n',
                    'load_dotenv(override=True)\n',
                    '\n',
                    '# Initialize OpenAI client\n',
                    'openai = OpenAI()\n',
                    '\n',
                    '# Verify API key\n',
                    'openai_api_key = os.getenv("OPENAI_API_KEY")\n',
                    'if not openai_api_key:\n',
                    '    print("❌ OpenAI API Key not set - please check your .env file")\n',
                    'else:\n',
                    '    print(f"✅ OpenAI API Key loaded (starts with {openai_api_key[:8]})...")\n',
                    '\n',
                    'print("=" * 50)\n',
                    '\n'
                ]

                # Insert setup code at the beginning of the cell
                notebook['cells'][i]['source'] = setup_code + notebook['cells'][i]['source']

                print(f'Added setup code to cell {i}')
                break

    # Write back to file
    with open('1_foundations/1_lab1.ipynb', 'w') as f:
        json.dump(notebook, f, indent=1)

    print('Setup code added successfully!')

if __name__ == "__main__":
    add_setup_to_cell()

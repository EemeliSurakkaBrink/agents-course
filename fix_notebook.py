#!/usr/bin/env python3
"""
Script to fix the conversation memory issue in the notebook
"""

import json

def fix_conversation_memory():
    # Read the notebook
    with open('1_foundations/1_lab1.ipynb', 'r') as f:
        notebook = json.load(f)

    # Find the cell with the problematic code
    for i, cell in enumerate(notebook['cells']):
        if cell['cell_type'] == 'code':
            source = ''.join(cell['source'])
            if 'pain_point = "What is the pain point in this industry?"' in source:
                # Replace with corrected code
                corrected_source = [
                    "# FIXED VERSION: Maintain conversation history to avoid memory loss\n",
                    "# The key issue was that ChatGPT API calls are stateless - each call only sees the messages you send it\n",
                    "# To maintain context, we need to keep all previous messages in the conversation\n",
                    "\n",
                    "# Initialize conversation with the first message\n",
                    'messages = [{"role": "user", "content": "Suggest one business area that might be worth exploring for an Agentic AI opportunity."}]\n',
                    "\n",
                    "# Make the first call\n",
                    "response = openai.chat.completions.create(\n",
                    "    model=\"gpt-4.1-mini\",\n",
                    "    messages=messages\n",
                    ")\n",
                    "\n",
                    "# Add the AI's response to the conversation history\n",
                    'messages.append({"role": "assistant", "content": response.choices[0].message.content})\n',
                    "\n",
                    "business_idea = response.choices[0].message.content\n",
                    "\n",
                    'print("Business Idea:")\n',
                    "print(business_idea)\n",
                    'print("\\n" + "="*50 + "\\n")\n',
                    "\n",
                    "# Now ask about pain points - the AI will remember the context from the previous message\n",
                    'pain_point_question = "What is the pain point in this industry?"\n',
                    'messages.append({"role": "user", "content": pain_point_question})\n',
                    "\n",
                    "pain_point_response = openai.chat.completions.create(\n",
                    "    model=\"gpt-4.1-mini\",\n",
                    "    messages=messages  # Now contains the full conversation history\n",
                    ")\n",
                    "\n",
                    "# Add this response to history too\n",
                    'messages.append({"role": "assistant", "content": pain_point_response.choices[0].message.content})\n',
                    "\n",
                    'print("Pain Points:")\n',
                    "print(pain_point_response.choices[0].message.content)\n",
                    'print("\\n" + "="*50 + "\\n")\n',
                    "\n",
                    "# Now ask for the solution - again with full context\n",
                    'solution_question = "What is the Agentic AI solution to this pain point?"\n',
                    'messages.append({"role": "user", "content": solution_question})\n',
                    "\n",
                    "solution_response = openai.chat.completions.create(\n",
                    "    model=\"gpt-4.1-mini\",\n",
                    "    messages=messages  # Full conversation history maintained\n",
                    ")\n",
                    "\n",
                    'print("Agentic AI Solution:")\n',
                    "print(solution_response.choices[0].message.content)\n",
                    "\n",
                    'print("\\n" + "="*50)\n',
                    'print("SUCCESS: Conversation memory maintained throughout!")\n',
                    'print("The AI now remembers the context from previous messages")\n',
                    'print("="*50)\n'
                ]

                notebook['cells'][i]['source'] = corrected_source
                print(f"Fixed cell {i}")
                break

    # Write back to file
    with open('1_foundations/1_lab1.ipynb', 'w') as f:
        json.dump(notebook, f, indent=1)

    print("Notebook updated successfully!")

if __name__ == "__main__":
    fix_conversation_memory()

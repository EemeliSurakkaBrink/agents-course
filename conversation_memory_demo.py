#!/usr/bin/env python3
"""
Conversation Memory Demo - How to Fix ChatGPT API Memory Issues

This script demonstrates the correct way to maintain conversation context
when using the OpenAI ChatGPT API. The key issue is that each API call is
stateless - it only sees the messages you send it in that specific request.

The solution is to maintain a conversation history by accumulating all
messages (both user and assistant) in a list and passing the entire
conversation to each API call.
"""

from dotenv import load_dotenv
from openai import OpenAI
import os

# Load environment variables
load_dotenv()

def demonstrate_conversation_memory():
    """Demonstrate proper conversation memory management"""

    # Initialize OpenAI client
    openai = OpenAI()

    print("=== CONVERSATION MEMORY DEMO ===\n")

    # STEP 1: Initialize conversation history
    messages = []

    # STEP 2: Start the conversation
    initial_question = "Suggest one business area that might be worth exploring for an Agentic AI opportunity."
    messages.append({"role": "user", "content": initial_question})

    print("User:", initial_question)
    print("-" * 50)

    # STEP 3: Make first API call with conversation history
    response = openai.chat.completions.create(
        model="gpt-4.1-mini",
        messages=messages
    )

    # STEP 4: Add AI response to conversation history
    ai_response = response.choices[0].message.content
    messages.append({"role": "assistant", "content": ai_response})

    print("Assistant:", ai_response)
    print("=" * 50)

    # STEP 5: Continue conversation - AI will remember context!
    follow_up = "What are the main pain points in this industry that could benefit from Agentic AI?"
    messages.append({"role": "user", "content": follow_up})

    print("User:", follow_up)
    print("-" * 50)

    # STEP 6: Make second API call with full conversation history
    pain_point_response = openai.chat.completions.create(
        model="gpt-4.1-mini",
        messages=messages  # Full conversation history
    )

    # STEP 7: Add this response to history too
    pain_points = pain_point_response.choices[0].message.content
    messages.append({"role": "assistant", "content": pain_points})

    print("Assistant:", pain_points)
    print("=" * 50)

    # STEP 8: One more follow-up - full context maintained
    solution_question = "What would be an effective Agentic AI solution to address these pain points?"
    messages.append({"role": "user", "content": solution_question})

    print("User:", solution_question)
    print("-" * 50)

    # STEP 9: Final API call with complete conversation history
    solution_response = openai.chat.completions.create(
        model="gpt-4.1-mini",
        messages=messages  # Complete conversation history
    )

    print("Assistant:", solution_response.choices[0].message.content)
    print("=" * 50)

    print("\n=== KEY LESSONS ===")
    print("1. ChatGPT API calls are STATELESS - each call only sees the messages you send it")
    print("2. To maintain memory, keep ALL messages in a list")
    print("3. Always append both user messages AND assistant responses to the conversation")
    print("4. Pass the ENTIRE conversation history to each API call")
    print("5. Never reset the messages list between calls!")

    print("\n=== WHAT HAPPENS IF YOU DON'T DO THIS ===")
    print("If you reset messages = [] between calls, the AI loses all context")
    print("It will ask 'which industry?' because it doesn't remember your previous messages!")

def demonstrate_wrong_way():
    """Show what happens when you don't maintain conversation history"""

    print("\n=== DEMONSTRATING THE WRONG WAY ===\n")

    openai = OpenAI()

    # WRONG WAY: Reset messages each time (loses context)
    messages = [{"role": "user", "content": "Suggest one business area for Agentic AI"}]
    response1 = openai.chat.completions.create(model="gpt-4.1-mini", messages=messages)

    print("First call result:")
    print(response1.choices[0].message.content[:200] + "...")

    # WRONG WAY: Reset messages again (context lost!)
    messages = [{"role": "user", "content": "What are pain points in this industry?"}]
    response2 = openai.chat.completions.create(model="gpt-4.1-mini", messages=messages)

    print("\nSecond call result (context lost):")
    print(response2.choices[0].message.content)
    print("\n❌ Notice how the AI asks for clarification - it forgot the previous context!")

if __name__ == "__main__":
    # Check if API key is available
    if not os.getenv('OPENAI_API_KEY'):
        print("❌ Please set your OPENAI_API_KEY in a .env file")
        exit(1)

    demonstrate_conversation_memory()
    demonstrate_wrong_way()

    print("\n" + "="*60)
    print("SUMMARY: Always maintain conversation history!")
    print("Use messages.append() to add new messages")
    print("Pass the full messages list to each API call")
    print("="*60)

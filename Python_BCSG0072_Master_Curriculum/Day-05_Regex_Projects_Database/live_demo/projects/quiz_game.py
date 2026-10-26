# quiz_game.py
# Capstone Project 3: Interactive Python Quiz Game with Persistent Score History
import random
import os
import time

SCORE_FILE = "quiz_scores.txt"

QUESTIONS = [
    {"q": "What is the output of print(type([]))?", "opts": ["A) list", "B) tuple", "C) dict", "D) set"], "ans": "A"},
    {"q": "Which keyword creates an anonymous function?", "opts": ["A) def", "B) anon", "C) lambda", "D) func"], "ans": "C"},
    {"q": "Which data structure is immutable in Python?", "opts": ["A) list", "B) set", "C) tuple", "D) dict"], "ans": "C"},
    {"q": "What does range(5) produce?", "opts": ["A) 1 to 5", "B) 0 to 4", "C) 0 to 5", "D) 1 to 4"], "ans": "B"},
    {"q": "What is the time complexity of dictionary key lookup?", "opts": ["A) O(N)", "B) O(log N)", "C) O(1)", "D) O(N^2)"], "ans": "C"}
]

def play_quiz():
    name = input("Enter Player Name: ").strip()
    score = 0
    shuffled_q = random.sample(QUESTIONS, len(QUESTIONS))
    
    print(f"\nWelcome {name}! Answer 5 questions. Type A, B, C, or D.")
    t0 = time.time()
    
    for i, item in enumerate(shuffled_q, 1):
        print(f"\nQ{i}: {item['q']}")
        for opt in item['opts']:
            print(f"   {opt}")
        ans = input("Your answer: ").strip().upper()
        if ans == item['ans']:
            print("[+] Correct!")
            score += 1
        else:
            print(f"[-] Wrong! Correct answer was: {item['ans']}")
            
    elapsed = time.time() - t0
    print(f"\nQuiz Finished! Score: {score}/{len(QUESTIONS)} in {elapsed:.1f} seconds")
    
    # Save score history
    with open(SCORE_FILE, "a", encoding="utf-8") as f:
        f.write(f"{name}|{score}/{len(QUESTIONS)}|{elapsed:.1f}s|{time.strftime('%Y-%m-%d %H:%M')}\n")
    print(f"[+] Score saved to {SCORE_FILE}")

if __name__ == "__main__":
    play_quiz()

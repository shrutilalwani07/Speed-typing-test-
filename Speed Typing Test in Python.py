#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random
import time

words = [
    "python",
    "challenge",
    "speed",
    "typing",
    "machine learning",
    "openai",
    "developer",
    "practice",
    "data science"
]

def get_random_word():
    return random.choice(words)

def typing_test():
    input("Press Enter to start the typing test...")
    start_time = time.time()
    word_count = 0

    while True:
        target_word = get_random_word()
        print(f"Type the word: '{target_word}'")
        user_input = input()
        
        if user_input == target_word:
            word_count += 1
            print(f"Correct! Words typed: {word_count}")
        else:
            print(f"Wrong! Words typed: {word_count}")
        
        elapsed_time = time.time() - start_time
        typing_speed = word_count / (elapsed_time / 60)  
        print(f"Time elapsed: {elapsed_time:.2f} seconds")
        print(f"Typing speed: {typing_speed:.2f} words per minute\n")

        if elapsed_time >= 60:
            break

    print("Typing test completed!")
    print(f"Total words typed: {word_count}")
    print(f"Total time: {elapsed_time:.2f} seconds")
    print(f"Typing speed: {typing_speed:.2f} words per minute")

if __name__ == "__main__":
    typing_test()


# In[ ]:





# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?
- What did the game look like the first time you ran it? When I first ran the game, it displayed a light mode interface with the title "Game Glitch Investigator" at the top of the page. The main screen included instructions to guess a number between 1 and 100 and had a text box where the user could enter a guess. Below that, there was a Submit Guess button, a New Game button, and a Show Hint checkbox. There was also a tab on the left that could be expanded as well as a settings sidebar where the difficulty could be changed to Easy, Normal, or Hard.
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
  1. The game continuously displays the hint "Go LOWER!" even when the secret number is higher than the player's most recent guess. Expected: The game should display "Go HIGHER!" when the player's guess is lower than secret number and "Go LOWER!" when the player's guess is higher than secret number.*
  2. The game accepts guesses between 1 to 100 but will later reveal that the secret number was outside the range, such as -33 or 130. Expected: The secret number should always generate within range of 1 to 100 according to instructions given.

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
| Guess: 50 when secret number is greater than 50| Game displays "Go HIGHER!" | Game displayed "Go LOWER!" | none |
| Start a new game and reveal secret number | Secret number is between 1 and 100 | Secret number generated outside range (ex: -33) | none |
| Change the difficulty level and start a new game | Number range and attempt limit update correctly | Difficulty settings not properly updated in game | none | 

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)? For this project, I used Claude through the VS Code extension to help me understand the code and identify possible causes of bugs. I verified this by testing guesses above and below the secret number. I also asked Claude to explain the game logic of various files, suggest general fixes, and fix sections of code. 
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result). One correct suggestion Claude made towards the end was that the attempts counter should start at 0 instead of 1. The original code initialized the attempts value to 1, which caused the game to count the attempts made incorrectly. I implemented the change and verified it by running the game again and checking that the number of remaining attempts was displayed correctly.
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result). One misleading suggestion Claude made was that the Hard difficulty range was incorrect because it used a smaller number range than Normal mode. However, after reviewing the assignment and game logic, I realized that Hard mode didn't necessarily need to use a larger range. The suggestion was based on assumptions made when compared to Normal mode rather than a confirmed bug so I did not make any fixes.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
I decided a bug was really fixed once I ran the game after making each change and checking whether the incorrect behavior still occurred or was fixed. I compared the updated behavior to the expected behavior I documented in my bug reproduction log to double check. If the issue no longer seemed to appear or there were no new errors, I considered the fix to be mostly successful.
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
One manual test I ran involved entering valid inputs such as letters instead of numbers. Before the fix, the game would use up an attempt even when the input was invalid. However, after moving the attempt counter update to occur only after successful validation, invalid inputs weren't counted towards the number of remaining attempts anymore. 
- Did AI help you design or understand any tests? How?
Yes, AI helped me identify specific cases that should be tested such as invalid inputs, score calculations, and tracking number of attempts. It also explained the logic behind how certain functions interacted with each other, which made it easier to confirm that my fixes worked right.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
I learned that Streamlit reruns the program when a user interacts with the application, such as pressing a button or entering a guess. Without session state, variables like secret number, score, and number of attempts would reset every time the page updates. Session state helps the game remember those values while the user is playing. I would probably explain it to a friend as a way for Streamlit to remember important information even though the page keeps refreshing.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
One strategy I want to reuse in future projects is testing each change immediately after making it. Running the application after every or a few fixes was a bit time consuming but helped me quickly identify whether my changes actually solved an error or might have created a new one. 
- What is one thing you would do differently next time you work with AI on a coding task?
Next time, I would spend more time verifying the suggestions Claude gave me before blindly implementing them. Though I checked all recommendations before making a change, I think it was easy to forget that not all of the suggestions it gave actually followed project requirements and were often based on assumptions. 
- In one or two sentences, describe how this project changed the way you think about AI generated code.
This project showed me that AI can be useful when brainstorming and debugging code and is better used as a collaborator than a crutch. Human testing was still very necessary to ensure that suggested fixes actually solved problems. 
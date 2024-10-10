# NYTLetterBoxed
A Python program designed to help players of the New York Times [Letter Boxed](https://www.nytimes.com/puzzles/letter-boxed) puzzle game. In this game, players create words using letters arranged around a square. The program identifies all possible words based on the letters provided, adhering to the game's rules that prohibit using letters from the same side consecutively.

## Features
- **Word Selection**: The program uses a predefined list of valid words stored in `words.txt`.
- **User Input**: Players enter letters for each side of the square, allowing the program to identify valid words.
- **Word Filtering**: The program filters words based on the following criteria:
  - Words must not use letters from the same side consecutively.
  - Words must be longer than two letters.
  - Words can only contain the letters provided by the user.

## Getting Started

### Prerequisites
- Python 3.x installed on your machine.

### Installation
1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/FarnoodID/NYTLetterBoxed.git
   ```
2. Navigate to the project directory:
   ```bash
   cd NYTLetterBoxed
   ```
### Usage
1. Run the program:
   ```
   python NYTLetterBoxed.py
   ```
2. The program will prompt you to enter letters for each side of the square, one side per line. For example:
   ```text
   abcd
   efgh
   ijkl
   mnop
   ```
3. The program will then display all available words that can be formed with those letters.
## How It Works
1. The program reads all words from words.txt into a list.
2. It removes any letters not included in the user input from consideration.
3. It checks each word against the rules of the game, ensuring that no two consecutive letters come from the same side.
4. Finally, it outputs all valid words that meet these criteria.

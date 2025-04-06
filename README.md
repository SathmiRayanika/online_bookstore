# Online Bookstore (Console App)

## Description
This is a simple 3-tier architecture console-based app for an online bookstore. Users can search for books by title or author. The books are listed in Singlish (Sinhala typed using English letters).

## How to Run the Program

1. Clone the repository or extract the zip file.
2. Open a terminal/command prompt and navigate to the folder where you saved the files.
3. Make sure you have Python installed. You can check by running:
   ```bash
   python --version
   ```
   If you don’t have Python installed, you can download it from [here](https://www.python.org/downloads/).

4. Run the program:
   ```bash
   python main.py
   ```

## Project Structure
- `main.py`: Presentation Layer (Handles user interaction)
- `business_logic.py`: Business Logic Layer (Handles book search)
- `data_access.py`: Data Access Layer (Contains hardcoded book data)

## Notes
- The program runs in the terminal.
- Data is hardcoded in a list.
- You can search books by their title or author written in Singlish.

### Example:
Enter `Madol` to search for books by title or `Wickramasinghe` for authors.

## License
This project is open-source. Feel free to modify it as needed.

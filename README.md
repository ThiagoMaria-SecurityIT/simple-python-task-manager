# TaskMaster Pro - Python Task Manager

A simple task management application built with Python and Tkinter. This project helps you organize your tasks and shopping lists with a clean, user-friendly interface.

<img width="991" height="1027" alt="image" src="https://github.com/user-attachments/assets/3cfd177d-09c6-4b18-abc4-9e4dc5c9912c" />

## Features

### 🎯 Easy Task Management
- Create multiple lists (e.g., "Grocery", "To-Do", "Shopping")
- Add unlimited items to each list
- Mark items as complete with checkboxes
- Edit item names with a simple click
- Delete items with trash icons

### 🎨 Clean Interface
- Sidebar navigation for easy list switching
- Visual progress bars for each list
- Color-coded task cards
- Clear statistics and completion tracking
- Helpful hints and tips throughout

### 📊 Smart Features
- Automatic saving (no save button needed!)
- Progress tracking for each list
- Creation and completion dates
- Export all data to text file
- Statistics overview

## How to Use

### Getting Started
1. Run the application: `python task_manager.py`
2. Click "Create New List" in the sidebar
3. Name your list (e.g., "Grocery Shopping")
4. Start adding tasks!

### Basic Operations
- **Add Item**: Type in the text field and press Enter or click "Add Task"
- **Complete Item**: Click the checkbox next to any item
- **Edit Item**: Click on the item text or use the "Rename" button
- **Delete Item**: Click the trash icon 🗑️ next to an item
- **Rename List**: Double-click a list name or use the "Rename" button
- **Delete List**: Select a list and click "Delete List"

### Tips & Tricks
- Press Enter to quickly add new tasks
- Double-click list names to rename them
- Check the statistics in the sidebar to track your progress
- Use Export feature to backup your tasks

## Installation

### Requirements
- Python 3.6 or higher
- Tkinter (usually comes with Python)

### Steps
1. Clone or download this repository
2. Make sure you have Python installed
3. Run the application:
```bash
python task_manager.py
```

No additional packages needed! Tkinter comes standard with Python.

## Project Structure

```
task_manager.py          # Main application file
task_data.json          # Where your tasks are saved (auto-created)
README.md              # This file
```

## How It Works

### Data Storage
- Tasks are automatically saved to `task_data.json`
- Data includes list names, items, completion status, and dates
- No manual saving required - everything auto-saves

### File Formats
- **Application**: Single Python file
- **Data**: JSON format (easy to read/edit if needed)
- **Export**: Plain text format

## Learning Points

This project demonstrates several Python concepts great for learners:

### Tkinter GUI Programming
- Creating windows and frames
- Using buttons, labels, and entry fields
- Listbox for navigation
- Canvas for scrollable areas

### Data Management
- JSON file reading/writing
- Object-oriented programming with classes
- Data persistence between sessions

### User Interface Design
- Organizing widgets in frames
- Creating responsive layouts
- Adding visual feedback
- Implementing user-friendly interactions

## Common Issues & Solutions

### "ModuleNotFoundError: No module named 'tkinter'"
- On Linux: `sudo apt-get install python3-tk`
- On Mac: Usually comes with Python
- On Windows: Usually comes with Python

### Application looks different on my computer
- Tkinter appearance can vary slightly between operating systems
- The functionality remains the same

### My tasks disappeared!
- Check if `task_data.json` exists in the same folder
- Make sure the application has write permissions

## AI Transparency

### About This Code
This project was created with assistance from AI (DeepSeek). Here's how AI contributed:

### AI's Role
1. **Code Generation**: The initial structure and logic were AI-generated
2. **GUI Design**: AI suggested the layout and visual elements
3. **Feature Implementation**: AI helped implement features like progress tracking and export
4. **Code Optimization**: AI suggested improvements for readability and performance

### Human Input
1. **Requirements**: The project goals and features were specified by a human
2. **Design Decisions**: Final design choices were made by a human
3. **Learning Focus**: The project was tailored for learning purposes
4. **Testing**: The application was tested and refined by a human

### Why This Matters
- **Learning Tool**: This project shows how AI can assist in learning programming
- **Transparency**: It's important to understand how AI tools can help with coding
- **Education**: The code includes comments and structure suitable for learners
- **Customization**: You can modify and extend this code for your own learning

### For Learners
- Study the code to understand how Python GUIs work
- Try modifying colors, layouts, or adding new features
- Use this as a foundation for your own projects
- Remember: AI is a tool to assist, not replace, learning

## Contributing

This is a learning project! Feel free to:
- Fork the project
- Add new features
- Improve the design
- Fix bugs
- Share your modifications

## License

This project is for educational purposes. Feel free to use, modify, and share it!

## Acknowledgements

- Built with Python and Tkinter
- Icons from Unicode characters
- Designed for clarity and learning

---

**Note**: This is a learning project. It's not intended for production use but is fully functional for personal task management. The code is well-commented and organized to help you learn Python GUI programming.

Happy task managing! 🚀


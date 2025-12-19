import tkinter as tk
from tkinter import ttk, messagebox, simpledialog, font
import json
import os
from datetime import datetime

class TaskItem:
    """Represents a single task item with checkbox"""
    def __init__(self, text="", done=False, created_at=None):
        self.text = text
        self.done = done
        self.created_at = created_at or datetime.now().strftime("%Y-%m-%d %H:%M")
        self.completed_at = None

class TaskList:
    """Represents a list of tasks (like 'Grocery' or 'To-Do')"""
    def __init__(self, name="New List", color=None):
        self.name = name
        self.color = color or "#4A90E2"  # Default blue
        self.items = []
        self.created_at = datetime.now().strftime("%Y-%m-%d")
    
    def add_item(self, text):
        self.items.append(TaskItem(text))
    
    def remove_item(self, index):
        if 0 <= index < len(self.items):
            self.items.pop(index)
    
    def toggle_item(self, index):
        if 0 <= index < len(self.items):
            self.items[index].done = not self.items[index].done
            if self.items[index].done:
                self.items[index].completed_at = datetime.now().strftime("%Y-%m-%d %H:%M")
            else:
                self.items[index].completed_at = None
    
    def edit_item(self, index, new_text):
        if 0 <= index < len(self.items):
            self.items[index].text = new_text
    
    def get_stats(self):
        total = len(self.items)
        completed = sum(1 for item in self.items if item.done)
        progress = (completed / total * 100) if total > 0 else 0
        return total, completed, progress

class ProfessionalTaskManagerApp:
    """Main application class with professional UI"""
    def __init__(self, root):
        self.root = root
        self.root.title("TaskMaster Pro")
        self.root.geometry("1000x1000")
        
        # Professional color scheme
        self.colors = {
            "primary": "#2C3E50",        # Dark blue-gray
            "secondary": "#34495E",       # Medium blue-gray
            "accent": "#3498DB",          # Bright blue
            "success": "#2ECC71",         # Green
            "warning": "#F39C12",         # Orange
            "danger": "#E74C3C",          # Red
            "light": "#ECF0F1",           # Light gray
            "dark": "#2C3E50",            # Dark gray
            "text": "#2C3E50",            # Text color
            "text_light": "#7F8C8D",      # Light text
            "background": "#FFFFFF",      # White background
            "sidebar": "#F8F9FA",         # Sidebar background
            "card": "#FFFFFF",            # Card background
            "border": "#E0E0E0"           # Border color
        }
        
        # Define professional icons (using unicode)
        self.icons = {
            "plus": "➕",
            "trash": "🗑️",
            "edit": "✏️",
            "check": "✓",
            "list": "📋",
            "stats": "📊",
            "search": "🔍",
            "export": "📤",
            "menu": "☰",
            "close": "✕",
            "complete": "✅",
            "incomplete": "⭕"
        }
        
        # Data storage
        self.task_lists = []
        self.current_list_index = -1
        
        # Configure styles first
        self.configure_styles()
        
        # Setup GUI
        self.setup_ui()
        
        # Load saved data
        self.load_data()
        
        # Select first list if exists
        if self.task_lists:
            self.select_list(0)
    
    def configure_styles(self):
        """Configure professional Tkinter styles"""
        style = ttk.Style()
        
        # Modern theme
        style.theme_use('clam')
        
        # Configure colors
        style.configure("Primary.TButton",
                       background=self.colors["accent"],
                       foreground="white",
                       borderwidth=0,
                       focusthickness=3,
                       focuscolor=self.colors["accent"],
                       font=("Segoe UI", 10, "bold"),
                       padding=10)
        
        style.configure("Secondary.TButton",
                       background=self.colors["light"],
                       foreground=self.colors["text"],
                       borderwidth=1,
                       bordercolor=self.colors["border"],
                       font=("Segoe UI", 10),
                       padding=8)
        
        style.configure("Danger.TButton",
                       background=self.colors["danger"],
                       foreground="white",
                       font=("Segoe UI", 10),
                       padding=8)
        
        style.configure("Success.TButton",
                       background=self.colors["success"],
                       foreground="white",
                       font=("Segoe UI", 10),
                       padding=8)
        
        style.configure("TFrame",
                       background=self.colors["background"])
        
        style.configure("Card.TFrame",
                       background=self.colors["card"],
                       relief="solid",
                       borderwidth=1,
                       bordercolor=self.colors["border"])
        
        style.configure("Sidebar.TFrame",
                       background=self.colors["sidebar"])
        
        style.configure("Title.TLabel",
                       background=self.colors["sidebar"],
                       foreground=self.colors["primary"],
                       font=("Segoe UI", 16, "bold"))
        
        style.configure("Heading.TLabel",
                       background=self.colors["background"],
                       foreground=self.colors["primary"],
                       font=("Segoe UI", 14, "bold"))
        
        style.configure("Body.TLabel",
                       background=self.colors["background"],
                       foreground=self.colors["text"],
                       font=("Segoe UI", 11))
        
        style.configure("Muted.TLabel",
                       background=self.colors["background"],
                       foreground=self.colors["text_light"],
                       font=("Segoe UI", 10))
        
        style.configure("Stats.TLabel",
                       background=self.colors["light"],
                       foreground=self.colors["primary"],
                       font=("Segoe UI", 12, "bold"),
                       padding=5)
    
    def setup_ui(self):
        """Create all GUI components with professional design"""
        # Configure grid weights
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)
        
        # Set background
        self.root.configure(bg=self.colors["background"])
        
        # ===== LEFT PANEL (Professional Sidebar) =====
        self.left_frame = ttk.Frame(self.root, style="Sidebar.TFrame", width=280)
        self.left_frame.grid(row=0, column=0, sticky="nswe")
        self.left_frame.grid_propagate(False)
        
        # Sidebar content with padding
        sidebar_content = ttk.Frame(self.left_frame, style="Sidebar.TFrame", padding="20")
        sidebar_content.pack(fill="both", expand=True)
        
        # App Logo/Title
        title_frame = ttk.Frame(sidebar_content, style="Sidebar.TFrame")
        title_frame.pack(fill="x", pady=(0, 25))
        
        ttk.Label(title_frame, 
                 text="📋 TaskMaster",
                 style="Title.TLabel").pack(anchor="w")
        
        ttk.Label(title_frame,
                 text="Professional Task Manager",
                 style="Muted.TLabel").pack(anchor="w")
        
        # Quick Stats Card
        self.stats_card = ttk.Frame(sidebar_content, style="Card.TFrame", padding="15")
        self.stats_card.pack(fill="x", pady=(0, 20))
        
        ttk.Label(self.stats_card,
                 text=f"{self.icons['stats']} Overview",
                 style="Heading.TLabel").pack(anchor="w", pady=(0, 10))
        
        self.stats_labels = ttk.Frame(self.stats_card, style="Card.TFrame")
        self.stats_labels.pack(fill="x")
        
        ttk.Label(self.stats_labels,
                 text="Total Lists: 0",
                 style="Stats.TLabel").pack(fill="x", pady=2)
        
        ttk.Label(self.stats_labels,
                 text="Total Tasks: 0",
                 style="Stats.TLabel").pack(fill="x", pady=2)
        
        ttk.Label(self.stats_labels,
                 text="Completed: 0%",
                 style="Stats.TLabel").pack(fill="x", pady=2)
        
        # Create List Button (Prominent)
        ttk.Button(sidebar_content,
                  text=f"{self.icons['plus']} Create New List",
                  style="Primary.TButton",
                  command=self.create_new_list).pack(fill="x", pady=(0, 20))
        
        # Lists Section
        lists_header = ttk.Frame(sidebar_content, style="Sidebar.TFrame")
        lists_header.pack(fill="x", pady=(0, 10))
        
        ttk.Label(lists_header,
                 text=f"{self.icons['list']} Your Lists",
                 style="Heading.TLabel").pack(side="left")
        
        # Listbox with modern styling
        listbox_container = ttk.Frame(sidebar_content, style="Card.TFrame", padding="5")
        listbox_container.pack(fill="both", expand=True, pady=(0, 15))
        
        self.listbox = tk.Listbox(
            listbox_container,
            font=("Segoe UI", 11),
            bg=self.colors["card"],
            fg=self.colors["text"],
            selectbackground=self.colors["accent"],
            selectforeground="white",
            highlightthickness=0,
            borderwidth=0,
            activestyle="none",
            relief="flat"
        )
        
        scrollbar = ttk.Scrollbar(listbox_container, orient="vertical", command=self.listbox.yview)
        self.listbox.configure(yscrollcommand=scrollbar.set)
        
        self.listbox.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Bind selection event
        self.listbox.bind('<<ListboxSelect>>', self.on_list_select)
        self.listbox.bind('<Double-Button-1>', lambda e: self.rename_list())
        
        # List Management Buttons
        button_frame = ttk.Frame(sidebar_content, style="Sidebar.TFrame")
        button_frame.pack(fill="x", pady=(0, 10))
        
        ttk.Button(button_frame,
                  text=f"{self.icons['edit']} Rename",
                  style="Secondary.TButton",
                  command=self.rename_list).pack(side="left", fill="x", expand=True, padx=(0, 5))
        
        ttk.Button(button_frame,
                  text=f"{self.icons['trash']} Delete",
                  style="Danger.TButton",
                  command=self.delete_list).pack(side="right", fill="x", expand=True)
        
        # Export Button
        ttk.Button(sidebar_content,
                  text=f"{self.icons['export']} Export All",
                  style="Secondary.TButton",
                  command=self.export_data).pack(fill="x")
        
        # ===== RIGHT PANEL (Main Content Area) =====
        self.right_frame = ttk.Frame(self.root, style="TFrame", padding="30")
        self.right_frame.grid(row=0, column=1, sticky="nswe")
        
        # Header with list title and stats
        self.header_frame = ttk.Frame(self.right_frame, style="TFrame")
        self.header_frame.pack(fill="x", pady=(0, 25))
        
        # List title with icon
        title_container = ttk.Frame(self.header_frame, style="TFrame")
        title_container.pack(fill="x", pady=(0, 15))
        
        self.list_icon_label = ttk.Label(title_container,
                                        text=self.icons["list"],
                                        font=("Segoe UI", 24),
                                        background=self.colors["background"])
        self.list_icon_label.pack(side="left", padx=(0, 15))
        
        self.current_list_label = ttk.Label(title_container,
                                           text="Select a list to begin",
                                           style="Title.TLabel")
        self.current_list_label.pack(side="left")
        
        # List statistics (progress bar)
        self.stats_frame = ttk.Frame(self.header_frame, style="Card.TFrame", padding="15")
        self.stats_frame.pack(fill="x")
        
        self.progress_frame = ttk.Frame(self.stats_frame, style="Card.TFrame")
        self.progress_frame.pack(fill="x", pady=(0, 10))
        
        self.progress_label = ttk.Label(self.progress_frame,
                                       text="Progress: 0/0 (0%)",
                                       style="Body.TLabel")
        self.progress_label.pack(side="left")
        
        # Progress bar
        self.progress_bar = ttk.Progressbar(self.progress_frame,
                                           length=200,
                                           mode='determinate')
        self.progress_bar.pack(side="right")
        
        # Date information
        self.date_label = ttk.Label(self.stats_frame,
                                   text="Created: --",
                                   style="Muted.TLabel")
        self.date_label.pack(anchor="w")
        
        # Items Container (Scrollable)
        items_container = ttk.Frame(self.right_frame, style="TFrame")
        items_container.pack(fill="both", expand=True, pady=(0, 20))
        
        # Items list with modern scrollable canvas
        self.canvas = tk.Canvas(items_container,
                               bg=self.colors["background"],
                               highlightthickness=0,
                               bd=0)
        
        scrollbar = ttk.Scrollbar(items_container,
                                 orient="vertical",
                                 command=self.canvas.yview)
        
        self.scrollable_frame = ttk.Frame(self.canvas, style="TFrame")
        
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )
        
        self.canvas.create_window((0, 0),
                                 window=self.scrollable_frame,
                                 anchor="nw",
                                 width=self.canvas.winfo_reqwidth())
        
        self.canvas.configure(yscrollcommand=scrollbar.set)
        
        self.canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Bind mousewheel for scrolling
        self.canvas.bind_all("<MouseWheel>", self._on_mousewheel)
        
        # Empty state message
        self.empty_state_frame = ttk.Frame(self.right_frame, style="TFrame")
        self.empty_state_frame.pack(fill="both", expand=True)
        
        ttk.Label(self.empty_state_frame,
                 text="🎯 No List Selected",
                 style="Heading.TLabel").pack(pady=(50, 10))
        
        ttk.Label(self.empty_state_frame,
                 text="Select a list from the sidebar or create a new one to get started.",
                 style="Body.TLabel",
                 wraplength=400).pack()
        
        ttk.Label(self.empty_state_frame,
                 text="💡 Tip: You can double-click a list name to rename it.",
                 style="Muted.TLabel",
                 wraplength=400).pack(pady=(20, 0))
        
        # Add Item Section (Initially hidden)
        self.add_item_frame = ttk.Frame(self.right_frame, style="Card.TFrame", padding="20")
        self.add_item_frame.pack_forget()
        
        ttk.Label(self.add_item_frame,
                 text="Add New Task",
                 style="Heading.TLabel").pack(anchor="w", pady=(0, 15))
        
        input_frame = ttk.Frame(self.add_item_frame, style="Card.TFrame")
        input_frame.pack(fill="x")
        
        self.new_item_var = tk.StringVar()
        self.item_entry = ttk.Entry(input_frame,
                                   textvariable=self.new_item_var,
                                   font=("Segoe UI", 12),
                                   width=40)
        self.item_entry.pack(side="left", fill="x", expand=True, padx=(0, 15))
        
        ttk.Button(input_frame,
                  text=f"{self.icons['plus']} Add Task",
                  style="Success.TButton",
                  command=self.add_new_item).pack(side="right")
        
        # Quick Tips
        tips_frame = ttk.Frame(self.add_item_frame, style="Card.TFrame")
        tips_frame.pack(fill="x", pady=(20, 0))
        
        ttk.Label(tips_frame,
                 text="💡 Quick Tips:",
                 style="Body.TLabel").pack(anchor="w", pady=(0, 5))
        
        ttk.Label(tips_frame,
                 text="• Press Enter to add tasks quickly",
                 style="Muted.TLabel").pack(anchor="w")
        
        ttk.Label(tips_frame,
                 text="• Click checkboxes to mark tasks complete",
                 style="Muted.TLabel").pack(anchor="w")
        
        ttk.Label(tips_frame,
                 text="• Click task text to edit, or use the edit button",
                 style="Muted.TLabel").pack(anchor="w")
        
        # Item Management Buttons
        self.item_buttons_frame = ttk.Frame(self.right_frame, style="TFrame")
        self.item_buttons_frame.pack_forget()
        
        ttk.Button(self.item_buttons_frame,
                  text=f"{self.icons['edit']} Rename Selected Task",
                  style="Secondary.TButton",
                  command=self.rename_selected_item).pack(side="left", padx=(0, 10))
        
        ttk.Label(self.item_buttons_frame,
                 text="or simply click on any task text",
                 style="Muted.TLabel").pack(side="left")
        
        # Bind Enter key to add item
        self.root.bind('<Return>', lambda e: self.add_new_item())
        
        # Update initial stats
        self.update_stats()
    
    def _on_mousewheel(self, event):
        """Handle mousewheel scrolling"""
        self.canvas.yview_scroll(int(-1*(event.delta/120)), "units")
    
    def update_stats(self):
        """Update statistics display"""
        total_lists = len(self.task_lists)
        total_tasks = sum(len(list_.items) for list_ in self.task_lists)
        completed_tasks = sum(sum(1 for item in list_.items if item.done) for list_ in self.task_lists)
        completion_rate = (completed_tasks / total_tasks * 100) if total_tasks > 0 else 0
        
        # Update stats labels
        for widget in self.stats_labels.winfo_children():
            widget.destroy()
        
        ttk.Label(self.stats_labels,
                 text=f"📋 Lists: {total_lists}",
                 style="Stats.TLabel").pack(fill="x", pady=2)
        
        ttk.Label(self.stats_labels,
                 text=f"✓ Tasks: {total_tasks}",
                 style="Stats.TLabel").pack(fill="x", pady=2)
        
        ttk.Label(self.stats_labels,
                 text=f"📈 Complete: {completion_rate:.1f}%",
                 style="Stats.TLabel").pack(fill="x", pady=2)
    
    def refresh_listbox(self):
        """Update the listbox with current task lists"""
        self.listbox.delete(0, tk.END)
        for task_list in self.task_lists:
            # Add list icon and stats
            total, completed, _ = task_list.get_stats()
            display_text = f"  {self.icons['list']}  {task_list.name}  ({completed}/{total})"
            self.listbox.insert(tk.END, display_text)
        
        self.update_stats()
    
    def refresh_items_display(self):
        """Update the display of items for the current list"""
        if self.current_list_index == -1:
            # Show empty state
            self.empty_state_frame.pack(fill="both", expand=True)
            self.add_item_frame.pack_forget()
            self.item_buttons_frame.pack_forget()
            self.header_frame.pack_forget()
            return
        
        # Hide empty state, show content
        self.empty_state_frame.pack_forget()
        self.header_frame.pack(fill="x", pady=(0, 25))
        self.add_item_frame.pack(fill="x", pady=(0, 20))
        
        current_list = self.task_lists[self.current_list_index]
        
        # Update header
        self.current_list_label.config(text=current_list.name)
        
        # Update list icon based on completion
        all_done = all(item.done for item in current_list.items) if current_list.items else False
        self.list_icon_label.config(text="✅" if all_done else self.icons["list"])
        
        # Update statistics
        total, completed, progress = current_list.get_stats()
        self.progress_label.config(text=f"Progress: {completed}/{total} ({progress:.1f}%)")
        self.progress_bar['value'] = progress
        
        # Update date
        self.date_label.config(text=f"Created: {current_list.created_at}")
        
        # Show/hide item buttons
        if current_list.items:
            self.item_buttons_frame.pack(fill="x", pady=(0, 20))
        else:
            self.item_buttons_frame.pack_forget()
        
        # Clear current items
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()
        
        # Display each item with professional styling
        if not current_list.items:
            # Show empty list state
            empty_card = ttk.Frame(self.scrollable_frame, style="Card.TFrame", padding="40")
            empty_card.pack(fill="x", pady=20)
            
            ttk.Label(empty_card,
                     text="📭 No tasks yet",
                     style="Heading.TLabel").pack(pady=(0, 10))
            
            ttk.Label(empty_card,
                     text="Add your first task using the form below",
                     style="Body.TLabel").pack()
        else:
            for i, item in enumerate(current_list.items):
                self.create_item_widget(i, item)
        
        # Focus on entry for quick typing
        self.item_entry.focus_set()
    
    def create_item_widget(self, index, item):
        """Create a professional widget for a single item"""
        # Create card frame
        card = ttk.Frame(self.scrollable_frame, style="Card.TFrame", padding="15")
        card.pack(fill="x", pady=5, padx=2)
        
        # Main content frame
        content_frame = ttk.Frame(card, style="Card.TFrame")
        content_frame.pack(fill="x")
        
        # Checkbox and text
        left_frame = ttk.Frame(content_frame, style="Card.TFrame")
        left_frame.pack(side="left", fill="x", expand=True)
        
        # Custom checkbox with better styling
        var = tk.BooleanVar(value=item.done)
        
        # Create a canvas for custom checkbox
        checkbox_canvas = tk.Canvas(left_frame,
                                   width=24,
                                   height=24,
                                   bg=self.colors["card"],
                                   highlightthickness=0)
        checkbox_canvas.pack(side="left", padx=(0, 15))
        
        # Draw checkbox
        checkbox_id = checkbox_canvas.create_oval(2, 2, 22, 22,
                                                 fill="white",
                                                 outline=self.colors["border"],
                                                 width=2)
        
        if item.done:
            checkbox_canvas.create_text(12, 12,
                                       text="✓",
                                       font=("Segoe UI", 12, "bold"),
                                       fill=self.colors["success"])
        
        # Bind click event
        checkbox_canvas.bind("<Button-1>", lambda e, idx=index: self.toggle_item(idx))
        
        # Item text with professional styling
        if item.done:
            text_widget = ttk.Label(left_frame,
                                   text=item.text,
                                   style="Body.TLabel",
                                   foreground=self.colors["text_light"],
                                   cursor="hand2")
        else:
            text_widget = ttk.Label(left_frame,
                                   text=item.text,
                                   style="Body.TLabel",
                                   cursor="hand2")
        
        text_widget.pack(side="left", fill="x", expand=True)
        
        # Make label editable on click
        text_widget.bind("<Button-1>", lambda e, idx=index: self.edit_item_text(idx))
        
        # Hover effect
        def on_enter(e):
            if not item.done:
                text_widget.configure(foreground=self.colors["accent"])
        
        def on_leave(e):
            if item.done:
                text_widget.configure(foreground=self.colors["text_light"])
            else:
                text_widget.configure(foreground=self.colors["text"])
        
        text_widget.bind("<Enter>", on_enter)
        text_widget.bind("<Leave>", on_leave)
        
        # Date and actions frame
        right_frame = ttk.Frame(content_frame, style="Card.TFrame")
        right_frame.pack(side="right")
        
        # Date info
        if item.done and item.completed_at:
            date_text = f"Completed: {item.completed_at}"
        else:
            date_text = f"Added: {item.created_at}"
        
        ttk.Label(right_frame,
                 text=date_text,
                 style="Muted.TLabel",
                 font=("Segoe UI", 9)).pack(side="left", padx=(0, 15))
        
        # Action buttons
        actions_frame = ttk.Frame(right_frame, style="Card.TFrame")
        actions_frame.pack(side="right")
        
        # Edit button
        edit_btn = ttk.Button(actions_frame,
                             text=self.icons["edit"],
                             style="Secondary.TButton",
                             width=3,
                             command=lambda idx=index: self.edit_item_text(idx))
        edit_btn.pack(side="left", padx=(0, 5))
        
        # Delete button
        delete_btn = ttk.Button(actions_frame,
                               text=self.icons["trash"],
                               style="Danger.TButton",
                               width=3,
                               command=lambda idx=index: self.delete_item(idx))
        delete_btn.pack(side="left")
    
    # [The rest of the methods remain mostly the same as before, 
    # but with updated styling references...]
    
    def on_list_select(self, event):
        """Handle list selection from listbox"""
        selection = self.listbox.curselection()
        if selection:
            self.select_list(selection[0])
    
    def select_list(self, index):
        """Select and display a task list"""
        if 0 <= index < len(self.task_lists):
            self.current_list_index = index
            self.listbox.selection_clear(0, tk.END)
            self.listbox.selection_set(index)
            self.listbox.activate(index)
            self.refresh_items_display()
    
    def create_new_list(self):
        """Create a new empty task list"""
        name = simpledialog.askstring(
            "Create New List", 
            f"{self.icons['plus']} Enter a name for your new list:",
            parent=self.root
        )
        
        if name:
            name = name.strip()
            if not name:
                messagebox.showwarning("Warning", "List name cannot be empty!")
                return
            
            # Check for duplicate names
            for task_list in self.task_lists:
                if task_list.name.lower() == name.lower():
                    messagebox.showerror("Error", f"A list named '{name}' already exists!")
                    return
            
            new_list = TaskList(name)
            self.task_lists.append(new_list)
            self.refresh_listbox()
            self.select_list(len(self.task_lists) - 1)
            self.save_data()
    
    def rename_list(self):
        """Rename the currently selected list"""
        if self.current_list_index == -1:
            messagebox.showwarning("Warning", "Please select a list first!")
            return
        
        current_list = self.task_lists[self.current_list_index]
        new_name = simpledialog.askstring(
            "Rename List", 
            f"{self.icons['rename']} Enter new name for the list:",
            initialvalue=current_list.name,
            parent=self.root
        )
        
        if new_name and new_name != current_list.name:
            new_name = new_name.strip()
            if not new_name:
                messagebox.showwarning("Warning", "List name cannot be empty!")
                return
            
            # Check for duplicate names
            for task_list in self.task_lists:
                if task_list.name.lower() == new_name.lower() and task_list != current_list:
                    messagebox.showerror("Error", f"A list named '{new_name}' already exists!")
                    return
            
            current_list.name = new_name
            self.refresh_listbox()
            self.select_list(self.current_list_index)
            self.save_data()
    
    def rename_selected_item(self):
        """Rename an item using a button"""
        if self.current_list_index == -1:
            messagebox.showwarning("Warning", "Please select a list first!")
            return
        
        current_list = self.task_lists[self.current_list_index]
        if not current_list.items:
            messagebox.showinfo("Info", "This list has no items to rename.")
            return
        
        # Create a selection dialog
        selection_dialog = tk.Toplevel(self.root)
        selection_dialog.title("Select Item to Rename")
        selection_dialog.geometry("400x300")
        selection_dialog.transient(self.root)
        selection_dialog.grab_set()
        
        # Center dialog
        selection_dialog.update_idletasks()
        x = self.root.winfo_x() + (self.root.winfo_width() // 2) - (400 // 2)
        y = self.root.winfo_y() + (self.root.winfo_height() // 2) - (300 // 2)
        selection_dialog.geometry(f"+{x}+{y}")
        
        ttk.Label(selection_dialog,
                 text=f"{self.icons['edit']} Select an item to rename:",
                 font=("Segoe UI", 12, "bold")).pack(pady=20)
        
        # Listbox for item selection
        listbox = tk.Listbox(selection_dialog,
                            font=("Segoe UI", 11),
                            selectbackground=self.colors["accent"])
        listbox.pack(fill="both", expand=True, padx=20, pady=(0, 20))
        
        for i, item in enumerate(current_list.items):
            status = "✓ " if item.done else "⭕ "
            listbox.insert(tk.END, f"{i+1}. {status}{item.text[:60]}")
        
        def on_select():
            selection = listbox.curselection()
            if selection:
                selection_dialog.destroy()
                self.edit_item_text(selection[0])
        
        ttk.Button(selection_dialog,
                  text="Rename Selected",
                  style="Primary.TButton",
                  command=on_select).pack(pady=(0, 20))
    
    def delete_list(self):
        """Delete the currently selected list"""
        if self.current_list_index == -1:
            messagebox.showwarning("Warning", "Please select a list first!")
            return
        
        list_name = self.task_lists[self.current_list_index].name
        item_count = len(self.task_lists[self.current_list_index].items)
        
        confirm = messagebox.askyesno(
            "Delete List",
            f"{self.icons['trash']} Delete the list '{list_name}'?\n\n"
            f"This will permanently delete {item_count} item{'s' if item_count != 1 else ''}.",
            icon="warning"
        )
        
        if confirm:
            self.task_lists.pop(self.current_list_index)
            self.refresh_listbox()
            self.current_list_index = -1
            self.refresh_items_display()
            self.save_data()
    
    def add_new_item(self):
        """Add a new item to the current list"""
        if self.current_list_index == -1:
            messagebox.showwarning("Warning", "Please select a list first!")
            return
        
        text = self.new_item_var.get().strip()
        if text:
            self.task_lists[self.current_list_index].add_item(text)
            self.new_item_var.set("")
            self.refresh_items_display()
            self.save_data()
    
    def toggle_item(self, index):
        """Toggle item completion status"""
        if self.current_list_index == -1:
            return
        
        self.task_lists[self.current_list_index].toggle_item(index)
        self.refresh_items_display()
        self.save_data()
    
    def edit_item_text(self, index):
        """Edit the text of an item"""
        if self.current_list_index == -1:
            return
        
        current_list = self.task_lists[self.current_list_index]
        if 0 <= index < len(current_list.items):
            item = current_list.items[index]
            new_text = simpledialog.askstring(
                "Edit Task", 
                f"{self.icons['edit']} Edit task description:",
                initialvalue=item.text,
                parent=self.root
            )
            if new_text:
                new_text = new_text.strip()
                if new_text and new_text != item.text:
                    current_list.edit_item(index, new_text)
                    self.refresh_items_display()
                    self.save_data()
    
    def delete_item(self, index):
        """Delete an item from the current list"""
        if self.current_list_index == -1:
            return
        
        current_list = self.task_lists[self.current_list_index]
        if 0 <= index < len(current_list.items):
            item_text = current_list.items[index].text
            
            if len(item_text) < 30:
                current_list.remove_item(index)
                self.refresh_items_display()
                self.save_data()
            else:
                if messagebox.askyesno("Delete Task", 
                                      f"{self.icons['trash']} Delete this task?"):
                    current_list.remove_item(index)
                    self.refresh_items_display()
                    self.save_data()
    
    def export_data(self):
        """Export all data to a file"""
        try:
            with open("taskmaster_export.txt", "w") as f:
                f.write("=" * 50 + "\n")
                f.write("TASKMASTER PRO EXPORT\n")
                f.write(f"Export Date: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n")
                f.write("=" * 50 + "\n\n")
                
                for task_list in self.task_lists:
                    total, completed, progress = task_list.get_stats()
                    f.write(f"📋 {task_list.name.upper()}\n")
                    f.write(f"   Progress: {completed}/{total} tasks ({progress:.1f}%)\n")
                    f.write(f"   Created: {task_list.created_at}\n")
                    f.write("-" * 40 + "\n")
                    
                    for i, item in enumerate(task_list.items, 1):
                        status = "✓" if item.done else "⭕"
                        f.write(f"   {i}. [{status}] {item.text}\n")
                        if item.done and item.completed_at:
                            f.write(f"       Completed: {item.completed_at}\n")
                    
                    f.write("\n")
                
                f.write("=" * 50 + "\n")
                f.write(f"Total Lists: {len(self.task_lists)}\n")
                total_tasks = sum(len(list_.items) for list_ in self.task_lists)
                f.write(f"Total Tasks: {total_tasks}\n")
                f.write("=" * 50 + "\n")
            
            messagebox.showinfo("Export Successful",
                              f"Data exported to 'taskmaster_export.txt'\n\n"
                              f"Lists: {len(self.task_lists)}\n"
                              f"Tasks: {sum(len(list_.items) for list_ in self.task_lists)}")
        except Exception as e:
            messagebox.showerror("Export Failed", f"Could not export data: {str(e)}")
    
    # ===== DATA PERSISTENCE =====
    
    def save_data(self):
        """Save all data to JSON file"""
        data = []
        for task_list in self.task_lists:
            list_data = {
                "name": task_list.name,
                "color": task_list.color,
                "created_at": task_list.created_at,
                "items": [{
                    "text": item.text,
                    "done": item.done,
                    "created_at": item.created_at,
                    "completed_at": item.completed_at
                } for item in task_list.items]
            }
            data.append(list_data)
        
        with open("taskmaster_data.json", "w") as f:
            json.dump(data, f, indent=2, default=str)
    
    def load_data(self):
        """Load data from JSON file"""
        if os.path.exists("taskmaster_data.json"):
            try:
                with open("taskmaster_data.json", "r") as f:
                    data = json.load(f)
                
                self.task_lists = []
                for list_data in data:
                    task_list = TaskList(list_data["name"], list_data.get("color"))
                    task_list.created_at = list_data.get("created_at", datetime.now().strftime("%Y-%m-%d"))
                    
                    for item_data in list_data["items"]:
                        item = TaskItem(
                            item_data["text"],
                            item_data.get("done", False)
                        )
                        item.created_at = item_data.get("created_at", datetime.now().strftime("%Y-%m-%d %H:%M"))
                        item.completed_at = item_data.get("completed_at")
                        task_list.items.append(item)
                    
                    self.task_lists.append(task_list)
                
                self.refresh_listbox()
            except Exception as e:
                messagebox.showerror("Error", f"Failed to load data: {str(e)}")
                # Create default list
                default_list = TaskList("Getting Started")
                default_list.add_item("Welcome to TaskMaster Pro!")
                default_list.add_item("Click checkboxes to mark tasks complete")
                default_list.add_item("Click task text to edit")
                default_list.add_item("Use the sidebar to manage your lists")
                self.task_lists = [default_list]
                self.refresh_listbox()
        else:
            # Create default list
            default_list = TaskList("Getting Started")
            default_list.add_item("Welcome to TaskMaster Pro!")
            default_list.add_item("Click checkboxes to mark tasks complete")
            default_list.add_item("Click task text to edit")
            default_list.add_item("Use the sidebar to manage your lists")
            self.task_lists = [default_list]
            self.refresh_listbox()

def main():
    """Start the professional application"""
    root = tk.Tk()
    
    # Set window icon and title
    root.title("TaskMaster Pro")
    
    # Set minimum window size
    root.minsize(900, 600)
    
    # Create application
    app = ProfessionalTaskManagerApp(root)
    
    # Center window on screen
    root.update_idletasks()
    width = root.winfo_width()
    height = root.winfo_height()
    x = (root.winfo_screenwidth() // 2) - (width // 2)
    y = (root.winfo_screenheight() // 2) - (height // 2)
    root.geometry(f'{width}x{height}+{x}+{y}')
    
    # Start main loop
    root.mainloop()

if __name__ == "__main__":
    main()

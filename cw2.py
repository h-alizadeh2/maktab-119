class Menu:
    def __init__(self, name, description, parent=None):
        self.name = name
        self.description = description
        self.parent = parent
        self.children = {}

    def add_child(self, child_menu):
        self.children[child_menu.name] = child_menu

    def display(self):
        print(f"\n--- {self.name} ---")
        print(self.description)
        for index, child in enumerate(self.children.values(), start=1):
            print(f"{index}. {child.name}")
        print("r. Return to previous menu")

    def handle_selection(self, choice):
        if choice == 'r' and self.parent:
            self.parent.display()
            self.parent.handle_selection(input(f"Select an option in {self.parent.name}: "))
        else:
            try:
                choice_index = int(choice) - 1
                selected_child = list(self.children.values())[choice_index]
                selected_child.display()
                selected_child.handle_selection(input(f"Select an option in {selected_child.name}: "))
            except (ValueError, IndexError):
                print("Invalid choice. Please try again.")
                self.display()
                self.handle_selection(input(f"Select an option in {self.name}: "))


class ActionMenu(Menu):
    def __init__(self, name, description, action, parent=None):
        super().__init__(name, description, parent)
        self.action = action

    def display(self):
        print(f"\n--- {self.name} ---")
        print(self.description)
        print("1. Perform Action")
        print("r. Return to previous menu")

    def handle_selection(self, choice):
        if choice == '1':
            self.action()
            self.parent.display()
            self.parent.handle_selection(input(f"Select an option in {self.parent.name}: "))
        elif choice == 'r' and self.parent:
            self.parent.display()
            self.parent.handle_selection(input(f"Select an option in {self.parent.name}: "))
        else:
            print("Invalid choice. Please try again.")
            self.display()
            self.handle_selection(input(f"Select an option in {self.name}: "))


# Define your actions
def action_one():
    print("Action One performed!")

def action_two():
    print("Action Two performed!")

# Create the menu structure
main_menu = Menu("Main Menu", "Welcome to the main menu.")

submenu_1 = Menu("Submenu 1", "Options for submenu 1.", main_menu)
submenu_2 = Menu("Submenu 2", "Options for submenu 2.", main_menu)

action_menu_1 = ActionMenu("Action Menu 1", "This performs action one.", action_one, submenu_1)
action_menu_2 = ActionMenu("Action Menu 2", "This performs action two.", action_two, submenu_2)

# Add child menus
main_menu.add_child(submenu_1)
main_menu.add_child(submenu_2)
submenu_1.add_child(action_menu_1)
submenu_2.add_child(action_menu_2)

# Start the menu
main_menu.display()
main_menu.handle_selection(input(f"Select an option in {main_menu.name}: "))
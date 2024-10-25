class Route:
    def __init__(self, name, callback=None, condition=None, description=None, children=None):
        self.name = name
        self.callback = callback
        self.condition = condition
        self.description = description
        self.children = children if children is not None else []

    def is_active(self):
        return self.condition is None or self.condition()


class Router:
    def __init__(self, root_route):
        self.root_route = root_route

    def display_menu(self, route=None):
        if route is None:
            route = self.root_route

            # Display the current route title/description
        print(f"\n{route.name}")
        if route.description:
            print(f"{route.description}")
        print("Select an option:")

        # List available child routes
        for index, child in enumerate(route.children):
            if child.is_active():
                print(f"{index + 1}. {child.name}")

        print("0. Exit")

        # Get user input
        choice = int(input("Choose an option: "))
        self.handle_choice(choice, route)

    def handle_choice(self, choice, route):
        if choice == 0:
            print("Exiting...")
            return  # Exit

        # Execute selected route
        active_options = [child for child in route.children if child.is_active()]
        if 1 <= choice <= len(active_options):
            selected_route = active_options[choice - 1]
            if selected_route.callback:
                selected_route.callback()  # Call the respective callback function
            if selected_route.children:
                self.display_menu(selected_route)  # Navigate to child menu if exists
            else:
                self.display_menu(route)  # Back to parent menu if no children
        else:
            print("Invalid choice. Please try again.")
            self.display_menu(route)  # Return to the current menu


# Example usage:
def login():
    print("Login functionality.")


def register():
    print("Register functionality.")


def register_event():
    print("Event registration functionality.")


def show_event_and_buy_ticket():
    print("Showing events and handling ticket buying.")


def logout():
    print("Logout functionality.")


class StateManager:
    _user_logged_in = False

    @staticmethod
    def get_user():
        return StateManager._user_logged_in

    @staticmethod
    def login():
        StateManager._user_logged_in = True

    @staticmethod
    def logout():
        StateManager._user_logged_in = False

    # Define the routes


router = Router(
    Route("Main", description="Ticket shop cli project", children=[
        Route("Login", callback=login, condition=lambda: not StateManager.get_user()),
        Route("Register", callback=register, condition=lambda: not StateManager.get_user()),
        Route("Admin Panel", condition=StateManager.get_user, children=[
            Route("Register Event", callback=register_event),
            Route("Reports", callback=None),
        ]),
        Route("Show Events | Buy Ticket", callback=show_event_and_buy_ticket),
        Route("Logout", callback=logout, condition=StateManager.get_user),
    ])
)

# Start the router menu interface
if __name__ == "__main__":
    router.display_menu()
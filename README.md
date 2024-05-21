AirBnB Clone

Description of the Project:

    This repository contains a simplified clone of the AirBnB web application.
    It is a comprehensive project designed to emulate the core functionalities
    of AirBnB, including property listings, user interactions, and booking
    features. The project is structured to follow a console-oriented approach
    for managing different aspects of the application, providing a foundation
    for understanding backend development and database interactions.

Description of the Command Interpreter:
    The command interpreter is a crucial part of this project, enabling
    users to interact with the application's data models through a command-line
    interface(CLI). It allows users to create, retrieve, update, and delete
    objects within the application.

How to Start the Command Interpreter:

    To start the command interpreter, follow these steps:

        First, clone the repository by using the following commands:
            git clone https: // github.com/Jenniscott/AirBnB_clone.git
            cd AirBnB_clone

Next, make the console executable by running the command:
    chmod + x console.py

Finally, run the console by executing the command:
    ./console.py

How to Use the Command Interpreter:

    The command interpreter supports several commands to manage the
    application's data. Below is a list of available commands and their
    descriptions:

        help: Displays a list of available commands or detailed help for a
        specific command.

quit: Exits the command interpreter.

EOF: Exits the command interpreter.

create < class > - Creates a new instance of the specified class.

show < class > < id > - Displays the string representation of an instance based
on the class and id.

destroy < class > < id > - Deletes an instance based on the class and id.

all < class > - Displays all instances of the specified class or all
instances if no class is specified.

update < class > < id > < attribute name > < attribute value > - Updates an
instance based on the class and id by adding or updating an attribute.

Examples:

    Here are some examples to demonstrate how to use the command interpreter:

        To create a new instance, use the command:
            (hbnb) create User

To show an instance, use the command:
    (hbnb) show User 1f3e9d1e-0df5-4c52-9f65-07bcdc6d736f

To update an instance, use the command:
    (hbnb) update User 1f3e9d1e-0df5-4c52-9f65-07bcdc6d736f name "John Doe"

To show all instances, use the command:
    (hbnb) all User

To destroy an instance, use the command:
    (hbnb) destroy User 1f3e9d1e-0df5-4c52-9f65-07bcdc6d736f

These commands provide a robust interface for interacting with the
application’s backend, allowing for effective testing and development of the
AirBnB clone project.

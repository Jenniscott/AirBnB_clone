import cmd
import models
from models.base_model import BaseModel
from models.user import User
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Command interpreter class."""
    prompt = "(hbnb) "

    classes = {
        'BaseModel': BaseModel,
        'User': User,
        'State': State,
        'City': City,
        'Amenity': Amenity,
        'Place': Place,
        'Review': Review,
    }

    def do_create(self, arg):
        """Creates a new instance of BaseModel, User, or any other valid class, saves it, and prints the id."""
        if not arg:
            print("** class name missing **")
            return
        if arg not in self.classes:
            print("** class doesn't exist **")
            return
        new_instance = self.classes[arg]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance based on the class name and id."""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = f"{args[0]}.{args[1]}"
        instance = models.storage.all().get(key)
        if instance:
            print(instance)
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id."""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = f"{args[0]}.{args[1]}"
        if key in models.storage.all():
            del models.storage.all()[key]
            models.storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representation of all instances based or not on the class name."""
        if arg and arg not in self.classes:
            print("** class doesn't exist **")
            return
        objects = models.storage.all()
        if arg:
            objects = {key: obj for key, obj in objects.items() if key.startswith(arg)}
        print([str(obj) for obj in objects.values()])

    def do_update(self, arg):
        """Updates an instance based on the class name and id by adding or updating attribute."""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = f"{args[0]}.{args[1]}"
        instance = models.storage.all().get(key)
        if not instance:
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        attribute = args[2]
        value = args[3].strip('"')
        if hasattr(instance, attribute):
            value_type = type(getattr(instance, attribute))
            setattr(instance, attribute, value_type(value))
        else:
            setattr(instance, attribute, value)
        instance.save()

    def do_quit(self, arg):
        """Exits the program."""
        return True

    def do_EOF(self, arg):
        """Exits the program."""
        print()
        return True

    def emptyline(self):
        """Overrides the default behavior to repeat the last command."""
        pass

if __name__ == "__main__":
    HBNBCommand().cmdloop()

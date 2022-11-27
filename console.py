#!/usr/bin/python3
''' defines the AirBnB Clone, aka, HBnB console '''

import cmd
import re #regex
from shlex import split
from models import storage
from models.base_model import BaseModel

def parse(arg):
    curly_braces = re.search(r'\{(.*?)\}', arg)
    brackets = re.search(r'\[(.*?)\]', arg)
    if curly_braces is None:
        if brackets is None:
            return [i.strip(',') for i in split(arg)]
        else:
            lexer = split(arg[:brackets.span()[0]])
            ret_one = [i.strip(',') for i in lexer]
            ret_one.append(brackets.group())
            return(ret_one)
    else:
        lexer = split(arg[:curly_braces.span()[0]])
        ret_one = [i.strip(',') for i in lexer]
        ret_one.append(curly_braces.group())
        return(ret_one)

class HBNBCommand(cmd.Cmd):
    ''' defines the HBnB command interprater
    Attributes:
    prompt (str): command prompt
    '''
    prompt = '(hbnb) '
    __classes = {
            'BaseModel',
            'User',
            'State',
            'Amenity',
            'Review'
            }

    def default(self, arg):
        ''' default behaviour for cmd module when input is invalid '''
        arg_dict = {
                'all': self.do_all,
                'show': self.do_show,
                'destroy': self.do_destroy,
                'count': self.do_count,
                'update': self.do_update
                }
        match = re.search(r'\.', arg)
        if match is not None:
            arg_one = [arg[:match.span()[0]], arg[match.span()[1]:]]
            match = re.search(r'\((.*?)\)', arg_one[1])
            if match is not None:
                command = [arg_one[1][:match.span()[0]], match.group()[1:-1]]
                if command[0] in arg_dict.keys():
                    call = '{} {}'.format(arg_one[0], command[1])
                    return arg_dict[command[0]](call)
        print('*** Unknown syntax: {}'.format(arg))
        return False

    def do_count(self, arg):
        '''Usage: count <class> or <class>.count()
        retrieve the number of instances of a given class
        '''
        arg_one = parse(arg)
        count = 0
        for obj in storage.all().values():
            if arg_one[0] == obj.__class__.__name__:
                count += 1
        print(count)

    def do_create(self, arg):
        ''' Usage: create <class>
        create new instance of `BaseModel` saves it (to the JSON file)
            prints the `id`
        '''
        arg_one = parse(arg)
        if len(arg_one) == 0:
            print('** class name missing **')
        elif arg_one[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            print(eval(arg_one[0])().id)
            storage.save()
    
    def do_show(self, arg):
        ''' Usage: show <class> <id> or class.show(<id>)
        display (class)BaseModel string representation of a given id 
        '''
        arg_one = parse(arg)
        obj_dict = storage.all()
        if len(arg_one) == 0:
            print('** class name missing **')
        elif arg_one[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(arg_one) == 1:
            print('** instance id missing **')
        elif '{}.{}'.format(arg_one[0], arg_one[1]) not in obj_dict:
            print('** no instance found **')
        else:
            print(obj_dict['{}.{}'.format(arg_one[0], arg_one[1])])

    def do_destroy(self, arg):
        ''' Usage: destroy <class> <id> or <class>.destroy(<id>)
        deletes an instance based on the class name and id (save change into JSON)
        '''
        arg_one = parse(arg)
        obj_dict = storage.all()
        if len(arg_one) == 0:
            print('** class name is missing **')
        elif arg_one[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(arg_one) == 1:
            print('** instance id is missing **')
        elif '{}.{}'.format(arg_one[0], arg_one[1]) not in obj_dict.keys():
            print('** no instance found **')
        else:
            del obj_dict['{}.{}'.format(arg_one[0], arg_one[1])]
            storage.save()

    def do_all(self, arg):
        ''' Usage: all or <class>.all()
        display (class)BaseModel string representations of all instances
        if no class is specified, display all instanciated objects 
        '''
        arg_one = parse(arg)
        if len(arg_one) > 0 and arg_one[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            obj_one = []
            for obj in storage.all().values():
                if len(arg_one) > 0 and arg_one[0] == obj.__class__.__name__:
                    obj_one.append(obj.__str__())
                elif len(arg_one) == 0:
                    obj_one.append(obj.__str__())
            print(obj_one)

    def do_update(self, arg):
        ''' Usage: update <class name> <id> <attribute name> "<attribute value"
        updaes an instance based on class name and id by adding or updating
        attribute (save change into JSON file)
        '''
        arg_one = parse(arg)
        obj_dict = storage.all()

        if len(arg_one) == 0:
            print('** class name missing **')
            return False
        if arg_one[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return False
        if len(arg_one) == 1:
            print('** instance id is mising **')
            return False
        if '{}.{}'.format(arg_one[0], arg_one[1]) not in obj_dict.keys():
            print('** no instance found **')
            return False
        if len(arg_one) == 2:
            print('** attribute name missing **')
            return False
        if len(arg_one) == 3:
            try:
                type(eval(arg_one[2])) != dict
            except NameError:
                print('** value missing **')
                return False
        if len(arg_one) == 4:
            obj = obj_dict['{}.{}'.format(arg_one[0], arg_one[1])]
            if arg_one[2] in obj.__class__.__dict__.keys():
                val_type = type(obj.__class__.__dict__[arg_one[2]])
                obj.__dict__[arg_one[2]] = val_type(arg_one[3])
            else:
                obj.__dict__[arg_one[2]] = arg_one[3]
        elif type(eval(arg_one[2])) == dict:
            obj = obj_dict['{}.{}'.format(arg_one[0], arg_one[1])]
            for key, vale in eval(arg_one[2]).items():
                if (key in obj.__class__.__dict__.keys() and
                        type(obj.__class__.__dict__[key]) in {str, int, float}):
                    obj.__dict__[key] = val_type(v)
                else:
                    obj.__dict__[key] = value
        storage.save()

    def emptyline(self):
        ''' empty line + `ENTER` shouldn't execute anything - pass '''
        pass

    def do_quit(self, arg):
        ''' quit command to exit the command interpreter '''
        return(True)

    def do_EOF(self, arg):
        ''' End Of File (EOF) signal to exit the command interpreter '''
        print('')
        return(True)

if __name__ == '__main__':
    HBNBCommand().cmdloop()

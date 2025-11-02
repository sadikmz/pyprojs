import os.path
import types
import sys

print("Running importer.py")

def import_(module_name, module_file,module_path):

    # if module_name not in sys.modules:
    #     return sys.modules[module_name]

    module_rel_file_path = os.path.join(module_path, module_file)
    module_abs_file_path = os.path.abspath(module_rel_file_path)

    # Read source code from file
    with open(module_rel_file_path, 'r') as code_file:
        source_code = code_file.read()

    # Create a module object
    mod = types.ModuleType(module_name)
    mod.__file__ = module_abs_file_path

    # Set a ref in sys.module
    sys.modules[module_name] = mod

    # Compile source code
    code = compile(source_code, filename=module_abs_file_path, mode='exec')

    # Execute compiled code
    exec(code, mod.__dict__)

    return sys.modules[module_name]


# # Done
#
# # mod.hello()
#
# import module1
# module1.hello()

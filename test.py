import os
print(os.path.dirname(os.path.realpath(__file__)).replace(os.getcwd() + "/", "").replace("/", "."))
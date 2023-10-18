import os
import src.colours as colours

__data = """
SQLUSER="root"
SQLPASSWD="password"
SQLHOST="localhost"
SQLDB="tig"

EMAILADDR="auth.imagegenerator@gmail.com"
APPPASSWD="gxuw btqk ffuc nznr"

OPENAIAUTHKEY="put your key here"
"""

if __name__ == '__main__':
    if os.path.isfile(".env"):
        print(colours.blue("ENV exists"))
    else:
        with open(".env", "w+") as env_file:
            env_file.write(__data.lstrip("\n"))
else:
    from dotenv import load_dotenv
    load_dotenv()
    print(colours.green("ENV successfully loaded"))

import os
import readline
import datetime as dt
from rich.prompt import Prompt
from rich.console import Console
from rich.table import Table

# Define Rich Console

console = Console()

# Setting

readline.parse_and_bind("tab: complete")
readline.parse_and_bind("set editing-mode vi")

# Welcome

console.print("[bold blue]M[/bold blue]: Welcome to MathConsole")

# Load Plugins

def list_files_in_directory(directory):
    files = os.listdir(directory)
    return files

def process_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        pluginresult = {}
        exec(content, globals(), pluginresult)
        globals().update(pluginresult)

def defineplugins(directory):
    files = list_files_in_directory(directory)

    for file in files:
        file_path = os.path.join(directory, file)
        if os.path.isfile(file_path):
            process_file(file_path)
        else:
            defineplugins(file_path)

directory_path = "/usr/local/share/mathconsole"

try:
    os.mkdir(directory_path)
except FileExistsError:
    pass

try:
    os.mkdir(directory_path + "/plugins")
except FileExistsError:
    pass

defineplugins(directory_path + "/plugins")

# Define Variables

that: any = 0
prev_prompt = ""
prev_result: any = 0
prompt_index = 0
local_vars = {}
result2: any = ""

# Define Standard Functions

now = dt.datetime.now() 

def modulo(a,b): 
    return a % b 
mod = modulo 

def date(a=now.year,b=now.month,c=now.day): 
    return dt.date(a,b,c) 

def time(a=now.hour,b=now.minute,c=now.second): 
    return dt.time(a,b,c) 

def datetime(a=now.year,b=now.month,c=now.day,d=now.hour,e=now.minute,f=now.second): 
    return dt.datetime(a,b,c,d,e,f) 

def prime_factors(ni):
    global result2
    n = int(ni)
    factors = []
    # 2で割れる限り割る
    while n % 2 == 0:
        factors.append(2)
        n = n // 2

    # 3以上の奇数で割れる限り割る
    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n = n // i

    # 最後にnが素数で残っていれば追加
    if n > 2:
        factors.append(n)

    text = f"{ni} = " + " * ".join(map(str, factors)) + "\n"

    for i in range(1, len(factors)):
        text += f"   #{i}: {factors[i]} [ {"- " * factors[i]}] \n"

    result2 = text
    
    return n
prfa = prime_factors

while True:

    try:

        prev_prompt = input(">>> ")
        prompt = "result = " + prev_prompt
        
        result = exec(prompt, globals(), local_vars)
        console.print("[bold green]M[/bold green]:", local_vars.get('result'))
        console.print("[bold green]T[/bold green]:", local_vars.get('result2'))
        globals().update(local_vars)
        that = local_vars.get('result')
        prev_result = that
        prompt_index += 1

    except KeyboardInterrupt:
        print()
        console.print("[bold yellow]E[/bold yellow]: Bye!")
        exit(0)

    except Exception as error:

        if not error == "'result'":

            console.print(f"[bold red]E[/bold red]: {error}")
            prompt_index += 1



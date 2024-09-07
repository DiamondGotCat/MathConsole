import datetime as dt
from rich.prompt import Prompt
from rich.console import Console

console = Console()

console.print("[bold blue]M[/bold blue]: Welcome to MathConsole")

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

that: any = 0
prev_prompt = ""
prev_result: any = 0
prompt_index = 0
local_vars = {}

while True:

    try:

        prev_prompt = Prompt.ask(f"[bold blue]P{prompt_index}[/bold blue]")
        prompt = "result = " + prev_prompt
        
        result = exec(prompt, globals(), local_vars)
        console.print(f"[bold green]M[/bold green]:", local_vars.get('result'))
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



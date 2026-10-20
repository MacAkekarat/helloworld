# โค้ดสี ANSI สำหรับ Terminal
CYAN = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BOLD = "\033[1m"
RESET = "\033[0m"

banner = rf"""{CYAN}{BOLD}
  _    _      _ _         __          __        _     _ 
 | |  | |    | | |        \ \        / /       | |   | |
 | |__| | ___| | | ___     \ \  /\  / /__  _ __| | __| |
 |  __  |/ _ \ | |/ _ \     \ \/  \/ / _ \| '__| |/ _` |
 | |  | |  __/ | | (_) |     \  /\  / (_) | |  | | (_| |
 |_|  |_|\___|_|_|\___/       \/  \/ \___/|_|  |_|\__,_|
{RESET}"""

box = f"""{YELLOW}
+------------------------------------------------------+
|  {GREEN}Status:{RESET} Online                                      {YELLOW}|
|  {GREEN}Message:{RESET} Welcome to the Python Terminal!            {YELLOW}|
+------------------------------------------------------+{RESET}
"""

print(banner)
print(box)
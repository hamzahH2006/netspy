import random

# List of available banners
banners = [
  "🔥 NetSpy - Ethical Hacking Toolkit 🔥",
    "💀 NetSpy - Network Scanner & Payload Generator 💀",
    "🕵️ NetSpy - Your Spy in the Network 🕵️",
    r"""
  _   _ _____ _____ ____  ______   __
 | \ | | ____|_   _/ ___||  _ \ \ / /
 |  \| |  _|   | | \___ \| |_) \ V /
 | |\  | |___  | |  ___) |  __/ | |
 |_| \_|_____| |_| |____/|_|    |_|
""",
    r"""
 _  _  ___  ___ __  ___ __ __
| \| || __||_ _/ _|| o \\ V /
| \\ || _|  | |\_ \|  _/ \ /
|_|\_||___| |_||__/|_|   |_|
""",
    r"""
   _  __ ___ _____  ___  ___  _  __
  / |/ // _//_  _/,' _/ / o || |/,'
 / || // _/  / / _\ `. / _,' | ,'  
/_/|_//___/ /_/ /___,'/_/   /_/    
""",
    r"""
 _   _  ____  _____  ___   ___  _   _ 
( \ ( )(  __)(_   _)/  _) (   )( \_/ )
| \\| || |_    | |  \_"-. | O  |\   / 
( )\\ )(  _)   ( )   __) )( __/  ( )  
/_\ \_\/____\  /_\  /___/ /_\    |_|  
"""
]

def get_banner():
    return random.choice(banners)

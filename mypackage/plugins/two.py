
from . import three

def run(state):
    print("Two's run() function was executed")
    print(f"State's something: {state.something}")
    three.run(state)

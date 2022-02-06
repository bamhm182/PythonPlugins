
def run(state):
    print("One's run() function was executed")
    print(f"State's Something: {state.something}")
    state.something = 'taco'
    print("Changed something to taco")

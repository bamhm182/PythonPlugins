#!/usr/bin/env python3

from handler import Handler
from state import State


def main(parsed_args):
    state = State()
    handler = Handler(state)
    handler.missions.get_missions()


if __name__ == '__main__':
    parsed_args = {}
    main(parsed_args)

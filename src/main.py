from src.canvas import Canvas
from src.cli import parse_command, create_shape_from_command


def main():
    canvas = Canvas()
    print("CLI Vector Editor. Commands: add <point|segment|circle|square> <args>, list, delete <id>, quit")
    while True:
        try:
            line = input("> ")
        except EOFError:
            break
        cmd = parse_command(line)
        if cmd is None:
            continue
        if cmd["action"] == "quit":
            break
        if cmd["action"] == "invalid":
            print("Invalid command")
            continue
        if cmd["action"] == "add":
            shape = create_shape_from_command(cmd)
            if shape is None:
                print("Invalid add arguments")
                continue
            sid = canvas.add(shape)
            print(f"Added {shape} with id {sid}")
            continue
        if cmd["action"] == "delete":
            canvas.delete(cmd["id"])
            print(f"Deleted id {cmd['id']}")
            continue
        if cmd["action"] == "list":
            for sid, shape in canvas.list_shapes():
                print(f"  {sid}: {shape}")
            continue
    print("Bye.")


if __name__ == "__main__":
    main()

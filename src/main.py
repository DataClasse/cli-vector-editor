from src.canvas import Canvas
from src.cli import parse_command, create_shape_from_command
from src.storage import save_canvas, load_canvas
import json


def main():
    canvas = Canvas()
    print(
        "CLI Vector Editor. Команды:\n"
        "  add <point|segment|circle|square|oval|rectangle> <аргументы>\n"
        "  list — список фигур\n"
        "  delete <id> — удалить по id\n"
        "  save <файл> — сохранить в JSON\n"
        "  load <файл> — загрузить из JSON\n"
        "  quit / exit / q — выход"
    )
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
            print("Неверная команда")
            continue
        if cmd["action"] == "add":
            shape = create_shape_from_command(cmd)
            if shape is None:
                print("Неверные аргументы add")
                continue
            sid = canvas.add(shape)
            print(f"Добавлено: {shape}, id={sid}")
            continue
        if cmd["action"] == "delete":
            canvas.delete(cmd["id"])
            print(f"Удалено id={cmd['id']}")
            continue
        if cmd["action"] == "list":
            for sid, shape in canvas.list_shapes():
                print(f"  {sid}: {shape}")
            continue
        if cmd["action"] == "save":
            try:
                save_canvas(canvas, cmd["path"])
                print(f"Сохранено в {cmd['path']}")
            except OSError as e:
                print(f"Ошибка сохранения: {e}")
            continue
        if cmd["action"] == "load":
            try:
                canvas = load_canvas(cmd["path"])
                print(f"Загружено из {cmd['path']}")
            except FileNotFoundError:
                print(f"Файл не найден: {cmd['path']}")
            except (ValueError, json.JSONDecodeError) as e:
                print(f"Ошибка загрузки: {e}")
            continue
    print("До свидания.")


if __name__ == "__main__":
    main()

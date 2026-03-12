from src.canvas import Canvas
from src.cli import parse_command, create_shape_from_command
from src.storage import save_canvas, load_canvas
import json
import sys


def main():
    canvas = Canvas()
    print(
        "CLI Vector Editor\n"
        "Команды:\n"
        "  add <фигура> <аргументы>\n"
        "    point x y\n"
        "    segment x1 y1 x2 y2\n"
        "    circle x y r          (центр и радиус)\n"
        "    square x y side       (угол и сторона)\n"
        "    oval x y a b          (центр и две полуоси)\n"
        "    rectangle x y w h     (угол, ширина, высота)\n"
        "  list                    — список фигур\n"
        "  delete <id>             — удалить по id\n"
        "  save <файл>             — сохранить в JSON\n"
        "  load <файл>             — загрузить из JSON\n"
        "  quit / exit / q         — выход",
        flush=True,
    )
    while True:
        try:
            sys.stdout.write("> ")
            sys.stdout.flush()
            line = input()
        except EOFError:
            break
        cmd = parse_command(line)
        if cmd is None:
            continue
        if cmd["action"] == "quit":
            break
        if cmd["action"] == "invalid":
            if cmd.get("hint") == "add":
                print("Неверная команда. Чтобы добавить фигуру, введите: add <тип> <аргументы>, например: add circle 10 20 30")
            else:
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
            shapes = canvas.list_shapes()
            if not shapes:
                print("  Список пуст")
            else:
                for sid, shape in shapes:
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

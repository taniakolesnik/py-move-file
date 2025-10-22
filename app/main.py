import os


def move_file(command: str) -> None:
    command = command.split()
    if len(command) != 3:
        return
    mv, source, target = command
    if mv != "mv":
        return

    folder_path = os.path.dirname(target)
    if folder_path:
        os.makedirs(folder_path, exist_ok=True)
    with open(source, "r") as s, open(target, "w") as t:
        for line in s:
            t.write(line)

    if os.path.exists(source):
        os.remove(source)

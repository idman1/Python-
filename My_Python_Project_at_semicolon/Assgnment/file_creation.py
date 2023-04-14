import pathlib


def file_creation():
    path = pathlib.Path.cwd() / "file_name"
    path.mkdir(exist_ok=True)
    another_file = path / "new_file" / path / "idman.py"
    another_file.touch()

    file = another_file / path / "new_file"
    file.write_text("duuuu")


# for path in another_file:
#     if (path==2):
#         another_file.write_text("jhgdfgh")


file_creation()

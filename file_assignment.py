from pathlib import Path

new_folder = Path.home()
myme_folder = new_folder / "my_folder"
myme_folder.mkdir(exist_ok=True)

creating_file_inside_folder = new_folder / "file1.txt"
creating_file_inside_folder.touch()
creating_file_inside_folder = new_folder / "file2.txt"
creating_file_inside_folder.touch()
creating_file_inside_folder = new_folder / "image.png"
creating_file_inside_folder.touch()

sorces = new_folder / "file1.txt"
destination = new_folder / "file1" / "file2"
destination.replace(sorces)

# myme_folder / "file2.txt",
# myme_folder / "image.png"

# for folder in file_path:
#     new_folder.touch()

# files = Path('file1.txt', '')
# files.touch()
#
# create_file = folder / 'file1.txt'
#
# create_file.touch()

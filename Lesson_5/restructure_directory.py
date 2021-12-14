from pathlib import Path
import re


def restructure_directory(directory: str) -> None:
    path_start = './' + directory + '/'
    path = Path('./' + directory + '/')
    for child in path.iterdir():
        if not child.is_dir():
            old_file_name = child.stem
            old_file_extension = child.suffix

            old_path = old_file_name + old_file_extension
            full_path = re.sub('-', r"\\", old_path)
            new_file_name = re.search(r"\d+\.txt", full_path).group(0)
            path_to_new_file = re.search(r"\d{4}\\\d+\\", full_path).group(0)
            Path(path_start + path_to_new_file).mkdir(parents=True, exist_ok=True)
            Path(path_start + path_to_new_file + new_file_name).touch()

            info_file = child.read_text()
            Path(path_start + path_to_new_file + new_file_name).write_text(info_file)

            child.unlink()

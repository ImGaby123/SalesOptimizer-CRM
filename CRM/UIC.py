import os
import subprocess

def is_modified(source_path, target_path):
    """Checks if the source file is newer than the target file."""
    if not os.path.exists(target_path):
        return True  # Convert if the target file does not exist
    return os.path.getmtime(source_path) > os.path.getmtime(target_path)

def convert_ui_to_py(ui_folder, py_folder, converted_files, skipped_files):
    """ Converts only modified .ui files to .py files """
    for file in os.listdir(ui_folder):
        if file.endswith(".ui"):
            ui_path = os.path.join(ui_folder, file)
            py_file = f"ui_{os.path.splitext(file)[0]}.py"
            py_path = os.path.join(py_folder, py_file)

            if is_modified(ui_path, py_path):
                subprocess.run(["pyside6-uic", ui_path, "-o", py_path], check=True)
                fix_import_paths(py_path, "import icons_rc", "import views.py.icons_rc")
                converted_files.append(py_file)
            else:
                skipped_files.append(py_file)

def convert_qrc_to_py(qrc_folder, py_folder, converted_files, skipped_files):
    """ Converts only modified .qrc files to .py files """
    for file in os.listdir(qrc_folder):
        if file.endswith(".qrc"):
            qrc_path = os.path.join(qrc_folder, file)
            py_file = f"{os.path.splitext(file)[0]}_rc.py"
            py_path = os.path.join(py_folder, py_file)

            if is_modified(qrc_path, py_path):
                subprocess.run(["pyside6-rcc", qrc_path, "-o", py_path], check=True)
                converted_files.append(py_file)
            else:
                skipped_files.append(py_file)

def fix_import_paths(py_path, old, new):
    """ Replaces incorrect import paths in the generated .py file """
    with open(py_path, "r", encoding="utf-8") as file:
        content = file.read()

    content = content.replace(old, new)

    with open(py_path, "w", encoding="utf-8") as file:
        file.write(content)

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    ui_folder = os.path.join(base_dir, "Views", "ui")
    qrc_folder = os.path.join(base_dir, "Views", "qrc")
    py_folder = os.path.join(base_dir, "Views", "py")

    if not os.path.exists(py_folder):
        os.makedirs(py_folder)

    converted_files = []
    skipped_files = []
    convert_ui_to_py(ui_folder, py_folder, converted_files, skipped_files)
    convert_qrc_to_py(qrc_folder, py_folder, converted_files, skipped_files)

    print("Conversion completed!")

    print("\nSkipped:")
    if skipped_files:
        for file in skipped_files:
            print(f" - {file}")
    else:
        print(" None")

    print("\nConverted Files:")
    if converted_files:
        for file in converted_files:
            print(f" - {file}")
    else:
        print(" None")

if __name__ == "__main__":
    main()

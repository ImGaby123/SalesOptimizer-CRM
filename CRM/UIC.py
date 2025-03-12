import os
import subprocess

def convert_ui_to_py(ui_folder, py_folder):
    """ Converts all .ui files in ui_folder to .py files in py_folder """
    for file in os.listdir(ui_folder):
        if file.endswith(".ui"):
            ui_path = os.path.join(ui_folder, file)
            py_file = f"ui_{os.path.splitext(file)[0]}.py"
            py_path = os.path.join(py_folder, py_file)

            subprocess.run(["pyside6-uic", ui_path, "-o", py_path], check=True)
            print(f"Converted: {ui_path} -> {py_path}")

            # Fix incorrect import path
            fix_import_paths(py_path, "import icons_rc", "import views.py.icons_rc")

def convert_qrc_to_py(qrc_folder, py_folder):
    """ Converts all .qrc files in qrc_folder to .py files in py_folder """
    for file in os.listdir(qrc_folder):
        if file.endswith(".qrc"):
            qrc_path = os.path.join(qrc_folder, file)
            py_file = f"{os.path.splitext(file)[0]}_rc.py"  # Ensure correct filename format
            py_path = os.path.join(py_folder, py_file)

            subprocess.run(["pyside6-rcc", qrc_path, "-o", py_path], check=True)
            print(f"Converted: {qrc_path} -> {py_path}")

def fix_import_paths(py_path, old, new):
    """ Replaces incorrect import paths in the generated .py file """
    with open(py_path, "r", encoding="utf-8") as file:
        content = file.read()

    content = content.replace(old, new)  # Replace incorrect imports

    with open(py_path, "w", encoding="utf-8") as file:
        file.write(content)

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    ui_folder = os.path.join(base_dir, "Views", "ui")
    qrc_folder = os.path.join(base_dir, "Views", "qrc")
    py_folder = os.path.join(base_dir, "Views", "py")

    if not os.path.exists(py_folder):
        os.makedirs(py_folder)

    convert_ui_to_py(ui_folder, py_folder)
    convert_qrc_to_py(qrc_folder, py_folder)

    print("Conversion completed!")

if __name__ == "__main__":
    main()

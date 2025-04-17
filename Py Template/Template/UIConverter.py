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

def convert_qrc_to_py(qrc_folder, py_folder):
    """ Converts all .qrc files in qrc_folder to .py files in py_folder """
    for file in os.listdir(qrc_folder):
        if file.endswith(".qrc"):
            qrc_path = os.path.join(qrc_folder, file)
            py_file = f"qrc_{os.path.splitext(file)[0]}.py"
            py_path = os.path.join(py_folder, py_file)

            subprocess.run(["pyside6-rcc", qrc_path, "-o", py_path], check=True)
            print(f"Converted: {qrc_path} -> {py_path}")

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    ui_folder = os.path.join(base_dir, "views", "ui")
    qrc_folder = os.path.join(base_dir, "views", "qss")
    py_folder = os.path.join(base_dir, "views", "py")

    if not os.path.exists(py_folder):
        os.makedirs(py_folder)

    convert_ui_to_py(ui_folder, py_folder)
    convert_qrc_to_py(qrc_folder, py_folder)
    print("Conversion completed!")
    print("import views.py.icons_rc")

if __name__ == "__main__":
    main()

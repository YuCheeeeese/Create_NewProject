import os
import tkinter as tk
from tkinter import messagebox

#フォルダ構成テンプレート 

BASE_FILES = {"README.md", "requirements.txt", ".gitignore"}
SUBFOLDER = {
    "src",
    "tests",
    "docs",
    os.path.join("data", "input"),
    os.path.join("data", "output"),
}


def create_project():

    #プロジェクト名が入力されたか確認
    project_name = entry.get().strip()
    if not project_name:
        messagebox.showerror("Error", "Please enter a project name.")
        return
    
    #フォルダ・ファイルの作成
    try:

        #プロジェクトフォルダの作成
        os.makedirs(project_name, exist_ok=True)
        
        #ルート配下にベースファイルを作成
        for file in BASE_FILES:
            open(os.path.join(project_name, file), 'a').close()

        #サブフォルダの作成
        for folder in SUBFOLDER:
            os.makedirs(os.path.join(project_name, folder), exist_ok=True)
            messagebox.showinfo("Success", f"Project '{project_name}' created successfully.")
    
         # ベースファイル作成
        for file in BASE_FILES:
            path = os.path.join(project_name, file)
            with open(path, "w") as f:
                
                # README.mdの入力テンプレート
                if file == "README.md":
                    f.write(f"# {project_name}\n\nThis project was generated using a GUI-based Python tool.\n\n## Folder Structure\n\n```\n{project_name}/\n├── README.md\n├── requirements.txt\n├── .gitignore\n├── src/\n│   └── main.py\n├── test/\n│   └── test_main.py\n├── data/\n│   ├── input/\n│   └── output/\n├── docs/\n```\n")
                
                # .gitignoreの入力テンプレート
                elif file == ".gitignore":
                    f.write("__pycache__/\n*.pyc\n.env\n")
                
                # requirements.txtの入力テンプレート
                elif file == "requirements.txt":
                    f.write("# Add your project dependencies here\n")

        # src配下にmain.pyを作成



        



        
        # エラーが発生した場合はメッセージを表示
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred:\n{e}")

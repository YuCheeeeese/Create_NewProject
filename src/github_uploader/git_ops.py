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
    
         # ベースファイルにテンプレートを追加
        for file in BASE_FILES:
            path = os.path.join(project_name, file)
            with open(path, "w") as f:
                
                # README.mdの入力テンプレート
                if file == "README.md":
                    f.write(f"# {project_name}\n\nThis project was generated using a GUI-based Python tool.\n\n## Folder Structure\n\n```\n\n{project_name}/\n\n├── README.md\n\n├── requirements.txt\n\n├── .gitignore\n\n├── src/\n\n│   └── main.py\n\n├── test/\n\n│   └── test_main.py\n\n├── data/\n\n│   ├── input/\n\n│   └── output/\n\n├── docs/\n\n```\n\n")
                
                # .gitignoreの入力テンプレート
                elif file == ".gitignore":
                    f.write("__pycache__/\n\n*.pyc\n\n.env\n\n")
                
                # requirements.txtの入力テンプレート
                elif file == "requirements.txt":
                    f.write("# Add your project dependencies here\n\n")

        # サブフォルダ内にテンプレートファイルを追加
        # src配下にmain.pyを作成・テンプレートを追加
        with open(os.path.join(project_name, "src", "main.py"), "w") as f:
            f.write("def main():\n\n    print('Hello, World!')\n\n\n\nif __name__ == '__main__':\n\n    main()\n\n")
        
        # tests配下にtest_main.pyを作成・テンプレートを追加
        with open(os.path.join(project_name, "tests", "test_main.py"), "w") as f:
            f.write("import unittest\n\n\n\nfrom src.main import main\n\n\n\n\n\nclass TestMain(unittest.TestCase):\n\n\n\n    def test_main(self):\n\n\n\n        # Here you can add tests for the main function\n\n\n\n        self.assertIsNone(main())\n\n\n\n\n\nif __name__ == '__main__':\n\n\n\n    unittest.main()\n\n\n\n")
        
        # 成功メッセージの表示
        messagebox.showinfo("Success", f"Project '{project_name}' created successfully.")
        
        # エラーが発生した場合はメッセージを表示
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred:\n{e}")


# GUIのセットアップ
root = tk.Tk() 
root.title("GitHub Project Generator")

label = tk.Label(root, text="Enter Project Name:").pack(pady=5)
entry = tk.Entry(root, width=40)
entry.pack(pady=5)

create_button = tk.Button(root, text="Create Project", command=create_project).pack(pady=10)

root.mainloop()
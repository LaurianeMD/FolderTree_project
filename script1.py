import os
import subprocess

class ProjectManager:
    def __init__(self, root_dir):
        self.root_dir = root_dir

    def add_commit_push(self, filepath, commit_message):
        subprocess.run(["git", "add", filepath],cwd=self.root_dir)
        subprocess.run(["git", "commit", "-m", commit_message],cwd=self.root_dir)
        subprocess.run(["git", "push", "origin", "master"],cwd=self.root_dir)

def main():
    root_directory = os.getcwd()  # Chemin absolu vers votre dépôt Git

    manager = ProjectManager(root_directory)
    
    new_file_path = os.path.join(root_directory, "src/utils.py")
    commit_message = "Ajout du fichier utils.py"
    
    with open(new_file_path, "w") as new_file:
        # Écrivez le contenu du fichier si nécessaire
        new_file.write('')
        
    manager.add_commit_push(new_file_path, commit_message)
    print("Fichier ajouté, commité et poussé avec succès.")
import os
import subprocess

class ProjectManager:
    def __init__(self, root_dir):
        self.root_dir = root_dir

    def add_commit_push(self, commit_message, filepath = '.'):
        subprocess.run(["git", "add", filepath],cwd=self.root_dir)
        subprocess.run(["git", "commit", "-m", commit_message],cwd=self.root_dir)
        subprocess.run(["git", "push", "origin", "main"],cwd=self.root_dir)

def main():
    root_directory = os.getcwd()  # Chemin absolu vers votre dépôt Git

    manager = ProjectManager(root_directory)

    # os.makedirs(os.path.join(root_directory, "docs"))
    # os.makedirs(os.path.join(root_directory, "models"))
    # os.makedirs(os.path.join(root_directory, "reports"))

    
    #new_file_path = os.path.join(root_directory, "requirements.txt")
    commit_message = "Ajout du contenu de readme #5"
    
    #with open(new_file_path, "w") as new_file:
        # Écrivez le contenu du fichier si nécessaire
       # new_file.write('')
        
    manager.add_commit_push(commit_message)
    print("Fichier ajouté, commité et poussé avec succès.")

main()
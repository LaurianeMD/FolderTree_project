import os
import subprocess

class ProjectManager:
    def __init__(self, root_dir):
        self.root_dir = root_dir

    def add_commit_push(self, filepath, commit_message):
        subprocess.run(["git", "add", filepath])
        subprocess.run(["git", "commit", "-m", commit_message])
        subprocess.run(["git", "push", "origin", "master"])

def main():
    root_directory = r"C:\chemin\vers\le\depot"  # Chemin absolu vers votre dépôt Git

    manager = ProjectManager(root_directory)
    
    new_file_path = os.path.join(root_directory, "src", "utils.py")
    commit_message = "Ajout du fichier utils.py"
    
    with open(new_file_path, "w") as new_file:
        # Écrivez le contenu du fichier si nécessaire
        pass
        
    manager.add_commit_push(new_file_path, commit_message)
    print("Fichier ajouté, commité et poussé avec succès.")

if __name__ == "__main__":
    main()
import os
import subprocess

class ProjectManager:
    def __init__(self, root_dir):
        self.root_dir = root_dir

    def add_commit_push(self, filepath, commit_message):
        subprocess.run(["git", "add", filepath])
        subprocess.run(["git", "commit", "-m", commit_message])
        subprocess.run(["git", "push", "origin", "master"])

def main():
    root_directory = r"c:\Users\HP ProBook\OneDrive\Documents\AMaster Laury\Master DIT\Semestre1\Devops\Project_Arborescence"  # Chemin absolu vers votre dépôt Git

    manager = ProjectManager(root_directory)
    
    new_file_path = os.path.join(root_directory, "src", "utils.py")
    commit_message = "Ajout du fichier utils.py"
    
    with open(new_file_path, "w") as new_file:
        # Écrivez le contenu du fichier si nécessaire
        pass
        
    manager.add_commit_push(new_file_path, commit_message)
    print("Fichier ajouté, commité et poussé avec succès.")

if __name__ == "__main__":
    main()

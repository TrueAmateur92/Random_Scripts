from pathlib import Path

path = Path("C:/Users/ADEITE TURNER/Documents/data analyst bootcamp")  ## Path to the folder where my PDFs are located.
print(path.exists())

new_folder = path / "Delani's_PDFs"    ## New folder to house my PDFs.
new_folder.mkdir(exist_ok = True)  

for file in path.rglob('*.pdf'):       ## Searching for all PDFs in the folder and subfolders.
    new_file_path = new_folder / file.name
    file.rename(new_file_path)   ## Moving PDFs to the new folder.
import qrcode
from git import Repo

def generate_qr_code(data, filename):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)
    print("QR code generated and saved as", filename)

def push_to_github(repo_path, commit_message):
    repo = Repo.init(repo_path)
    repo.index.add(repo_path)
    repo.index.commit(commit_message)
    origin = repo.create_remote('origin', '<repository_url>')
    origin.push()
    print("Codebase pushed to GitHub successfully.")

# Generate QR code
data = "https://www.example.com"
filename = "qrcode.png"
generate_qr_code(data, filename)

# Push codebase to GitHub
repo_path = '/path/to/your/project/folder'
commit_message = "Initial commit"
push_to_github(repo_path, commit_message)

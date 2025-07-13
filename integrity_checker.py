import hashlib

def calculate_hash(file_stream):
    sha256 = hashlib.sha256()
    while True:
        chunk = file_stream.read(4096)
        if not chunk:
            break
        sha256.update(chunk)
    return sha256.hexdigest()
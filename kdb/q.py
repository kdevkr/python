import os

import pykx as kx
from dotenv import load_dotenv

load_dotenv()

Q_HOST = os.getenv("Q_HOST")
Q_PORT = os.getenv("Q_PORT")

print(f"Q_HOST: {Q_HOST}")
print(f"Q_PORT: {Q_PORT}")

if __name__ == "__main__":
    with kx.SyncQConnection(host=Q_HOST, port=int(Q_PORT), reconnection_attempts=3) as q:
        print(f"current_timestamp: {q('.z.p').np()}")

        expr = "Hallo, byte"
        q(f'-1"{expr}"')  # Print to Q server.
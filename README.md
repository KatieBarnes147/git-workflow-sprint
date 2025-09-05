# Week 2 — gRPC Workflow Sprint · `git-workflow-sprint`

Week 2 focuses on a **gRPC stack** (Go, Node.js, Python) and clean Git workflow habits (branches, merges, safe reverts).  
Because gRPC isn’t a browser UI, I include a small static “success” page for portfolio viewing.

---

## 🎯 Objectives
- Feature-branch → merge workflow (no force-pushes)
- Resolve merge conflicts safely
- Use **`git revert`** (preserve history)
- Run **Go/Node/Python** gRPC services via Compose

---

## 🔧 Tech Stack
- **gRPC** (Go, Node.js, Python)
- **Docker & Docker Compose**
- **PowerShell / Bash** for local ops
- **GitHub Actions** (Gitleaks secret scan)

---

## 🚀 How to Run

### Option A — All services with Docker Compose
```bash
# from repo root
docker compose up --build -d
docker compose ps   # shows ports
Expected ports:

Go → 50051

Node → 50052

Python → 50053

Stop:

bash
Copy code
docker compose down
Option B — Run one service (Node)
bash
Copy code
cd grpc_project/nodejs-server
npm install
# if server reads PORT, this keeps it standard:
# (PowerShell)  $env:PORT="50052"
# (bash)        PORT=50052
node server.js
🧪 Quick gRPC test with grpcurl (no client code needed)
List services (talk to Node on 50052):

bash
Copy code
docker run --rm fullstorydev/grpcurl -plaintext host.docker.internal:50052 list
Describe one:

bash
Copy code
docker run --rm fullstorydev/grpcurl -plaintext host.docker.internal:50052 describe <ServiceName>
Call a method (replace placeholders with your service/method & request):

bash
Copy code
docker run --rm -i fullstorydev/grpcurl -plaintext \
  -d '{"id":1}' host.docker.internal:50052 <ServiceName>/<MethodName>
Tip: Service & RPC names are in grpc_project/proto/*.proto.

🖼️ Screenshots
✅ Week 2 — Success (static page for portfolio)
<p align="center"> <img src="./docs/week2-success.png" alt="Week 2 running — static confirmation page" width="760"> </p> <!-- Optional second image if you add it later: ### 🧩 gRPC services (Compose) <p align="center"> <img src="./docs/week2-grpc.png" alt="docker compose ps showing go/node/python on 50051/50052/50053" width="820"> </p> -->
🔒 Security
Real secrets are not committed (env files ignored).

Example values live in .env.example.

CI runs Gitleaks on every push/PR (see badge above).

🗂️ Structure (high level)
bash
Copy code
.
├─ grpc_project/
│  ├─ go-server/        # Go gRPC
│  ├─ nodejs-server/    # Node gRPC
│  ├─ python-server/    # Python gRPC
│  └─ proto/            # .proto definitions
├─ docker-compose.yml   # exposes 50051/50052/50053 (gRPC)
├─ Dockerfile.golang
├─ Dockerfile.node
├─ Dockerfile.python
├─ .env.example
├─ README.md
└─ docs/
   └─ week2-success.png
✍️ Notes

Ports shown are local dev only (localhost), not internet-exposed.

For a web UI preview, use the static page above; the real services are gRPC.
Ports shown are local dev only (localhost), not internet-exposed.

For a web UI preview, use the static page above; the real services are gRPC.

✍️ Author

Katie Barnes
GitHub: @KatieBarnes147

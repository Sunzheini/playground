# First deploy locally with Docker Compose, then push to Docker Hub and pull on AWS EC2. This guide covers both local development and AWS deployment.

---

## Local Development (no AWS deploy)

```powershell
# First time or after code changes — builds image and runs locally:
cd "D:\BigBusiness\Telesky\Project\EmployeeFastApiPython"
docker compose up --build -d

# Subsequent starts (no code changes):
docker compose up -d

# Stop everything (keeps DB data):
docker compose down

# Full reset (wipes DB, re-seeds on next up):
docker compose down -v
```

> ⚠️ `docker compose up --build` only builds and runs the image **locally**.
> It does NOT push anything to Docker Hub. You must run `docker push` separately (see below).

---

## Deploy to AWS (full sequence, run every time you have changes)

### Step A — Local machine: build + push to Docker Hub

```powershell
cd "D:\BigBusiness\Telesky\Project\EmployeeFastApiPython"
docker compose up --build -d          # 1. build from local code + run locally
docker push sunzheini1407/employee-fastapi:latest  # 2. upload to Docker Hub
```

### Step B — EC2: pull new image + restart

```bash
cd ~/app
docker pull sunzheini1407/employee-fastapi:latest
docker compose up -d
```

---

## AWS EC2 Deployment (Full Guide)

### Instance Details
- **Instance ID**: i-05fe12888732737a3 (AI_Boss)
- **AMI**: Amazon Linux
- **Instance Type**: t2.medium
- **Key Pair**: KeyPair1.pem (saved on Desktop)
- **Elastic IP (permanent)**: 52.58.72.131
- **Public DNS**: ec2-52-58-72-131.eu-central-1.compute.amazonaws.com
- **Allocation ID**: eipalloc-0e5c35e464be5aac6
- **App URL**: http://52.58.72.131:8000 ✅ permanent, never changes

---

### Step 1 — Fix .pem Key Permissions (PowerShell, run once)

```powershell
icacls "C:\Users\User\Desktop\KeyPair1.pem" /inheritance:r /grant:r "User:R"
```

---

### Step 2 — SSH Into EC2 (PowerShell)

```powershell
ssh -i "C:\Users\User\Desktop\KeyPair1.pem" ec2-user@52.58.72.131
```

---

### Step 3 — Install Docker on EC2 (Amazon Linux) — run once (only in the beginning)

```bash
sudo yum update -y
sudo yum install -y docker
sudo systemctl start docker
sudo systemctl enable docker
sudo usermod -aG docker ec2-user
# Exit and re-login so group change takes effect
exit
```

---

### Step 4 — Install Docker Compose Plugin on EC2 — run once (only in the beginning)

```bash
sudo mkdir -p /usr/local/lib/docker/cli-plugins
sudo curl -SL https://github.com/docker/compose/releases/latest/download/docker-compose-linux-x86_64 -o /usr/local/lib/docker/cli-plugins/docker-compose
sudo chmod +x /usr/local/lib/docker/cli-plugins/docker-compose

# Verify
docker --version
docker compose version
```

---

### Step 5 — Transfer Files from Local to EC2 using PowerShell (only in the beginning)

Run these from your local machine (not EC2):

```powershell
# Create app folder on EC2
ssh -i "C:\Users\User\Desktop\KeyPair1.pem" ec2-user@52.58.72.131 "mkdir -p ~/app"

# Transfer docker-compose.yml
scp -i "C:\Users\User\Desktop\KeyPair1.pem" "D:\BigBusiness\Telesky\Project\EmployeeFastApiPython\docker-compose.yml" ec2-user@52.58.72.131:~/app/

# Transfer .env file (secrets)
scp -i "C:\Users\User\Desktop\KeyPair1.pem" "D:\BigBusiness\Telesky\Project\EmployeeFastApiPython\.env" ec2-user@52.58.72.131:~/app/

# Transfer database backup
scp -i "C:\Users\User\Desktop\KeyPair1.pem" "D:\BigBusiness\Telesky\Project\EmployeeFastApiPython\AI-database_test.backup" ec2-user@52.58.72.131:~/app/

# Transfer training_data folder
scp -i "C:\Users\User\Desktop\KeyPair1.pem" -r "D:\BigBusiness\Telesky\Project\EmployeeFastApiPython\training_data" ec2-user@52.58.72.131:~/app/
```

> ℹ️ On EC2 there is no `Dockerfile`, so the `build: .` line in `docker-compose.yml` is automatically ignored. EC2 always pulls the image from Docker Hub via the `image:` line.

---

### Step 6 — Run the App on EC2 (Run this after changes)

```bash
cd ~/app
docker pull sunzheini1407/employee-fastapi:latest
docker compose up -d

# Check containers are running
docker compose ps

# View logs
docker compose logs app
```

---

### Step 7 — AWS Security Group (run once in AWS Console)

In **EC2 → Security Groups → Edit Inbound Rules**, add:

| Type       | Port | Source    |
|------------|------|-----------|
| SSH        | 22   | My IP     |
| Custom TCP | 8000 | 0.0.0.0/0 |

---

### Useful EC2 Commands

```bash
# Stop containers (keeps DB data)
docker compose down

# Full reset (wipes DB)
docker compose down -v

# Restart after pushing a new image
docker pull sunzheini1407/employee-fastapi:latest
docker compose up -d

# View live logs
docker compose logs -f app
```

---

### .env Notes

The `.env` file must use:
- `DATABASE_URL=postgresql://postgres:postgres@db:5432/ai_database_test` (use `db` not `localhost`)
- `LIBREOFFICE_PATH=/usr/bin/soffice` (Linux path, not Windows)

---

## Troubleshooting

### `no space left on device` error during `docker pull` on EC2
**Cause**: The EC2 instance's disk is full — the new image (~900MB) has no room to extract.  
**Fix**: Free up space by pruning unused Docker data:

```bash
# 1. Check disk usage
df -h

# 2. Remove all stopped containers, unused images and dangling layers
docker system prune -af

# 3. Check disk again — should now have enough free space
df -h

# 4. Pull and restart as normal
docker pull sunzheini1407/employee-fastapi:latest
docker compose up -d
```

> ✅ `docker system prune -af` is safe — it will NOT touch running containers or the `pgdata` volume (your database is safe).  
> If disk is still full after pruning, the EBS volume may need to be expanded: AWS Console → EC2 → Volumes → select volume → Actions → Modify Volume.

---

### App stops being accessible after EC2 restart
**Cause**: The EC2 public IP changes every time the instance is stopped and restarted.  
**Fix**: Assign a permanent **Elastic IP** (already done for AI_Boss → `52.58.72.131`).  
**How to do it for a new instance**:
1. AWS Console → **EC2 → Elastic IPs** → **Allocate Elastic IP address** → **Allocate**
2. Select the new Elastic IP → **Actions → Associate Elastic IP address**
3. Select the instance → **Associate**

The Elastic IP will never change even after restarts.



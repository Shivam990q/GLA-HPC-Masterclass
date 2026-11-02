# 🛠️ MODULE 03: HANDS-ON STUDENT LAB ACTIVITIES & EXERCISES
## 8 Graded Practical Labs for Linux Basics, Shell Scripting & Secured Shell (SSH)

---

### 📋 Overview & Lab Delivery Guidelines
This lab manual is designed for classroom execution, self-paced student assignments, or live hackathon evaluations.
- **Target Audience**: Undergraduate/Graduate Computer Science, High Performance Computing, and Cloud Engineering students.
- **Estimated Completion Time**: 3.5 to 4.5 Hours (or divided into two 2-hour lab sessions).
- **Grading Methodology**: Each lab has a maximum score of **100 Points** (cumulative 800 Points total), with specific automated verification commands that students must run to prove completion.

---

# 🧪 LAB 1: Linux Filesystem Topology & Inode Archaeology
- **Estimated Time**: 25 Minutes
- **Maximum Points**: 100
- **Primary Focus**: Absolute vs. Relative Paths, FHS Navigation, Inodes, Hard Links vs. Soft Links.

### 🎯 Objective
Construct an isolated multi-tier directory structure, investigate virtual filesystems (`/proc`), and demonstrate the mathematical and physical difference between hard links and symbolic links at the inode level.

### 📝 Step-by-Step Tasks

#### Task 1.1: Directory Tree Construction
Navigate to your user home directory and create the following directory hierarchy with a single command:
```bash
~/hpc_lab/
├── datasets/
│   ├── raw/
│   └── processed/
├── binaries/
└── logs/
```
*Requirement*: Use `mkdir` with the `-p` (parents) flag.

#### Task 1.2: File Creation & Inode Examination
1. Inside `~/hpc_lab/datasets/raw/`, create a file named `sensor_data_oct2026.csv` with 5 lines of dummy sensor readings:
   ```bash
   cat << 'EOF' > ~/hpc_lab/datasets/raw/sensor_data_oct2026.csv
   timestamp,sensor_id,temperature_c,pressure_kpa
   2026-10-24T10:00:01Z,TH-01,24.5,101.3
   2026-10-24T10:00:02Z,TH-02,26.1,101.4
   2026-10-24T10:00:03Z,TH-01,24.8,101.2
   2026-10-24T10:00:04Z,TH-03,28.9,100.9
   EOF
   ```
2. Inspect the inode number and link count of `sensor_data_oct2026.csv` using `ls -li` and `stat`.

#### Task 1.3: Hard Link vs. Symbolic Link Laboratory
1. Create a **hard link** to `sensor_data_oct2026.csv` located at `~/hpc_lab/datasets/processed/data_hardlink.csv`.
2. Create a **symbolic (soft) link** to `sensor_data_oct2026.csv` located at `~/hpc_lab/datasets/processed/data_symlink.csv`.
3. Compare the inode numbers of the original file, the hard link, and the soft link using `ls -l -i ~/hpc_lab/datasets/processed/`.
4. Delete the original file `~/hpc_lab/datasets/raw/sensor_data_oct2026.csv`.
5. Attempt to read the content of `data_hardlink.csv` using `cat`.
6. Attempt to read the content of `data_symlink.csv` using `cat`. Note the difference in behavior and explain why in a short comment.

### ✅ Verification Drill
Run this verification command to validate Lab 1 completion:
```bash
echo "=== LAB 1 VERIFICATION ==="
ls -lid ~/hpc_lab/datasets/processed/*
cat ~/hpc_lab/datasets/processed/data_hardlink.csv | wc -l
```
*Expected Output*:
- Hardlink displays 5 lines despite original file deletion.
- Symlink shows a broken link error (`No such file or directory`).

---

# 🧪 LAB 2: File Permissions, Octal Math & Security Triage
- **Estimated Time**: 30 Minutes
- **Maximum Points**: 100
- **Primary Focus**: POSIX Permissions (rwx), Octal Bit Calculations, `umask`, `chmod`, `chown`, SUID/SGID/Sticky Bits.

### 🎯 Objective
Perform permission forensics on sensitive configuration files, calculate octal permission masks, implement directory collaboration using SGID, and secure temporary scratch directories using the Sticky Bit.

### 📝 Step-by-Step Tasks

#### Task 2.1: Octal Permission Calculation Matrix
Set up three test files in `~/hpc_lab/binaries/`:
- `worker_daemon.sh`
- `cluster_credentials.env`
- `public_benchmark.log`

Apply the exact required permissions using `chmod` in **octal format**:
1. `worker_daemon.sh`: Owner can Read, Write, Execute (7); Group can Read, Execute (5); Others have No Access (0). $\rightarrow$ **750**
2. `cluster_credentials.env`: Owner can Read, Write (6); Group can Read (4); Others have No Access (0). $\rightarrow$ **640**
3. `public_benchmark.log`: Owner can Read, Write (6); Group can Read (4); Others can Read (4). $\rightarrow$ **644**

#### Task 2.2: Umask Deep-Dive
1. Check your current shell `umask` by running `umask`.
2. Temporarily set your `umask` to `077`.
3. Create a test file `test_security.txt` and check its permissions using `ls -l test_security.txt`.
4. Explain why `umask 077` generates `-rw-------` (600) for files and `drwx------` (700) for directories.
5. Restore default umask: `umask 022`.

#### Task 2.3: Special Bits (SGID & Sticky Bit)
1. Create a collaboration directory: `~/hpc_lab/shared_scratch/`.
2. Set the **Sticky Bit** on this directory (`chmod +t` or `chmod 1777 ~/hpc_lab/shared_scratch/`).
3. Verify that the permission string displays `drwxrwxrwt`.
4. Explain in your lab notebook: What prevents User B from deleting User A's temporary file in a Sticky Bit directory?

### ✅ Verification Drill
```bash
echo "=== LAB 2 VERIFICATION ==="
stat -c "%a %A %n" ~/hpc_lab/binaries/*
stat -c "%a %A %n" ~/hpc_lab/shared_scratch/
```

---

# 🧪 LAB 3: Environment Configuration & Shell Startup Lifecycle
- **Estimated Time**: 25 Minutes
- **Maximum Points**: 100
- **Primary Focus**: Environment Variables, `$PATH` Traversal, `~/.bashrc`, Subshell vs. Sourcing.

### 🎯 Objective
Configure custom environment paths, automate persistent developer aliases, and demonstrate why child subshells cannot mutate parent environment variables unless sourced.

### 📝 Step-by-Step Tasks

#### Task 3.1: Binary Path Injection
1. Create an executable bash script in `~/hpc_lab/binaries/hpc-stat`:
   ```bash
   cat << 'EOF' > ~/hpc_lab/binaries/hpc-stat
   #!/usr/bin/env bash
   echo "[HPC-STAT] Active Node: $(hostname) | Uptime: $(uptime -p) | Core Count: $(nproc)"
   EOF
   chmod +x ~/hpc_lab/binaries/hpc-stat
   ```
2. Try executing `hpc-stat` directly from your terminal prompt without `./` or path prefix. Notice the `command not found` error.
3. Prepend `~/hpc_lab/binaries` to your `$PATH` variable for the current session:
   ```bash
   export PATH="$HOME/hpc_lab/binaries:$PATH"
   ```
4. Now execute `hpc-stat` from any working directory and observe the output.

#### Task 3.2: Persistence in `~/.bashrc`
1. Append the new `$PATH` export and a custom alias to your `~/.bashrc`:
   ```bash
   echo 'export PATH="$HOME/hpc_lab/binaries:$PATH"' >> ~/.bashrc
   echo "alias cdl='cd ~/hpc_lab && ls -la'" >> ~/.bashrc
   ```
2. Reload your environment without logging out using `source ~/.bashrc`.
3. Test your new alias `cdl`.

#### Task 3.3: Sourcing vs. Subshell Empirical Proof
1. Create `test_env.sh`:
   ```bash
   echo 'export LAB_SESSION_KEY="GLA_HPC_2026"' > test_env.sh
   ```
2. Run it via subshell: `bash test_env.sh`. Check `echo $LAB_SESSION_KEY` (Expected: Empty).
3. Run it via sourcing: `source test_env.sh`. Check `echo $LAB_SESSION_KEY` (Expected: `GLA_HPC_2026`).

---

# 🧪 LAB 4: I/O Redirection, Pipelines & File Descriptor Plumbing
- **Estimated Time**: 30 Minutes
- **Maximum Points**: 100
- **Primary Focus**: Standard Streams (`0`, `1`, `2`), Merging Streams (`2>&1`), `tee`, `/dev/null`.

### 🎯 Objective
Master POSIX stream routing by separating error streams from data streams, discarding noisy output, and multiplexing live stream logs to both console and file.

### 📝 Step-by-Step Tasks

#### Task 4.1: Stream Isolation & Error Segregation
1. Construct a command that searches `/etc/` for all files ending in `.conf`:
   ```bash
   find /etc/ -name "*.conf"
   ```
   Notice that unprivileged permission denied errors clutter the output.
2. Route standard output (`stdout`) to `~/hpc_lab/logs/found_confs.txt` and standard error (`stderr`) to `~/hpc_lab/logs/find_errors.log`:
   ```bash
   find /etc/ -name "*.conf" > ~/hpc_lab/logs/found_confs.txt 2> ~/hpc_lab/logs/find_errors.log
   ```
3. Inspect the line counts of both generated files:
   ```bash
   wc -l ~/hpc_lab/logs/found_confs.txt ~/hpc_lab/logs/find_errors.log
   ```

#### Task 4.2: Merging Streams and Blackhole Discard
1. Run a command that redirects standard error into standard output, and sends the unified stream into a single log file:
   ```bash
   ls -la /root /home 2>&1 > ~/hpc_lab/logs/combined_listing.log
   ```
2. Fix the common student mistake above! (Note: In the above command, `2>&1` happened before `> file`, so stderr went to the original stdout!). Correct it to:
   ```bash
   ls -la /root /home > ~/hpc_lab/logs/combined_listing.log 2>&1
   ```
3. Discard errors completely into the bit-bucket:
   ```bash
   grep -r "root" /etc/ 2> /dev/null | head -n 10
   ```

#### Task 4.3: Real-Time Stream Multiplexing with `tee`
Generate a sequence of 10 ping packets to `127.0.0.1`, displaying the output on the terminal while simultaneously saving it to `~/hpc_lab/logs/ping_telemetry.log` using `tee`:
```bash
ping -c 10 127.0.0.1 | tee ~/hpc_lab/logs/ping_telemetry.log
```

---

# 🧪 LAB 5: The Log Forensic Triad (`grep`, `sed`, `awk`)
- **Estimated Time**: 35 Minutes
- **Maximum Points**: 100
- **Primary Focus**: Regex Matching with `grep`, Stream Replacement with `sed`, Columnar Analysis & Metric Aggregation with `awk`.

### 🎯 Objective
Parse and forensic-audit a production server access log to detect security brute-force incidents and aggregate bandwidth metrics.

### 📝 Step-by-Step Tasks

#### Task 5.1: Sample Log Generation
Create `~/hpc_lab/logs/auth_traffic.log`:
```bash
cat << 'EOF' > ~/hpc_lab/logs/auth_traffic.log
2026-10-24 08:12:01 node-01 sshd[1042]: Failed password for invalid user admin from 192.168.1.105 port 44212 ssh2
2026-10-24 08:12:05 node-01 sshd[1045]: Accepted publickey for shivam from 192.168.1.50 port 52100 ssh2: ED25519
2026-10-24 08:12:12 node-01 sshd[1048]: Failed password for invalid user root from 192.168.1.105 port 44214 ssh2
2026-10-24 08:12:19 node-01 sshd[1051]: Failed password for invalid user oracle from 192.168.1.105 port 44218 ssh2
2026-10-24 08:13:02 node-01 sshd[1055]: Accepted publickey for researcher from 192.168.1.60 port 52110 ssh2: RSA
2026-10-24 08:14:22 node-01 sshd[1060]: Failed password for student from 10.0.0.15 port 39812 ssh2
2026-10-24 08:14:28 node-01 sshd[1062]: Failed password for student from 10.0.0.15 port 39814 ssh2
2026-10-24 08:15:00 node-01 sshd[1070]: Failed password for invalid user admin from 192.168.1.105 port 44222 ssh2
EOF
```

#### Task 5.2: `grep` Extraction
Extract all lines reporting "Failed password" and display the output with line numbers:
```bash
grep -n "Failed password" ~/hpc_lab/logs/auth_traffic.log
```

#### Task 5.3: `sed` Masking & Transformation
Sanitize internal IP addresses starting with `192.168.1.` to `[INTERNAL-SUBNET]` and output to terminal:
```bash
sed -E 's/192\.168\.1\.[0-9]{1,3}/[INTERNAL-SUBNET]/g' ~/hpc_lab/logs/auth_traffic.log
```

#### Task 5.4: `awk` Forensic Analysis & Attacker IP Counter
Use `awk` to extract the attacker IP address from all failed password attempts, count occurrences, and print the top offending IP addresses:
```bash
awk '/Failed password/ {
    for (i = 1; i <= NF; i++) {
        if ($i == "from") {
            ip = $(i+1)
            count[ip]++
        }
    }
}
END {
    print "=== OFFENDING IP REPORT ==="
    printf "%-18s %-10s\n", "IP Address", "Attempts"
    print "----------------------------"
    for (addr in count) {
        printf "%-18s %-10d\n", addr, count[addr]
    }
}' ~/hpc_lab/logs/auth_traffic.log
```

---

# 🧪 LAB 6: Production-Hardened Shell Scripting
- **Estimated Time**: 40 Minutes
- **Maximum Points**: 100
- **Primary Focus**: Bash Shebang, Strict Error Trapping (`set -euo pipefail`), CLI Flag Parsing (`getopts`), Exit Codes.

### 🎯 Objective
Write an automated directory backup script that validates user inputs, creates compressed tarballs with timestamp prefixes, computes SHA-256 integrity hashes, and handles abnormal interruptions gracefully via `trap`.

### 📝 Step-by-Step Tasks

#### Task 6.1: Script Blueprint & Logic
Create the file `~/hpc_lab/binaries/cluster_backup.sh` with the following production specifications:
1. Must begin with `#!/usr/bin/env bash`.
2. Must enforce strict safety flags: `set -euo pipefail`.
3. Must use a `trap` to clean up temporary scratch files if the user hits `Ctrl+C` (`SIGINT`) or if an error occurs (`ERR`).
4. Must parse two options using `getopts`:
   - `-s <source_dir>`: Directory to back up.
   - `-d <dest_dir>`: Directory where backup `.tar.gz` will be placed.
5. Must verify that `<source_dir>` actually exists. If not, print an error to `stderr` and exit with code `2`.
6. Must create the backup archive named `backup_<dirname>_<YYYYMMDD_HHMMSS>.tar.gz`.
7. Must compute and save the SHA256 checksum alongside the archive: `backup_<name>.tar.gz.sha256`.

#### Task 6.2: Complete Script Implementation
```bash
cat << 'EOF' > ~/hpc_lab/binaries/cluster_backup.sh
#!/usr/bin/env bash
# ==============================================================================
# Script: cluster_backup.sh
# Purpose: Production-hardened directory backup with SHA-256 checksum & trap
# ==============================================================================

set -euo pipefail

TEMP_WORK_DIR=""

cleanup() {
    local exit_code=$?
    if [[ -n "${TEMP_WORK_DIR}" && -d "${TEMP_WORK_DIR}" ]]; then
        echo "[CLEANUP] Removing ephemeral staging directory: ${TEMP_WORK_DIR}"
        rm -rf "${TEMP_WORK_DIR}"
    fi
    if [[ ${exit_code} -ne 0 ]]; then
        echo "[ERROR] Backup failed with exit code: ${exit_code}" >&2
    fi
}
trap cleanup EXIT INT TERM

SOURCE_DIR=""
DEST_DIR=""

usage() {
    echo "Usage: $0 -s <source_directory> -d <destination_directory>" >&2
    exit 1
}

while getopts ":s:d:h" opt; do
    case "${opt}" in
        s) SOURCE_DIR="${OPTARG}" ;;
        d) DEST_DIR="${OPTARG}" ;;
        h) usage ;;
        \?) echo "[ERROR] Invalid option: -${OPTARG}" >&2; usage ;;
        :)  echo "[ERROR] Option -${OPTARG} requires an argument." >&2; usage ;;
    esac
done

if [[ -z "${SOURCE_DIR}" || -z "${DEST_DIR}" ]]; then
    echo "[ERROR] Both -s and -d flags are mandatory." >&2
    usage
fi

if [[ ! -d "${SOURCE_DIR}" ]]; then
    echo "[ERROR] Source directory does not exist: ${SOURCE_DIR}" >&2
    exit 2
fi

mkdir -p "${DEST_DIR}"
TEMP_WORK_DIR=$(mktemp -d /tmp/backup_stage_XXXXXX)
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")
BASE_NAME=$(basename "${SOURCE_DIR}")
ARCHIVE_NAME="backup_${BASE_NAME}_${TIMESTAMP}.tar.gz"
TARGET_ARCHIVE="${DEST_DIR}/${ARCHIVE_NAME}"

echo "[INFO] Commencing backup of: ${SOURCE_DIR}"
tar -czf "${TARGET_ARCHIVE}" -C "$(dirname "${SOURCE_DIR}")" "${BASE_NAME}"

echo "[INFO] Computing SHA-256 integrity hash..."
sha256sum "${TARGET_ARCHIVE}" > "${TARGET_ARCHIVE}.sha256"

echo "[SUCCESS] Backup complete: ${TARGET_ARCHIVE}"
echo "[CHECKSUM] Generated: ${TARGET_ARCHIVE}.sha256"
exit 0
EOF
chmod +x ~/hpc_lab/binaries/cluster_backup.sh
```

#### Task 6.3: Execution & Verification
1. Run backup of `~/hpc_lab/datasets/` to `~/hpc_lab/backups/`:
   ```bash
   ~/hpc_lab/binaries/cluster_backup.sh -s ~/hpc_lab/datasets -d ~/hpc_lab/backups
   ```
2. Verify integrity using `sha256sum -c`:
   ```bash
   cd ~/hpc_lab/backups && sha256sum -c *.sha256
   ```

---

# 🧪 LAB 7: Cryptographic SSH Key Management & Host Aliasing
- **Estimated Time**: 30 Minutes
- **Maximum Points**: 100
- **Primary Focus**: Ed25519 Key Generation, Passphrase Protection, `ssh-agent`, File Permissions (700/600), `~/.ssh/config`.

### 🎯 Objective
Generate state-of-the-art Ed25519 elliptic-curve keypairs, configure `ssh-agent` for single sign-on memory caching, secure permission boundaries, and build a declarative SSH client configuration file with host aliases.

### 📝 Step-by-Step Tasks

#### Task 7.1: Ed25519 Key Generation
1. Check if `~/.ssh/` exists; if not, create it and enforce strict permissions:
   ```bash
   mkdir -p ~/.ssh && chmod 700 ~/.ssh
   ```
2. Generate an Ed25519 keypair with an institutional comment:
   ```bash
   ssh-keygen -t ed25519 -C "student_gla_hpc_2026" -f ~/.ssh/id_ed25519_hpc
   ```
3. Set the private key permissions to `600` and public key to `644`:
   ```bash
   chmod 600 ~/.ssh/id_ed25519_hpc
   chmod 644 ~/.ssh/id_ed25519_hpc.pub
   ```

#### Task 7.2: In-Memory Key Caching via `ssh-agent`
1. Initialize the ssh-agent in the current shell:
   ```bash
   eval "$(ssh-agent -s)"
   ```
2. Add your newly created private key:
   ```bash
   ssh-add ~/.ssh/id_ed25519_hpc
   ```
3. Verify loaded keys:
   ```bash
   ssh-add -l
   ```

#### Task 7.3: Declarative Host Configuration (`~/.ssh/config`)
Create `~/.ssh/config` (or append to it) with strict permissions (`600`):
```bash
cat << 'EOF' >> ~/.ssh/config
# Global SSH Default Settings
Host *
    ServerAliveInterval 60
    ServerAliveCountMax 3
    AddKeysToAgent yes
    IdentitiesOnly yes

# HPC Master Cluster Gateway
Host hpc-gateway
    HostName 127.0.0.1
    Port 22
    User student
    IdentityFile ~/.ssh/id_ed25519_hpc

# HPC Compute Node 01
Host node01
    HostName 192.168.10.11
    User clusteruser
    IdentityFile ~/.ssh/id_ed25519_hpc
EOF
chmod 600 ~/.ssh/config
```

---

# 🧪 LAB 8: SSH Port Forwarding & Cluster Gateway Bastion
- **Estimated Time**: 35 Minutes
- **Maximum Points**: 100
- **Primary Focus**: Local Port Forwarding (`-L`), Remote Port Forwarding (`-R`), ProxyJump (`-J`), Tunnel Testing.

### 🎯 Objective
Bypass network firewalls and securely access remote internal services (such as a remote Jupyter Notebook or cluster dashboard running on `127.0.0.1:8888`) over encrypted SSH tunnels.

### 📝 Step-by-Step Tasks

#### Task 8.1: Mock Remote Service Simulation
In terminal tab 1, start a local Python HTTP server on port `8080` to simulate a remote private dashboard:
```bash
python3 -m http.server 8080 --bind 127.0.0.1
```

#### Task 8.2: Local Port Forwarding (`-L`)
In terminal tab 2, establish a secure local port forwarding tunnel that maps your local machine's port `9999` to the remote service on `127.0.0.1:8080`:
```bash
ssh -N -L 9999:127.0.0.1:8080 localhost
```
*Flags Breakdown*:
- `-N`: Do not execute remote shell commands (tunnel only).
- `-L 9999:127.0.0.1:8080`: Forward local port `9999` to remote host `127.0.0.1` port `8080`.

#### Task 8.3: Tunnel Verification Drill
In terminal tab 3, test the tunnel using `curl`:
```bash
curl -I http://127.0.0.1:9999
```
*Expected Output*: `HTTP/1.0 200 OK` or directory listing returned from the python server.

#### Task 8.4: Bastion Jump Host Configuration
Add a multi-hop ProxyJump configuration to your `~/.ssh/config`:
```bash
cat << 'EOF' >> ~/.ssh/config

# Internal Storage Node reachable ONLY through Gateway Bastion
Host internal-storage
    HostName 10.10.20.55
    User datamanager
    ProxyJump hpc-gateway
    IdentityFile ~/.ssh/id_ed25519_hpc
EOF
```
*Explanation*: `ProxyJump` establishes an end-to-end encrypted SSH channel through the intermediate gateway without decrypting payloads on the bastion.

---

### 📊 Lab Grading & Evaluation Checkpoint Matrix

| Lab # | Lab Focus Area | Verification Criteria | Points |
| :---: | :--- | :--- | :---: |
| **Lab 1** | Filesystem Topology & Inodes | Hardlink intact after original deleted; symlink broken | 100 |
| **Lab 2** | Permissions & Octal Math | Exact `750`, `640`, `644`, and `1777` permissions verified | 100 |
| **Lab 3** | Environment & `$PATH` | `hpc-stat` executable from any directory without `./` | 100 |
| **Lab 4** | Stream Redirection & `tee` | Standard error cleanly segregated from stdout to logs | 100 |
| **Lab 5** | Log Forensics (`grep`/`sed`/`awk`) | Offending IP address frequency table rendered | 100 |
| **Lab 6** | Hardened Backup Script | Script runs with `set -euo pipefail`, trap works, hash verified | 100 |
| **Lab 7** | SSH Keys & Config | Ed25519 keys generated, permissions `600`/`700`, host alias | 100 |
| **Lab 8** | SSH Port Forwarding | Local port `9999` forwards traffic to test server | 100 |
| **Total** | **Comprehensive Evaluation** | **Cumulative Student Lab Mastery Score** | **800 / 800** |

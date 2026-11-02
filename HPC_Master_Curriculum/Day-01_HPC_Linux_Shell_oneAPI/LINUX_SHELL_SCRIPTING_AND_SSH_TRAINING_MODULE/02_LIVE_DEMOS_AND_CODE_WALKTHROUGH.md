# 🖥️ LIVE DEMOS & CODE WALKTHROUGH FOR TRAINERS
## Exact On-Screen Terminal Commands, Expected Outputs & Live Talking Points

**Author:** Shivam Gupta | **Target:** Live Classroom Projection / Virtual Terminal Screen  
**Duration:** 8 Modular Live Demonstrations (10 - 15 minutes each)  
**Environment:** Ubuntu 22.04 LTS / RHEL 9 / Debian Linux terminal  

---

## 📋 DEMO SEQUENCE OVERVIEW
1. [Demo 1: Virtual Filesystem (VFS) & Live Hardware Introspection](#demo-1-virtual-filesystem-vfs--live-hardware-introspection)
2. [Demo 2: Inodes, Nested Directory Trees & Permission Math](#demo-2-inodes-nested-directory-trees--permission-math)
3. [Demo 3: Environment Setup, Variable Scoping & $PATH Engineering](#demo-3-environment-setup-variable-scoping--path-engineering)
4. [Demo 4: Building an Automated Preflight Health Script](#demo-4-building-an-automated-preflight-health-script)
5. [Demo 5: Standard Streams (0, 1, 2), Pipelines & grep/sed/awk Filtering](#demo-5-standard-streams-0-1-2-pipelines--grepsedawk-filtering)
6. [Demo 6: Asymmetric Cryptography & Passwordless SSH Setup](#demo-6-asymmetric-cryptography--passwordless-ssh-setup)
7. [Demo 7: Professional SSH Client Configuration (~/.ssh/config)](#demo-7-professional-ssh-client-configuration-sshconfig)
8. [Demo 8: Remote Synchronization (rsync) & SSH Port Forwarding Tunneling](#demo-8-remote-synchronization-rsync--ssh-port-forwarding-tunneling)

---

## Demo 1: Virtual Filesystem (VFS) & Live Hardware Introspection

### 🎯 Objective
Show students that in Linux, hardware and system state are represented as readable files inside `/proc` and `/sys`.

### 💻 Commands to Type on Screen
```bash
# 1. Inspect operating system kernel identity
uname -srmo

# 2. Inspect CPU hardware specifications and vector flags
lscpu | grep -E "Model name|Socket|Thread|NUMA|Flags"

# 3. Prove that /proc/cpuinfo is a live kernel memory stream
head -n 25 /proc/cpuinfo

# 4. View RAM capacity and buffer allocation
free -h

# 5. Check mounted filesystems, disk space, and filesystem types
df -hT /
```

### 🖥️ Simulated Terminal Output
```
student@gla-node:~$ uname -srmo
Linux 5.15.0-101-generic x86_64 GNU/Linux

student@gla-node:~$ lscpu | grep -E "Model name|Socket|Thread|NUMA|Flags"
Model name:            Intel(R) Xeon(R) Platinum 8380 CPU @ 2.30GHz
Thread(s) per core:    2
Socket(s):             2
NUMA node(s):          2
Flags:                 fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts acpi mmx fxsr sse sse2 ss ht tm pbe syscall nx pdpe1gb rdtscp lm constant_tsc art arch_perfmon pebs bts rep_good nopl xtopology nonstop_tsc cpuid aperfmperf pni pclmulqdq dtes64 monitor ds_cpl vmx smx est tm2 ssse3 sdbg fma cx16 xtpr pdcm pcid dca sse4_1 sse4_2 x2apic movbe popcnt tsc_deadline_timer aes xsave avx f16c rdrand lahf_lm abm 3dnowprefetch cpuid_fault epb cat_l3 cdp_l3 invpcid_single intel_ppin ssbd mba ibrs ibpb stibp ibrs_enhanced fsgsbase tsc_adjust bmi1 avx2 smep bmi2 erms invpcid cqm rdt_a avx512f avx512dq rdseed adx smap avx512ifma clflushopt clwb intel_pt avx512cd sha_ni avx512bw avx512vl xsaveopt xsavec xgetbv1 xsaves cqm_llc cqm_occup_llc cqm_mbm_total cqm_mbm_local split_lock_detect wbnoinvd dtherm ida arat pln pts hwp hwp_act_window hwp_epp hwp_pkg_req vnmi avx512_vbmi umip pku ospke avx512_vbmi2 gfni vaes vpclmulqdq avx512_vnni avx512_bitalg tme avx512_vpopcntdq la57 rdpid fsrm md_clear pconfig flush_l1d arch_capabilities

student@gla-node:~$ free -h
               total        used        free      shared  buff/cache   available
Mem:           251Gi        18Gi       182Gi       1.2Gi        51Gi       231Gi
Swap:          8.0Gi          0B       8.0Gi

student@gla-node:~$ df -hT /
Filesystem     Type  Size  Used Avail Use% Mounted on
/dev/nvme0n1p2 ext4  1.8T  214G  1.5T  13% /
```

### 🎙️ Trainer Talking Points
- Point out `avx512f`, `avx512dq`, and `avx512vl` in the CPU flags: *"In Day 2 and Day 3, our C++/SYCL code will utilize these exact SIMD vector units to execute 16 floating-point calculations in a single CPU clock tick!"*
- Explain `buff/cache` in `free -h`: Linux does not leave RAM idle; it uses unallocated memory to cache frequently read disk blocks. When an application needs RAM, the kernel frees this cache instantly.

---

## Demo 2: Inodes, Nested Directory Trees & Permission Math

### 🎯 Objective
Show the creation of complex project directories, inspect underlying inode numbers, and demonstrate exact octal permission modification (`755`, `644`, `600`).

### 💻 Commands to Type on Screen
```bash
# 1. Create a production directory structure with a single command
mkdir -p ~/hpc_project/{data,src,bin,logs,config}

# 2. Verify the tree structure
ls -ld ~/hpc_project/*

# 3. Create a test script and a private key placeholder
cat << 'EOF' > ~/hpc_project/src/launcher.sh
#!/usr/bin/env bash
echo "[$(date '+%Y-%m-%d %H:%M:%S')] Launcher initialized on $(hostname)"
EOF

echo "SUPER_SECRET_TOKEN_DO_NOT_SHARE" > ~/hpc_project/config/api_token.key

# 4. Inspect current default permissions and Inode numbers
ls -li ~/hpc_project/src/launcher.sh ~/hpc_project/config/api_token.key

# 5. Apply correct permissions:
# - launcher.sh: Needs execute for owner & group (755)
# - api_token.key: Sensitive secret, ONLY owner can read/write (600)
chmod 755 ~/hpc_project/src/launcher.sh
chmod 600 ~/hpc_project/config/api_token.key

# 6. Verify modified permissions
ls -l ~/hpc_project/src/launcher.sh ~/hpc_project/config/api_token.key
```

### 🖥️ Simulated Terminal Output
```
student@gla-node:~$ mkdir -p ~/hpc_project/{data,src,bin,logs,config}

student@gla-node:~$ ls -ld ~/hpc_project/*
drwxr-xr-x 2 student student 4096 Nov  2 11:45 /home/student/hpc_project/bin
drwxr-xr-x 2 student student 4096 Nov  2 11:45 /home/student/hpc_project/config
drwxr-xr-x 2 student student 4096 Nov  2 11:45 /home/student/hpc_project/data
drwxr-xr-x 2 student student 4096 Nov  2 11:45 /home/student/hpc_project/logs
drwxr-xr-x 2 student student 4096 Nov  2 11:45 /home/student/hpc_project/src

student@gla-node:~$ chmod 755 ~/hpc_project/src/launcher.sh
student@gla-node:~$ chmod 600 ~/hpc_project/config/api_token.key

student@gla-node:~$ ls -l ~/hpc_project/src/launcher.sh ~/hpc_project/config/api_token.key
-rw------- 1 student student   32 Nov  2 11:46 /home/student/hpc_project/config/api_token.key
-rwxr-xr-x 1 student student   94 Nov  2 11:46 /home/student/hpc_project/src/launcher.sh
```

### 🎙️ Trainer Talking Points
- Explain brace expansion: `mkdir -p ~/hpc_project/{data,src,bin,logs,config}` saves typing 5 separate `mkdir` commands.
- Highlight the `-rw-------` on `api_token.key`: Notice the 6 dashes at the end! Group has `0` (`---`) and Others have `0` (`---`). Even other students on this shared server cannot read this file!

---

## Demo 3: Environment Setup, Variable Scoping & $PATH Engineering

### 🎯 Objective
Demystify environment variables, child subshell inheritance, and demonstrate how to install a custom script into `$PATH` so it can be called from anywhere.

### 💻 Commands to Type on Screen
```bash
# 1. Local variable vs. Exported variable demonstration
LOCAL_VAR="OnlyInCurrentShell"
export EXPORTED_VAR="InheritedByChildProcesses"

# 2. Spawn a child bash subshell and test visibility
bash -c 'echo "Inside Subshell -> LOCAL: [$LOCAL_VAR] | EXPORTED: [$EXPORTED_VAR]"'

# 3. Notice LOCAL_VAR is empty in the child!
echo "Back in Parent Shell -> LOCAL: [$LOCAL_VAR] | EXPORTED: [$EXPORTED_VAR]"

# 4. Move launcher.sh into ~/hpc_project/bin
mv ~/hpc_project/src/launcher.sh ~/hpc_project/bin/launcher

# 5. Try calling 'launcher' without a path
launcher
# (Returns: command not found)

# 6. Add ~/hpc_project/bin to PATH permanently in ~/.bashrc
echo 'export PATH="$HOME/hpc_project/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc

# 7. Verify launcher is now globally accessible!
which launcher
launcher
```

### 🖥️ Simulated Terminal Output
```
student@gla-node:~$ bash -c 'echo "Inside Subshell -> LOCAL: [$LOCAL_VAR] | EXPORTED: [$EXPORTED_VAR]"'
Inside Subshell -> LOCAL: [] | EXPORTED: [InheritedByChildProcesses]

student@gla-node:~$ launcher
Command 'launcher' not found, did you mean: ...

student@gla-node:~$ echo 'export PATH="$HOME/hpc_project/bin:$PATH"' >> ~/.bashrc
student@gla-node:~$ source ~/.bashrc

student@gla-node:~$ which launcher
/home/student/hpc_project/bin/launcher

student@gla-node:~$ launcher
[2026-11-02 11:48:22] Launcher initialized on gla-node
```

### 🎙️ Trainer Talking Points
- Emphasize the importance of `source ~/.bashrc`: *"When you edit `.bashrc`, the changes do not take effect in your open terminal until you re-source it into the active process memory!"*
- Show `which launcher`: It resolved instantly because Linux searched each folder in `$PATH` from left to right.

---

## Demo 4: Building an Automated Preflight Health Script

### 🎯 Objective
Live code a production-style shell script featuring defensive flags (`set -euo pipefail`), positional arguments, conditionals, and colorized terminal output.

### 💻 Code to Write Live: `preflight_check.sh`
```bash
cat << 'EOF' > ~/hpc_project/bin/preflight_check.sh
#!/usr/bin/env bash
# ==============================================================================
# Script: preflight_check.sh
# Purpose: Cluster node preflight hardware and storage validator
# ==============================================================================
set -euo pipefail

# ANSI Color Codes
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

# Default threshold values
MIN_RAM_GB="${1:-16}"
MIN_DISK_GB="${2:-50}"

echo -e "${CYAN}==========================================================${NC}"
echo -e "${CYAN}        GLA CLUSTER NODE PREFLIGHT VERIFICATION           ${NC}"
echo -e "${CYAN}==========================================================${NC}"
echo "Hostname   : $(hostname)"
echo "Kernel     : $(uname -r)"
echo "Timestamp  : $(date '+%Y-%m-%d %H:%M:%S')"
echo "----------------------------------------------------------"

# 1. RAM Verification
TOTAL_RAM_KB=$(grep MemTotal /proc/meminfo | awk '{print $2}')
TOTAL_RAM_GB=$(( TOTAL_RAM_KB / 1024 / 1024 ))

echo -n "Checking RAM capacity (Requirement: >= ${MIN_RAM_GB} GB)... "
if [[ ${TOTAL_RAM_GB} -ge ${MIN_RAM_GB} ]]; then
    echo -e "${GREEN}[PASS] Found ${TOTAL_RAM_GB} GB${NC}"
else
    echo -e "${RED}[FAIL] Only ${TOTAL_RAM_GB} GB available!${NC}"
    exit 1
fi

# 2. Disk Space Verification on /
AVAIL_DISK_GB=$(df -BG / | awk 'NR==2 {print $4}' | tr -d 'G')

echo -n "Checking Root Disk Space (Requirement: >= ${MIN_DISK_GB} GB)... "
if [[ ${AVAIL_DISK_GB} -ge ${MIN_DISK_GB} ]]; then
    echo -e "${GREEN}[PASS] ${AVAIL_DISK_GB} GB free${NC}"
else
    echo -e "${YELLOW}[WARN] Low disk headroom: ${AVAIL_DISK_GB} GB free${NC}"
fi

# 3. Check for oneAPI Compiler or GCC
echo -n "Checking Compiler Toolchain... "
if command -v icx >/dev/null 2>&1; then
    echo -e "${GREEN}[PASS] Intel oneAPI DPC++/C++ Compiler (icx) installed${NC}"
elif command -v gcc >/dev/null 2>&1; then
    echo -e "${YELLOW}[WARN] Intel icx not found; GNU GCC fallback detected${NC}"
else
    echo -e "${RED}[FAIL] No C/C++ compiler detected!${NC}"
    exit 2
fi

echo -e "${CYAN}==========================================================${NC}"
echo -e "${GREEN}>>> PREFLIGHT AUDIT COMPLETE: NODE READY FOR WORKLOAD <<<${NC}"
exit 0
EOF

chmod +x ~/hpc_project/bin/preflight_check.sh
~/hpc_project/bin/preflight_check.sh 32 100
```

### 🖥️ Simulated Terminal Output
```
student@gla-node:~$ ~/hpc_project/bin/preflight_check.sh 32 100
==========================================================
        GLA CLUSTER NODE PREFLIGHT VERIFICATION           
==========================================================
Hostname   : gla-node
Kernel     : 5.15.0-101-generic
Timestamp  : 2026-11-02 11:52:10
----------------------------------------------------------
Checking RAM capacity (Requirement: >= 32 GB)... [PASS] Found 251 GB
Checking Root Disk Space (Requirement: >= 100 GB)... [PASS] 1536 GB free
Checking Compiler Toolchain... [PASS] Intel oneAPI DPC++/C++ Compiler (icx) installed
==========================================================
>>> PREFLIGHT AUDIT COMPLETE: NODE READY FOR WORKLOAD <<<

student@gla-node:~$ echo "Exit Code: $?"
Exit Code: 0
```

### 🎙️ Trainer Talking Points
- Highlight `${1:-16}` parameter expansion: *"If the user passes argument 1, use it; otherwise, default to 16. This provides great UX without crashes."*
- Demonstrate `$?`: Show that the exit code is `0` when all checks pass. Ask students: *"What exit code will it return if RAM is insufficient?"* (Answer: `1`).

---

## Demo 5: Standard Streams (0, 1, 2), Pipelines & grep/sed/awk Filtering

### 🎯 Objective
Demonstrate stdout (1) vs. stderr (2) separation, and construct a real forensic pipeline that parses a sample web/auth log file to count IP occurrences.

### 💻 Commands to Type on Screen
```bash
# 1. Demonstration of stdout (FD 1) vs stderr (FD 2)
# Create a dummy command where stdout goes to one file and stderr goes to another
ls -l /etc/hosts /nonexistent_file > ~/hpc_project/logs/stdout.txt 2> ~/hpc_project/logs/stderr.txt

cat ~/hpc_project/logs/stdout.txt
cat ~/hpc_project/logs/stderr.txt

# 2. Create a simulated cluster authentication log
cat << 'EOF' > ~/hpc_project/logs/cluster_auth.log
Nov  2 08:12:01 hpc-node01 sshd[1234]: Failed password for invalid user admin from 192.168.1.105 port 44212 ssh2
Nov  2 08:12:05 hpc-node01 sshd[1236]: Failed password for student from 10.0.0.12 port 51230 ssh2
Nov  2 08:12:09 hpc-node01 sshd[1239]: Failed password for invalid user root from 192.168.1.105 port 44218 ssh2
Nov  2 08:12:15 hpc-node01 sshd[1245]: Accepted publickey for student from 10.0.0.12 port 51232 ssh2
Nov  2 08:12:22 hpc-node01 sshd[1250]: Failed password for invalid user oracle from 192.168.1.105 port 44224 ssh2
Nov  2 08:13:01 hpc-node01 sshd[1258]: Failed password for invalid user test from 172.16.5.99 port 38910 ssh2
EOF

# 3. Construct the Forensic Pipeline step-by-step:
# Step A: Filter only rows with "Failed password"
grep "Failed password" ~/hpc_project/logs/cluster_auth.log

# Step B: Extract IP addresses (Notice: IP is in column 11 or 13 depending on "invalid user")
grep "Failed password" ~/hpc_project/logs/cluster_auth.log | \
awk '{
    for (i=1; i<=NF; i++) {
        if ($i == "from") {
            print $(i+1)
        }
    }
}'

# Step C: Complete pipeline: Count attack attempts per IP and sort descending!
grep "Failed password" ~/hpc_project/logs/cluster_auth.log | \
awk '{for (i=1; i<=NF; i++) if ($i == "from") print $(i+1)}' | \
sort | uniq -c | sort -nr
```

### 🖥️ Simulated Terminal Output
```
student@gla-node:~$ cat ~/hpc_project/logs/stdout.txt
-rw-r--r-- 1 root root 221 Nov  2 09:00 /etc/hosts

student@gla-node:~$ cat ~/hpc_project/logs/stderr.txt
ls: cannot access '/nonexistent_file': No such file or directory

student@gla-node:~$ grep "Failed password" ~/hpc_project/logs/cluster_auth.log | \
> awk '{for (i=1; i<=NF; i++) if ($i == "from") print $(i+1)}' | \
> sort | uniq -c | sort -nr
      3 192.168.1.105
      1 172.16.5.99
      1 10.0.0.12
```

### 🎙️ Trainer Talking Points
- Explain `sort | uniq -c | sort -nr`: This is the classic Unix reporting idiom! `sort` brings duplicates together, `uniq -c` counts them, and `sort -nr` sorts by numeric count in descending order.
- In 1 line of shell code, we built a security incident report that identifies `192.168.1.105` as an automated brute-force scanner!

---

## Demo 6: Asymmetric Cryptography & Passwordless SSH Setup

### 🎯 Objective
Generate a modern Ed25519 elliptic-curve key pair, inspect public vs. private keys, and demonstrate passwordless authentication.

### 💻 Commands to Type on Screen
```bash
# 1. Clean existing test keys (if any) and create ~/.ssh with 700
mkdir -p ~/.ssh && chmod 700 ~/.ssh

# 2. Generate a 256-bit Ed25519 key pair with comment
ssh-keygen -t ed25519 -C "student@gla-cluster" -f ~/.ssh/id_ed25519 -N ""

# 3. Inspect generated keys and their strict permissions
ls -la ~/.ssh/id_ed25519*

# 4. View Public Key (safe to share)
cat ~/.ssh/id_ed25519.pub

# 5. Simulate deploying public key to localhost authorized_keys
cat ~/.ssh/id_ed25519.pub >> ~/.ssh/authorized_keys
chmod 600 ~/.ssh/authorized_keys

# 6. Test passwordless SSH to localhost
ssh -i ~/.ssh/id_ed25519 -o StrictHostKeyChecking=no localhost "echo '>>> SUCCESS: Connected via passwordless SSH! User: \$(whoami) at \$(hostname)'"
```

### 🖥️ Simulated Terminal Output
```
student@gla-node:~$ ssh-keygen -t ed25519 -C "student@gla-cluster" -f ~/.ssh/id_ed25519 -N ""
Generating public/private ed25519 key pair.
Your identification has been saved in /home/student/.ssh/id_ed25519
Your public key has been saved in /home/student/.ssh/id_ed25519.pub
The key fingerprint is:
SHA256:d8Q+4k9/2LmXkPq5RvTg7bN1x9aZ3sW8eF2c4uI1o6M student@gla-cluster
The key's randomart image is:
+--[ED25519 256]--+
|  .o+o=o.        |
|  .  + = .       |
|    . * + o      |
|     + B * .     |
|      = S = .    |
|     + o = + .   |
|    . o = + o    |
|       . o E .   |
|                 |
+----[SHA256]-----+

student@gla-node:~$ ls -la ~/.ssh/id_ed25519*
-rw------- 1 student student 419 Nov  2 11:58 /home/student/.ssh/id_ed25519
-rw-r--r-- 1 student student 102 Nov  2 11:58 /home/student/.ssh/id_ed25519.pub

student@gla-node:~$ ssh -i ~/.ssh/id_ed25519 -o StrictHostKeyChecking=no localhost "echo '>>> SUCCESS: Connected via passwordless SSH! User: \$(whoami) at \$(hostname)'"
>>> SUCCESS: Connected via passwordless SSH! User: student at gla-node
```

### 🎙️ Trainer Talking Points
- Highlight the size comparison: Notice that `id_ed25519` is only 419 bytes and the public key is only 102 bytes! An RSA-4096 key would be ~3.3 KB. Ed25519 is smaller, faster, and immune to timing side-channel attacks.
- Note `-N ""` sets an empty passphrase for automated cluster jobs (e.g. Slurm inter-node communication). In personal machines, always protect keys with a strong passphrase.

---

## Demo 7: Professional SSH Client Configuration (`~/.ssh/config`)

### 🎯 Objective
Show how to eliminate memorizing IP addresses, ports, and key paths by creating a clean `~/.ssh/config` file with host aliases.

### 💻 Commands to Type on Screen
```bash
# 1. Create ~/.ssh/config with 600 permissions
cat << 'EOF' > ~/.ssh/config
# Global Defaults
Host *
    ServerAliveInterval 30
    ServerAliveCountMax 3
    IdentitiesOnly yes

# Local Cluster Loopback Test Alias
Host local-node
    HostName 127.0.0.1
    User student
    IdentityFile ~/.ssh/id_ed25519
    Port 22

# Simulated Supercomputer Gateway
Host cluster-head
    HostName 10.0.0.1
    User hpcadmin
    IdentityFile ~/.ssh/id_ed25519
    Port 2222
EOF

chmod 600 ~/.ssh/config

# 2. Connect using the short alias 'local-node'
ssh local-node "uptime"
```

### 🖥️ Simulated Terminal Output
```
student@gla-node:~$ chmod 600 ~/.ssh/config

student@gla-node:~$ ssh local-node "uptime"
 12:02:14 up 14 days,  3:18,  2 users,  load average: 0.12, 0.08, 0.02
```

### 🎙️ Trainer Talking Points
- Show that typing `ssh local-node` automatically used `127.0.0.1`, user `student`, port `22`, and key `~/.ssh/id_ed25519`.
- Point out `ServerAliveInterval 30`: This sends a periodic encrypted keepalive packet to prevent university firewalls from terminating idle terminal sessions!

---

## Demo 8: Remote Synchronization (rsync) & SSH Port Forwarding Tunneling

### 🎯 Objective
Demonstrate delta-compression remote directory sync with `rsync`, and explain how SSH Local Port Forwarding (`-L`) tunnels browser traffic through firewalls.

### 💻 Commands to Type on Screen
```bash
# 1. Prepare sample dataset
mkdir -p ~/dataset_local
echo "Sample HPC input data batch 1" > ~/dataset_local/batch1.dat
echo "Sample HPC input data batch 2" > ~/dataset_local/batch2.dat

# 2. Synchronize dataset to remote directory using rsync over SSH
rsync -avzP -e ssh ~/dataset_local/ local-node:~/dataset_remote/

# 3. Simulate updating batch2.dat and re-running rsync
echo "Appended new sensor telemetry" >> ~/dataset_local/batch2.dat

# Notice rsync ONLY transfers the modified file!
rsync -avzP -e ssh ~/dataset_local/ local-node:~/dataset_remote/

# 4. Demonstrate Local Port Forwarding syntax (for Jupyter / Web interfaces)
echo "Command to access a remote Jupyter notebook running on cluster port 8888:"
echo "ssh -L 8888:localhost:8888 student@hpc-master"
```

### 🖥️ Simulated Terminal Output
```
student@gla-node:~$ rsync -avzP -e ssh ~/dataset_local/ local-node:~/dataset_remote/
sending incremental file list
created directory /home/student/dataset_remote
./
batch1.dat
             31 100%    0.00kB/s    0:00:00 (xfr#1, to-chk=1/3)
batch2.dat
             31 100%   30.27kB/s    0:00:00 (xfr#2, to-chk=0/3)

sent 215 bytes  received 68 bytes  566.00 bytes/sec
total size is 62  speedup is 0.22

student@gla-node:~$ echo "Appended new sensor telemetry" >> ~/dataset_local/batch2.dat

student@gla-node:~$ rsync -avzP -e ssh ~/dataset_local/ local-node:~/dataset_remote/
sending incremental file list
batch2.dat
             62 100%   60.55kB/s    0:00:00 (xfr#1, to-chk=0/3)

sent 156 bytes  received 35 bytes  382.00 bytes/sec
total size is 93  speedup is 0.49
```

### 🎙️ Trainer Talking Points
- Point out the second run output: `batch1.dat` was completely skipped because `rsync` checked its timestamp and size! Only the modified `batch2.dat` was sent. In a 500 GB dataset, this saves hours of bandwidth.
- Conclude with the `-L` syntax: Explain that when students launch Jupyter or TensorBoard on a remote compute node, `-L 8888:localhost:8888` bridges the remote port straight to `http://localhost:8888` on their laptop.

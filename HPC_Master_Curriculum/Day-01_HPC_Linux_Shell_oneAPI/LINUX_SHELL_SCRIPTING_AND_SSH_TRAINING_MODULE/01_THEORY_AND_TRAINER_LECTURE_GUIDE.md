# 📖 MASTER TRAINER LECTURE GUIDE: LINUX BASICS, SHELL SCRIPTING & SSH
## Comprehensive Conceptual Architecture, Theory & Pedagogical Delivery Blueprint

**Author:** Shivam Gupta | **Target:** University Masterclass / Enterprise HPC Track  
**Module Duration:** 3 Hours Lecture & Concept Deep-Dive + 3 Hours Lab  
**Prerequisites:** Basic understanding of computer operating systems and hardware components.  

---

## 📑 TABLE OF CONTENTS
1. [Module Overview & Trainer Delivery Blueprint](#1-module-overview--trainer-delivery-blueprint)
2. [Section 1: Linux Architecture & Filesystem Hierarchy Standard (FHS)](#2-section-1-linux-architecture--filesystem-hierarchy-standard-fhs)
3. [Section 2: Essential Command Ergonomics & Virtual Filesystem (VFS)](#3-section-2-essential-command-ergonomics--virtual-filesystem-vfs)
4. [Section 3: Linux Permissions, Ownership & Security Architecture](#4-section-3-linux-permissions-ownership--security-architecture)
5. [Section 4: Linux Environment Setup, Profiles & Shell Initialization](#5-section-4-linux-environment-setup-profiles--shell-initialization)
6. [Section 5: Shell Scripting Foundations & Execution Mechanics](#6-section-5-shell-scripting-foundations--execution-mechanics)
7. [Section 6: Shell Control Flow, Functions & Error Discipline](#7-section-6-shell-control-flow-functions--error-discipline)
8. [Section 7: Standard Streams, Redirection, Pipes & Text Processing Workhorses](#8-section-7-standard-streams-redirection-pipes--text-processing-workhorses)
9. [Section 8: Secured Shell (SSH) Architecture, Cryptography & Cluster Access](#9-section-8-secured-shell-ssh-architecture-cryptography--cluster-access)
10. [Section 9: Advanced SSH: Tunneling, Multiplexing & Daemon Hardening](#10-section-9-advanced-ssh-tunneling-multiplexing--daemon-hardening)
11. [Section 10: High-Frequency Student Traps & Trainer Answers](#11-section-10-high-frequency-student-traps--trainer-answers)

---

## 1. Module Overview & Trainer Delivery Blueprint

### 🎯 Core Pedagogical Philosophy
When training engineers on Linux and Shell, the most dangerous pedagogical failure is presenting Linux as a **"list of arbitrary commands to memorize"**.
Instead, instill the **Unix Philosophy and Systemic Mental Model**:
1. **"Everything is a file"**: Hardware devices, process tables, network sockets, and kernel memory are exposed through unified byte-stream interfaces.
2. **Small, sharp tools**: Each utility does one single job with forensic perfection (`grep` searches, `awk` formats, `sort` orders).
3. **Composable stream pipelines**: The standard output of one tool becomes the standard input of another via kernel ring buffers (pipes).
4. **Configuration in human-readable plain text**: Every system policy, user account, and daemon setting lives in readable, auditable text files under `/etc`.

---

## 2. Section 1: Linux Architecture & Filesystem Hierarchy Standard (FHS)

### 2.1 The 4-Layer Operating System Ring Architecture

```
+──────────────────────────────────────────────────────────────────────────+
|                        USER SPACE (Ring 3)                               |
|   Applications, Shell (bash, zsh), Compilers (gcc, icx), SSH Client      |
+──────────────────────────────────────────────────────────────────────────+
                                     │ Syscalls (read, write, fork, execve)
                                     ▼
+──────────────────────────────────────────────────────────────────────────+
|                        KERNEL SPACE (Ring 0)                             |
|  Process Scheduler (CFS), Virtual Filesystem (VFS), TCP/IP Stack, Device |
|  Drivers (NVMe, Ethernet, Intel GPU/Xeon KMD)                            |
+──────────────────────────────────────────────────────────────────────────+
                                     │ Memory-Mapped I/O, Interrupts (IRQs)
                                     ▼
+──────────────────────────────────────────────────────────────────────────+
|                        PHYSICAL HARDWARE                                 |
|  Intel Xeon CPU, DDR5 RAM, PCIe Bus, NVMe SSD, Network Interface Card    |
+──────────────────────────────────────────────────────────────────────────+
```

### 2.2 Filesystem Hierarchy Standard (FHS 3.0)
Unlike Windows which uses drive letters (`C:\`, `D:\`), Linux presents a **single unified hierarchical inverted tree** rooted at `/` (root directory). Even separate physical hard drives, network NFS shares, or memory-mapped filesystems are mounted as branches within this single tree.

```
/ (Root Directory)
├── bin -> usr/bin          # Essential user command binaries (ls, cp, bash)
├── sbin -> usr/sbin        # System administration binaries (fdisk, reboot, iptables)
├── boot/                   # Static bootloader files, GRUB config, Linux Kernel (vmlinuz), initramfs
├── dev/                    # Device nodes (devfs) - virtual access to disks (/dev/nvme0n1), terminals
├── etc/                    # Host-specific system configuration files (passwd, shadow, ssh/, fstab)
├── home/                   # User personal home directories (/home/student1, /home/shivam)
├── root/                   # Superuser (root) home directory (isolated outside /home)
├── lib -> usr/lib          # Essential shared system libraries (.so) and kernel modules
├── media/ & mnt/           # Mount points for removable media and manual filesystem mounts
├── opt/                    # Optional add-on software packages (e.g., /opt/intel/oneapi)
├── proc/                   # Virtual kernel process & system state filesystem (RAM only, 0 bytes on disk)
├── sys/                    # Virtual kernel device & driver subsystem filesystem (sysfs)
├── tmp/                    # Ephemeral temporary files (frequently cleared on reboot)
├── usr/                    # Secondary hierarchy: user utilities, headers, libraries (/usr/local)
└── var/                    # Variable data: log files (/var/log), spool queues, package caches
```

> [!IMPORTANT]
> **Trainer Whiteboard Point: The Magic of `/proc` and `/sys`**  
> Explain to students that `/proc/cpuinfo`, `/proc/meminfo`, and `/sys/class/net` do **not** take any space on the SSD. When a command like `cat /proc/cpuinfo` is executed, the Linux Virtual Filesystem driver intercepts the `read()` syscall and dynamically renders kernel memory tables into ASCII text strings on the fly!

---

## 3. Section 2: Essential Command Ergonomics & Virtual Filesystem (VFS)

### 3.1 Path Resolution: Absolute vs. Relative Paths
- **Absolute Path:** Starts with the root `/`. Unambiguous from any working directory (e.g., `/home/student/workspace/project/`).
- **Relative Path:** Starts relative to the Current Working Directory (`pwd`).
  - `.` refers to the current directory.
  - `..` refers to the parent directory.
  - `~` expands to the current user's home directory (`$HOME`).
  - `-` refers to the previous working directory (`cd -`).

### 3.2 Core Command Ergonomics Table

| Category | Command | Flags / Syntax | Deep System Explanation |
|:---|:---|:---|:---|
| **Navigation** | `pwd` | `-P` | Prints physical directory resolving any symbolic links. |
| | `cd` | `cd -` / `cd ~` | Changes process working directory via `chdir()` syscall. |
| **Directory Inspection** | `ls` | `ls -lahtr` | `-l` long format, `-a` hidden files, `-h` human sizes, `-t` sort by time, `-r` reverse. |
| **Directory Mutation** | `mkdir` | `mkdir -p a/b/c` | `-p` (parents) creates entire nested tree without throwing error if exists. |
| **File Creation** | `touch` | `touch file.txt` | Creates empty file or updates access & modification timestamps (`utime()`). |
| **File Mutation** | `cp` | `cp -av src/ dst/` | `-a` (archive: preserves permissions, symlinks, timestamps), `-v` verbose. |
| | `mv` | `mv old new` | If on same filesystem, it is an $O(1)$ atomic directory inode pointer update (`rename()`). |
| | `rm` | `rm -rf dir/` | `-r` recursive, `-f` force (suppresses non-existent prompts). Use with extreme caution. |
| **Content Viewing** | `cat` | `cat file` | Concatenates and dumps entire file stream to standard output. |
| | `less` | `less file` | Memory-efficient interactive pager (reads file chunk-by-chunk using terminal curses). |
| | `head` / `tail` | `head -n 20` / `tail -f` | `-n` line count; `tail -f` continuously follows appending writes in real-time. |
| **System Identity** | `uname` | `uname -a` | Prints Linux kernel release version, architecture (`x86_64`), and hostname. |
| | `lscpu` | `lscpu` | Interrogates CPU sockets, cores, threads, NUMA nodes, and vector flags (AVX-512, AMX). |
| | `free` | `free -h` | Reads `/proc/meminfo` displaying Total, Used, Free, Shared, Buffers/Cache, Available RAM. |
| | `df` | `df -hT` | Displays mounted filesystem disk usage, block capacities, and filesystem types (ext4, xfs). |

---

## 4. Section 3: Linux Permissions, Ownership & Security Architecture

### 4.1 Inode Permission Matrix Anatomy
In Linux, every file and directory has an **Inode** holding metadata:
- **File Type Indicator**: `-` (regular file), `d` (directory), `l` (symbolic link), `c` (character device), `b` (block device), `s` (socket), `p` (named pipe).
- **Three Triads of Permissions**: Owner (User `u`), Group (`g`), Others (`o`).

```
  -   r w x   r - x   r - -     1   shivam   engineers   4096   Nov 2 10:00   audit.sh
  ▲   ─────   ─────   ─────     ▲     ▲          ▲
  │     │       │       │       │     │          └── Owning Group
  │     │       │       │       │     └───────────── Owning User
  │     │       │       │       └────────────────── Hard link count
  │     │       │       └────────────────────────── Others permissions (Read only)
  │     │       └────────────────────────────────── Group permissions (Read + Execute)
  │     └────────────────────────────────────────── Owner permissions (Read + Write + Execute)
  └──────────────────────────────────────────────── File type (- = regular file)
```

### 4.2 The Octal Binary Representation (4-2-1 Rule)
Each permission corresponds to a bit position in a 3-bit binary register:

| Permission | Symbol | Binary Bit | Decimal Octal Value | Meaning on Regular Files | Meaning on Directories |
|:---:|:---:|:---:|:---:|:---|:---|
| **Read** | `r` | `100` | **4** | Can read file contents | Can list directory contents (`ls`) |
| **Write** | `w` | `010` | **2** | Can modify file contents | Can create, delete, rename files inside |
| **Execute** | `x` | `001` | **1** | Can run file as executable program | Can traverse/enter directory (`cd`) |
| **None** | `-` | `000` | **0** | No permissions | No access |

#### Essential Octal Permission Presets:
- `chmod 755 script.sh` $\rightarrow$ Owner: `rwx` (7), Group: `r-x` (5), Others: `r-x` (5) $\rightarrow$ Standard for scripts/binaries.
- `chmod 644 config.txt` $\rightarrow$ Owner: `rw-` (6), Group: `r--` (4), Others: `r--` (4) $\rightarrow$ Standard for configuration files.
- `chmod 600 id_ed25519` $\rightarrow$ Owner: `rw-` (6), Group: `---` (0), Others: `---` (0) $\rightarrow$ Mandatory for SSH private keys.
- `chmod 700 ~/.ssh` $\rightarrow$ Owner: `rwx` (7), Group: `---` (0), Others: `---` (0) $\rightarrow$ Mandatory for SSH directory.

### 4.3 Ownership Modification
- `chown student:developers script.sh` : Changes owner to `student` and group to `developers`.
- `chown -R student:student /opt/project` : Recursively modifies ownership across the entire directory tree.
- `umask` (User Mask): Default permission filter applied when new files are created. Default `022` results in files created with `666 - 022 = 644`, and directories created with `777 - 022 = 755`.

---

## 5. Section 4: Linux Environment Setup, Profiles & Shell Initialization

### 5.1 Environment Variables vs. Shell Local Variables
- **Shell Local Variable**: Exists only within the current running shell instance. Child processes spawned by the shell do **not** inherit it.
  ```bash
  CLUSTER_NAME="GLA-Alpha"      # Local variable
  ```
- **Environment Variable**: Marked with `export`. Placed in the process environment block and inherited by all child processes, scripts, and subprocesses.
  ```bash
  export CLUSTER_NAME="GLA-Alpha"  # Environment variable inherited by child processes
  ```

### 5.2 The `$PATH` Variable: How Linux Locates Executables
When a user types `python3` or `gcc`, the shell does **not** search the entire hard drive. It looks sequentially through colon-delimited directory paths stored in `$PATH`:
```bash
echo $PATH
# Output: /usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/opt/intel/oneapi/compiler/latest/bin
```
#### Modifying `$PATH` Correctly:
```bash
# Correct: Appends custom directory to existing PATH
export PATH="$PATH:/home/student/custom_bin"

# Correct: Prepends custom directory (highest priority)
export PATH="/home/student/custom_bin:$PATH"

# FATAL ERROR (Common student mistake): Overwrites existing PATH!
export PATH="/home/student/custom_bin"  # Breaks ls, cp, grep immediately!
```

### 5.3 Shell Startup & Profile Lifecycle
Different initialization files are parsed depending on how the shell is invoked:

```
                       ┌─────────────────────────┐
                       │   How was Shell Started? │
                       └────────────┬────────────┘
                                    │
               ┌────────────────────┴────────────────────┐
               ▼                                         ▼
   [ Login Shell ]                           [ Non-Interactive / Non-Login ]
   (SSH login, su - user,                    (Opening terminal in GUI,
    console login)                            running a script ./job.sh)
               │                                         │
               ├─────────────────────────┐               │
               ▼                         ▼               ▼
      /etc/profile                ~/.bashrc       Inherits exported env,
               │                         ▲        executes script non-interactively
               ▼                         │
     ~/.bash_profile                     │
      (or ~/.profile) ── sources ────────┘
```

- `/etc/profile` & `/etc/bash.bashrc`: System-wide settings for all users.
- `~/.bashrc`: User-specific configuration for interactive non-login shells (aliases, prompt colors `$PS1`, functions).
- `~/.bash_profile`: User-specific login environment initialization. Typically includes:
  ```bash
  if [ -f ~/.bashrc ]; then
      . ~/.bashrc
  fi
  ```

---

## 6. Section 5: Shell Scripting Foundations & Execution Mechanics

### 6.1 What is a Shell Script?
A shell script is an ASCII text file containing a sequence of commands executed sequentially by an interpreter.

### 6.2 The Shebang (`#!`) Line
The very first two bytes of an executable script must be the magic number `#!` (hex `0x23 0x21`). The Linux kernel loader (`execve()`) reads the path following the shebang to invoke the designated interpreter.

```bash
#!/usr/bin/env bash
```
> **Why `#!/usr/bin/env bash` is superior to `#!/bin/bash`:**  
> In modern heterogeneous Linux distributions, NixOS, or custom user environments, `bash` may reside in `/usr/bin/bash`, `/usr/local/bin/bash`, or under an environment manager. Using `env` queries the active `$PATH` and guarantees portability!

### 6.3 Subshell Execution vs. Current Shell Sourcing
- **Subshell Execution (`./script.sh` or `bash script.sh`)**:
  Spawns a child process. Any variables declared or modified inside the script disappear when the child process exits.
- **Sourcing (`source script.sh` or `. script.sh`)**:
  Executes the script instructions directly within the **current** shell process. Variables, exported functions, and aliases persist in the active session. This is why environment setup scripts (like Intel oneAPI's `setvars.sh` or Python virtual environment `activate`) MUST be invoked with `source`.

### 6.4 Positional Parameters & Special Reserved Variables

| Variable | Meaning | Example / Purpose |
|:---:|:---|:---|
| `$0` | Name of the executing script itself | Used in usage/help messages (`echo "Usage: $0 <args>"`) |
| `$1` .. `$9` | First through ninth command-line argument | `CLUSTER=$1` |
| `${10}` .. | Tenth and subsequent arguments (brackets mandatory!) | `${12}` |
| `$#` | Total count of command-line arguments passed | `if [[ $# -ne 2 ]]; then exit 1; fi` |
| `$@` | Array of all arguments as separate quoted strings | `for arg in "$@"; do ...` (Best practice) |
| `$*` | All arguments concatenated into a single string | `echo "Received: $*"` |
| `$?` | Exit status code of the immediately preceding command | `0` = Success; `1-255` = Failure |
| `$$` | Process ID (PID) of the currently running script | Used to create unique temporary files: `/tmp/out_$$` |
| `$!` | Process ID (PID) of the most recently spawned background job | Used in job monitoring |

### 6.5 Quoting Rules
- **Single Quotes `'...'`**: Literal string. Suppresses all expansions (`$VAR`, `$(cmd)`, `\n` are printed verbatim).
- **Double Quotes `"..."`**: Weak quoting. Allows parameter expansion (`$VAR`), command substitution (`$(cmd)`), and arithmetic expansion (`$((1+1))`), while preventing word splitting and glob expansion.
- **Command Substitution `$(...)`**: Executes the command inside a subshell and returns its standard output text. (Replaces legacy backticks `` `cmd` ``).

---

## 7. Section 6: Shell Control Flow, Functions & Error Discipline

### 7.1 Defensive Shell Scripting Header (The Industrial Standard)
Every production automation script should start with defensive flags:
```bash
#!/usr/bin/env bash
set -euo pipefail
IFS=$'\n\t'
```
- `set -e` (`errexit`): Immediately aborts the script if any command returns a non-zero exit code.
- `set -u` (`nounset`): Treats unset variables as an immediate error and aborts (prevents accidental disaster like `rm -rf "$UNSET_VAR/*"`).
- `set -o pipefail`: In a pipeline (`cmd1 | cmd2 | cmd3`), if `cmd1` fails, the pipeline exit code reflects that failure rather than masked by `cmd3`.
- `IFS=$'\n\t'`: Sets the Internal Field Separator to newline and tab only, preventing bugs with filenames containing spaces.

### 7.2 Modern Conditionals: `[[ ... ]]` vs. Legacy `[ ... ]`
Always teach students to use `[[ ... ]]` (Bash extended test) over legacy POSIX `[ ... ]`:
- `[[ ... ]]` does not undergo word splitting or pathname expansion on expressions.
- Supports regular expression pattern matching with `=~`.
- Supports direct boolean operators `&&` and `||` inside the brackets.

#### Essential Test Operators:
- `-f file`: True if file exists and is a regular file.
- `-d dir`: True if path exists and is a directory.
- `-s file`: True if file exists and has size greater than zero bytes.
- `-z str`: True if string length is zero (empty).
- `-n str`: True if string length is non-zero.
- `str1 == str2` / `str1 != str2`: String equality and inequality.
- `num1 -eq num2` / `-ne` / `-lt` / `-gt` / `-le` / `-ge`: Integer comparisons.

### 7.3 Conditional Syntax Blueprint
```bash
if [[ -f "/var/log/syslog" ]]; then
    echo "[INFO] System log found."
elif [[ -f "/var/log/messages" ]]; then
    echo "[INFO] Enterprise log found."
else
    echo "[WARN] No standard log found." >&2
    exit 1
fi
```

### 7.4 Loops in Shell Automation
#### For Loop (Array / Collection):
```bash
NODES=("node01" "node02" "node03" "node04")

for node in "${NODES[@]}"; do
    echo "Pinging cluster node: ${node}..."
    ping -c 1 -W 2 "${node}" >/dev/null 2>&1 && echo "  [OK] Online" || echo "  [FAIL] Unreachable"
done
```

#### While Loop (Reading Line-by-Line Safely):
```bash
while IFS= read -r line || [[ -n "${line}" ]]; do
    echo "Processing entry: ${line}"
done < "/etc/hosts"
```

### 7.5 Functions & Scoping
Functions in bash must declare private variables with `local` to prevent polluting the global shell scope:
```bash
compute_disk_headroom() {
    local target_mount="$1"
    local usage_pct
    usage_pct=$(df -h "${target_mount}" | awk 'NR==2 {print $5}' | tr -d '%')
    
    if [[ "${usage_pct}" -gt 85 ]]; then
        echo "[CRITICAL] Disk ${target_mount} usage at ${usage_pct}%!"
        return 1
    fi
    echo "[HEALTHY] Disk ${target_mount} usage at ${usage_pct}%."
    return 0
}
```

---

## 8. Section 7: Standard Streams, Redirection, Pipes & Text Processing Workhorses

### 8.1 The Standard POSIX Streams & File Descriptors (FD)

```
                       ┌─────────────────────────┐
    File Descriptor 0  │  STANDARD INPUT (stdin) │ ◄── Keyboard / Pipe / File (<)
                       └─────────────────────────┘
                                    │
                                    ▼
                         [ RUNNING LINUX PROCESS ]
                                    │
         ┌──────────────────────────┴──────────────────────────┐
         ▼                                                     ▼
┌──────────────────────────┐                         ┌──────────────────────────┐
│ STANDARD OUTPUT (stdout) │                         │ STANDARD ERROR (stderr)  │
│    File Descriptor 1     │                         │    File Descriptor 2     │
└──────────────────────────┘                         └──────────────────────────┘
         │                                                     │
         ▼                                                     ▼
Screen Display / Overwrite (>) / Append (>>)         Terminal Error Log (2>)
```

### 8.2 Redirection Syntax Mastery Table

| Syntax | Description | Example |
|:---|:---|:---|
| `cmd > file` | Redirects stdout, overwriting destination file | `lscpu > cpu_spec.txt` |
| `cmd >> file` | Redirects stdout, appending to destination file | `echo "New event" >> events.log` |
| `cmd 2> file` | Redirects stderr only | `gcc main.c 2> compile_errors.log` |
| `cmd > file 2>&1` | Merges stderr into stdout, writing both to file | `./audit.sh > full_run.log 2>&1` |
| `cmd &> file` | Modern bash shorthand for stdout + stderr merge | `./audit.sh &> full_run.log` |
| `cmd < file` | Feeds file content into stdin of command | `mail -s "Alert" admin < report.txt` |
| `cmd 2>/dev/null`| Discards error messages into the bit-bucket | `find / -name "test" 2>/dev/null` |
| `cat << 'EOF'` | Heredoc: feeds multi-line string block into stdin | `cat << 'EOF' > setup.sh` |

### 8.3 The Pipeline Operator (`|`)
The pipe creates an anonymous kernel FIFO buffer connecting File Descriptor 1 (stdout) of the upstream process directly to File Descriptor 0 (stdin) of the downstream process in parallel execution:
```bash
cat /var/log/auth.log | grep "Failed password" | awk '{print $11}' | sort | uniq -c | sort -nr
```

### 8.4 The Text Processing Triad: `grep`, `sed`, `awk`

```
  Input Stream ──► [ grep: Filter Rows ] ──► [ sed: Mutate Strings ] ──► [ awk: Compute & Report ]
```

#### 1. `grep` (Global Regular Expression Print)
Filters rows based on pattern matching:
- `grep "pattern" file`
- `-i`: Case-insensitive search.
- `-v`: Invert match (returns lines NOT matching pattern).
- `-r` / `-R`: Recursive directory search.
- `-E`: Extended regular expressions (enables `+`, `?`, `|`, `()`).
- `-c`: Count of matching lines.

#### 2. `sed` (Stream Editor)
Performs inline string transforms without opening a visual text editor:
- Substitute pattern: `sed 's/find/replace/g' file.txt`
- In-place modification: `sed -i 's/192.168.1.10/10.0.0.1/g' config.cfg`
- Delete lines matching pattern: `sed '/^#/d' config.cfg` (deletes all comment lines).

#### 3. `awk` (Aho, Weinberger, Kernighan - Column Processing Language)
Awk parses structured, delimited data into records and columns:
- `$0`: Entire input line.
- `$1, $2, ... $NF`: Column 1, Column 2, Last Column (`NF` = Number of Fields).
- `NR`: Current row/record number.
- `FS`: Field separator (default: whitespace).

```bash
# Print username (col 1) and shell (col 7) for system users from /etc/passwd:
awk -F: '$3 >= 1000 {print "User: " $1 " -> Shell: " $7}' /etc/passwd
```

---

## 9. Section 8: Secured Shell (SSH) Architecture, Cryptography & Cluster Access

### 9.1 Why SSH? (The Demise of Telnet and RSH)
Before SSH (created by Tatu Ylönen in 1995), remote administration relied on **Telnet** (Port 23) and **RSH/Rlogin** (Port 514). These legacy protocols transmitted usernames, passwords, and commands in **raw, unencrypted plaintext**. Any attacker running a packet sniffer (`tcpdump`, Wireshark) on the local switch could instantly intercept root credentials!

### 9.2 The Three Cryptographic Pillars of SSH (RFC 4251 - 4254)

```
+─────────────────────────────────────────────────────────────────────────+
|                           SSH ARCHITECTURE                              |
+─────────────────────────────────────────────────────────────────────────+
| 1. KEY EXCHANGE (Transport Layer)                                       |
|    Diffie-Hellman / ECDH (Curve25519)                                   |
|    Client and Server independently compute a shared ephemeral session   |
|    key without ever transmitting the key over the wire!                 |
+─────────────────────────────────────────────────────────────────────────+
| 2. SERVER AUTHENTICATION (Anti-Impersonation)                           |
|    Server presents its Host Key. Client checks ~/.ssh/known_hosts.      |
|    Protects against Man-in-the-Middle (MITM) spoofing.                  |
+─────────────────────────────────────────────────────────────────────────+
| 3. SYMMETRIC ENCRYPTION & INTEGRITY                                     |
|    Bulk traffic encrypted with AES-256-GCM or ChaCha20-Poly1305.        |
+─────────────────────────────────────────────────────────────────────────+
| 4. USER AUTHENTICATION (User Layer)                                     |
|    Asymmetric Public/Private Key Pair: ed25519 or RSA 4096-bit.        |
|    Client signs a challenge with Private Key; Server verifies signature |
|    against authorized public keys in ~/.ssh/authorized_keys.            |
+─────────────────────────────────────────────────────────────────────────+
```

### 9.3 Asymmetric Key Pair Generation & Deployment
```bash
# Generate modern, high-security Ed25519 key pair with comment:
ssh-keygen -t ed25519 -C "shivam@gla.ac.in" -f ~/.ssh/id_ed25519
```
This produces two files:
1. `~/.ssh/id_ed25519` (**Private Key**): Must be kept strictly secret. Never emailed, copied, or uploaded. Protected by passphrase.
2. `~/.ssh/id_ed25519.pub` (**Public Key**): Safe to share publicly. Placed on remote servers to grant access.

#### Key Deployment:
```bash
# Automated key copy to remote server:
ssh-copy-id -i ~/.ssh/id_ed25519.pub student@10.0.0.101

# Under the hood, ssh-copy-id performs:
# cat ~/.ssh/id_ed25519.pub | ssh student@10.0.0.101 'mkdir -p ~/.ssh && chmod 700 ~/.ssh && cat >> ~/.ssh/authorized_keys && chmod 600 ~/.ssh/authorized_keys'
```

### 9.4 The Non-Negotiable Permission Shield (Why SSH Rejects Connections)
OpenSSH enforces strict permission audits (`StrictModes yes` in `sshd_config`). If permissions on the client private key or server `.ssh` folder are too open, SSH **aborts with an error**:
- `Permissions 0777 for 'id_ed25519' are too open!`

```bash
# CLIENT-SIDE PERMISSIONS
chmod 700 ~/.ssh                 # drwx------ (Only owner can read/enter)
chmod 600 ~/.ssh/id_ed25519      # -rw------- (Only owner can read/write private key)
chmod 644 ~/.ssh/id_ed25519.pub  # -rw-r--r-- (Public key can be readable)
chmod 600 ~/.ssh/config          # -rw------- (SSH config file)

# SERVER-SIDE PERMISSIONS
chmod 700 ~/.ssh                 # drwx------ (Server .ssh directory)
chmod 600 ~/.ssh/authorized_keys # -rw------- (Only owner can read/write keys list)
chmod 755 /home/student          # (Must NOT be writable by group or others!)
```

### 9.5 SSH Client Configuration File (`~/.ssh/config`)
Instead of typing cumbersome commands like `ssh -i ~/.ssh/hpc_key -p 2222 student@172.16.20.50`, define aliases in `~/.ssh/config`:

```ssh-config
# Global Defaults
Host *
    ServerAliveInterval 60
    ServerAliveCountMax 3
    AddKeysToAgent yes
    IdentitiesOnly yes

# Cluster Master Node
Host hpc-master
    HostName 172.16.20.50
    User student
    Port 22
    IdentityFile ~/.ssh/id_ed25519
    ForwardAgent no

# Compute Node 1 (Accessed via Master as a Jump Host)
Host hpc-node01
    HostName 10.0.1.101
    User cluster
    ProxyJump hpc-master
    IdentityFile ~/.ssh/cluster_worker_key
```
Now, simply typing `ssh hpc-master` or `ssh hpc-node01` handles all ports, keys, and jump tunnels automatically!

---

## 10. Section 9: Advanced SSH: Tunneling, Multiplexing & Daemon Hardening

### 10.1 Port Forwarding & SSH Tunneling

```
  [ Local Machine ]                   [ SSH Jump Server ]                  [ Internal Network ]
  Port 8888 (Browser) ── Encrypted ──► Port 22 (SSH Daemon) ── Plaintext ─► Port 8888 (Jupyter Notebook)
```

#### 1. Local Port Forwarding (`-L`)
Forwards traffic from a local port on the client machine through the SSH tunnel to a remote destination:
```bash
# Access a remote Jupyter Notebook or oneAPI Web Portal running on cluster port 8888:
ssh -L 8888:localhost:8888 student@hpc-master
# Now open http://localhost:8888 on the local laptop browser!
```

#### 2. Remote / Reverse Port Forwarding (`-R`)
Forwards traffic from a port on the remote server back to the local client:
```bash
# Expose a local mock server running on port 3000 to remote server port 9000:
ssh -R 9000:localhost:3000 student@hpc-master
```

#### 3. Dynamic Port Forwarding (`-D` - SOCKS5 Proxy)
Turns the remote SSH connection into a local SOCKS5 proxy server. Any browser or app configured to use `localhost:1080` routes all its network traffic securely through the remote cluster:
```bash
ssh -D 1080 student@hpc-master
```

### 10.2 Secure Remote File Transfer: `scp` vs. `rsync`
- **`scp` (Secure Copy)**: Good for simple, one-off file transfers.
  ```bash
  scp -r ./data student@hpc-master:/home/student/workspace/
  ```
- **`rsync` over SSH (Industry Gold Standard)**:
  Uses the delta-transfer algorithm (only transfers changed bytes), supports compression, displays real-time progress, and allows resuming interrupted transfers:
  ```bash
  rsync -avzP -e ssh ./dataset/ student@hpc-master:/home/student/dataset/
  ```
  - `-a`: Archive mode (recurses directories and preserves symlinks, permissions, timestamps, owner, and group).
  - `-v`: Verbose.
  - `-z`: Compresses data stream during transmission.
  - `-P`: Combines `--progress` (real-time progress bar) and `--partial` (resumes interrupted transfers).

### 10.3 SSH Daemon (`/etc/ssh/sshd_config`) Security Hardening
In an enterprise or HPC server, harden the SSH daemon with these non-negotiable policies:
```sshd-config
# 1. Disable Root Login via Password
PermitRootLogin prohibit-password

# 2. Enforce Public Key Authentication only (Disable passwords)
PasswordAuthentication no
PubkeyAuthentication yes

# 3. Limit Maximum Authentication Tries before Dropping Connection
MaxAuthTries 3

# 4. Whitelist Specific Authorized Users
AllowUsers student clusteradmin

# 5. Disable Empty Passwords
PermitEmptyPasswords no

# 6. Disable Obsolete Protocol Versions
Protocol 2
```
After editing, always test syntax and reload:
```bash
sudo sshd -t && sudo systemctl reload sshd
```

---

## 11. Section 10: High-Frequency Student Traps & Trainer Answers

| # | Student Confusion / Bug | Underlying Mechanism | Trainer Whiteboard Answer |
|:---|:---|:---|:---|
| **1** | *"I wrote `export PATH=/my/bin` and now `ls`, `grep`, `cp` are all broken with 'command not found'!"* | Overwrote the entire `$PATH` array instead of appending/prepending. | Run `/bin/export PATH="/usr/bin:/bin:$PATH"`. Explain that `$PATH` is a list; never omit `$PATH` during assignment. |
| **2** | *"My script fails with `Permission denied` even though I am the owner."* | In Linux, creating a text file gives default `644` (rw-r--r--). Files lack the execute bit by default for security. | Run `chmod +x script.sh` (or `chmod 755 script.sh`). Explain that file extensions (`.sh`) do not confer execution rights in Linux. |
| **3** | *"I ran `ssh-copy-id`, but it still asks me for the remote password every time!"* | Permissions on remote `~/.ssh` or `~/.ssh/authorized_keys` are too permissive, or home directory is group-writable. | Check permissions on remote machine: `chmod 700 ~/.ssh && chmod 600 ~/.ssh/authorized_keys`. Also verify `StrictModes yes` in `sshd_config`. |
| **4** | *"Why did `export VAR=val` inside `./setup.sh` not change my terminal environment?"* | Executing `./setup.sh` spawns a child subshell. Environment variables cannot travel backwards up the process tree to the parent. | Must run `source ./setup.sh` (or `. ./setup.sh`) to execute the commands inside the current shell process. |
| **5** | *"Why does `rm -rf $DIR/*` delete root if `$DIR` is not set?"* | If `$DIR` is unset, `$DIR/*` expands to `/*`! The shell executes `rm -rf /*`. | Always use `set -u` at the top of the script, and quote variables: `rm -rf "${DIR:?Variable unset}/*"`. |
| **6** | *"What is the difference between `$@` and `$*`?"* | When double-quoted, `"$@"` preserves each argument as an independent token (`"arg 1" "arg 2"`), whereas `"$*"` flattens all arguments into a single string separated by IFS (`"arg 1 arg 2"`). | Always use `for item in "$@"` when iterating over script arguments. |

# ⚡ Linux, Bash Scripting & SSH Quick Reference Cheat Sheet
**Master High-Density Pocket Guide for Trainers & Engineers**  
*Covers FHS 3.0, Inode & Permission Math, Core CLI, Bash Scripting Boilerplate, Parameter Expansion, Redirections, Regex/Sed/Awk, and OpenSSH 9.x.*

---

## 1. Linux Filesystem Hierarchy (FHS 3.0) & Storage

### Directory Roles at a Glance
| Directory | Full Name | Purpose & Mounting Constraint |
|:---|:---|:---|
| `/` | Root | Top-level root directory; all partitions mount underneath. |
| `/bin` | User Binaries | Symlink to `/usr/bin` in modern distributions; essential commands. |
| `/sbin` | System Binaries | Symlink to `/usr/sbin`; administrative binaries (`iptables`, `fdisk`). |
| `/etc` | Host Configuration | Static text configuration files (`passwd`, `ssh/sshd_config`, `hosts`). |
| `/dev` | Device Nodes | Virtual pseudo-filesystem populated by `udev` (`sda`, `nvme0n1`, `urandom`, `null`). |
| `/proc` | Process & Kernel API | In-memory pseudo-filesystem exposing live kernel & process states. |
| `/sys` | Hardware & Subsystems | Sysfs exposing hardware devices, buses, drivers, and power tuning. |
| `/var` | Variable Data | Frequently mutating runtime files: `/var/log`, `/var/spool`, `/var/mail`. |
| `/tmp` | Temporary Storage | Ephemeral storage cleared on boot or by `systemd-tmpfiles-clean`. |
| `/home` | User Space | Non-root user home directories (`/home/<username>`). |
| `/root` | Superuser Home | Root user's private home directory (kept on root partition). |
| `/opt` | Optional Packages | Self-contained third-party software (e.g., `/opt/intel/oneapi`). |

### Inode & Link Quick Reference
```bash
# View file inode number, size, blocks, permissions, and timestamps
stat filename

# List directory with inode numbers in column 1
ls -lai

# Create Hard Link (Shared Inode, cannot cross filesystem boundaries)
ln original_file.txt hard_link.txt

# Create Soft/Symbolic Link (Distinct Inode storing path pointer, crosses filesystems)
ln -s /path/to/target.txt sym_link.txt

# Check remaining free inodes on all mounted filesystems
df -ih
```

---

## 2. File Permissions & Umask Math Matrix

### The 4-2-1 Octal Calculation
| Value | Binary | Permission | Meaning on File | Meaning on Directory |
|:---:|:---:|:---:|:---|:---|
| **4** | `100` | Read (`r`) | View file byte contents | List names in directory (`ls`) |
| **2** | `010` | Write (`w`) | Modify file byte contents | Create, rename, or delete files |
| **1** | `001` | Execute (`x`) | Execute file as binary/script | Traverse into directory (`cd`, `stat`) |
| **0** | `000` | None (`-`) | Zero access | Zero access |

### Special Permission Bits
| Bit Name | Octal Value | Representation | Effect on File | Effect on Directory |
|:---|:---:|:---:|:---|:---|
| **SUID** (Set User ID) | `4000` | `rwsr-xr-x` | Executes with owner's UID (e.g., `/usr/bin/passwd`) | No effect on Linux |
| **SGID** (Set Group ID) | `2000` | `rwxr-sr-x` | Executes with group's GID | Newly created files inherit directory's group |
| **Sticky Bit** | `1000` | `rwxrwxrwt` | No effect on Linux files | Only file owner or root can delete files (`/tmp`) |

```bash
# Applying Special Bits
chmod 4755 /path/to/binary   # Set SUID (rwsr-xr-x)
chmod 2775 /shared/project   # Set SGID (rwxrwsr-x)
chmod 1777 /tmp/shared       # Set Sticky Bit (rwxrwxrwt)
chmod u+s,g+s,o+t /target    # Symbolic equivalent
```

### Umask Calculation Formula
$$\text{Base File Mode} = 0666 \quad (\text{rw-rw-rw-}) \quad \longrightarrow \quad \text{New File} = 0666 - \text{umask}$$
$$\text{Base Dir Mode} = 0777 \quad (\text{rwxrwxrwx}) \quad \longrightarrow \quad \text{New Dir} = 0777 - \text{umask}$$

| Umask | File Permission (Math) | Directory Permission (Math) | Security Level |
|:---:|:---:|:---:|:---|
| `0000` | `666` (`rw-rw-rw-`) | `777` (`rwxrwxrwx`) | Insecure / Unrestricted |
| `0022` | `644` (`rw-r--r--`) | `755` (`rwxr-xr-x`) | Standard Linux User Default |
| `0027` | `640` (`rw-r-----`) | `750` (`rwxr-x---`) | Group accessible, world closed |
| `0077` | `600` (`rw-------`) | `700` (`rwx------`) | High Security / Private User |

---

## 3. Core Linux CLI Swiss Army Knife

### File & Search Operations
```bash
# Find files larger than 100MB modified in the last 7 days
find /var/log -type f -name "*.log" -size +100M -mtime -7

# Find and safely delete empty directories
find /tmp/scratch -type d -empty -delete

# Find files with 777 permissions and change them to 755
find /var/www -type d -perm 0777 -exec chmod 755 {} +

# Locate which files are currently held open by a process
lsof -p <PID>

# See which process has locked a specific file or port
lsof /var/log/syslog
lsof -i :8080
```

### Process & System Inspection
```bash
# Process list with full CLI arguments, sorted by memory usage
ps aux --sort=-%mem | head -n 10

# Process tree showing parent-child hierarchy
ps -ef --forest

# Active listening TCP/UDP ports with process names and PIDs
ss -tulpn

# Memory usage in human-readable mebibytes with cache breakdown
free -h

# Mounted disk usage with filesystem types
df -hT

# Directory disk usage sorted by largest consumer
du -ah /var/log | sort -hr | head -n 10
```

### Signals & Process Termination
| Signal | Number | Flag | Behavior | Interceptable? |
|:---|:---:|:---:|:---|:---:|
| **SIGHUP** | 1 | `-HUP` / `-1` | Hangup / Reload daemon config | Yes |
| **SIGINT** | 2 | `-INT` / `-2` | Terminal Interrupt (`Ctrl+C`) | Yes |
| **SIGKILL** | 9 | `-KILL` / `-9` | Immediate kernel termination; uncatchable | **NO** |
| **SIGTERM** | 15 | `-TERM` / `-15` | Polite termination request (default) | Yes |
| **SIGSTOP** | 19 | `-STOP` / `-19` | Pause process execution; uncatchable | **NO** |
| **SIGCONT** | 18 | `-CONT` / `-18` | Resume paused process | Yes |

---

## 4. Environment & Shell Initialization Order

### Bash Startup Lifecycle
```
[ Login Shell ] (SSH, console login, `su - user`, `bash --login`)
  1. /etc/profile
  2. First found of: ~/.bash_profile  ->  ~/.bash_login  ->  ~/.profile
     (Inside ~/.bash_profile, it sources ~/.bashrc)
  3. On logout: ~/.bash_logout

[ Non-Login Interactive Shell ] (Opening a new terminal window inside GUI, running `bash`)
  1. /etc/bash.bashrc (distribution dependent)
  2. ~/.bashrc

[ Non-Interactive Shell ] (Running a script: `bash script.sh`)
  1. Reads variable $BASH_ENV (if set)
  2. Neither /etc/profile nor ~/.bashrc is loaded!
```

### Path & Variable Syntax
```bash
# Export variable for subshells and child processes
export CLUSTER_ENV="production"

# Prepend directory to PATH (Priority over system defaults)
export PATH="/opt/tools/bin:$PATH"

# Append directory to PATH
export PATH="$PATH:/opt/tools/bin"

# Unset variable completely
unset CLUSTER_ENV

# View all active environment variables
printenv
```

---

## 5. Shell Scripting Cheat Sheet

### Production Boilerplate
```bash
#!/usr/bin/env bash
# ==============================================================================
# Fail-fast strict mode:
# -e : Exit immediately if a command exits with a non-zero status
# -u : Treat unset variables as an error and exit immediately
# -o pipefail : Pipeline exit status reflects rightmost non-zero exit
# ==============================================================================
set -euo pipefail
IFS=$'\n\t'

# Trap cleanup on script termination or error
cleanup() {
    local exit_code=$?
    rm -rf /tmp/scratch_$$
    echo "[INFO] Cleaned up scratch files. Exiting with code ${exit_code}."
}
trap cleanup EXIT INT TERM
```

### Special Variables Reference Table
| Variable | Description |
|:---|:---|
| `$0` | Name of the currently executing script. |
| `$1` .. `$9` | Positional parameters 1 through 9. |
| `${10}` .. `${N}` | Positional parameters 10 and above (curly braces mandatory). |
| `$#` | Total count of positional arguments passed. |
| `$@` | All arguments as separate quoted words: `"$1"` `"$2"` `"$3"` (**Preferred**). |
| `$*` | All arguments joined as a single string: `"$1 $2 $3"`. |
| `$?` | Exit status code of the last executed command (`0` = success). |
| `$$` | Process ID (PID) of the currently running script. |
| `$!` | Process ID (PID) of the most recently spawned background job. |
| `$_` | Last argument of the previous command. |

### Parameter Expansion Matrix
| Syntax | Meaning | Example (`NAME="cluster_node"`) | Result |
|:---|:---|:---|:---|
| `${VAR:-word}` | If unset or null, use `word`; do not assign | `${PORT:-8080}` | `8080` (if `PORT` unset) |
| `${VAR:=word}` | If unset or null, assign `word` to `VAR` | `${PORT:=8080}` | Sets `PORT=8080` |
| `${VAR:?error}` | If unset or null, print `error` and abort | `${TOKEN:?"API token missing"}` | Aborts script if empty |
| `${VAR:+word}` | If set and not null, use `word`; else null | `${DEBUG:+"--verbose"}` | Adds flag only if set |
| `${#VAR}` | Length of the string in characters | `${#NAME}` | `12` |
| `${VAR:offset:len}` | Substring extraction | `${NAME:0:7}` | `cluster` |
| `${VAR#pattern}` | Strip shortest matching prefix | `${NAME#cluster_}` | `node` |
| `${VAR##pattern}` | Strip longest matching prefix | `${NAME##*_}` | `node` |
| `${VAR%pattern}` | Strip shortest matching suffix | `${NAME%_node}` | `cluster` |
| `${VAR%%pattern}` | Strip longest matching suffix | `${NAME%%_*}` | `cluster` |
| `${VAR/pattern/rep}` | Replace first occurrence | `${NAME/node/worker}` | `cluster_worker` |
| `${VAR//pattern/rep}`| Replace all occurrences | `${NAME//_/--}` | `cluster--node` |
| `${VAR^^}` | Convert to uppercase | `${NAME^^}` | `CLUSTER_NODE` |
| `${VAR,,}` | Convert to lowercase | `VAR="TEST"; echo ${VAR,,}` | `test` |

### Conditional Test Operators (`[[ ... ]]`)
```bash
# File Attributes
[[ -e "$PATH" ]]   # True if path exists (any type)
[[ -f "$FILE" ]]   # True if path exists and is a regular file
[[ -d "$DIR" ]]    # True if path exists and is a directory
[[ -s "$FILE" ]]   # True if file exists and has size > 0 bytes
[[ -r "$FILE" ]]   # True if file is readable
[[ -w "$FILE" ]]   # True if file is writable
[[ -x "$FILE" ]]   # True if file is executable
[[ -L "$LINK" ]]   # True if file is a symbolic link

# String Comparisons
[[ -z "$STR" ]]    # True if string is null/empty (length == 0)
[[ -n "$STR" ]]    # True if string is NOT empty (length > 0)
[[ "$A" == "$B" ]] # True if strings are identical
[[ "$A" != "$B" ]] # True if strings differ
[[ "$A" =~ ^[0-9]+$ ]] # Regex match (A contains only digits)

# Integer Comparisons (Use inside [[ ]] or (( )))
[[ "$NUM1" -eq "$NUM2" ]]  # Equal
[[ "$NUM1" -ne "$NUM2" ]]  # Not equal
[[ "$NUM1" -lt "$NUM2" ]]  # Less than
[[ "$NUM1" -le "$NUM2" ]]  # Less than or equal
[[ "$NUM1" -gt "$NUM2" ]]  # Greater than
[[ "$NUM1" -ge "$NUM2" ]]  # Greater than or equal

# Arithmetic Evaluator
if (( NUM1 > NUM2 && COUNT % 2 == 0 )); then
    echo "True"
fi
```

### Control Flow Structures
```bash
# If-Elif-Else
if [[ "$ENV" == "prod" ]]; then
    echo "Production"
elif [[ "$ENV" == "stage" ]]; then
    echo "Staging"
else
    echo "Development"
fi

# Case Statement
case "$ACTION" in
    start|run)
        echo "Starting service..."
        ;;
    stop|kill)
        echo "Stopping service..."
        ;;
    status)
        echo "Querying status..."
        ;;
    *)
        echo "Unknown action: $ACTION" >&2
        exit 1
        ;;
esac

# For Loop (List)
for node in master worker01 worker02; do
    echo "Checking node: $node"
done

# For Loop (C-Style)
for (( i = 1; i <= 5; i++ )); do
    echo "Iteration: $i"
done

# While Loop Reading Lines Safely
while IFS=',' read -r username uid role || [[ -n "$username" ]]; do
    echo "Processing $username (UID: $uid, Role: $role)"
done < "users.csv"
```

### Stream Redirection Matrix
| Redirection | Syntax | Meaning |
|:---|:---|:---|
| **Overwrite Stdout** | `cmd > file.txt` | Directs FD 1 (stdout) to file, truncating it |
| **Append Stdout** | `cmd >> file.txt` | Directs FD 1 (stdout) to file, appending |
| **Overwrite Stderr** | `cmd 2> error.log` | Directs FD 2 (stderr) to file |
| **Append Stderr** | `cmd 2>> error.log` | Appends FD 2 (stderr) to file |
| **Combine Stdout & Stderr** | `cmd &> all.log` or `cmd > all.log 2>&1` | Directs both FD 1 and FD 2 to same file |
| **Silence Everything** | `cmd > /dev/null 2>&1` | Discards both streams |
| **Split to File & Screen** | `cmd \| tee output.txt` | Duplicates stdout to terminal and file |
| **Pipe Stdout & Stderr** | `cmd1 \|& cmd2` | Pipes both stdout and stderr of cmd1 to cmd2 |
| **Here-Document** | `cmd << 'EOF'` | Passes multi-line text block as stdin |
| **Here-String** | `cmd <<< "$VAR"` | Passes string variable directly as stdin |

---

## 6. The Text Forensic Triad: Grep, Sed & Awk

### Grep Quick Idioms
```bash
# Case-insensitive, line numbers, recursive search
grep -inr "SSLHandshake" /var/log/

# Exact word match, invert match (exclude comments and blank lines)
grep -Ev "^(#|$|[[:space:]]*#)" /etc/ssh/sshd_config

# Show 2 lines before and 3 lines after match
grep -B 2 -A 3 "FATAL ERROR" /var/log/syslog

# Count matching occurrences across files
grep -c "Failed password" /var/log/auth.log

# PCRE regex with match-only output (Extract IP addresses)
grep -oP '\b([0-9]{1,3}\.){3}[0-9]{1,3}\b' /var/log/auth.log
```

### Sed Stream Editor Quick Idioms
```bash
# Global string replacement in stream
sed 's/localhost/127.0.0.1/g' config.conf

# In-place file modification with backup file (.bak)
sed -i.bak 's/PermitRootLogin yes/PermitRootLogin no/g' /etc/ssh/sshd_config

# Delete blank lines and comments
sed -e '/^[[:space:]]*$/d' -e '/^[[:space:]]*#/d' config.conf

# Print only lines 10 through 25
sed -n '10,25p' access.log

# Append line after match
sed -i '/\[Service\]/a Restart=always' /etc/systemd/system/app.service
```

### Awk Processing Quick Idioms
```bash
# Print specific columns with custom delimiter
awk -F: '{print "User: " $1 " | Shell: " $7}' /etc/passwd

# Filter lines where column 5 exceeds 80% (Disk usage alert)
df -h | awk '$5+0 > 80 {print "WARNING: Partition " $6 " is at " $5}'

# Calculate sum and average of column 3
awk '{sum += $3; count++} END {print "Total:", sum, "| Avg:", (count>0?sum/count:0)}' metrics.txt

# Count frequencies of unique items (Column 1)
awk '{count[$1]++} END {for (item in count) print item, count[item]}' access.log | sort -k2 -rn

# Format output as clean aligned table
awk -F, 'BEGIN {printf "%-15s %-10s %-8s\n", "NAME", "ROLE", "STATUS"}
         {printf "%-15s %-10s %-8s\n", $1, $2, $3}' nodes.csv
```

---

## 7. Secured Shell (SSH) & Cluster Synchronization

### Modern Key Generation & Permissions
```bash
# Generate high-security Ed25519 keypair with comment
ssh-keygen -t ed25519 -C "admin@hpc-cluster.lan" -f ~/.ssh/id_ed25519

# Generate 4096-bit RSA keypair (Legacy fallback)
ssh-keygen -t rsa -b 4096 -C "admin@hpc-cluster.lan" -f ~/.ssh/id_rsa

# Install public key onto remote host
ssh-copy-id -i ~/.ssh/id_ed25519.pub user@10.0.0.21
```

### SSH File Permission Rule Matrix
| Path | Description | Required Permissions | Octal |
|:---|:---|:---|:---:|
| `~/.ssh` | SSH configuration directory | `drwx------` | **`700`** |
| `~/.ssh/id_*` | Any private key | `-rw-------` | **`600`** |
| `~/.ssh/config` | Client configuration file | `-rw-------` | **`600`** |
| `~/.ssh/authorized_keys` | Remote public keys list | `-rw-------` | **`600`** |
| `~/.ssh/id_*.pub` | Public keys (shareable) | `-rw-r--r--` | **`644`** |
| `~/.ssh/known_hosts` | Verified host fingerprint cache | `-rw-r--r--` | **`644`** |

```bash
# Enforce permissions with one command
chmod 700 ~/.ssh && chmod 600 ~/.ssh/id_* ~/.ssh/config ~/.ssh/authorized_keys 2>/dev/null || true
```

### `~/.ssh/config` Master Template
```ssh-config
# Global default options
Host *
    AddKeysToAgent yes
    IdentitiesOnly yes
    ServerAliveInterval 60
    ServerAliveCountMax 3
    StrictHostKeyChecking ask

# Direct target host
Host hpc-head
    HostName 10.0.0.10
    User hpcadmin
    Port 22
    IdentityFile ~/.ssh/id_ed25519

# Worker node isolated in private subnet via JumpHost (Bastion)
Host hpc-worker01
    HostName 192.168.10.101
    User nodeuser
    ProxyJump hpc-head
    IdentityFile ~/.ssh/id_ed25519
```

### Port Forwarding (Tunneling) Cheat Table
| Flag | Name | Syntax | Traffic Direction & Purpose |
|:---:|:---|:---|:---|
| **`-L`** | **Local Forwarding** | `ssh -L 8888:127.0.0.1:8080 user@remote` | Forward `localhost:8888` on **my laptop** to `127.0.0.1:8080` on **remote server**. (View remote dashboard). |
| **`-R`** | **Remote Forwarding** | `ssh -R 9000:127.0.0.1:3000 user@remote` | Forward `9000` on **remote server** to `localhost:3000` on **my laptop**. (Expose local dev server to remote). |
| **`-D`** | **Dynamic SOCKS5** | `ssh -D 1080 user@remote` | Spawns a local SOCKS5 proxy on `1080`. Routes all browser traffic through remote host. |

```bash
# Useful background flags for tunnels:
# -N : Do not execute remote command (port forwarding only)
# -f : Go into background before command execution
ssh -f -N -L 8888:127.0.0.1:8888 user@remote_server
```

### Essential SSH Interactive Escape Sequences
*(Must type Enter, then tilde `~`, then key)*
| Sequence | Action |
|:---|:---|
| `Enter` `~` `.` | **Force disconnect** hung or unresponsive SSH session immediately. |
| `Enter` `~` `^Z` | Suspend SSH process to background (resume with `fg`). |
| `Enter` `~` `#` | List all active forwarded connections and ports. |
| `Enter` `~` `?` | Display help menu of all available escape sequences. |

### File Transfer: Rsync & Scp
```bash
# Rsync over SSH: Archive mode (-a), verbose (-v), compress (-z), progress (-P), delete stale (--delete)
rsync -avzP --delete -e "ssh -p 22" /local/dir/ user@remote:/remote/dir/

# Dry-run before actual transfer
rsync -avzn --delete /local/dir/ user@remote:/remote/dir/

# SCP recursive copy of directory
scp -r -P 22 /local/dir/ user@remote:/remote/dir/
```

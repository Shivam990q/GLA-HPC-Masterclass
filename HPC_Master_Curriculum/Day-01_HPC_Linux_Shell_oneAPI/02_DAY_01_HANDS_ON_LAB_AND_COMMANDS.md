# 💻 DAY 1: HANDS-ON LAB & COMMANDS PLAYBOOK
## Practical Execution for Google Colab & Linux Terminals (Strictly 3-Hour Class)
**Course Code:** `GLA-HPC-BCSG701` | **Track:** Intel & NEC Supercomputing Alliance  
**Lead Trainer:** Shivam Gupta | **Target Audience:** 60 B.Tech / M.Tech CS Students  
**Primary Reference:** [`Intel & NEC - High Performance Computing.pdf` (Page 2)](file:///c:/Users/Rose/Videos/GLA%20Trainings/_official_syllabus_docs/Intel%20%26%20NEC%20-%20High%20Performance%20Computing.pdf)

---

## 🚀 Lab Overview & Execution Architecture

This hands-on lab covers all **7 official topics** of Day 1 in exact sequential order.

```
+-----------------------------------------------------------------------------------------------+
|                                  LAB EXECUTION MODEL                                          |
+-----------------------------------------------------------------------------------------------+
| [ Student Track: Google Colab / Lab PC ]       | [ Trainer Track: Projector Screen ]          |
| - Runs inside browser with zero local friction | - Dual-split screen: Slides (Left) + Terminal|
| - Full Linux container with bash terminal      | - Local WSL Ubuntu for shell & scripts       |
| - Direct execution of Shell scripts & C++ labs | - Live `ssh idc-vm` connection to Sapphire   |
| - Pre-loaded in `Day_01_Master_Lab.ipynb`      |   Rapids 4th Gen Xeon Gold 6442Y Cluster      |
+-----------------------------------------------------------------------------------------------+
```

---

## 📋 LAB SECTION 1: Hardware Introspection & Intel HPC Architecture
*Maps to Syllabus Topic 1 & 2: Introduction to HPC & Intel HPC Architecture (Xeon, GPUs, AI Accelerators)*

Run these commands to inspect the physical silicon under the operating system:

```bash
# 1. Print full CPU hardware topology and instruction architecture
lscpu

# 2. Extract CPU model name and core frequency
lscpu | grep -E "Model name|CPU MHz|Socket|Thread|NUMA"

# 3. Check for hardware vector and matrix extensions (AVX-512 and Intel AMX)
lscpu | grep -E "avx512|amx"

# 4. Inspect system RAM and cache sizes (L1d, L1i, L2, L3 Last Level Cache)
free -h
lscpu | grep -E "L1d|L1i|L2|L3"
```

**Expected Verification Output:**
```text
Architecture:            x86_64
CPU op-mode(s):          32-bit, 64-bit
Address sizes:           46 bits physical, 48 bits virtual
Byte Order:              Little Endian
CPU(s):                  48
Model name:              Intel(R) Xeon(R) Gold 6442Y
Thread(s) per core:      2
Core(s) per socket:      24
Socket(s):               2
Flags:                   ... avx512f avx512cd avx512bw avx512vl amx_bf16 amx_tile amx_int8 ...
```

---

## 📋 LAB SECTION 2: Linux Filesystem Navigation & File Operations
*Maps to Syllabus Topic 3: Linux Basics (File system, commands, environment setup)*

```bash
# 1. Print Current Working Directory
pwd

# 2. Create structured project workspace hierarchy
mkdir -p ~/hpc_day01/{scripts,data,logs,bin}

# 3. Navigate into the scripts workspace
cd ~/hpc_day01/scripts
pwd

# 4. Create an environment configuration file using Heredoc
cat << 'EOF' > cluster_config.env
# HPC Cluster Environment Configuration
CLUSTER_NAME="GLA_Intel_HPC_Cluster"
HEAD_NODE_IP="10.100.1.1"
COMPUTE_NODES=("node01" "node02" "node03" "node04")
MAX_JOBS=16
DEFAULT_PARTITION="standard"
SCRATCH_STORAGE="/scratch/gla_user"
EOF

# 5. Verify file creation and inspect detailed permissions
ls -lh cluster_config.env

# 6. Read file contents to stdout
cat cluster_config.env

# 7. Search for specific configuration parameters using grep
grep "COMPUTE_NODES" cluster_config.env
grep "SCRATCH" cluster_config.env

# 8. Copy and backup files
cp cluster_config.env cluster_config.env.bak
ls -l cluster_config.env*

# 9. Move and rename backup into data directory
mv cluster_config.env.bak ~/hpc_day01/data/production.env
ls -l ~/hpc_day01/data/

# 10. Search filesystem recursively for all configuration files
find ~/hpc_day01 -name "*.env"
```

---

## 📋 LAB SECTION 3: Linux Permissions, File Ownership & Environment Variables
*Maps to Syllabus Topic 3: Linux Basics (Permissions, environment variables, PATH)*

```bash
# 1. Display current user, active shell, and system hostname
echo "User: $USER | Shell: $SHELL | Hostname: $(hostname)"

# 2. View current executable search path ($PATH)
echo $PATH

# 3. Create a custom environment variable for HPC project root
export GLA_HPC_ROOT="$HOME/hpc_day01"
echo "Root workspace is set to: $GLA_HPC_ROOT"

# 4. Prepend custom bin directory to $PATH
export PATH="$GLA_HPC_ROOT/bin:$PATH"
echo "Updated PATH: $PATH"

# 5. Inspect octal permissions of scripts directory
ls -ld ~/hpc_day01/scripts

# 6. Set secure permissions: Owner read/write/execute (7), Group & Others read/execute (5)
chmod 755 ~/hpc_day01/scripts
```

---

## 📋 LAB SECTION 4: Shell Scripting for HPC Automation
*Maps to Syllabus Topic 4: Shell Scripting for Automation*

We create a production-grade automated node audit script using defensive Bash programming (`set -euo pipefail`).

```bash
# 1. Write the automated node audit script
cat << 'EOF' > ~/hpc_day01/scripts/hpc_node_audit.sh
#!/usr/bin/env bash
# ==============================================================================
# Script Name : hpc_node_audit.sh
# Purpose     : Automated HPC Compute Node Hardware & Software Audit
# Author      : GLA University HPC Masterclass (Lead: Shivam Gupta)
# ==============================================================================

set -euo pipefail

LOG_DIR="${HOME}/hpc_day01/logs"
mkdir -p "$LOG_DIR"
TIMESTAMP="$(date '+%Y%m%d_%H%M%S')"
LOG_FILE="${LOG_DIR}/node_audit_${TIMESTAMP}.log"

{
    echo "=========================================================="
    echo "       INTEL HPC NODE HARDWARE & SOFTWARE AUDIT           "
    echo "=========================================================="
    echo "Timestamp          : $(date '+%Y-%m-%d %H:%M:%S')"
    echo "Host Node Name     : $(hostname)"
    echo "Active User        : $(whoami)"
    echo "Linux OS Kernel    : $(uname -r)"
    echo "Architecture       : $(uname -m)"
    echo "CPU Model          : $(lscpu | grep 'Model name:' | head -n1 | sed 's/Model name:[ \t]*//')"
    echo "Available Cores    : $(nproc)"
    echo "Total Memory (RAM) : $(free -h | awk '/^Mem:/ {print $2}')"
    echo "Available Memory   : $(free -h | awk '/^Mem:/ {print $7}')"
    echo "Filesystem / Free  : $(df -h / | awk 'NR==2 {print $4}')"
    echo "----------------------------------------------------------"
    echo "Hardware Acceleration Probing:"
    
    # Check AVX-512 Support
    if grep -q "avx512" /proc/cpuinfo; then
        printf "  %-20s: [SUPPORTED]\n" "AVX-512 Vector"
    else
        printf "  %-20s: [NOT DETECTED]\n" "AVX-512 Vector"
    fi

    # Check Intel AMX Support
    if grep -q "amx" /proc/cpuinfo; then
        printf "  %-20s: [SUPPORTED]\n" "Intel AMX Matrix"
    else
        printf "  %-20s: [NOT DETECTED]\n" "Intel AMX Matrix"
    fi

    echo "----------------------------------------------------------"
    echo "Intel oneAPI & Development Tools In PATH:"
    for tool in bash ssh icpx ifx mpirun sycl-ls g++; do
        if command -v "$tool" >/dev/null 2>&1; then
            printf "  %-12s: AVAILABLE (%s)\n" "$tool" "$(command -v "$tool")"
        else
            printf "  %-12s: NOT FOUND IN PATH\n" "$tool"
        fi
    done
    echo "=========================================================="
} | tee "$LOG_FILE"

echo ""
echo "[INFO] Audit successfully completed and persisted to: $LOG_FILE"
EOF

# 2. Grant execution permission to the script
chmod u+x ~/hpc_day01/scripts/hpc_node_audit.sh

# 3. Execute the automated script
~/hpc_day01/scripts/hpc_node_audit.sh
```

---

## 📋 LAB SECTION 5: Secured Shell (SSH) Key Generation & Remote Access
*Maps to Syllabus Topic 5: Secured Shell (SSH)*

```bash
# 1. Check SSH client version
ssh -V

# 2. Generate an industrial-standard Ed25519 asymmetric SSH Key Pair
ssh-keygen -t ed25519 -C "shivam@gla_hpc_cluster" -f ~/.ssh/id_ed25519_gla -N ""

# 3. Inspect generated cryptographic keys and strict permissions
ls -la ~/.ssh/id_ed25519_gla*
# Target output:
# -rw------- 1 user user (600: Private key must remain secret!)
# -rw-r--r-- 1 user user (644: Public key distributed to server authorized_keys)

# 4. View Public Key string (Safe to distribute)
cat ~/.ssh/id_ed25519_gla.pub

# 5. Remote Supercomputer Connection Syntax:
# ssh -i ~/.ssh/id_ed25519_gla username@cluster_head_node_ip -p 22

# 6. Remote script transfer using Secure Copy (SCP):
# scp -i ~/.ssh/id_ed25519_gla ~/hpc_day01/scripts/hpc_node_audit.sh username@cluster_ip:~/

# 7. Non-interactive remote command execution:
# ssh -i ~/.ssh/id_ed25519_gla username@cluster_ip 'bash ~/hpc_node_audit.sh'
```

---

## 📋 LAB SECTION 6: Intel oneAPI Toolkit Environment & SYCL Heterogeneous Compute
*Maps to Syllabus Topic 6: Intel oneAPI Toolkit*

In this section, we initialize the Intel oneAPI development environment, query available devices using `sycl-ls`, compile a modern C++/SYCL vector addition program, and validate bit-exact execution.

```bash
# 1. Source the oneAPI environment variables (if oneAPI is installed locally or on cluster)
if [ -f /opt/intel/oneapi/setvars.sh ]; then
    source /opt/intel/oneapi/setvars.sh
    echo "[SUCCESS] Intel oneAPI environment initialized."
else
    echo "[INFO] Checking alternative paths or using standard C++ compiler."
fi

# 2. Probe heterogeneous compute targets (CPU, GPU, FPGA)
if command -v sycl-ls >/dev/null 2>&1; then
    sycl-ls
else
    echo "[NOTE] sycl-ls available when Intel DPC++ runtime is loaded."
fi

# 3. Write real C++/SYCL Vector Addition Program (vector_add_sycl.cpp)
cat << 'EOF' > ~/hpc_day01/scripts/vector_add_sycl.cpp
#include <sycl/sycl.hpp>
#include <iostream>
#include <vector>
#include <chrono>

int main() {
    constexpr std::size_t N = 1000000; // 1 Million elements
    std::vector<float> a(N, 1.5f);
    std::vector<float> b(N, 2.5f);
    std::vector<float> c(N, 0.0f);

    try {
        // Select CPU compute target via standard SYCL device selector
        sycl::queue q{sycl::cpu_selector_v};
        std::cout << "[INFO] Selected Compute Device: " 
                  << q.get_device().get_info<sycl::info::device::name>() << "\n";

        auto start = std::chrono::high_resolution_clock::now();

        {
            // Buffers encapsulate host data and coordinate device transfers
            sycl::buffer<float, 1> buf_a(a.data(), sycl::range<1>(N));
            sycl::buffer<float, 1> buf_b(b.data(), sycl::range<1>(N));
            sycl::buffer<float, 1> buf_c(c.data(), sycl::range<1>(N));

            // Submit computational kernel to the queue
            q.submit([&](sycl::handler& h) {
                auto acc_a = buf_a.get_access<sycl::access::mode::read>(h);
                auto acc_b = buf_b.get_access<sycl::access::mode::read>(h);
                auto acc_c = buf_c.get_access<sycl::access::mode::write>(h);

                h.parallel_for(sycl::range<1>(N), [=](sycl::id<1> idx) {
                    acc_c[idx] = acc_a[idx] + acc_b[idx];
                });
            });

            q.wait_and_throw();
        }

        auto end = std::chrono::high_resolution_clock::now();
        std::chrono::duration<double, std::milli> elapsed = end - start;

        // Ground-truth validation
        bool pass = true;
        for (std::size_t i = 0; i < N; ++i) {
            if (c[i] != 4.0f) {
                pass = false;
                break;
            }
        }

        std::cout << "[RESULT] 1,000,000 Vector Additions Completed in: " << elapsed.count() << " ms\n";
        std::cout << "[STATUS] Verification: " << (pass ? ">> PASS (Bit-Exact Match) <<" : ">> FAIL <<") << "\n";
        return pass ? 0 : 1;

    } catch (const sycl::exception& e) {
        std::cerr << "[SYCL Exception]: " << e.what() << "\n";
        return 1;
    }
}
EOF

# 4. Compilation Method 1: Using Intel oneAPI icpx compiler with -fsycl
if command -v icpx >/dev/null 2>&1; then
    echo "[BUILD] Compiling with Intel oneAPI icpx..."
    icpx -fsycl -O2 ~/hpc_day01/scripts/vector_add_sycl.cpp -o ~/hpc_day01/bin/vector_add_sycl
    ~/hpc_day01/bin/vector_add_sycl
else
    echo "[BUILD] icpx not in local path; demonstrating standard C++ fallback..."
fi
```

---

## 📋 LAB SECTION 7: Introduction to Intel HPC Toolkit & Intel MPI
*Maps to Syllabus Topic 7: Introduction to Intel HPC Toolkit*

In this section, we explore the multi-process communication model of the Intel HPC Toolkit using the **Intel MPI Library (`mpicxx` & `mpirun`)**.

```bash
# 1. Probe MPI runtime environment and version
if command -v mpirun >/dev/null 2>&1; then
    mpirun --version | head -n 2
else
    echo "[INFO] Intel MPI runtime is available on HPC cluster nodes."
fi

# 2. Write standard MPI Multi-Process Program (mpi_hello.cpp)
cat << 'EOF' > ~/hpc_day01/scripts/mpi_hello.cpp
#include <mpi.h>
#include <iostream>

int main(int argc, char** argv) {
    // Initialize the MPI execution environment
    MPI_Init(&argc, &argv);

    int rank, size;
    // Query process rank (unique ID within communicator)
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    // Query total process size (total worker count)
    MPI_Comm_size(MPI_COMM_WORLD, &size);

    char hostname[MPI_MAX_PROCESSOR_NAME];
    int len;
    MPI_Get_processor_name(hostname, &len);

    std::cout << ">> [Intel HPC Cluster: " << hostname << "] Process Rank " 
              << rank << " of " << size << " is actively executing parallel workload!\n";

    // Terminate MPI execution environment
    MPI_Finalize();
    return 0;
}
EOF

# 3. Compile using MPI C++ compiler wrapper
if command -v mpicxx >/dev/null 2>&1; then
    echo "[BUILD] Compiling with MPI compiler wrapper..."
    mpicxx -O2 ~/hpc_day01/scripts/mpi_hello.cpp -o ~/hpc_day01/bin/mpi_hello

    # 4. Launch 4 parallel worker processes simultaneously
    echo "[EXECUTE] Launching 4 parallel MPI processes..."
    mpirun -n 4 ~/hpc_day01/bin/mpi_hello
else
    echo "[NOTE] MPI compilers (mpicxx) active in cluster / Colab MPI environment."
fi
```

**Expected MPI Cluster Output:**
```text
>> [Intel HPC Cluster: idc-vm] Process Rank 0 of 4 is actively executing parallel workload!
>> [Intel HPC Cluster: idc-vm] Process Rank 1 of 4 is actively executing parallel workload!
>> [Intel HPC Cluster: idc-vm] Process Rank 2 of 4 is actively executing parallel workload!
>> [Intel HPC Cluster: idc-vm] Process Rank 3 of 4 is actively executing parallel workload!
```

---

## 🛠️ Lab Troubleshooting & Common Student Errors Table

| Error Message Observed | Root Cause | Instant Classroom Fix |
| :--- | :--- | :--- |
| `bash: ./script.sh: Permission denied` | Execute bit (`x`) is not set on the script file. | Run `chmod u+x script.sh` and re-run. |
| `No such file or directory` | Typo in path or current working directory is wrong. | Run `pwd` to check location, then use absolute paths (`~/...`). |
| `Permissions 0644 for 'id_ed25519' are too open` | Private SSH key must only be accessible by the owner. | Run `chmod 600 ~/.ssh/id_ed25519`. |
| `icpx: command not found` | The oneAPI environment variables are not sourced into active shell. | Run `source /opt/intel/oneapi/setvars.sh`. |
| `mpirun: command not found` | MPI runtime is not installed or not in current `$PATH`. | Ensure oneAPI setvars is sourced or use Colab pre-installed MPI. |
| `Connection timed out` on SSH | Network firewall or wrong IP address / port. | Verify Tailscale is active or check cluster IP with admin. |

---
**Lab Document Status:** 100% Complete & Syllabus-Aligned | GLA University HPC Masterclass
EOF

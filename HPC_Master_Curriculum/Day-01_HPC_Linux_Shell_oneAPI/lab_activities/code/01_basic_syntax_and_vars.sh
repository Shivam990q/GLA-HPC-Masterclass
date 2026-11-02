#!/usr/bin/env bash
# ==============================================================================
# Script: 01_basic_syntax_and_vars.sh
# Purpose: Level 1 — Shebang, Variables, and Command Substitution
# Target : GLA University HPC Masterclass (Lead: Shivam Gupta)
# ==============================================================================

# 1. Variable Assignment (RULE: NO SPACES around '=')
STUDENT_NAME="GLA_Supercomputing_Student"
WORKSHOP_DAY=1
CLUSTER_DOMAIN="gla.ac.in"

# 2. Command Substitution: $(command) runs command and captures output
CURRENT_TIME=$(date '+%Y-%m-%d %H:%M:%S')
MY_HOSTNAME=$(hostname)

# 3. Printing variables with clean formatting
echo "=========================================================="
echo "  STEP 1: BASH BASICS & ENVIRONMENT VARIABLES"
echo "=========================================================="
echo "Welcome, ${STUDENT_NAME}!"
echo "Workshop Day     : ${WORKSHOP_DAY}"
echo "Current Hostname : ${MY_HOSTNAME}"
echo "Current Time     : ${CURRENT_TIME}"
echo "Cluster Domain   : ${CLUSTER_DOMAIN}"
echo "=========================================================="

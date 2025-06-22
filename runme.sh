#!/usr/bin/env bash
set -euo pipefail

PYTHON_SCRIPT="hashclash.py"
echo "[*] Running chosen-prefix collision under perf…"
perf stat -I 60000 -e power/energy-pkg/ python3 ${PYTHON_SCRIPT} 2> running_power_with_non_empty_prefixes.log

rm -rf workdir* data file*.bin step*.log

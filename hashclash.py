import os
import subprocess
import time
import uuid
from pathlib import Path

def hashclash_cmd(workdir, root):
    ''' Return a ready-to-run command list for HashClash. '''
    workdir.mkdir(parents=True, exist_ok=True)

    p1 = workdir / 'p1.bin'
    p2 = workdir / 'p2.bin'
    p1.write_bytes(b'Arquivo 1') # empty prefixes are easier and quicker
    p2.write_bytes(b'Arquivo 2, diferente do arquivo1')
    return [f'{root}/scripts/cpc.sh', str(p1), str(p2)]

def run_single(threads, hashclash_root):
    run_id = uuid.uuid4().hex[:8]
    outdir = Path('results') / f'{run_id}_MD5'
    cmd = hashclash_cmd(outdir, hashclash_root)

    env = os.environ.copy()
    env['OMP_NUM_THREADS'] = str(threads)

    print(f'[+] MD5 | {threads:>2} thread(s) | id {run_id}')
    t0 = time.time()
    proc = subprocess.run(cmd, env=env, check=False)
    if proc.returncode not in (0,1):
        raise RuntimeError(f'Command failed with return code {proc.returncode}: {cmd}')
    t1 = time.time()
    print(f'Finished in {t1 - t0:.2f} s\n')

def main():
    run_single(THREADS, HASHCLASH_ROOT)


HASHCLASH_ROOT = '/home/isaac/workbench/crypto/hashclash'
THREADS = 8

if __name__ == '__main__':
    main()

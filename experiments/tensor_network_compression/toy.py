"""Tensorize a 16x16 matrix into interleaved sites; TT-SVD yields an MPO.
Educational dense reconstruction only; no LLM kernels or CompactifAI reproduction.
"""
import argparse
import json
import numpy as np

def mpo(matrix, bond):
    if matrix.shape != (16,16) or bond < 1:
        raise ValueError("Toy MPO requires a 16x16 matrix and positive bond")
    # row bits (i0..i3), column bits (j0..j3) -> sites (i0,j0)..(i3,j3)
    tensor = matrix.reshape([2]*8).transpose(0,4,1,5,2,6,3,7).reshape([4]*4)
    cores=[]; rest=tensor; rank=1
    for site in range(3):
        u,s,vh=np.linalg.svd(rest.reshape(rank*4,-1),full_matrices=False)
        r=min(bond,len(s)); cores.append(u[:,:r].reshape(rank,4,r))
        rest=s[:r,None]*vh[:r]; rank=r
    cores.append(rest.reshape(rank,4,1))
    rebuilt=cores[0]
    for core in cores[1:]:
        rebuilt=np.tensordot(rebuilt,core,axes=([-1],[0]))
    rebuilt=rebuilt.squeeze((0,-1)).reshape([2]*8).transpose(0,2,4,6,1,3,5,7).reshape(16,16)
    return cores,rebuilt

def experiment(seed=42):
    rng=np.random.default_rng(seed)
    # A sum of Kronecker products gives controlled compressible structure; add noise.
    matrix=np.kron(np.kron(np.kron(rng.normal(size=(2,2)),rng.normal(size=(2,2))),rng.normal(size=(2,2))),rng.normal(size=(2,2)))
    matrix+=.01*rng.normal(size=(16,16))
    result=[]
    for bond in (1,2,4,8,16):
        cores,approx=mpo(matrix,bond); count=sum(c.size for c in cores)
        result.append({"bond":bond,"original_parameters":matrix.size,"mpo_parameters":count,
            "parameter_ratio":matrix.size/count,"relative_frobenius_error":float(np.linalg.norm(matrix-approx)/np.linalg.norm(matrix)),
            "warning":"A ratio below 1 means expansion; dense reconstruction provides no inference speedup."})
    u,s,vh=np.linalg.svd(matrix,full_matrices=False)
    rank=2; low=(u[:,:rank]*s[:rank])@vh[:rank]
    return {"seed":seed,"status":"toy_only", "svd_rank2":{"parameters":rank*(16+16+1),"relative_frobenius_error":float(np.linalg.norm(matrix-low)/np.linalg.norm(matrix))},"mpo":result}

if __name__=="__main__":
    p=argparse.ArgumentParser();p.add_argument("--out",default="results/runs/toy-mpo.json");a=p.parse_args()
    from pathlib import Path
    Path(a.out).parent.mkdir(parents=True,exist_ok=True)
    Path(a.out).write_text(json.dumps(experiment(),indent=2)+"\n")

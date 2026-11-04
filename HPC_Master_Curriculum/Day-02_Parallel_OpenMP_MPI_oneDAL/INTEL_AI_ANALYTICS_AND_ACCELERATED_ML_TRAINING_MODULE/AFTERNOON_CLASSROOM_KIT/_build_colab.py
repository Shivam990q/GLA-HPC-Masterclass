# Builds the Day-2 afternoon Colab notebook (syllabus topics 4–5 only).
import json
from pathlib import Path

nb = {"nbformat": 4, "nbformat_minor": 5, "metadata": {
    "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
    "language_info": {"name": "python", "pygments_lexer": "ipython3"},
    "colab": {"provenance": [], "toc_visible": True},
}}

def md(src):
    return {"cell_type": "markdown", "metadata": {}, "source": src if isinstance(src, list) else src.splitlines(True)}

def code(src):
    return {"cell_type": "code", "metadata": {}, "execution_count": None, "outputs": [],
            "source": src if isinstance(src, list) else src.splitlines(True)}

cells = []

cells.append(md("""# Day 2 Afternoon Colab — Intel AI Analytics Toolkit + sklearnex
**Syllabus only (official Day 2 topics 4 and 5)**
1. **Topic A — Using Intel AI Analytics Toolkit** (optimized NumPy, Pandas, Scikit-learn)
2. **Topic B — Intel Extension for Scikit-learn** (`patch_sklearn()`, oneDAL algorithms)

**Not in this notebook:** OpenMP/MPI C++ (morning), TensorFlow, oneDNN, Slurm, Horovod, VTune, Gaudi, OpenVINO.

**How to run:** Runtime → Run all. After every code cell, complete the **5 MCQs** before going on.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Shivam990q/GLA-HPC-Masterclass/blob/main/COLAB_NOTEBOOKS/Day_02_Intel_AI_Analytics_and_Accelerated_ML_Colab.ipynb)
"""))

cells.append(md("""## Topic A / Module A0 — Colab environment (paths, pip, sklearnex)
**Run this cell first.** On Google Colab it may **restart the kernel once** after installing `scikit-learn-intelex`. That is required: pip must not leave SciPy’s old `.so` files loaded (the `scipy._cyutility / __Pyx__Import` crash). After the auto-restart, **Runtime → Run all** again. No Google Drive.
"""))

cells.append(code(r'''import os, sys, site, subprocess, platform
from pathlib import Path

IN_COLAB = Path("/content").exists() or ("google.colab" in sys.modules)
WORKSPACE_DIR = Path("/content/hpc_intel_analytics_workspace") if IN_COLAB else Path.cwd() / "hpc_intel_analytics_workspace"
WORKSPACE_DIR.mkdir(parents=True, exist_ok=True)
REPORTS_DIR = WORKSPACE_DIR / "reports"
REPORTS_DIR.mkdir(parents=True, exist_ok=True)

def _pip(*args):
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-q", *args])

def _colab_restart_once(reason):
    """Unload mixed NumPy/SciPy C extensions. Only used on Colab after pip."""
    if not IN_COLAB:
        print("Non-Colab: skip auto-restart.", reason)
        return
    print("=" * 66)
    print(reason)
    print("Colab kernel is restarting ONCE. Then click Runtime -> Run all.")
    print("=" * 66)
    os.kill(os.getpid(), 9)

def _sklearn_scipy_broken():
    try:
        from sklearn.datasets import make_blobs  # noqa: F401
        return False
    except Exception as exc:
        text = str(exc).lower()
        keys = ("scipy._cyutility", "pyx__import", "does not export expected c function", "numpy.dtype size changed")
        return any(k in text for k in keys)

need_sklearnex = False
try:
    import sklearnex  # noqa: F401
except ImportError:
    need_sklearnex = True

if _sklearn_scipy_broken():
    print("Repairing broken SciPy/sklearn binaries (Colab pip mixed C extensions)...")
    _pip("--force-reinstall", "--no-cache-dir", "scipy", "scikit-learn")
    _pip("scikit-learn-intelex")
    _colab_restart_once("SciPy was repaired. Kernel restart required.")

if need_sklearnex:
    # Do not --upgrade numpy/scipy. sklearnex still may replace scipy wheels;
    # Colab must restart so old scipy._cyutility is not left in memory.
    _pip("scikit-learn-intelex")
    site.main()
    _colab_restart_once("scikit-learn-intelex installed. Kernel restart required.")

# Reached only when sklearnex is already importable in this kernel.
site.main()
for sp in list(site.getsitepackages()) + [site.getusersitepackages()]:
    if sp and sp not in sys.path:
        sys.path.insert(0, sp)

import numpy as np
import pandas as pd
import sklearn
import sklearnex
from sklearnex import patch_sklearn, unpatch_sklearn
import importlib

if _sklearn_scipy_broken():
    raise ImportError(
        "sklearn/scipy C extensions are still mixed. "
        "In Colab: Runtime -> Restart session, then run this cell again."
    )

def safe_patch(algorithm_name=None):
    """Selective patch with short names and fully-qualified names (sklearnex version drift)."""
    if algorithm_name is None:
        patch_sklearn(verbose=False)
        return
    canonical = {
        "KMeans": ["sklearn.cluster.KMeans", "KMeans"],
        "RandomForestClassifier": ["sklearn.ensemble.RandomForestClassifier", "RandomForestClassifier"],
        "PCA": ["sklearn.decomposition.PCA", "PCA"],
        "KNeighborsClassifier": ["sklearn.neighbors.KNeighborsClassifier", "KNeighborsClassifier"],
        "StandardScaler": ["sklearn.preprocessing.StandardScaler", "StandardScaler"],
    }
    for target in canonical.get(algorithm_name, [algorithm_name]):
        try:
            patch_sklearn(name=[target], verbose=False)
            return
        except Exception:
            continue
    patch_sklearn(verbose=False)

def fresh_class(module_name, class_name):
    """Read the live class from the module AFTER patch/unpatch.
    Do not importlib.reload — reload re-executes sklearn and can wipe the patch.
    """
    mod = importlib.import_module(module_name)
    return getattr(mod, class_name)

def show_mcqs(title, questions):
    """Clickable 5-question check. questions = [{q, choices, k, why}, ...]"""
    import json, uuid
    from IPython.display import HTML, display
    uid = "m" + uuid.uuid4().hex[:10]
    payload = json.dumps(questions)
    display(HTML(f"""
    <div id="{uid}" style="font-family:Segoe UI,Arial,sans-serif;border:1px solid #cfdbe8;border-radius:14px;padding:14px;background:#fff;margin:8px 0">
      <div style="font-weight:800;color:#07182c">{title} · click an answer · 5 questions</div>
      <div class="body"></div>
      <div class="score" style="margin-top:8px;font-weight:700;color:#0071c5"></div>
    </div>
    <script>
    (function(){{
      const root = document.getElementById("{uid}");
      const qs = {payload};
      let i=0, score=0, lock=false;
      const body = root.querySelector(".body");
      const scoreEl = root.querySelector(".score");
      function render(){{
        lock=false;
        if(i>=qs.length){{
          body.innerHTML = "<b>Section score: "+score+" / "+qs.length+"</b> — go to the next cell.";
          scoreEl.textContent="";
          return;
        }}
        const q=qs[i];
        body.innerHTML = "<p style='margin:10px 0 6px'><b>Q"+(i+1)+".</b> "+q.q+"</p>" +
          q.choices.map((c,idx)=>"<button data-i='"+idx+"' style='display:block;width:100%;text-align:left;margin:5px 0;padding:8px 10px;border-radius:10px;border:1px solid #cfdbe8;background:#f8fbfe;cursor:pointer'>"+"ABCD"[idx]+". "+c+"</button>").join("") +
          "<div class='why' style='display:none;margin-top:8px;padding:8px;background:#fff8e4;border-radius:8px'></div>" +
          "<button class='nx' style='display:none;margin-top:8px;background:#0071c5;color:#fff;border:0;padding:8px 12px;border-radius:8px;font-weight:700'>Next</button>";
        body.querySelectorAll("button[data-i]").forEach(b=>b.onclick=()=>pick(+b.dataset.i,q,b));
        body.querySelector(".nx").onclick=()=>{{i++;render();}};
        scoreEl.textContent = "Score "+score+" / "+qs.length+" · question "+(i+1);
      }}
      function pick(idx,q,btn){{
        if(lock) return; lock=true;
        body.querySelectorAll("button[data-i]").forEach((b,j)=>{{
          if(j===q.k) b.style.background="#e7f7ee";
          if(j===idx && idx!==q.k) b.style.background="#fdecee";
        }});
        if(idx===q.k) score++;
        const why=body.querySelector(".why");
        why.style.display="block";
        why.textContent = (idx===q.k ? "Correct. " : "Not quite. ") + q.why;
        body.querySelector(".nx").style.display="inline-block";
        scoreEl.textContent = "Score "+score+" / "+qs.length;
      }}
      render();
    }})();
    </script>
    """))

print("=" * 66)
print("ENVIRONMENT READY")
print(f"  Python          : {platform.python_version()}  {platform.system()} {platform.machine()}")
print(f"  In Google Colab : {IN_COLAB}")
print(f"  NumPy           : {np.__version__}")
print(f"  Pandas          : {pd.__version__}")
print(f"  Scikit-learn    : {sklearn.__version__}")
print(f"  sklearnex       : {sklearnex.__version__}")
print(f"  Workspace       : {WORKSPACE_DIR.resolve()}")
print(f"  Reports         : {REPORTS_DIR.resolve()}")
print("=" * 66)
assert WORKSPACE_DIR.is_dir()
assert sklearnex.__version__
'''))

cells.append(code('''show_mcqs("MCQ after environment cell — Topic A", [
  {"q":"Why may Colab restart the kernel once after pip install scikit-learn-intelex?","choices":["To mount Google Drive","So SciPy/NumPy C extensions reload; otherwise sklearn.datasets hits scipy._cyutility / __Pyx__Import","To enable CUDA","To disable the GIL"],"k":1,"why":"pip can replace SciPy files on disk while old .so modules stay in RAM. Restart loads one consistent set."},
  {"q":"Where is the workspace on Colab vs a laptop?","choices":["Always C:/Users"," /content/hpc_intel_analytics_workspace on Colab, otherwise ./hpc_intel_analytics_workspace","Google Drive only","/tmp/onedal"],"k":1,"why":"If /content exists we use Colab local disk. No Drive auth."},
  {"q":"Official pip package for Intel Extension for Scikit-learn?","choices":["intel-sklearn-turbo","scikit-learn-intelex","onedal-python-accel","intel-ai-core-ml"],"k":1,"why":"Import name is sklearnex; pip name is scikit-learn-intelex."},
  {"q":"This afternoon is Day 2 syllabus topics:","choices":["4 and 5: AI Analytics Toolkit + sklearnex","TensorFlow-MKL and Horovod","Slurm and VTune","Gaudi and OpenVINO"],"k":0,"why":"Morning already did OpenMP/MPI. Deep learning is Day 3+."},
  {"q":"safe_patch(name=['KMeans']) tries both short and fully-qualified names because:","choices":["Intel requires both always","sklearnex versions disagree on name= lists","KMeans is not acceleratable","Colab forbids short names"],"k":1,"why":"Older wheels want KMeans; newer want sklearn.cluster.KMeans. The helper tries both, then global patch."}
])
'''))

cells.append(md("""## Topic A / Module A2–A5 — Hardware, SIMD, NumPy BLAS
Read CPU flags if `/proc/cpuinfo` exists (Linux/Colab). On Windows the cell still runs. Then inspect NumPy’s BLAS (oneMKL vs OpenBLAS).
"""))

cells.append(code(r'''import os, multiprocessing, platform
from pathlib import Path

num_cores = multiprocessing.cpu_count() or os.cpu_count() or 1
print("=" * 66)
print("HARDWARE / SIMD / BLAS")
print(f"  OS / machine     : {platform.system()} {platform.release()} {platform.machine()}")
print(f"  Logical CPUs     : {num_cores}")
print(f"  OMP_NUM_THREADS  : {os.environ.get('OMP_NUM_THREADS', '(unset - runtime default)')}")
print(f"  MKL_NUM_THREADS  : {os.environ.get('MKL_NUM_THREADS', '(unset)')}")

cpuinfo_path = Path("/proc/cpuinfo")
if cpuinfo_path.exists():
    text = cpuinfo_path.read_text(errors="ignore")
    flag_lines = [ln for ln in text.splitlines() if ln.lower().startswith("flags") or "Features" in ln]
    blob = flag_lines[0].lower() if flag_lines else text.lower()
    print(f"  AVX-512          : {'YES' if 'avx512' in blob else 'NO (Colab often AVX2 only - speedup still real, just smaller)'}")
    print(f"  AVX2             : {'YES' if 'avx2' in blob else 'NO'}")
    print(f"  SSE4.2           : {'YES' if 'sse4_2' in blob or 'sse4.2' in blob else 'NO'}")
else:
    print("  /proc/cpuinfo missing (Windows laptop). SIMD flags skipped; sklearnex still runs.")

print("-" * 66)
print("NumPy BLAS / LAPACK (look for mkl, openblas, flexiblas):")
try:
    np.show_config()
except Exception as exc:
    print("  np.show_config() unavailable:", exc)
    print("  numpy:", np.__version__)
print("=" * 66)
'''))

cells.append(code('''show_mcqs("MCQ after hardware cell — Topic A", [
  {"q":"What does AVX-512 mean for oneDAL/oneMKL?","choices":["A Python lock","512-bit SIMD: 8 float64 or 16 float32 per instruction","A Pandas dtype","A Slurm partition"],"k":1,"why":"Single Instruction Multiple Data. Colab VMs often have AVX2 (256-bit) only."},
  {"q":"If Colab prints AVX-512 NO, the labs:","choices":["Must fail","Still run; speedup may be 4x–15x instead of 20x+","Require a GPU runtime","Need OpenVINO"],"k":1,"why":"oneDAL picks AVX2 kernels. Do not stop the class."},
  {"q":"How do you inspect whether NumPy is linked to Intel MKL?","choices":["numpy.check_mkl_status()","numpy.show_config()","lscpu --mkl","pip show mkl-only"],"k":1,"why":"Look for blas_mkl_info / mkl_rt. Colab is often OpenBLAS — still much faster than Python loops."},
  {"q":"OMP_NUM_THREADS=4 on 8 cores does what?","choices":["Caps OpenMP to 4 threads","Starts 4 MPI ranks","Limits RAM to 4 GB","Enables AVX-512"],"k":0,"why":"oneDAL and MKL read OpenMP. Match physical cores; oversubscribe hurts."},
  {"q":"Why is /proc/cpuinfo wrapped in a path check?","choices":["It is secret","Linux/Colab have it; Windows trainer laptops do not — the cell must not crash","sklearnex requires it","NumPy writes it"],"k":1,"why":"Multiple paths: Colab Linux vs local Windows. Both must work."}
])
'''))

cells.append(md("""## Topic A / Module A6 — Optimized NumPy (oneMKL / BLAS DGEMM)
Pure Python triple loop vs `np.dot`. Same math; contiguous buffer + BLAS vs boxed PyObjects + GIL.
"""))

cells.append(code(r'''import time
import numpy as np

print("=" * 66)
print("DEMO: PYTHON LOOPS vs NUMPY BLAS")

N_small = 160  # 160^3 is enough to feel GIL+boxing without stalling the class
A_list = [[1.0] * N_small for _ in range(N_small)]
B_list = [[2.0] * N_small for _ in range(N_small)]
C_list = [[0.0] * N_small for _ in range(N_small)]
t0 = time.perf_counter()
for i in range(N_small):
    for j in range(N_small):
        s = 0.0
        for k in range(N_small):
            s += A_list[i][k] * B_list[k][j]
        C_list[i][j] = s
t_python = time.perf_counter() - t0
print(f"  Pure Python {N_small}x{N_small}: {t_python:.4f}s")

N_large = 1024
A_np = np.ones((N_large, N_large), dtype=np.float64)
B_np = np.full((N_large, N_large), 2.0, dtype=np.float64)
# warmup so first-touch pages are not billed to BLAS
_ = np.dot(A_np[:8, :8], B_np[:8, :8])
t0 = time.perf_counter()
C_np = np.dot(A_np, B_np)
t_mkl = time.perf_counter() - t0
gflops = (2.0 * (N_large ** 3) / t_mkl) / 1e9
print(f"  NumPy BLAS  {N_large}x{N_large}: {t_mkl:.4f}s  ({gflops:.2f} GFLOP/s)")
print(f"  Check: C[0,0] = {C_np[0,0]:.1f}  (expect {float(N_large * 2):.1f})")
assert abs(C_np[0, 0] - (N_large * 2.0)) < 1e-6
print("=" * 66)
'''))

cells.append(code('''show_mcqs("MCQ after NumPy cell — Topic A (optimized NumPy)", [
  {"q":"Why is a Python list of floats slow for DGEMM?","choices":["Lists live on disk","Each float is a boxed PyObject; the list stores pointers; SIMD cannot load a packed 64-byte line","NumPy forbids lists","The GIL doubles the clock"],"k":1,"why":"Pointer chasing + GIL. NumPy is one contiguous buffer."},
  {"q":"What library actually accelerates np.dot in the Intel AI Analytics Toolkit?","choices":["oneDNN","oneMKL (BLAS DGEMM)","Horovod","OpenVINO"],"k":1,"why":"oneMKL = linear algebra. oneDNN is Day 3 neural nets."},
  {"q":"np.dot releases the GIL during the C BLAS call. That means:","choices":["Python bytecode still uses 64 cores","Native threads can run the multiply on many cores","Pandas becomes multi-process","You must call patch_sklearn first"],"k":1,"why":"BLAS is C. patch_sklearn is for sklearn estimators, not np.dot."},
  {"q":"float32 vs float64 in a 512-bit AVX-512 register?","choices":["Same count","16 float32 vs 8 float64","8 float32 vs 16 float64","Only int8 fits"],"k":1,"why":"Precision rule on the cheat sheet. Labs use contiguous arrays."},
  {"q":"FMA does which operation in one instruction?","choices":["Only add","(A×B)+C with one rounding","Disk compress","MPI_Reduce"],"k":1,"why":"Fused multiply-add is why GEMM hits high GFLOP/s."}
])
'''))

cells.append(md("""## Topic A — Optimized Pandas (Intel Distribution of Modin)
Syllabus names Pandas next to NumPy and Scikit-learn. Stock `pandas` is largely single-threaded. The toolkit drop-in is `import modin.pandas as pd`. This cell uses **stock pandas already on Colab** for a small groupby, then tells you the Modin one-liner. We do **not** `pip install modin` here (it pulls Ray/Dask and can break a class VM).
"""))

cells.append(code(r'''import time
import numpy as np
import pandas as pd

n = 200_000
rng = np.random.default_rng(42)
df = pd.DataFrame({
    "segment": rng.integers(0, 8, size=n),
    "spend": rng.random(n) * 100.0,
    "items": rng.integers(1, 12, size=n),
})
t0 = time.perf_counter()
summary = df.groupby("segment", as_index=False)[["spend", "items"]].mean()
t_pandas = time.perf_counter() - t0
print("Stock pandas groupby on", n, "rows:", f"{t_pandas:.4f}s")
print(summary.head())
print()
print("Syllabus Pandas accelerator:")
print("    pip install modin")
print("    import modin.pandas as pd   # same DataFrame API, cores split the work")
print("oneDAL/sklearnex still wants a numeric NumPy array for .fit():")
print("    X = np.ascontiguousarray(df[['spend','items']].to_numpy(), dtype=np.float32)")
try:
    import modin.pandas as mpd  # noqa: F401
    print("Modin is already installed in this kernel.")
except Exception:
    print("Modin not installed in this kernel (expected on Colab). Remember the import for MCQs.")
'''))

cells.append(code('''show_mcqs("MCQ after Pandas cell — Topic A (optimized Pandas)", [
  {"q":"Intel AI Analytics Toolkit drop-in for Pandas is:","choices":["import intel.pandas","import modin.pandas as pd","import onedal.pandas","import sklearnex.pandas"],"k":1,"why":"Intel Distribution of Modin. Same API, partitioned execution."},
  {"q":"Why is stock Pandas often one-core?","choices":["DataFrames cannot use RAM","Many pandas ops are single-threaded Python/Cython","Xeon blocks pandas","You forgot MPI"],"k":1,"why":"That is why the syllabus lists Optimized Pandas as a toolkit piece."},
  {"q":"oneDAL KMeans.fit needs:","choices":["A pandas Styler","Numeric contiguous ndarray (float32/64), not raw strings","A JSON file","A GPU tensor"],"k":1,"why":"Encode categoricals first, then ascontiguousarray."},
  {"q":"IPEX, Neural Compressor, and Intel MPI accelerate Pandas. True?","choices":["True","False — those are PyTorch, quantization, and cluster MPI","True on Gaudi","True if SKLEARNEX_VERBOSE=INFO"],"k":1,"why":"MCQ bank Q08. Modin is the Pandas answer."},
  {"q":"We skipped pip install modin on Colab because:","choices":["Modin is illegal","Ray/Dask extras can destabilize a live class kernel; the API line is still required knowledge","Pandas cannot groupby","oneDAL includes Pandas"],"k":1,"why":"Stay on sklearnex+NumPy for timed labs; still teach the Modin import."}
])
'''))

cells.append(md("""## Topic B / Module B1–B4 — K-Means with `patch_sklearn`
Unpatch → stock timing → `safe_patch("KMeans")` → re-import → Intel timing → inertia parity.
If Colab has no AVX-512, speedup can be modest. **Parity is the pass.**
"""))

cells.append(code(r'''import time
import numpy as np
from sklearn.datasets import make_blobs

print("Generating 500,000 samples for K-Means...")
X_km, _ = make_blobs(n_samples=500_000, n_features=10, centers=8, random_state=42)
X_km = np.ascontiguousarray(X_km, dtype=np.float64)

unpatch_sklearn()
StockKMeans = fresh_class("sklearn.cluster", "KMeans")
print(f"1. Stock KMeans module: {StockKMeans.__module__}")
km_stock = StockKMeans(n_clusters=8, init="k-means++", n_init=3, max_iter=100, random_state=42)
t0 = time.perf_counter()
km_stock.fit(X_km)
t_km_stock = time.perf_counter() - t0
inertia_stock = float(km_stock.inertia_)
print(f"   stock time={t_km_stock:.3f}s  inertia={inertia_stock:,.1f}")

safe_patch("KMeans")
IntelKMeans = fresh_class("sklearn.cluster", "KMeans")
print(f"2. Intel KMeans module: {IntelKMeans.__module__}")
km_intel = IntelKMeans(n_clusters=8, init="k-means++", n_init=3, max_iter=100, random_state=42)
t0 = time.perf_counter()
km_intel.fit(X_km)
t_km_intel = time.perf_counter() - t0
inertia_intel = float(km_intel.inertia_)
print(f"   intel time={t_km_intel:.3f}s  inertia={inertia_intel:,.1f}")

km_speedup = t_km_stock / max(t_km_intel, 1e-9)
inertia_diff_pct = abs(inertia_stock - inertia_intel) / max(inertia_stock, 1e-9) * 100.0
print("=" * 66)
print(f"K-MEANS speedup={km_speedup:.2f}x  inertia delta={inertia_diff_pct:.4f}%")
print("=" * 66)
assert inertia_diff_pct < 1.0, "Inertia drifted too far - check patch/import order"
'''))

cells.append(code('''show_mcqs("MCQ after K-Means — Topic B", [
  {"q":"Minimum code to accelerate sklearn?","choices":["Rename .fit to .fit_intel","from sklearnex import patch_sklearn; patch_sklearn() BEFORE estimator imports","Recompile sklearn with icx","Inherit IntelEstimatorBase"],"k":1,"why":"Two lines. Zero API change."},
  {"q":"patch_sklearn works by:","choices":["Editing .pyc on disk","Monkey-patching sys.modules / sklearn class slots with oneDAL wrappers","ptrace","Starting Docker"],"k":1,"why":"That is why a stale `from sklearn.cluster import KMeans` stays stock."},
  {"q":"Why call unpatch_sklearn() before the stock timer?","choices":["To delete NumPy","So this kernel is not still patched from a previous cell","To enable AVX","To mount Drive"],"k":1,"why":"Same process A/B test."},
  {"q":"oneDAL K-Means is fast mainly because:","choices":["It guesses clusters randomly in one pass","AVX distance + OpenMP assignment + cache-tiled centroids, same Lloyd math","It uses 8-bit clusters","It writes swap"],"k":1,"why":"Speed is not a cheaper algorithm."},
  {"q":"Pass condition if Colab speedup is only 3x?","choices":["Fail the student","Inertia nearly matches; record the speedup you actually got","Restart until 25x","Switch to TensorFlow"],"k":1,"why":"VM SIMD and N amortize overhead. Parity is the academic bar."}
])
'''))

cells.append(md("""## Topic B — Random Forest (fraud-style tabular)
"""))

cells.append(code(r'''import time
import numpy as np
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score

print("Generating 100,000 samples for Random Forest...")
X_rf, y_rf = make_classification(
    n_samples=100_000, n_features=20, n_informative=15, n_redundant=5,
    weights=[0.97, 0.03], random_state=42,
)
X_rf = np.ascontiguousarray(X_rf, dtype=np.float32)
X_rf_train, X_rf_test, y_rf_train, y_rf_test = train_test_split(
    X_rf, y_rf, test_size=0.2, random_state=42
)

unpatch_sklearn()
StockRF = fresh_class("sklearn.ensemble", "RandomForestClassifier")
print(f"1. Stock RF module: {StockRF.__module__}")
rf_stock = StockRF(n_estimators=80, max_depth=12, n_jobs=-1, random_state=42)
t0 = time.perf_counter()
rf_stock.fit(X_rf_train, y_rf_train)
t_rf_stock = time.perf_counter() - t0
auc_stock = roc_auc_score(y_rf_test, rf_stock.predict_proba(X_rf_test)[:, 1])
print(f"   stock time={t_rf_stock:.3f}s  AUC={auc_stock:.4f}")

safe_patch("RandomForestClassifier")
IntelRF = fresh_class("sklearn.ensemble", "RandomForestClassifier")
print(f"2. Intel RF module: {IntelRF.__module__}")
rf_intel = IntelRF(n_estimators=80, max_depth=12, n_jobs=-1, random_state=42)
t0 = time.perf_counter()
rf_intel.fit(X_rf_train, y_rf_train)
t_rf_intel = time.perf_counter() - t0
auc_intel = roc_auc_score(y_rf_test, rf_intel.predict_proba(X_rf_test)[:, 1])
print(f"   intel time={t_rf_intel:.3f}s  AUC={auc_intel:.4f}")

rf_speedup = t_rf_stock / max(t_rf_intel, 1e-9)
auc_delta = abs(auc_stock - auc_intel)
print("=" * 66)
print(f"RF speedup={rf_speedup:.2f}x  AUC delta={auc_delta:.5f}")
print("=" * 66)
assert auc_delta < 0.03, "AUC mismatch too large"
'''))

cells.append(code('''show_mcqs("MCQ after Random Forest — Topic B", [
  {"q":"Stock sklearn n_jobs=-1 often uses joblib processes. That costs:","choices":["Nothing","pickle/IPC and RAM copies because of the GIL","Extra AVX registers","GPU memory"],"k":1,"why":"oneDAL trees use OpenMP threads after dropping the GIL."},
  {"q":"oneDAL RF speedup mechanism?","choices":["Train 1 tree and copy it","Histogram binning + OpenMP split finding","Max depth forced to 3","8-bit labels"],"k":1,"why":"Same ensemble API."},
  {"q":"Weights 0.97 / 0.03 in make_classification simulate:","choices":["Balanced ImageNet","Imbalanced fraud (mostly legit)","MPI ranks","AVX lanes"],"k":1,"why":"Lab 3 story. Metric is ROC-AUC, not raw accuracy."},
  {"q":"If patch is called AFTER `from sklearn.ensemble import RandomForestClassifier`:","choices":["The old name auto-upgrades","The bound name stays stock","SyntaxError","sklearn uninstalls"],"k":1,"why":"fresh_class / re-import after patch is required."},
  {"q":"Acceptable AUC delta stock vs Intel?","choices":["25%","about 0.005–0.03, not a different model","AUC must be exactly 1.0","Intel must be worse"],"k":1,"why":"IEEE-ish parity; parallel reduction order can move ulps."}
])
'''))

cells.append(md("""## Topic B — PCA (dimensionality reduction / oneMKL SVD path)
"""))

cells.append(code(r'''import time
import numpy as np

print("Generating 250,000 x 50 matrix for PCA...")
rng = np.random.default_rng(42)
latent = rng.standard_normal((250_000, 10)).astype(np.float32)
mixing = rng.standard_normal((10, 50)).astype(np.float32)
X_pca = np.ascontiguousarray(latent @ mixing + 0.1 * rng.standard_normal((250_000, 50)).astype(np.float32))

def fit_pca(label):
    PCA = fresh_class("sklearn.decomposition", "PCA")
    print(f"{label} module: {PCA.__module__}")
    # sklearnex may ignore svd_solver; default is the portable choice if 'full' errors.
    try:
        model = PCA(n_components=10, svd_solver="full", random_state=42)
    except TypeError:
        model = PCA(n_components=10, random_state=42)
    t0 = time.perf_counter()
    model.fit(X_pca)
    dt = time.perf_counter() - t0
    var = float(np.sum(model.explained_variance_ratio_))
    print(f"   time={dt:.3f}s  explained={var:.4f}")
    return dt, var

unpatch_sklearn()
t_pca_stock, var_stock = fit_pca("1. Stock PCA")
safe_patch("PCA")
t_pca_intel, var_intel = fit_pca("2. Intel PCA")
pca_speedup = t_pca_stock / max(t_pca_intel, 1e-9)
var_delta = abs(var_stock - var_intel)
print("=" * 66)
print(f"PCA speedup={pca_speedup:.2f}x  variance delta={var_delta:.6f}")
print("=" * 66)
assert var_delta < 1e-3
'''))

cells.append(code('''show_mcqs("MCQ after PCA — Topic B", [
  {"q":"PCA in the toolkit is accelerated mainly via:","choices":["oneDNN convolutions","oneMKL LAPACK SVD / covariance in oneDAL","OpenVINO tokenizers","MPI_Scatter"],"k":1,"why":"Dimensionality reduction is classical ML (oneDAL), not deep learning."},
  {"q":"After patch, the method name for projection is:","choices":["pca.onedal_project","pca.transform (same sklearn API)","pca.accelerated_transform","pca.fit_and_project_intel"],"k":1,"why":"Zero API change."},
  {"q":"np.ascontiguousarray(..., float32) helps because:","choices":["It compresses to JPEG","C-order packed floats feed SIMD; float32 doubles AVX density vs float64","It enables CUDA","It turns on Modin"],"k":1,"why":"oneDAL wants contiguous numeric buffers."},
  {"q":"If an estimator hyperparameter is unsupported, sklearnex:","choices":["Crashes with IntelAccelerationError","Silently returns zeros","Falls back to stock sklearn","Deletes the DataFrame"],"k":2,"why":"Robust fallback. SKLEARNEX_VERBOSE=INFO shows it."},
  {"q":"Which estimator is NOT in the sklearnex accelerated set?","choices":["PCA","RandomForestClassifier","SVC","BayesianGaussianMixture"],"k":3,"why":"Quiz trap from the MCQ bank."}
])
'''))

cells.append(md("""## Topic B / Module B5 — Selective patch (Lab 5)
Patch only KMeans and PCA. RandomForest must stay stock. Then `unpatch_sklearn()`.
"""))

cells.append(code(r'''unpatch_sklearn()
K0 = fresh_class("sklearn.cluster", "KMeans")
RF0 = fresh_class("sklearn.ensemble", "RandomForestClassifier")
print("Before selective patch:")
print("  KMeans", K0.__module__)
print("  RF    ", RF0.__module__)

try:
    patch_sklearn(name=["sklearn.cluster.KMeans", "sklearn.decomposition.PCA"], verbose=False)
except Exception:
    patch_sklearn(name=["KMeans", "PCA"], verbose=False)

K1 = fresh_class("sklearn.cluster", "KMeans")
P1 = fresh_class("sklearn.decomposition", "PCA")
RF1 = fresh_class("sklearn.ensemble", "RandomForestClassifier")
print("After selective patch:")
print("  KMeans", K1.__module__)
print("  PCA   ", P1.__module__)
print("  RF    ", RF1.__module__)

def is_intel(mod):
    return ("sklearnex" in mod) or ("daal4py" in mod) or ("onedal" in mod)

assert is_intel(K1.__module__), "KMeans should be patched"
assert is_intel(P1.__module__), "PCA should be patched"
assert not is_intel(RF1.__module__), "RF should remain stock"
unpatch_sklearn()
K2 = fresh_class("sklearn.cluster", "KMeans")
assert not is_intel(K2.__module__), "unpatch failed"
print("Selective patch + unpatch assertions passed.")
'''))

cells.append(code('''show_mcqs("MCQ after selective patch — Topic B", [
  {"q":"Correct selective call?","choices":["patch_sklearn(only=['KMeans'])","patch_sklearn(name=['KMeans', 'PCA'])","sklearnex.enable_specific(...)","patch_sklearn(filter=KMeans)"],"k":1,"why":"Argument is name=. New wheels may want fully-qualified strings; this cell tries both."},
  {"q":"python -m sklearnex train.py means:","choices":["Compile C++","Patch then run a legacy script with zero source edits","Start Slurm","Enable CUDA"],"k":1,"why":"sklearnex __main__."},
  {"q":"unpatch_sklearn() requires a kernel restart. True?","choices":["True","False — it restores stock classes in this process"],"k":1,"why":"That is how A/B benches work."},
  {"q":"SKLEARNEX_VERBOSE=INFO prints:","choices":["Disk SMART data","Whether oneDAL ran or fell back","MPI ranks","Gaudi temperature"],"k":1,"why":"Cheat-sheet knob."},
  {"q":"Sparse csr_matrix on an estimator without a sparse oneDAL kernel:","choices":["Always densifies to 100 GB","Crashes","Falls back to stock sparse sklearn","Converts values to 1.0"],"k":2,"why":"MCQ bank Q24."}
])
'''))

cells.append(md("""## Topic B / Module B5 Lab 6 — Pipeline: StandardScaler + PCA + KNN
Same sklearn `Pipeline` API. Global `patch_sklearn()`. Compare fit time and accuracy.
"""))

cells.append(code(r'''import time
import numpy as np
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score

X, y = make_classification(
    n_samples=40_000, n_features=40, n_informative=25, n_classes=8, random_state=42
)
X = np.ascontiguousarray(X, dtype=np.float32)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=4000, random_state=42)

def make_pipe():
    StandardScaler = fresh_class("sklearn.preprocessing", "StandardScaler")
    PCA = fresh_class("sklearn.decomposition", "PCA")
    KNN = fresh_class("sklearn.neighbors", "KNeighborsClassifier")
    return Pipeline([
        ("scaler", StandardScaler()),
        ("pca", PCA(n_components=12, random_state=42)),
        ("knn", KNN(n_neighbors=5)),
    ])

unpatch_sklearn()
pipe_stock = make_pipe()
t0 = time.perf_counter()
pipe_stock.fit(X_train, y_train)
t_pipe_stock = time.perf_counter() - t0
acc_stock = accuracy_score(y_test, pipe_stock.predict(X_test))
print(f"Stock pipeline fit {t_pipe_stock:.3f}s  acc={acc_stock:.4f}")

patch_sklearn(verbose=False)
pipe_intel = make_pipe()
t0 = time.perf_counter()
pipe_intel.fit(X_train, y_train)
t_pipe_intel = time.perf_counter() - t0
acc_intel = accuracy_score(y_test, pipe_intel.predict(X_test))
print(f"Intel pipeline fit {t_pipe_intel:.3f}s  acc={acc_intel:.4f}")
pipe_speedup = t_pipe_stock / max(t_pipe_intel, 1e-9)
acc_delta = abs(acc_stock - acc_intel)
print(f"Pipeline speedup={pipe_speedup:.2f}x  acc delta={acc_delta:.4f}")
assert acc_delta < 0.05
unpatch_sklearn()
'''))

cells.append(code('''show_mcqs("MCQ after pipeline — Topic B", [
  {"q":"Do you rewrite Pipeline step class names for Intel?","choices":["Yes, IntelScaler","No — patch then the same StandardScaler/PCA/KNN names","Yes, onedal.Pipeline","Only KNN changes"],"k":1,"why":"Zero-code-change is the product."},
  {"q":"KNN in oneDAL is faster mainly due to:","choices":["Fewer neighbors forced to 1","Vectorized distances / parallel queries","Approximate hashing that changes labels a lot","GPU only"],"k":1,"why":"Lab 6 story: batch scoring."},
  {"q":"Best order in a notebook cell?","choices":["import KMeans; patch_sklearn()","patch or unpatch; then fresh import of estimators; then fit","fit; then patch","pip after fit"],"k":1,"why":"Binding order is the #1 gotcha."},
  {"q":"oneDAL vs oneDNN?","choices":["Identical","oneDAL=classical ML (this notebook); oneDNN=deep nets (Day 3)","oneDAL is ARM-only","oneDNN is today's lab"],"k":1,"why":"Do not mix names on Day 2."},
  {"q":"Production takeaway for this afternoon?","choices":["Rewrite all ML in MPI C++","Keep sklearn Python; patch into oneDAL on Xeon for tabular/clustering","Buy a GPU or nothing works","Use OpenVINO for KMeans"],"k":1,"why":"That is the Day 2 afternoon learning outcome."}
])
'''))

cells.append(md("""## Topic B / Module B4 — Chart the three main speedups
Saves under the workspace `reports/` path (Colab or local).
"""))

cells.append(code(r'''import matplotlib.pyplot as plt
import numpy as np

algorithms = ["K-Means (500k)", "Random Forest (100k)", "PCA (250k)"]
stock_times = [t_km_stock, t_rf_stock, t_pca_stock]
intel_times = [t_km_intel, t_rf_intel, t_pca_intel]
speedups = [km_speedup, rf_speedup, pca_speedup]

x = np.arange(len(algorithms))
width = 0.35
style = "seaborn-v0_8-whitegrid" if "seaborn-v0_8-whitegrid" in plt.style.available else "default"
plt.style.use(style)
fig, ax = plt.subplots(figsize=(10, 6), dpi=120)
r1 = ax.bar(x - width/2, stock_times, width, label="Stock sklearn", color="#d9534f")
r2 = ax.bar(x + width/2, intel_times, width, label="Intel oneDAL", color="#0071c5")
ax.set_ylabel("Seconds (lower is better)")
ax.set_title("Day 2 afternoon - stock sklearn vs sklearnex/oneDAL")
ax.set_xticks(x)
ax.set_xticklabels(algorithms)
ax.legend()
for a, b, sp in zip(r1, r2, speedups):
    ax.annotate(f"{a.get_height():.2f}s", xy=(a.get_x()+a.get_width()/2, a.get_height()),
                xytext=(0, 3), textcoords="offset points", ha="center", fontsize=9)
    ax.annotate(f"{b.get_height():.2f}s\n{sp:.1f}x", xy=(b.get_x()+b.get_width()/2, b.get_height()),
                xytext=(0, 3), textcoords="offset points", ha="center", fontsize=9)
fig.tight_layout()
out = REPORTS_DIR / "intel_ai_analytics_benchmark.png"
fig.savefig(out, dpi=150, bbox_inches="tight")
print("Saved", out.resolve())
try:
    plt.show()
except Exception:
    plt.close(fig)
'''))

cells.append(code('''show_mcqs("MCQ after chart — wrap Topic A+B", [
  {"q":"Where did the PNG go on Colab?","choices":["Google Drive root","/content/hpc_intel_analytics_workspace/reports/","/mnt/c only","Nowhere"],"k":1,"why":"WORKSPACE_DIR branch set in cell 1."},
  {"q":"Deck proof numbers (K-Means ~25x, RF ~13x) are:","choices":["Guaranteed on every Colab","Measured on a fat AVX-512 node; your VM will differ; still plot YOUR times","Fake","GPU-only"],"k":1,"why":"Teach the method, not a magic multiplier."},
  {"q":"Optimized NumPy, Pandas, Scikit-learn map to:","choices":["oneMKL, Modin, oneDAL/sklearnex","oneDNN, Horovod, OpenVINO","Slurm, VTune, Gaudi","OpenMP C++, MPI C++, CUDA"],"k":0,"why":"That is Topic A in one sentence."},
  {"q":"Topic B in one sentence:","choices":["Write CUDA kernels","patch_sklearn() redirects sklearn to oneDAL C++","Fine-tune LLMs","sbatch a job"],"k":1,"why":"Two-line patch."},
  {"q":"Tomorrow (Day 3) starts with:","choices":["More KMeans","Deep learning: TensorFlow-MKL / oneDNN — not today","OpenVINO LLMs","False sharing labs again"],"k":1,"why":"Stop at the syllabus line."}
])
'''))

cells.append(md("""## Done
You covered **only** Day 2 afternoon syllabus:

| Topic | What you ran |
|---|---|
| A Toolkit | Env + paths, SIMD/BLAS, NumPy DGEMM, Pandas/Modin name, workspace |
| B sklearnex | KMeans, RandomForest, PCA, selective patch, Pipeline, chart |

Trainer: keep `AFTERNOON_CLASSROOM_KIT/classroom.html` on the projector (slide vs animation per module). This notebook is the student half.
"""))

nb["cells"] = cells
text = json.dumps(nb, indent=1)
print("cells", len(cells), "bytes", len(text))

root = Path(r"c:\Users\Rose\Videos\GLA Trainings")
targets = [
    root / r"HPC_Master_Curriculum\Day-02_Parallel_OpenMP_MPI_oneDAL\INTEL_AI_ANALYTICS_AND_ACCELERATED_ML_TRAINING_MODULE\Day_02_Intel_AI_Analytics_and_Accelerated_ML_Colab.ipynb",
    root / r"HPC_Master_Curriculum\Day-02_Parallel_OpenMP_MPI_oneDAL\Day_02_Intel_AI_Analytics_and_Accelerated_ML_Colab.ipynb",
    root / r"HPC_Master_Curriculum\Day-02_Parallel_OpenMP_MPI_oneDAL\lab_activities\Day_02_Intel_AI_Analytics_and_Accelerated_ML_Colab.ipynb",
    root / r"COLAB_NOTEBOOKS\Day_02_Intel_AI_Analytics_and_Accelerated_ML_Colab.ipynb",
]
for t in targets:
    t.parent.mkdir(parents=True, exist_ok=True)
    t.write_text(text, encoding="utf-8")
    print("wrote", t)

"""
离线下载 Stanza 中文模型（在能联网的机器上运行）

用法: python download_stanza_models.py

会下载以下文件到当前目录下的 stanza_models/ 文件夹:
  - resources.json
  - zh/tokenize/  (分词模型)
  - zh/pos/       (词性标注模型)
  - zh/ner/       (命名实体识别模型)

下载完成后，将 stanza_models/ 整个文件夹复制到离线机器的合适位置，
然后在离线机器上运行 demo 脚本即可。
"""

import os, sys, requests, zipfile
from pathlib import Path

# 如果在中国网络环境，可取消下面两行的注释来使用镜像
# os.environ["STANZA_RESOURCES_URL"] = "https://raw.staticdn.net/stanfordnlp/stanza-resources/main"
# os.environ["HF_ENDPOINT"] = "https://hf-mirror.com"

MODEL_DIR = Path(__file__).parent / "stanza_models"
MODEL_DIR.mkdir(parents=True, exist_ok=True)

# 1. 下载 resources.json
resources_url = os.environ.get(
    "STANZA_RESOURCES_URL",
    "https://raw.githubusercontent.com/stanfordnlp/stanza-resources/main"
)
print("==> 下载 resources.json ...")
url = f"{resources_url}/resources_1.13.0.json"
r = requests.get(url, timeout=60)
r.raise_for_status()
resources_path = MODEL_DIR / "resources.json"
resources_path.write_text(r.text, encoding="utf-8")
print(f"    OK -> {resources_path}")

# 2. 下载中文模型包（default.zip）
lang = "zh"
hf_endpoint = os.environ.get("HF_ENDPOINT", "https://huggingface.co")
hf_url = f"{hf_endpoint}/stanfordnlp/stanza-{lang}/resolve/v1.13.0/models/default.zip"
print(f"\n==> 下载中文模型包 -> {hf_url}")
r = requests.get(hf_url, timeout=300)
r.raise_for_status()

dest_dir = MODEL_DIR / lang
dest_dir.mkdir(parents=True, exist_ok=True)
zip_path = dest_dir / "default.zip"
zip_path.write_bytes(r.content)

with zipfile.ZipFile(zip_path, "r") as zf:
    zf.extractall(dest_dir)
zip_path.unlink()

# 3. 验证
print(f"\n==> 下载完成！目录结构：{MODEL_DIR}")
for f in sorted(MODEL_DIR.rglob("*")):
    if f.is_file():
        rel = f.relative_to(MODEL_DIR)
        size = f.stat().st_size
        print(f"    {rel} ({size:,} bytes)")

print(f"\n=== 下载完毕 ===")
print(f"请将 {MODEL_DIR} 文件夹复制到离线机器上")
print(f"然后修改 stanza_demo.py 中的 STANZA_RESOURCES_DIR 路径")

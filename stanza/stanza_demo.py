import os
os.environ["STANZA_RESOURCES_DIR"] = os.path.join(os.environ["TEMP"], "stanza_resources")
os.environ["STANZA_RESOURCES_URL"] = "https://raw.githubusercontent.com/stanfordnlp/stanza-resources/main"
os.environ["STANZA_MODEL_URL"] = "https://huggingface.co/stanfordnlp/stanza-{lang}/resolve/v{resources_version}/models/{filename}"
os.environ["HF_ENDPOINT"] = "https://hf-mirror.com"

import stanza
from stanza.pipeline.core import DownloadMethod

nlp = stanza.Pipeline("zh", processors="tokenize,pos,ner", download_method=DownloadMethod.NONE)
doc = nlp("北京大学位于北京市海淀区")
for sent in doc.sentences:
    for word in sent.words:
        print(f"{word.text}\t{word.upos}\t{word.ner}")

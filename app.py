import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent / "src"))

from chain import build_chain
import gradio as gr
from dotenv import load_dotenv
from chain import build_chain

import subprocess
from pathlib import Path

chroma_dir = Path(__file__).resolve().parent / "data" / "chroma"
if not chroma_dir.exists() or not any(chroma_dir.iterdir()):
    print("[app] No index found — running ingestion...")
    subprocess.run(["python", "src/ingest.py"], check=True)

load_dotenv()

print("[app] Initializing RAG chain...")
chain = build_chain()
print("[app] Ready.")

EXAMPLES = [
    "Can I prescribe metformin to a diabetic patient with stage 3 chronic kidney disease?",
    "Are there any issues with using repaglinide with clopidogrel?",
    "What complications should I consider when prescribing mirabegron to a hypertensive patient?",
    "Is oxybutynin safe to use in a patient already on anticholinergics?",
    "What CrCL threshold is considered safe for ranolazine administration?",
    "Are there drug interactions between lisinopril and potassium supplements?",
    "What are the cardiac contraindications for ziprasidone?",
    "Is Lorbrena safe to prescribe alongside CYP3A inducers?",
]


def query_rag(question: str) -> tuple[str, str, str]:
    #run question through RAG chain, returns answer,source text, metadata
    if not question or not question.strip():
        return "Please enter a question.", "", ""

    result = chain.query(question.strip(), run_grounding_check=True)

    if result["refused"]:
        answer_text = f"Query refused — insufficient retrieval confidence.\n\n{result['answer']}"
    else:
        answer_text = result["answer"]

    if not result["sources"]:
        sources_text = "No sources retrieved."
    else:
        source_lines = []
        for src in result["sources"]:
            source_lines.append(
                f"[{src['index']}] {src['drug_name']} — {src['section']}\n"
                f"    Relevance score: {src['rerank_score']:.4f}\n"
                f"    Preview: {src['text_preview']}\n"
            )
        sources_text = "\n".join(source_lines)

    meta = result["metadata"]
    meta_lines = []

    if meta.get("reformulated_queries"):
        meta_lines.append("Query variants generated:")
        for q in meta["reformulated_queries"]:
            meta_lines.append(f"  • {q}")

    meta_lines.append(f"\nChunks retrieved: {meta.get('num_chunks_retrieved', 0)}")
    meta_lines.append(f"Top rerank score: {meta.get('top_rerank_score', 0):.4f}")
    meta_lines.append(f"Refused: {result['refused']}")

    metadata_text = "\n".join(meta_lines)

    return answer_text, sources_text, metadata_text

with gr.Blocks(title="FDA Drug Label RAG") as demo:

    gr.Markdown("""
# FDA Drug Label Clinical Query System

Query FDA-approved drug labels using natural language.
Designed to support clinical prescribing decisions by surfacing
contraindications, warnings, drug interactions, and dosing considerations.

**Use case:** A clinician wants to prescribe drug A to a patient with condition B.
Rather than manually cross-referencing a 40-page label PDF, they query this system
for a cited, grounded answer drawn directly from the official FDA label.

> **Disclaimer:** This system is a research prototype for portfolio demonstration.
> It is not intended for clinical use. Always consult official prescribing information
> and clinical judgment before making prescribing decisions.
    """)

    with gr.Row():
        with gr.Column(scale=2):
            question_input = gr.Textbox(
                label="Clinical question",
                placeholder="e.g. Can I prescribe metformin to a patient with stage 3 CKD?",
                lines=3,
            )
            submit_btn = gr.Button("Submit", variant="primary")
            gr.Examples(
                examples=EXAMPLES,
                inputs=question_input,
                label="Example queries",
            )

    with gr.Row():
        with gr.Column(scale=2):
            answer_output = gr.Textbox(
                label="Answer",
                lines=12,
                interactive=False,
            )
        with gr.Column(scale=1):
            sources_output = gr.Textbox(
                label="Retrieved sources",
                lines=12,
                interactive=False,
            )

    with gr.Row():
        metadata_output = gr.Textbox(
            label="Query metadata",
            lines=6,
            interactive=False,
        )

    submit_btn.click(
        fn=query_rag,
        inputs=question_input,
        outputs=[answer_output, sources_output, metadata_output],
    )

    question_input.submit(
        fn=query_rag,
        inputs=question_input,
        outputs=[answer_output, sources_output, metadata_output],
    )

    gr.Markdown("""
---
**Architecture:** LangGraph query reformulation → Hybrid retrieval (ChromaDB + BM25) →
RRF fusion → Cross-encoder reranking → Groq Llama 3.3 70B generation

**Eval results:** Faithfulness 0.91 · Answer relevancy 0.88 · Context recall 0.65

**Corpus:** 1,000 FDA drug labels via openFDA API · ~22,000 indexed chunks
    """)


if __name__ == "__main__":
    demo.launch()
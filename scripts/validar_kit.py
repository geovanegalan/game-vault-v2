"""Verifica estrutura documental; não executa testes da aplicação."""
from pathlib import Path
import re

root = Path(__file__).resolve().parents[1]
required = ["AGENTS.md", "README.md", "docs/00-contexto.md", "docs/STATUS.md",
            "docs/decisoes/REGISTRO.md", "prompts/INICIO-CODEX.md",
            "docs/AMBIENTE.md", "docs/ambiente/DIAGNOSTICO.md",
            "docs/modelos/PLANO-AMBIENTE.md", "docs/modelos/COMPARACAO-STACK.md"]
errors = []
for name in required:
    path = root / name
    if not path.is_file() or not path.read_text(encoding="utf-8").strip():
        errors.append(f"Arquivo ausente ou vazio: {name}")
for name in ["gv-ambiente", "gv-entrevista", "gv-planejamento", "gv-implementacao-guiada", "gv-code-review"]:
    path = root / ".agents" / "skills" / name / "SKILL.md"
    if not path.is_file():
        errors.append(f"Skill ausente: {name}")
        continue
    text = path.read_text(encoding="utf-8")
    match = re.match(r"\A---\n(.*?)\n---\n", text, re.S)
    if not match:
        errors.append(f"Frontmatter ausente: {name}")
        continue
    fields = dict(line.split(":", 1) for line in match[1].splitlines() if ":" in line)
    if fields.get("name", "").strip() != name or not fields.get("description", "").strip():
        errors.append(f"Metadados inválidos: {name}")
if errors:
    raise SystemExit("\n".join(errors))
print("OK: bootstrap documental e cinco skills presentes. Produto não testado.")

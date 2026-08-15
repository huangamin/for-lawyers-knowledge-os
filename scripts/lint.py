# -*- coding: utf-8 -*-
"""
Knowledge OS Lint（结构检查 + 内容四查）
用法: python lint.py [VAULT_PATH]
环境变量 VAULT_PATH 或命令行参数指定知识库根目录。
只读扫描，不修改任何文件。
"""
import os, re, sys, datetime, glob

VAULT = os.environ.get("VAULT_PATH") or (sys.argv[1] if len(sys.argv) > 1 else "")
if not VAULT or not os.path.isdir(VAULT):
    print("请通过环境变量 VAULT_PATH 或参数指定知识库路径")
    sys.exit(2)

SKILL_DIR = os.path.join(VAULT, "_Skill工作区")
issues = []


def md_files():
    for dp, dn, fn in os.walk(VAULT):
        dn[:] = [d for d in dn if d not in (".obsidian", ".git", "node_modules")]
        for f in fn:
            if f.lower().endswith(".md"):
                yield os.path.join(dp, f)


def read(path):
    with open(path, encoding="utf-8") as fh:
        return fh.read()


def frontmatter(text):
    if text.startswith("---"):
        end = text.find("\n---", 3)
        if end > 0:
            return text[3:end]
    return ""


def main():
    print(f"== Lint: {VAULT} ==")
    files = list(md_files())
    rels = [os.path.relpath(p, VAULT).replace("\\", "/") for p in files]
    names = {os.path.splitext(os.path.basename(p))[0] for p in files}
    print(f"md 总数: {len(files)}")

    # 1. 结构检查
    for p, rel in zip(files, rels):
        if rel.startswith("_Skill工作区/"):
            continue
        text = read(p)
        fm = frontmatter(text)
        if "maturity" not in fm:
            issues.append(f"[结构] 缺 maturity: {rel}")
        if not fm:
            issues.append(f"[结构] 缺 frontmatter: {rel}")
        if "[[CLAUDE.md]]" in text or "[[知识库总控台" in text:
            pass
        # 无外链（仅 frontmatter 文件）提示
        if len(re.findall(r"\[\[", text)) == 0:
            issues.append(f"[结构] 无双向链接: {rel}")

    # 2. 内容三查（启发式）
    today = datetime.date.today().isoformat()
    for p, rel in zip(files, rels):
        text = read(p)
        for m in re.finditer(r"review_after:\s*([\d-]+)", text):
            if m.group(1) < today:
                issues.append(f"[治理] review_after 已到期: {rel} ({m.group(1)})")
        if re.search(r"（V1\.\d）|V1\.\d", text):
            pass  # 版本号一致性由治理检查处理

    # 3. 治理文件同步检查
    gf = os.path.join(SKILL_DIR, "知识库搭建规范.md")
    sf = os.path.join(SKILL_DIR, "Codex 进化治理与法学类比说明书.md")
    if os.path.exists(gf) and os.path.exists(sf):
        gt = read(gf)
        st = read(sf)
        gv = re.search(r"（V([\d.]+)）", gt)
        if gv:
            ver = gv.group(1)
            for label, line in [("第一节", "知识库搭建规范.md`（V"), ("第三节", "| L1 | `知识库搭建规范.md`")]:
                for l in st.splitlines():
                    if line in l and f"V{ver}" not in l:
                        issues.append(f"[治理] 说明书{label}版本漂移（规范 V{ver}）")
                        break
        # 变动记录比对：说明书第四节 vs log 最近规则操作
        logf = os.path.join(SKILL_DIR, "wiki", "log.md")
        if os.path.exists(logf):
            lt = read(logf)
            last_log = [l for l in lt.splitlines() if l.startswith("| 2026")]
            last_sf = [l for l in st.splitlines() if l.startswith("| 2026")]
            if last_log and last_sf:
                if last_log[-1][:11] != last_sf[-1][:11]:
                    issues.append("[治理] 说明书变动记录未同步 log 最近规则操作")

    # 4. 报告
    if issues:
        print(f"发现 {len(issues)} 个问题：")
        for it in issues:
            print(" -", it)
        sys.exit(1)
    print("✅ 未发现问题")


if __name__ == "__main__":
    main()

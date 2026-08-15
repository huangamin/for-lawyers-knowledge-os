# for-lawyers-knowledge-os —— 法学生的知识库搭建手册

以"法秩序"思维搭建与治理 Obsidian 知识库（Knowledge OS）的可复用 Codex Skill。

## 这是什么

一套经过真实知识库验证的建库方法论，包含：

- **宪法层**（CLAUDE.md 模板）：共同进化、核心元原则、maturity 闸门、update-in-place；
- **法律层**（搭建规范模板）：板块分类路由、摄入/编译/回写/体检流程、规则治理、统一元数据；
- **治理地图**（治理说明书模板）：L0–L5 规则位阶、压缩优先 6 查、废止制度、变动记录同步义务；
- **驾驶舱**（总控台模板）：Dataview 动态面板 + 静态快照；
- **SOP**（多设备同步模板）：单一 Source of Truth、新电脑 14 步接入；
- **Lint 脚本**：结构检查 + 内容四查（含治理文件同步检查）。

## 安装

方式 A（复制）：把本仓库克隆/下载后，将内容复制到 `~/.codex/skills/for-lawyers-knowledge-os/`。

方式 B（skill-installer）：在 Codex 中执行 `skill-installer install for-lawyers-knowledge-os`。

## 快速开始

1. 新建 Obsidian Vault；
2. 按 `references/CLAUDE.md.template` 创建 `CLAUDE.md`，按 `references/知识库搭建规范.template` 创建规范，按 `references/治理说明书.template` 创建说明书；
3. 按 `references/总控台.template` 创建总控台；
4. 对 Codex 说"摄入 xxx 资料" / "lint 一下"，即按本 skill 的流程执行。

## 目录

```text
SKILL.md                          # 技能入口
METHODOLOGY_REPORT.md             # 方法论提取报告（来源/体系/泛化/排除）
references/                       # 通用模板（宪法/规范/说明书/总控台/SOP/页面模板）
scripts/lint.py                   # Lint 脚本（四查）
docs/                             # 实际工作文档（参考实现）
README.md
```

## 隐私与边界

本仓库只含通用建库方法论；不含任何个人/组织业务内容。`docs/` 为方法论来源文档（含 <知识库名称> 特有内容，仅供理解结构，请勿原样用于他处）。

---
name: for-lawyers-knowledge-os
description: 以法学式规则位阶（宪法—法律—SOP—案例—证据）搭建并治理 Obsidian 知识库（LLM Wiki / Knowledge OS）。读取目标库的 CLAUDE.md 执行操作，支持 Store/Ingest/Query/Archive/Lint（四查）、规则账本、maturity 闸门、多设备同步。用于"搭建知识库""摄入/整理资料""知识库体检""规则治理""多设备接入"等场景。
version: 0.1.0
triggers:
  - 搭建知识库
  - Knowledge OS
  - 知识库治理
  - 摄入
  - ingest
  - 知识库体检
  - lint
  - 规则位阶
  - 多设备同步知识库
  - 新电脑接入知识库
---

# for-lawyers-knowledge-os —— 法学生的知识库搭建手册

> 以"法秩序"的思维搭建和治理个人/组织知识库：上位约束下位、修改优先于堆叠、规则可废止。核心目标是让知识库与学习/工作**共同进化**（系统进化 ≠ 知识增加；Maximum Generalization + Minimum Complexity）。

## 1. 使用前提

- 目标 Vault 已存在或待创建；需要 Obsidian（可选：Dataview 插件用于总控台动态面板）。
- 首次使用时：按 `references/CLAUDE.md.template` 创建 Vault 根目录的 `CLAUDE.md`，按 `references/知识库搭建规范.template` 创建规范，按 `references/治理说明书.template` 创建说明书——三者是本体系的宪法与法律层。
- 本 skill 通过读取目标 Vault 的 `CLAUDE.md` 执行操作；若缺失则先引导创建。

## 2. 结构总览

```text
<VAULT>/
├── 00 Inbox ~ 09 <领域>       # 内容板块（默认 10 板块，可按领域裁剪）
├── 知识库总控台.md             # 驾驶舱（动态面板 + 静态快照）
├── CLAUDE.md                  # L0 宪法层
└── _Skill工作区/
    ├── 知识库搭建规范.md        # L1 法律层
    ├── Codex 进化治理与法学类比说明书.md  # 位阶地图 + 变动记录
    ├── raw/                    # L5 证据层（只读）
    ├── wiki/                   # index / log / hot / synthesis
    ├── _templates/             # 页面模板
    └── assets/                 # 图片等附件
```

## 3. 操作流程

### Store（存到 raw）
1. 按主题放到 `<VAULT>/_Skill工作区/raw/<主题>/`（只读层，不修改）；
2. 更新 `wiki/log.md`（标注"已存储，待摄入"）；
3. 询问是否需要摄入。

### Ingest（摄入）
1. 先与用户对齐 key takeaways；
2. 读 `知识库搭建规范.md` 确定目标板块/子目录；
3. 按模板建页并融入内容序列；
4. **编译-矛盾检测**：扫描 2–5 个最相关旧页，冲突则在新页 frontmatter 标 `conflict: [[旧页]]`，判断留给用户；
5. **编译-链式更新**：受影响旧页做最小修正+反链，记入 log；
6. 更新 `wiki/index.md`、`wiki/log.md`、`wiki/hot.md`；
7. 涉及规则变动时同步《治理说明书》第四节变动记录；
8. 新页至少链 1 个已有页；maturity 默认 ≤ `💡 #hypothesis`。

### Query（查询）
1. 读 `wiki/hot.md` → `wiki/index.md` → 具体页面；
2. 综合回答并附 `[[页面]]` 引用；
3. 值得沉淀的答案经用户确认后写入 `wiki/synthesis/` 或指定板块。

### Archive（归档）
成熟内容写入 `wiki/synthesis/`，更新索引与日志。

### Lint（体检 · 四查）
1. 结构检查：孤立页、缺 maturity、缺链接、缺索引、raw 污染；
2. 内容三查：跨页矛盾 / 过期结论 / 概念缺口（≥3 处出现无独立页 → 建议建页）；
3. 治理文件同步检查：规范版本号 vs 说明书标注版本；说明书第四节 vs log 最近规则操作；`review_after` 到期扫描；
4. 只报告问题清单，用户确认后才修。

## 4. 规则治理（法学式）

- **位阶**：L0 宪法（CLAUDE.md）→ L1 法律（搭建规范）→ L2 领域（板块路由）→ L3 SOP（skill/模板）→ L4 案例 → L5 证据。
- **压缩优先 6 查**：能解释？重复？冲突？改上位？一次性？显著提升？——六问不过则不加新规则。
- **废止制度**：规则可 ACTIVE → AMENDED / MERGED / DEPRECATED / RETIRED；`review_after` 挂规则载体页 frontmatter，Lint 负责到期扫描。
- **账本最小实装**：规则数少时用页面 frontmatter 承载；超过约十几条再升级独立注册表。
- **法律严谨点**："实施细则"非我国固定法规范等级，位阶为架构类比，须在说明书中声明。

## 5. 元数据规范（页面 frontmatter）

所有页面统一字段：`type / domain / subdomain / layer（治理页必填）/ maturity（知识页必填）/ status / origin / source / parent / related_os / confidence / created / updated`。存量页下次编辑时补齐，不批量返工。

## 6. 多设备同步

见 `references/SOP-多设备同步.template`：单一 Source of Truth、新电脑 14 步接入、配置同步规则、冲突处理、备份与恢复（Sync ≠ Backup）。

## 7. 安全规则

1. 不修改 `raw/` 下任何文件的内容或文件名；
2. 不删除页面（用 archived 代替）；
3. 每次操作后更新 `wiki/index.md` 与 `wiki/log.md`；
4. 不确定信息标 `confidence: low`；
5. 涉及学生/个人隐私时只用代号；
6. 不擅自将 maturity 升级到 `#evidence` / `#protocol`；
7. 不为同一概念新建版本化页面（update-in-place）。

## 8. 安装

- 方式 A：将本目录复制到 `~/.codex/skills/for-lawyers-knowledge-os/`；
- 方式 B：用 skill-installer 从 GitHub 安装（仓库：`for-lawyers-knowledge-os`）。

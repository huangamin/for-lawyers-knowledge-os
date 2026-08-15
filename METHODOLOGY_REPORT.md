# 方法论提取报告（for-lawyers-knowledge-os）

> 本报告说明 skill 的方法论来源、体系结构、泛化处理与被排除内容。生成日期：2026-08-15。

## 1. 来源（2026-08-15 快照）

| 来源文件 | 层级 | 提取内容 |
|---|---|---|
| `<VAULT>/CLAUDE.md` | L0 宪法 | 共同进化、核心元原则、maturity 闸门、update-in-place、Agent 设计原则、Store/Ingest/Query/Archive/Lint 流程、Safety Rules |
| `<VAULT>/_Skill工作区/知识库搭建规范.md`（VX.X） | L1 法律 | 板块分类与路由、摄入/编译/回写/体检、规则治理（第 9 节）、知识元数据（第 10 节）、附件链接规则 |
| `<VAULT>/_Skill工作区/Codex 进化治理与法学类比说明书.md` | L0–L5 | 规则位阶总览、案例→规则演化、压缩优先 6 查、废止制度、账本最小实装、变动记录同步义务 |
| `<VAULT>/知识库总控台.md` | 治理工具 | 双模式总控台（Dataview 动态面板 + 静态快照）、板块/成熟度/空白区/进化状态面板 |
| `<VAULT>/_Skill工作区/_templates/*.md` | L3 SOP | 页面模板：concept / entity / source / synthesis / comparison |
| `<VAULT>/07 Operations/SOP/SOP｜Obsidian Knowledge OS 多设备同步与新电脑接入.md` | L3 SOP | 多设备同步架构、新电脑接入流程、配置同步规则、备份与恢复 |

## 2. 体系地图（L0–L5）

```text
L0 宪法层    CLAUDE.md：共同进化 · 系统进化≠知识增加 · Maximum Generalization + Minimum Complexity
             · maturity 闸门（AI 写入 ≤💡，📊/⚙️ 需用户确认）· update-in-place · 先宪法后 SOP
              ↓ 约束
L1 法律层    知识库搭建规范：分类路由 · 摄入/编译/回写/体检 · 规则治理（压缩 6 查 / 废止制度 / 账本）
              ↓ 约束
L2 领域层    板块 MOC × 10 + 路由表：Inbox / Strategy / LearningOS / Science / Curriculum / Students /
             Coaching / Operations / Growth / Research
              ↓ 约束
L3 SOP 层    五大操作 + 模板：Store / Ingest / Query / Archive / Lint（四查）
              ↓ 约束
L4 案例层    学生案例 / Decision Log：Case ≠ Rule
              ↓ 约束
L5 证据层    raw/（只读）：原始资料按主题归档，永不修改
```

进化循环：积累 → 抽象 → 合并 → 修正 → 废止 → 再评估；目标函数 = Execution Gain / Complexity Cost 最大化。
案例升级闸门：单次案例=观察 → 重复模式=候选规则 → 稳定规律=正式规则。

## 3. 核心规则的来源 / 作用 / 边界

| 规则 | 来源 | 作用 | 边界 |
|---|---|---|---|
| 共同进化 | CLAUDE.md 顶部 | 学习驱动知识库、知识库反哺学习；一切设计以此为准 | 不与具体学科内容绑定 |
| 核心元原则 | 全局规范 → 规范 9.1 | 系统进化≠知识增加；复杂度受控 | 适用于规则/流程，不约束内容创作 |
| maturity 闸门 | CLAUDE.md Conventions #2 | AI 写入默认 ≤💡，升级需用户确认+证据 | 只约束 AI 写入，用户可自行升级 |
| update-in-place | 规范 7.5 | 同一概念一页制，禁 v2；版本活在 log | raw/ 只读层与按编号分实体记录除外 |
| 分类不重不漏 | 规范（板块路由）+ 总控台 | 10 板块分类基准 | 现实允许少量重复/遗漏 |
| 摄入编译（矛盾检测+链式更新） | CLAUDE.md Ingest 4–5 | 冲突标 conflict，受影响旧页最小修正+反链 | 判断留给用户 |
| Lint 四查 | CLAUDE.md Lint（2026-08-15 审计修复） | 结构检查 + 跨页矛盾/过期结论/概念缺口 + 治理文件同步检查 | 只报告，不擅自修改 |
| 规则位阶 L0–L5 | 说明书第一节 | 上位约束下位、改上位优先于堆叠、规则可废止 | 法学类比，非现实法规范位阶（已声明） |
| 压缩优先 6 查 | 说明书 2.2 / 规范 9.4 | 新增规则前按序检查，能合并则合并 | 适用于规则治理，不约束内容摄入 |
| 废止制度 + 账本最小实装 | 说明书 2.3 / 规范 9.5 | 规则必须可废止；frontmatter 承载 review_after，超十几条升级注册表 | 统计字段允许留空待采集 |
| 元数据规范 | 规范第 10 节 | 统一 Properties（type/domain/layer/maturity/status/origin/created…） | 存量页下次编辑补齐，不批量返工 |
| 附件链接带扩展名 | 规范第 10 节附件规则 | 防止 Obsidian 误建 0 字节空壳 | 针对 PDF/DOCX/图片等附件 |
| 多设备同步（单一 Source of Truth） | SOP 多设备 | 云端唯一主库；新电脑 14 步接入 | 需同步工具 + 文件夹始终可用 |

## 4. 泛化处理（skill 化）

- 名称：`学引力 / LearnGravity` → `<知识库名称>`
- 版本：`V1.8` → `VX.X`
- 路径：`G:\我的云端硬盘\LearnGravity知识库\LearnGravity` → `<VAULT>`
- 板块示例：保留 10 板块骨架，但说明可按领域调整
- 治理文档：以模板形式提供（`references/*.template`），并附实际工作文档（`docs/`）供参照
- 脱敏：不含学生身份信息、不含商业合作细节、不含具体教研内容

## 5. 被排除的内容（明确不纳入）

- 03 Learning Science 全部内容（含"学习的逻辑"方法论文本——用户明确排除）
- 04 Curriculum / 09 Research / 05 Students / 06 Coaching 的具体业务与教研内容
- 进步本 / 12132 / 解题程序表 / 犀师数学 / Eureka 研究的具体正文
- 任何学生真实身份信息与案例细节

## 6. 待人工复核的模糊点

- 板块数量是否作为固定标准（10 板块）还是可配置参数（建议：模板默认 10，允许按领域裁剪）
- lint.py 的"跨页矛盾/过期结论"为提示型检查（依赖语义），只做关键词/结构级启发，正式结论仍需人判

# PR #2 模板评审收尾 — 编码补修

当前源码 **S2**：`fb0511c02128841eb11686d19322672452861513`；前驱验收头 **E**：`d82d470ba55b90cc62c73d6d124deeed132e0dd5`。
保留原 S/E，追加 S2 和证据提交 E2；E2 直接继承 S2，且只修改本目录。
最终 E2 的 SHA、复验与 CI 由 PR 正文外部绑定，避免记录自身 SHA 的循环。
采集时区：**Asia/Shanghai（+08:00）**；外部记录保留原有 UTC 偏移。

本集合只支持模板、编码和记录完整性检查，不是原生 Agent 或 Game 实机验收。
P2 的两处读取显式采用 UTF-8；P3 的 PR-EPIC 成功期望改为 REALISTIC。
修复前的两个隔离解码失败和 Windows CP936 原生失败均保留，未改记为 PASS。
含 CRLF 或尾随空格的原始输出以 JSON 的 raw_text 无损保留；按 UTF-8 编码
可恢复原始字节并复算原摘要和大小，不修改原始输出或放宽空白规则。

| 文件 | 当前用途 |
|---|---|
| source-inputs.json | 全部 878 个已跟踪非证据输入的完整 SHA-256、大小；原字节由 S2 恢复 |
| checks.json、check-output/ | S2 的九项 Linux 检查，178 项通过、零跳过，六项 POSIX 实际执行 |
| lint-summary.json、lint-classification.tsv | 零错误、465 警告；前驱到 S2 465 继承、零新增、零移除；源码上下文和 owner 字节一致 |
| review-dispositions.json、spec-structure.json | 26 项处置及结构记录；历史结论与当前独立复验分别标注 |
| encoding-followup.json | P2/P3 修复、输入身份、失败/通过日志、原 20 文件的不可变 Git 恢复地址 |
| history-rewrite.json | 保留旧归档不可达核查，明确本轮追加提交而非再次重写 |
| author-review.md | 历史作者审阅和本轮窄修说明，不作为独立批准 |
| verify.py | 完整只读校验；Windows 默认编码无需额外 UTF-8 开关 |

原集合 20 文件、974,299 字节和原 877 个非证据输入仍可从前驱 E 原样恢复；
本目录是明确的新修订，不凭时间戳替代旧观察。旧源 S 为 `037615b9c3f1d38ab4abc570980a1558db067d8c`。
原首轮 env-python/PATH 错误日志仍保留为历史文件；本轮沿用既有测试环境 PATH，
未修改或跳过失败测试。322 个生成文件 fresh，Linux 全部 0644，契约未放宽。

前驱 E 的独立验收已完成，结论 **CONCERNS**：26 项处置、lint 分类、归档与绑定通过，
发现 P2 编码问题和非阻塞 P3 词汇偏差。原三系统 CI 关联 E，但实际检出合并测试提交；
文件树一致。旧 Ubuntu/macOS 各 176 项、零跳过；Windows 170 通过、6 项 POSIX 跳过。
后续 CI 同样分别披露关联 head、实际检出提交及树一致性，不将跳过记为通过。

S2 的原生 Windows 运行针对候选记录；E2 提交后再次复验已提交集合，最终结果外部绑定。
最终独立关闭仍由原验收方确认；作者复验不能把 CONCERNS 自动变为独立 PASS。

旧 165 文件、708,050,921 字节归档及 69 个压缩对象仍不在新 PR 可达历史；
旧头仅保留本地回退引用。不增加大型归档，不声称远端对象物理擦除或存储回收。
原 44 个 FAIL 切片、早期两份完整索引和一个缺失线程的恢复限制继续保留。
Codex 旧 FAIL/Partial/Pending 及未覆盖原生交互不因本轮模板检查变 PASS。
Claude 未登录仍是历史 Blocked，Claude 专项不作为本轮模板关闭的阻塞；固定旧版本、
Hook 激活和未覆盖运行时检查继续 NotRun，由维护者另行安排。

保持 Draft，不合并、不发布，不初始化 Memory Bank。
复算当前记录：`python production/qa/evidence/pr2-template-review-2026-10-08/verify.py`。

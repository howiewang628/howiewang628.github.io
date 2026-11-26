# 网站内容

网站的全部文字都在这个文件夹里，每个部分一个文件。在 GitHub 上点开文件，点右上角的铅笔图标修改，再点 **Commit changes**，一两分钟后网站就会更新。

| 文件 | 对应网站上的哪一部分 |
|---|---|
| `homepage.json` | 首页顶部：姓名、职位、照片、邮箱、链接、CV、研究兴趣标签 |
| `intro.json` | 首页 About me |
| `research_interests.json` | 首页 Research interest |
| `news.json` | 首页 News |
| `pub.json` | 论文：Publications 页、首页 Selected Publications、CV |
| `research_agenda.json` | Research Agenda 页 |
| `education.json` | 教育背景：首页和 CV |
| `employment.json` | 工作经历（`employment`，首页和 CV）；产业与学术团体（`industry`，CV） |
| `service.json` | 学术服务：首页和 CV |
| `software.json` | Software & Intellectual Property 页的“软件开发著作权”，以及 CV |
| `unitemind.json` | Software & Intellectual Property 页的“UniteMind AI”：标志图片（`logo`，删掉这一行就显示文字标题）、角色、一句话介绍、链接 |
| `honors.json` | 荣誉（`honors`）和竞赛（`competitions`）：Awards 页和 CV |
| `teaching.json` | 教学：Teaching & Talks 页和 CV |
| `talk.json` | 特邀报告：Teaching & Talks 页和 CV |
| `mentoring.json` | 指导学生：Teaching & Talks 页和 CV |
| `collaborate.json` | 首页的合作者致谢 |
| `settings.json` | 背景颜色、标签的中文（`zhLabels`）、导航栏外链 |

## 规则

- 每条文字中英文写在一起：`{ "en": "...", "zh": "..." }`，两种都要改。
- 日期只写英文，如 `"Dec 2026"`，中文会自动转换。
- 用英文双引号 `"`；文字里要用引号时，写中文引号 `“ ”`。
- 多写的逗号会自动忽略。如果某个文件写错了，网站上只有这一部分会显示上次发布的内容，其他部分照常。
- 想清空某一部分，把列表改成 `[]`，不要删掉整个键。
- 不要改文件名，也不要新建文件（网站只读上面这些文件）。需要新的部分，找 Claude。
- 加链接：在 `links` 里加一行，如 `"GitHub": "https://..."`；链接也可以中英文分开，写成 `{ "en": "...", "zh": "..." }`。新的链接名称（如 `GitHub`）要在 `settings.json` 的 `zhLabels` 里加中文。
- 网址后面加 `?check`（如 `https://howiewang628.github.io/?check`），会列出写错的文件和没有中文的地方。

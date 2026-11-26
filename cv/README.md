# 简历 PDF

网站 CV 页上的 **CV (PDF) / 简历（PDF）** 按钮，打开的就是这个文件夹里的 `Haonan_Wang_CV.pdf`。

## 换新简历（在 GitHub 网页上）

1. 在电脑上把新的 PDF 改名为 `Haonan_Wang_CV.pdf`，名字要完全一样，包括大小写。
2. 在这个页面（`cv` 文件夹）点右上角 **Add file → Upload files**，把文件拖进去。
3. 点 **Commit changes**。同名文件会被替换，一两分钟后网站上就是新简历。
   如果浏览器里还是旧的，按 `Cmd + Shift + R` 强制刷新。

## 不想改名也可以

上传新文件后，把 `content/homepage.json` 里的 `"cvPdf"` 改成新文件名，比如 `"cv/新文件名.pdf"`，再删掉旧的 PDF。

## 注意

- 这个 PDF 是公开的，任何人都能下载。
- 在网页上换过简历后，下次让 Claude 改网站时说一声，它会先取回新简历，不会用旧的覆盖。

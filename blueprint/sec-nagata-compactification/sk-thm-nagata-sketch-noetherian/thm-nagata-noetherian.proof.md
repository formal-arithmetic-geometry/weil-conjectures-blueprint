+++
kind  = "proof"
of    = "thm-nagata-noetherian"
uses = ["def-nagata-compactification", "def-nagata-dense-affine-cover", "def-nagata-noetherian-compactification", "def-nagata-partial-affine-unions", "lemma-nagata-dense-affine-cover"]
+++
Since $S$ is Noetherian and $X\to S$ is of finite type, $X$ is Noetherian,
hence quasi-compact and quasi-separated with finitely many irreducible
components. So [lemma-nagata-dense-affine-cover] provides the selected
dense affine cover $\mathcal U_X=(U_1,\ldots,U_n)$ of
[def-nagata-dense-affine-cover]: affine opens $U_i$ covering $X$ whose
total intersection is dense in $X$. Apply
[def-nagata-noetherian-compactification] to this family. Its stage
$\mathsf C_n$ is a compactification of $X_n\to S$ in the sense of
[def-nagata-compactification], and since the $U_i$ cover $X$ the partial
union $X_n=U_1\cup\cdots\cup U_n$ of [def-nagata-partial-affine-unions] is
$X$ itself. Thus $\mathsf C_{\mathrm{Noeth}}(X/S)=\mathsf C_n$ is a
compactification of $X\to S$, and $X\to S$ is compactifiable in the sense
of [def-nagata-compactifiable].

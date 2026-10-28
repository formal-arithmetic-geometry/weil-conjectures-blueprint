+++
kind = "proof"
of = "det-proper-image-localizing-proper"
+++
$Rp_*$ is exact on $\D(X_{\mathrm{proét}},\Lambda)$. The argument of [det-proper-image-localizing-principle]
applies with "preserves direct sums" required only for families in $\Loc(\Dctf(X,\Lambda))$: the
subcategory $\mathcal S=\{K\in\Loc(\Dctf(X,\Lambda)):Rp_*K\in\Loc(\Dctf(Y,\Lambda))\}$ contains $\Dctf(X,\Lambda)$,
is triangulated, and for a family $(K_s)$ in $\mathcal S$, $Rp_*\bigoplus K_s\cong\bigoplus Rp_*K_s\in\Loc(\Dctf(Y,\Lambda))$.
So $\mathcal S$ is localizing and equals $\Loc(\Dctf(X,\Lambda))$.

For $\Lambda=E,\Qlb$: $\Dctf=\Dbc$, $Rp_*$ preserves $\Dbc$ by [sk-thm-sfb-proper-base-change], and since
$\Loc(\Dbc(X,\Lambda))\subset\Dic(X,\Lambda)$ ([sk-cor-ambient-ind-derived]),
[det-lem-proper-unbounded-window-ii] gives preservation of sums. The other cases are quoted.

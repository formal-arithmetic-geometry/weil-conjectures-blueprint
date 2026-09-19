+++
id = "def-finite-extension-by-zero"
kind = "definition"
title = "Finite-level extension-by-zero sheaf"
order = 33
uses = ["def-weil-finite-coefficient-datum", "def-weil-finite-torsion-constructible", "def-weil-small-proetale-site"]
+++
Fix an auxiliary finite coefficient datum
$(\ell,\Qlb;E,\mathcal O_E,\varpi_E)$ of
Definition [def-weil-finite-coefficient-datum].
For $n\geq1$ and an open immersion
$j:U\hookrightarrow\overline X$, put
$V_U=V\times_{\overline X}U$ for
$V\to\overline X$ in $\overline X_{\mathrm{proet}}$. For a sheaf
$\mathcal F$ of $(\mathcal O_E/\varpi_E^n)_U$-modules, first define the
presheaf

$$
P_{j,!,n}(\mathcal F)(V)=
\left\{s\in\mathcal F(V_U):
\operatorname{Supp}_{V_U}(s)\text{ is closed in }V\right\}.
$$

Here $\operatorname{Supp}_{V_U}(s)$ is the set of geometric points of
$V_U$ at which the germ of $s$ is nonzero, viewed as a subset of
$|V|$. Thus the condition says precisely that the section vanishes on a
neighborhood of the boundary $V\setminus V_U$. Define the heart-level
extension by zero to be its sheafification

$$
j^{\mathrm{sh}}_{!,n}\mathcal F:=aP_{j,!,n}(\mathcal F).
$$

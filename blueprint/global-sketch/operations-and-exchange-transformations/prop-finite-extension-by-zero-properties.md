+++
id = "prop-finite-extension-by-zero-properties"
kind = "theorem"
title = "Properties of finite extension by zero"
order = 34
tags = ["latex:proposition"]
uses = ["def-finite-extension-by-zero", "def-weil-finite-coefficient-datum", "thm-openclosed-exact"]
+++
Fix an auxiliary finite coefficient datum
$(\ell,\Qlb;E,\mathcal O_E,\varpi_E)$, an integer $n\geq1$, and an
open immersion $j:U\hookrightarrow\overline X$.
The sheafification in Definition [def-finite-extension-by-zero] defines
an exact
functor

$$
j^{\mathrm{sh}}_{!,n}: \Sh\bigl(U_{\mathrm{proet}},(\mathcal O_E/\varpi_E^n)_U\bigr)
\longrightarrow
\Sh\bigl(\overline X_{\mathrm{proet}},
(\mathcal O_E/\varpi_E^n)_{\overline X}\bigr)
$$

left adjoint to $j^*$. For every sheaf $\mathcal F$ in the source,
the geometric stalk of $j^{\mathrm{sh}}_{!,n}\mathcal F$ is
$\mathcal F_{\bar x}$ for $\bar x\in U$ and is zero for
$\bar x\in\overline X\setminus U$.

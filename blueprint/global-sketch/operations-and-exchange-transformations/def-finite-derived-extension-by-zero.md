+++
id = "def-finite-derived-extension-by-zero"
kind = "definition"
title = "Finite-level derived extension by zero"
order = 35
uses = ["def-finite-extension-by-zero", "def-weil-finite-coefficient-datum", "prop-finite-extension-by-zero-properties"]
+++
Fix an auxiliary finite coefficient datum
$(\ell,\Qlb;E,\mathcal O_E,\varpi_E)$ of
Definition [def-weil-finite-coefficient-datum].
For an open immersion $j:U\hookrightarrow\overline X$ and $n\geq1$,
define

$$
j_{!,n}:D\bigl(U_{\mathrm{proet}},(\mathcal O_E/\varpi_E^n)_U\bigr)
\longrightarrow
D\bigl(\overline X_{\mathrm{proet}},
(\mathcal O_E/\varpi_E^n)_{\overline X}\bigr)
$$

by applying $j^{\mathrm{sh}}_{!,n}$ degreewise to complexes. The exactness
asserted in Proposition [prop-finite-extension-by-zero-properties]
ensures that this degreewise construction sends quasi-isomorphisms to
quasi-isomorphisms; the notation $j_{!,n}$ is reserved for this derived
finite-level operation.

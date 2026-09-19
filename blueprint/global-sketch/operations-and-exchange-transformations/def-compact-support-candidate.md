+++
id = "def-compact-support-candidate"
kind = "definition"
title = "Compact-support candidate attached to a compactification"
order = 45
uses = ["def-compactification-category", "def-derived-direct-image", "def-finite-derived-extension-by-zero", "def-weil-finite-coefficient-datum"]
+++
Fix an auxiliary finite coefficient datum
$(\ell,\Qlb;E,\mathcal O_E,\varpi_E)$ of
Definition [def-weil-finite-coefficient-datum]. Let
$f:X\to Y$ be separated and of finite type, let $n\geq1$, let
$c=(j,\bar f)\in\operatorname{Comp}(f)$, and set

$$
Rf_{!,n}^{c}=R\bar f_{*,n}\,j_{!,n}:
D\bigl(X_{\mathrm{proet}},(\mathcal O_E/\varpi_E^n)_X\bigr)
\longrightarrow
D\bigl(Y_{\mathrm{proet}},(\mathcal O_E/\varpi_E^n)_Y\bigr).
$$

Here $R\bar f_{*,n}$ is the K-injective derived direct image and
$j_{!,n}$ is the finite-level exact functor of extension by zero.

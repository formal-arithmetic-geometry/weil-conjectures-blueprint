+++
id = "def-compact-support-direct-image"
kind = "definition"
title = "Compactification-independent finite-level constructible direct image"
order = 47
uses = ["def-compact-support-candidate", "def-weil-finite-coefficient-datum", "prop-compactification-coherence"]
+++
Fix an auxiliary finite coefficient datum
$(\ell,\Qlb;E,\mathcal O_E,\varpi_E)$ of
Definition [def-weil-finite-coefficient-datum]. Let
$f:X\to Y$ be separated and of finite type, let $n\geq1$, and choose
$c\in\operatorname{Comp}(f)$. Define

$$
Rf_{!,n}=Rf_{!,n}^{c}:
D^b_c\bigl(X,\mathcal O_E/\varpi_E^n\bigr)
\longrightarrow
D\bigl(Y_{\mathrm{proet}},(\mathcal O_E/\varpi_E^n)_Y\bigr),
$$

equipped with the canonical comparison isomorphisms of
Proposition [prop-compactification-coherence]. The cocycle condition
makes this an exact triangulated functor independent of $c$ up to the
specified unique coherent isomorphism.

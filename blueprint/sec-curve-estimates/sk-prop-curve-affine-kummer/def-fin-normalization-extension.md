+++
id = "def-fin-normalization-extension"
kind = "definition"
title = "Normalization in a finite extension"
lean = ["AlgebraicGeometry.Scheme.normalizationIn", "AlgebraicGeometry.Scheme.fromNormalizationIn"]
order = 1418
uses = ["def-sc-normalization", "def-weil-pbc-scheme-conventions"]
+++
Let $X$ be an
integral scheme
with function field $K$, and let $L/K$ be a field extension.
The normalization of $X$ in $L$ is the relative
spectrum of the integral closure of $\mathcal O_X$ in
$L$, with its canonical map to $X$. On an
affine open
$\operatorname{Spec}B$, this is
$\operatorname{Spec}\overline B^{\,L}$, where $\overline B^{\,L}$
is the integral closure of $B$ in $L$.

For $L=K$ this is exactly the normalization [def-sc-normalization].

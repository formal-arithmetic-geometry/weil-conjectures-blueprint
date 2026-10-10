+++
id = "def-nagata-dense-compactification"
kind = "definition"
title = "Scheme-theoretically dense compactification"
order = 7
lean = ["AlgebraicGeometry.IsSchemeTheoreticallyDominant"]
uses = ["def-nagata-compactification", "def-nagata-scheme-theoretically-dense-open"]
+++
A compactification $X\xrightarrow{j}\overline X\to S$ is
*scheme-theoretically dense* when $j$ is scheme-theoretically dominant:
the largest quasi-coherent ideal of $\mathcal O_{\overline X}$ contained in
the kernel of

$$
\mathcal O_{\overline X}\longrightarrow j_*\mathcal O_X
$$

is zero. When $j$ is quasi-compact this is the predicate of
[def-nagata-scheme-theoretically-dense-open], i.e. the displayed map is
injective.

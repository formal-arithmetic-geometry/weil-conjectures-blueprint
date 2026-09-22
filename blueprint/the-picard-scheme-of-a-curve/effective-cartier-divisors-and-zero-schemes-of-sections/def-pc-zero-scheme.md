+++
id = "def-pc-zero-scheme"
kind = "definition"
title = "The zero scheme of a section"
order = 4225
lean = ["AlgebraicGeometry.zeroScheme"]
uses = ["def-pc-scheme", "lem-pc-zero-scheme-properties"]
+++
Let $X$ be a scheme, $\mathcal{M}$ an invertible $\mathcal{O}_X$-module and
$s\in H^0(X,\mathcal{M})$. The *zero scheme* $Z(s)\subseteq X$ of $s$ is
the closed subscheme defined by the ideal sheaf
$$
\mathcal{I}_{Z(s)}:=\operatorname{im}\Bigl(s^\vee:\mathcal{M}^\vee
\;\longrightarrow\;\mathcal{O}_X\Bigr).
$$
Its basic properties (well-definedness, local form
$\operatorname{Spec}(A/(a))$, compatibility with flat base change,
$Z(s)=X\Leftrightarrow s=0$) are [lem-pc-zero-scheme-properties].

Unresolved dependencies: def:sc-invertible-module

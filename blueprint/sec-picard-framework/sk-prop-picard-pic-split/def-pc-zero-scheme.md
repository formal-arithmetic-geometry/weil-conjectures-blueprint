+++
id = "def-pc-zero-scheme"
kind = "definition"
title = "The zero scheme of a section"
lean = ["AlgebraicGeometry.Scheme.Modules.Hom.imageSubobject_dualMap_comp_dualUnitIso", "AlgebraicGeometry.Scheme.Modules.Hom.zeroLocus"]
order = 650
uses = ["def-pc-scheme", "def-sc-invertible-module"]
+++
Let $X$ be a scheme, $\mathcal{M}$ an
invertible $\mathcal{O}_X$-module and
$s\in H^0(X,\mathcal{M})$. The *zero scheme* $Z(s)\subseteq X$ of $s$ is
the closed subscheme defined by the ideal sheaf

$$
\mathcal{I}_{Z(s)}:=\operatorname{im}\Bigl(s^\vee:\mathcal{M}^\vee
\;\longrightarrow\;\mathcal{O}_X\Bigr).
$$

If $U=\operatorname{Spec}(A)\subseteq X$ is an open affine with
$\mathcal M|_U\cong\mathcal O_U$ and $s|_U$ corresponds to $a\in A$,
then $Z(s)\cap U=\operatorname{Spec}(A/(a))$. The formation of $Z(s)$
is compatible with flat base change, and $Z(s)=X$ if and only if
$s=0$.

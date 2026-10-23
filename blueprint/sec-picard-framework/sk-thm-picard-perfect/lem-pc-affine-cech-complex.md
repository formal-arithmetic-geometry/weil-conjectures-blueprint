+++
id = "lem-pc-affine-cech-complex"
kind = "lemma"
title = "The Cech complex of a standard affine covering"
lean = ["AlgebraicGeometry.Scheme.Modules.exactAt_cechComplex_basicOpen"]
order = 755
uses = ["def-pc-scheme", "lem-pc-cech-exact"]
+++
Let $X$ be a scheme, $\mathcal F$ a quasi-coherent $\mathcal O_X$-module,
$V\subseteq X$ an affine open and $f_1,\dots,f_n\in\Gamma(V,\mathcal O_X)$
with $V=D(f_1)\cup\dots\cup D(f_n)$. Then the Cech complex of $\mathcal F$
for the covering $\{D(f_i)\}$ of $V$,

$$
\prod_{i}\mathcal F(D(f_i))
\longrightarrow\prod_{i,j}\mathcal F(D(f_if_j))\longrightarrow\cdots,
$$

is exact in every positive degree. In terms of $V=\operatorname{Spec}(A)$
and $M=\mathcal F(V)$: the $f_i$ generate the unit ideal of $A$, and
$\mathcal F(D(f_{i_0}\cdots f_{i_p}))=M_{f_{i_0}\cdots f_{i_p}}$.

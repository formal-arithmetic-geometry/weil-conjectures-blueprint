+++
id = "def-weil-pbc-proper-open-comparison"
kind = "definition"
title = "Comparison map for a proper map fixing an open"
order = 3304
lean = ["AlgebraicGeometry.Etale.properOpenComparison"]
uses = ["lem-weil-pbc-proper-open-identification"]
+++
Let $u:T_1\to T_2$ be proper, and let $j_i:X\hookrightarrow T_i$ be open
immersions with $uj_1=j_2$. Fix a finite ring $\Lambda$ and
$K\in D^+(X_{\Et},\Lambda)$. Set $V=T_1\times_{T_2}X$, with projections
$b:V\to T_1$ and $p:V\to X$, and let $s:X\to V$ be the morphism induced by
$j_1$, so that $bs=j_1$ and $ps=\operatorname{id}_X$. Define
$$
 \alpha_{u,K}:j_{2!}K\longrightarrow Ru_*j_{1!}K
$$
to be the adjoint, under $j_{2!}\dashv j_2^{-1}$, of
$\theta_{u,K}^{-1}$. The functor $Ru_*$ here is the derived direct image.

Here $\theta_{u,K}:j_2^{-1}Ru_*j_{1!}K\xrightarrow{\sim}K$ is the specified
isomorphism constructed in [lem-weil-pbc-proper-open-identification]; the
source states the definition before that lemma and names $\theta_{u,K}$
forward.

Unresolved dependencies: def:weil-pbc-scheme-conventions, def:weil-pbc-derived-categories, def:weil-pbc-extension-by-zero, def:weil-pbc-direct-image

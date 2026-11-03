+++
id = "det-uniform-constructible-ext-rational"
kind = "lemma"
title = "The stratum bound with rational coefficients"
order = 2420
uses = ["det-uniform-constructible-ext-integral", "sk-lem-stratified-lattice", "sk-lem-constructible-ext-continuity", "sk-lem-lisse-finite-descent"]
+++
Let $a\colon S\hookrightarrow X$, $j$ be as in [det-uniform-constructible-ext-torsion] and put
$c_a=\operatorname{cd}_\ell(j)+\operatorname{cd}_\ell(S)+2$. For $\Lambda=E$ or $\Qlb$, every lisse
$\Lambda_S$-module $L$, every locally closed $b\colon T\hookrightarrow X$ and every lisse
$\Lambda_T$-module $M$, let $S=\bigsqcup_kS_k$ be the finite stratification of
[sk-lem-stratified-lattice] attached to $L$ (it depends only on $L$), write each
$a_k\colon S_k\hookrightarrow X$ as in [det-uniform-constructible-ext-torsion] with $Z_k$ the closure of
$S_k$ and complement $j_k$, and put $c_{a,L}=\max_k\bigl(\operatorname{cd}_\ell(j_k)+\operatorname{cd}_\ell(S_k)+2\bigr)$.
Then

$$
\Ext^q_\Lambda(a_!L,b_!M)=0\qquad(q>c_{a,L}).
$$

If $L$ has a lisse $\mathcal O_E$-lattice on $S$ (resp. on $S$ after a finite extension $E$, for
$\Lambda=\Qlb$), no refinement of $S$ is needed and the bound is $c_a$. In general the refined
bound can exceed $c_a$: for $Z=X$ smooth, $S$ affine of dimension $d$ and a stratum of codimension
$c\geq2$ one gets $(2c-1)+(d-c)+2>d+2$.

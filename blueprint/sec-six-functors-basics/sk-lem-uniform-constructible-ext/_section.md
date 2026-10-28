+++
id = "sk-lem-uniform-constructible-ext"
kind = "lemma"
title = "Uniform Ext bound"
order = 2416
uses = ["sk-def-sfb-constructible", "sk-def-cd", "sk-lem-stratified-lattice"]
tags = ["sketch"]
+++
Let $\Lambda=E$ or $\Qlb$, with $\Ext$ taken in $\D(X_{\mathrm{proét}},\Lambda)$. For every
$C\in\Cons(X,\Lambda)$ ([sk-def-sfb-constructible]) there is an integer $d_C\geq0$ such that

$$
\Ext^q(C,N)=0
\qquad\text{for all }q>d_C\text{ and all }N\in\Cons(X,\Lambda).
$$

If $C=a_!L$, with $a$ factored as $S\hookrightarrow Z\hookrightarrow X$ and $j$ the open complement of
$Z$, and $L$ contains a lisse $\mathcal O_E$-lattice (which holds after refining $S$, by
[sk-lem-stratified-lattice]), the proof gives $d_C=\operatorname{cd}_\ell(j)+\operatorname{cd}_\ell(S)+2$
(cohomological dimensions as in [sk-def-cd]). One of the two extra degrees comes from the cone defining
$R\underline\Gamma_Z$, and the other from a derived inverse limit over the reductions modulo $\pi_E^n$.

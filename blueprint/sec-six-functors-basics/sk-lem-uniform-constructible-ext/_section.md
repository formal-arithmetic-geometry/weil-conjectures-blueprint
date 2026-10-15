+++
id = "sk-lem-uniform-constructible-ext"
kind = "lemma"
title = "Uniform Ext bound"
order = 1522
uses = ["sk-lem-coefficient-heart", "sk-def-cd", "sk-lem-formal-closed-support"]
tags = ["sketch"]
+++
Let $\Lambda=E$ or $\Qlb$. For every $C\in\Cons(X,\Lambda)$ there is an integer $d_C\geq0$ such that

$$
\Ext^q_{\Lambda}(C,N)=0
\qquad\text{for all }q>d_C\text{ and all }N\in\Cons(X,\Lambda),
$$

the Ext groups being taken in $\D(X_{\mathrm{proét}},\Lambda)$.

For $C=a_!L$, with $a$ factored as $S\hookrightarrow Z\hookrightarrow X$ and $j$ the open complement of
$Z$, the proof gives $d_C=\operatorname{cd}_\ell(j)+\operatorname{cd}_\ell(S)+2$ (cohomological
dimensions as in [sk-def-cd]). One of the two extra degrees comes from the cone defining
$R\underline\Gamma_Z$, the other from a derived inverse limit over the reductions modulo $\pi_E^n$.

+++
id = "thm-sf-ambient-adjoint-class"
kind = "theorem"
title = "The exceptional adjoint on the bounded comparison class"
order = 2145
uses = ["def-sf-fullcd-class", "def-weil-pbc-site-comparison-morphism", "lem-amb-etale-compact-comparisons", "lem-sf-class-compact-support-comparison", "thm-amb-etale-exceptional-adjoint", "thm-sf-fullcd-class", "thm-weil-pbc-site-comparison"]
+++
Let $f:X\to Y$ be separated of finite type over $\Fbar$, with a
compactification of dimension at most $d$, and let $A=A_{E,n}$.
Then the following statements hold:

1. The class-restricted dimension datum
[def-sf-fullcd-class] holds with bound $2d$.
1. Let $f^\times$ be the right adjoint of the étale
compact-support functor. On bounded-below pro-étale coefficients put
$$
Rf_n^\times L=\nu_X^* f^\times R\nu_{Y,*}L.
$$
For every bounded-below $K$ of étale origin and every bounded-below
$L$, there is a natural bijection
$$
\operatorname{Hom}(Rf_{!,n}K,L)
\cong\operatorname{Hom}(K,Rf_n^\times L).
$$
Thus this formula is the right adjoint relative to the bounded-below
comparison class.
1. Compactification comparisons of these functors are canonical and
satisfy the cocycle condition.

No adjunction on arbitrary unbounded pro-étale objects is asserted.

+++
id = "lem-pur-divisor-class"
kind = "lemma"
title = "Kummer class of a divisor and its $c_1$"
order = 2249
uses = ["def-coefficient-twists-detailed", "def-pur-affine-line-datum", "def-pur-conventions", "def-pur-frame-class", "def-pur-support-cohomology", "def-weil-derived-cohomology-sheaves", "lem-pur-frame-independence", "lem-pur-kummer-additivity"]
+++
In the purity conventions of this chapter ([def-pur-conventions] fixed setting),
let $T\to B$ be smooth of relative dimension $n$ and let
$D\hookrightarrow T$ be a closed subfamily, smooth over $B$, of pure
codimension one. The *Kummer class of the divisor $D$* is the
class $\operatorname{cl}(D)\in H^2_D(T,\Lambda(1))$ of
[def-pur-frame-class] of a frame of the ideal of $D$, well
defined by [lem-pur-frame-independence]. Moreover:

$$
\begin{array}{rcll}
\text{(a)}& \operatorname{cl}(D)|_{D\cap U}=\partial(\kappa(f))&
\text{for a local equation }f\text{ of }D\text{ on }U,&\\
\text{(b)}& \operatorname{cl}(D_1+D_2)=\operatorname{cl}(D_1)+\operatorname{cl}(D_2),&
\text{and forgetting support sends }\operatorname{cl}(D)\text{ to }c_1(\mathcal O_T(D)).&
\end{array}
$$

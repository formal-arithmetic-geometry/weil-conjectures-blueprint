+++
id = "lem-pur-p1-diagonal-class"
kind = "lemma"
title = "The class of the diagonal"
order = 3573
uses = ["def-coefficient-twists-detailed", "def-pur-conventions", "def-weil-scheme-morphism-properties", "def-weil-small-proetale-site-detailed", "lem-pur-divisor-class", "lem-pur-kummer-additivity", "thm-pur-p1-decomposition"]
+++
In the purity conventions of this chapter ([def-pur-conventions] fixed setting),
let $P=\mathbf P^1_Y$, $W=P\times_YP$ and $\Delta\subset W$ the
diagonal. The diagonal is an effective Cartier divisor of $W$
(relative to the projection $W\to Y$, with the section
$x_0y_1-x_1y_0$ of $p_1^*\mathcal O(1)\otimes p_2^*\mathcal O(1)$),
and

$$
\mathcal O_W(\Delta)=p_1^*\mathcal O(1)\otimes p_2^*\mathcal O(1),
$$

so by [lem-pur-kummer-additivity] and
[lem-pur-divisor-class]

$$
\operatorname{cl}(\Delta)\ \in\ H^2_\Delta(W,\Lambda(1)),
\qquad
\operatorname{cl}(\Delta)\ \text{forgets to}\ p_1^*h+p_2^*h= h_1+h_2.
$$

## Proof

The section $x_0y_1-x_1y_0$ of
$p_1^*\mathcal O(1)\otimes p_2^*\mathcal O(1)$ vanishes exactly on
$\Delta$ (on the open chart $(\mathbf A^1_Y)^2$ with coordinates
$x,y$ it is $x-y$ up to a unit, and the two other charts are
similar), so $\Delta$ is an effective Cartier divisor with the
stated line bundle, and
$\operatorname{cl}(\Delta)=c_1\bigl(p_1^*\mathcal O(1)\otimes p_2^*\mathcal O(1)\bigr)=p_1^*h+p_2^*h$ by
[lem-pur-divisor-class](b) and [lem-pur-kummer-additivity].

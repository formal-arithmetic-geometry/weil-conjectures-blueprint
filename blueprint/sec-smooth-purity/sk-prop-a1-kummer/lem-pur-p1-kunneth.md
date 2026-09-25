+++
id = "lem-pur-p1-kunneth"
kind = "lemma"
title = "Kunneth compatibility on the product"
order = 2003
uses = ["def-exchange-projection", "def-pur-conventions", "def-pur-p1-integration", "def-weil-derived-pullback-tensor-hom", "def-weil-derived-tensor", "def-weil-pbc-proetale-site", "def-weil-scheme-morphism-properties", "prop-weil-proet-finite-proper-base-change", "thm-pur-p1-decomposition"]
+++
In the purity conventions of this chapter ([def-pur-conventions] fixed setting),
let $Y$ be a separated finite-type $k$-scheme, let $P=\mathbf P^1_Y$, $W=P\times_YP$, with projections $p_1,p_2$, and let
$h_1=p_1^*h$, $h_2=p_2^*h$. Then:

1. (dec) for $\alpha\in\{\Lambda\}$, the projections
$p_i:W\to P$ are $\mathbf P^1$-bundles over $P=P^1_Y$, i.e. the
base change of $q:\mathbf P^1_Y\to Y$ along the other
projection; $\mathcal O_{W/P_i}(1)=p_{3-i}^*\mathcal O(1)$, and the
decomposition of [thm-pur-p1-decomposition] base-changed along
$p_{3-i}$ identifies
$$
R(p_i)_*\Lambda_W\;\cong\;\Lambda_P\oplus\Lambda_P(-1)[-2]
$$
with components the unit and $h_{3-i}$.
1. (integral) under this identification and for the relative
$\mathbf P^1$ structure maps (see the integration of
[def-pur-p1-integration],
base-changed along $p_{3-i}$),
$$
R(p_2)_*(p_1^*A\otimes^L_{\Lambda_W}p_2^*B)\;\cong\;
Lq^*\bigl(Rq_!A\bigr)\otimes^L_{\Lambda_P}B
$$
for $A\in D^b_{ctf}(Y,\Lambda)$, $B\in D^b_{ctf}(P,\Lambda)$, and
$$
(p_2)_*(1_W)=0,\qquad
(p_2)_*(h_2)=0,\qquad
(p_2)_*(h_1)=1_P,
\qquad
(p_2)_*(h_1h_2)=h_2,
$$
i.e. the fiber integration of the relative section class is $1$,
that of the unit and of a pullback is zero, and the contraction
identities of the diagonal hold.

## Proof

All products below are the derived tensors and pullbacks of [def-weil-derived-tensor], [def-weil-derived-pullback-tensor-hom].
Item (1): $W\to P$ via $p_i$ is the P-bundle
$\operatorname{Proj}(\mathcal O_P\oplus\mathcal O_P)\cong\mathbf P^1_P$, i.e. the base change of $q$ under the other projection;
the relative $\mathcal O(1)$ is $p_{3-i}^*\mathcal O(1)$, the
class of the relative divisor at infinity, and the decomposition
follows from the base-change compatibility of
[thm-pur-p1-decomposition]. Item (2): the Kunneth comparison is
the compatibility of $R(p_2)_!$ with the base change
([def-exchange-projection], [prop-weil-proet-finite-proper-base-change])
and the projection formula. The three displayed values: the class
$h_2$ is the pullback $p_2^*h$, whose $(p_2)_*$-image is
$h\cdot(p_2)_*(1_W)$ by the projection formula and the second
component of $(p_2)_*(1_W)$ is $0$ (it is the $1_P$-component of
the decomposition), hence $(p_2)_*(h_2)=0$; the class $h_1$ is
the relative divisor at infinity of the fibration $p_2$, i.e. the
generator of the second summand in (1), whose $(p_2)_*$-image is
$1_P$ (the fiber at infinity is a section of the projection).

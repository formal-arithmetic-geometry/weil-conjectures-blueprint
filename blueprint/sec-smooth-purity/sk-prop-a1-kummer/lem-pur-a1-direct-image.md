+++
id = "lem-pur-a1-direct-image"
kind = "lemma"
title = "The affine line has no higher direct images"
order = 2021
uses = ["def-coefficient-twists-detailed", "def-pur-conventions", "def-weil-derived-direct-image", "def-weil-scheme-morphism-properties", "fix-prop-adjunctions", "lem-pur-divisor-class", "lem-pur-support-localization-triangle", "prop-weil-pbc-inverse-image-derived-adjunction", "thm-pur-affine-line-orientation", "thm-pur-p1-decomposition", "thm-pur-rank-one-local-calculation"]
+++
In the purity conventions of this chapter ([def-pur-conventions] fixed setting),
let $B$ be a separated
finite-type $k$-scheme and let $\pi:\mathbf A^1_B\to B$ be the
projection, with the adjunction $L\pi^*\dashv R\pi_*$ and unit
$\eta_\pi$ of [fix-prop-adjunctions]. Then

$$
\eta_\pi(\Lambda_B):\quad
\Lambda_B\xrightarrow{\ \sim\ }R\pi_*\Lambda_{\mathbf A^1_B}
$$

is an isomorphism: the affine line has no higher direct images for the
constant coefficients, and its $H^0$ is the unit.

## Proof

Step 1: the localization triangle on the projective line. Let
$q:\mathbf P^1_B\to B$ be the projective line of
[thm-pur-p1-decomposition], and let
$j:\mathbf A^1_B\hookrightarrow\mathbf P^1_B$ be the open immersion
whose closed complement is the infinity section
$i_\infty:B\hookrightarrow\mathbf P^1_B$, so that $qj=\pi$. The
localization triangle of [lem-pur-support-localization-triangle]
for the closed–open pair $(i_\infty,j)$ and
$K=\Lambda_{\mathbf P^1_B}$ is

$$
i_{\infty,*}Ri_\infty^!\Lambda_{\mathbf P^1_B}
\longrightarrow\Lambda_{\mathbf P^1_B}
\longrightarrow Rj_*\Lambda_{\mathbf A^1_B}\xrightarrow{+1};
$$

applying the direct image of [def-weil-derived-direct-image]
along $q$, with the derived adjunction of
[prop-weil-pbc-inverse-image-derived-adjunction] and with
$qi_\infty=\operatorname{id}_B$, $qj=\pi$, turns it into the
distinguished triangle (the right adjoint of a composite of exact
pullbacks is the composite of their derived right adjoints)

$$
Ri_\infty^!\Lambda_{\mathbf P^1_B}
\longrightarrow Rq_*\Lambda_{\mathbf P^1_B}
\xrightarrow{\ \beta\ }R\pi_*\Lambda_{\mathbf A^1_B}
\xrightarrow{+1}.
$$

Step 2: the first map is the class of the divisor at infinity. By
[thm-pur-p1-decomposition] the morphism

$$
(1,h):\ \Lambda_B\oplus\Lambda_B(-1)[-2]
\xrightarrow{\ \sim\ }Rq_*\Lambda_{\mathbf P^1_B}
$$

is an isomorphism whose components are the unit and the image $h$ of
the class $\operatorname{cl}(D_\infty)$ of the divisor at infinity
under the [def-coefficient-twists-detailed] identifications; by
[lem-pur-divisor-class] the class $h=c_1(\mathcal O(1))$
restricts to zero on the open complement $\mathbf A^1_B$, on which
$\mathcal O(1)$ is trivial. The first map of the triangle of Step 1
is, under the same identifications, the forgetting of the support of
the class of the divisor supported on $D_\infty$, so it is $h$: it
is the inclusion of the second summand of the decomposition, normalized
by [thm-pur-affine-line-orientation] and
[thm-pur-rank-one-local-calculation] at the point at infinity.
Step 3: the unit. The cone of the inclusion of a direct summand is the
complementary summand, so the triangle of Step 1 identifies $\beta$,
the restriction to the open complement, with the projection onto the
first summand,

$$
\beta:\ Rq_*\Lambda_{\mathbf P^1_B}\cong
\Lambda_B\oplus\Lambda_B(-1)[-2]\longrightarrow\Lambda_B,
\qquad R\pi_*\Lambda_{\mathbf A^1_B}\cong\Lambda_B .
$$

By [fix-prop-adjunctions](3) the unit of the composite $\pi=qj$
is the composite of the units, so
$\eta_\pi(\Lambda_B)=\beta\circ\eta_q(\Lambda_B)$; the unit
$\eta_q(\Lambda_B)$ is the first component of the decomposition of
Step 2 and $\beta$ is the projection onto the first summand, whence
$\eta_\pi(\Lambda_B)=\operatorname{id}_{\Lambda_B}$ under that
decomposition. In particular $\eta_\pi(\Lambda_B)$ is an
isomorphism.

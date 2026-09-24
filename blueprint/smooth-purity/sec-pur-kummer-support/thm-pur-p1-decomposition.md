+++
id = "thm-pur-p1-decomposition"
kind = "theorem"
title = "The projective-line decomposition"
order = 3570
uses = ["cor-weil-pbc-geometric-fiber-finite", "def-coefficient-twists-detailed", "def-pur-conventions", "def-pur-support-cohomology", "def-sbc-smooth-morphisms", "def-weil-derived-cohomology-sheaves", "def-weil-scheme-morphism-properties", "def-weil-small-proetale-site-detailed", "lem-pur-divisor-class", "thm-pur-affine-line-orientation", "thm-pur-kummer-affine-line", "thm-pur-rank-one-local-calculation", "thm-pur-with-support-exactness", "thm-weil-pbc-finite-torsion"]
+++
In the purity conventions of this chapter ([def-pur-conventions] fixed setting),
let $Y$ be a
separated finite-type
$k$-scheme and let $q:\mathbf P^1_Y\to Y$ be the projective line over
$Y$. Let $D_\infty\subset\mathbf P^1_Y$ be the section at infinity
(an effective Cartier divisor with the line bundle
$\mathcal O_{\mathbf P^1_Y}(D_\infty)=\mathcal O(1)$), and let

$$
h:\Lambda_Y(-1)[-2]\longrightarrow Rq_*\Lambda_{\mathbf P^1_Y}
$$

be the image of $\operatorname{cl}(D_\infty)$ under the canonical
identifications of [def-coefficient-twists-detailed]: forgetting the
support and identifying $H^2(\mathbf P^1_Y,\Lambda(1))$ with
$\operatorname{Hom}_{D(Y,\Lambda)}(\Lambda_Y(-1)[-2],Rq_*\Lambda_{\mathbf P^1_Y})$.
Then the morphism

$$
(1,h):\ \Lambda_Y\oplus\Lambda_Y(-1)[-2]
\xrightarrow{\ \sim\ }Rq_*\Lambda_{\mathbf P^1_Y}
$$

is an isomorphism, base-change compatible. Its components are the
unit and the class of the divisor at infinity; $h$ is
$c_1(\mathcal O(1))$ by [lem-pur-divisor-class](b).

## Proof

Step 1: on a geometric fiber. Let $\bar y\to Y$ be a geometric
point with algebraically closed $\Omega$, and let
$j:\mathbf A^1_{\bar y}\hookrightarrow\mathbf P^1_{\bar y}$ be the
open complement of the closed point $\infty$. By
[thm-pur-with-support-exactness] and [thm-pur-kummer-affine-line],

$$
H^q_\infty(\mathbf P^1_{\bar y},\Lambda(1))=0\quad(q\neq2),\qquad
H^2_\infty(\mathbf P^1_{\bar y},\Lambda(1))=\Lambda\cdot
\partial\kappa(t_\infty)
$$

with the boundary of the Kummer class of the coordinate
$t_\infty$ at infinity, i.e. the rank-one local calculation
[thm-pur-rank-one-local-calculation] at the point
$\infty$. The long exact sequence of the pair $(\mathbf P^1_{\bar y},\infty)$, read with the values of
[thm-pur-kummer-affine-line] on $\mathbf A^1_{\bar y}$, gives

$$
H^0(\mathbf P^1_{\bar y},\Lambda(1))=\Lambda\cdot 1,\quad
H^1(\mathbf P^1_{\bar y},\Lambda(1))=0,\quad
H^2(\mathbf P^1_{\bar y},\Lambda(1))=\Lambda\cdot h_{\bar y},
$$

where $h_{\bar y}$ is the image of $\partial\kappa(t_\infty)$, the
class of the rational point $\infty$. Untwisting
(the [def-coefficient-twists-detailed] identifications), this is
$R\Gamma(\mathbf P^1_{\bar y},\Lambda)=\Lambda\oplus\Lambda(-1)[-2]$
with second component the image of $h$, and the identification is
compatible with the unit.

Step 2: the map is an isomorphism. The morphism $(1,h)$ of the
statement is defined globally, $h$ being the class of the divisor
$D_\infty\subset\mathbf P^1_Y$ ([lem-pur-divisor-class]). For a
base change $Y'\to Y$, the proper base change of
[thm-weil-pbc-finite-torsion] and the
[cor-weil-pbc-geometric-fiber-finite] identify the pullback of
$(1,h)$ at each geometric point of $Y'$ with the fiberwise
calculation of Step 1 (the class of $D_\infty$ restricts to the
class $h_{\bar y}$ by the compatibility of
[lem-pur-divisor-class] with base change and the normalization
of [thm-pur-affine-line-orientation]). The cone of the morphism
is a bounded constructible complex whose geometric stalks are zero by
Step 1; being constructible and bounded, it is zero
([def-weil-derived-cohomology-sheaves] and the standard
truncation argument of [def-pur-support-cohomology]). This
proves the assertion, and base-change compatibility is the same
statement for the pullbacks.

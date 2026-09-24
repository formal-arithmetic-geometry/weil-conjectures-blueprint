+++
id = "thm-pur-regular-immersion-purity"
kind = "theorem"
title = "Purity for regular closed immersions"
order = 3625
uses = ["cor-pur-affine-space-purity", "def-coefficient-twists-detailed", "def-pur-conventions", "def-pur-frame-class", "def-pur-regular-immersion", "def-weil-derived-tensor", "def-weil-exceptional-inverse-image", "def-weil-pbc-proetale-site", "def-weil-scheme-morphism-properties", "lem-pur-frame-independence", "lem-pur-immersion-twist", "lem-pur-kunneth-supported", "lem-pur-regular-immersion-linearization", "lem-pur-regular-immersion-smooth-structure", "thm-pur-diagonal-dualizing-object"]
+++
In the purity conventions of this chapter ([def-pur-conventions] fixed setting),
let $i:Z\hookrightarrow X$ be a
regular closed immersion of pure
codimension $c$, with $X$ smooth over the perfect field $k$ and
$Z$ regular. There is a canonical isomorphism

$$
Ri^!\Lambda_X\xrightarrow{\ \sim\ }\Lambda_Z(-c)[-2c],
$$

carrying $1$ to the fundamental class $[Z\subset X]$ of
[def-pur-frame-class]. It is compatible with etale base change and
with exterior products.

## Proof

Cancellation of the Tate factor uses the invertibility and twist identifications of [def-coefficient-twists-detailed].
Step 1: the $\omega$-identification. Work on each open-and-closed
connected component of $X$; the resulting isomorphisms assemble
over their disjoint union. By
[lem-pur-regular-immersion-smooth-structure], $a_X$ and $a_Z$
are smooth of dimensions $n$ and $m=n-c$, and
$a_Z=a_X\circ i$. The composition law for the exceptional inverse
image ([def-weil-exceptional-inverse-image]) gives

$$
\omega_{Z/k}=Ra_Z^!\Lambda_k
\;\cong\;Ri^!\bigl(Ra_X^!\Lambda_k\bigr)
=Ri^!\omega_{X/k},
$$

and by the smooth purity of the structure morphisms
([thm-pur-diagonal-dualizing-object] applied to $a_X$ and
$a_Z$),

$$
\omega_{X/k}\;\cong\;\Lambda_X(n)[2n],
\qquad
\omega_{Z/k}\;\cong\;\Lambda_Z(m)[2m].
$$

Step 2: the co-projection removes the twist. By
[lem-pur-immersion-twist] (with $K=\Lambda_X$ and $m=n$),

$$
Ri^!\Lambda_X(n)[2n]
\;\cong\;\bigl(Ri^!\Lambda_X\bigr)\otimes^L_{\Lambda_Z}\Lambda_Z(n)[2n].
$$

Combined with Step 1 and the cancellation of the invertible
$\Lambda_Z(n)[2n]$ (in the monoid of invertible objects of
[def-weil-derived-tensor]):

$$
Ri^!\Lambda_X
\;\cong\;\Lambda_Z(m-n)[2m-2n]
=\Lambda_Z(-c)[-2c].
$$

Step 3: the class. The identification of Steps 1–2 is canonical, so
it carries the canonical generator of $\Lambda_Z$ to a class
$[Z\subset X]\in H^{2c}_Z(X,\Lambda(c))$; we show that this is the
class of [def-pur-frame-class]. By
[lem-pur-regular-immersion-linearization], etale-locally the pair
$(X,Z)$ is the linear pair $(\mathbf A^{c+m}_k,\mathbf A^m_k)$; on
the model, the structure-morphism identifications of Step 1 are the
affine-space purity comparisons of [cor-pur-affine-space-purity]
for the projections, hence the composite identification carries $1$
to the $c$-fold exterior product of the rank-one Kummer boundaries of
the coordinates, i.e. to the class
$\operatorname{cl}(f)=\partial_1\kappa(f_1)\cup\cdots\cup\partial_c\kappa(f_c)$
of the standard frame, by [lem-pur-kunneth-supported] and
[lem-pur-frame-independence] (the frame class depends only on the
pair, and the identification of Steps 1–2 is compatible with the
etale-localization to the model by the base-change compatibility of
[thm-pur-diagonal-dualizing-object]). Hence the two global
classes agree: they are defined by the same canonical construction
(the Kummer boundary of the ideal of the pair, with the uniqueness of
the class of [lem-pur-frame-independence]), and the class of
[def-pur-frame-class] is by definition the Kummer boundary of the
same pair.

Step 4: the compatibilities. The canonical identification is the
composite of the smooth-purity identifications of the two structure
morphisms, the composition law for $(-)^!$, and the co-projection;
each of these is compatible with etale base change and with the
exterior-product (Künneth) structure by the corresponding
compatibilities of [thm-pur-diagonal-dualizing-object] and
[lem-pur-kunneth-supported], and the class of Step 3 is
compatible with them by [lem-pur-frame-independence].

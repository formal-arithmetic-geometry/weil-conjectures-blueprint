+++
id = "lem-pur-gysin-structure"
kind = "lemma"
title = "Structure of the exceptional inverse image of the zero section"
order = 2005
uses = ["cor-amb-affine-space-adjunction", "def-coefficient-twists-detailed", "def-pur-affine-line-datum", "def-pur-conventions", "def-sbc-smooth-morphisms", "def-weil-exceptional-inverse-image", "def-weil-pbc-proetale-site", "def-weil-scheme-morphism-properties", "lem-amb-cartier-kummer-map", "lem-amb-closed-support-hom", "thm-pur-with-support-exactness", "thm-sf-ambient-adjoint-class", "thm-weil-pbc-site-comparison"]
+++
In the purity conventions of this chapter ([def-pur-conventions] fixed setting),
explicit ingredients, let $\Lambda=A$, and let
$s:Y\hookrightarrow\mathbf A^1_Y$ be the zero section. Then:

1. The object $Rs^!\Lambda_{\mathbf A^1_Y}(1)[2]$ lies in
$D^b_{ctf}(Y,\Lambda)$ and is concentrated in degree zero after the
displayed shift, with lisse rank-one cohomology sheaf.
1. Under the long exact sequence of
[thm-pur-with-support-exactness] for the pair
$(s(Y),\mathbf A^1_Y)$, there is a canonical identification
$$
\Gamma\!\left(Y,\mathcal H^0\bigl(Rs^!\Lambda_{\mathbf A^1_Y}(1)[2]\bigr)\right)
\cong H^2_{s(Y)}\bigl(\mathbf A^1_Y,\Lambda(1)\bigr),
$$
via which the boundary of the
Kummer class of $t$ corresponds
to an element of the space of morphisms
$$
\operatorname{Hom}_{D(Y,\Lambda)}\bigl(\Lambda_Y,Rs^!\Lambda_{\mathbf A^1_Y}(1)[2]\bigr).
$$

(Source: the Gysin sequence of the zero section, i.e. the
affine-line case of the fundamental exact sequence of cohomological
purity – Milne, Lectures on Etale Cohomology, Section 16, Theorems
16.1 and 16.7, and Proposition 16.11 (the case $r=2c-1=1$).)

## Proof

Work first on the ordinary etale site. Write $p:\mathbf A^1_Y\to Y$.
The explicit adjunction of [cor-amb-affine-space-adjunction] gives
$p^\times\Lambda_Y=\Lambda_{\mathbf A^1_Y}(1)[2]$. The composition
of exceptional right adjoints, obtained by composing their Hom
adjunctions as in [def-weil-exceptional-inverse-image], and
$ps=\operatorname{id}_Y$ therefore give

$$
Rs^!\Lambda_{\mathbf A^1_Y}(1)[2]
\cong Rs^!p^\times\Lambda_Y
\cong R(ps)^!\Lambda_Y=\Lambda_Y.
$$

This proves concentration, constructibility, and the free rank-one
assertion together; constancy is not inferred from constancy of ranks.
The comparison of actual ambient adjoints in
[thm-sf-ambient-adjoint-class] and the fully faithful realization
[thm-weil-pbc-site-comparison] transport this calculation, including
its counits, to the etale-origin objects on the small pro-etale site.

For the second assertion, the support identification
[lem-amb-closed-support-hom] identifies
$H^2_{s(Y)}(\mathbf A^1_Y,\Lambda(1))$ with
$\operatorname{Hom}_Y(\Lambda_Y,Rs^!\Lambda(1)[2])$.
Since the target is concentrated in degree zero, this Hom group is
$\Gamma(Y,\mathcal H^0(Rs^!\Lambda(1)[2]))$.
The boundary of the coordinate class in
[def-pur-affine-line-datum], [thm-pur-with-support-exactness]
is precisely the supported Cartier morphism of
[lem-amb-cartier-kummer-map]; the latter construction also gives
its compatibility with base change of this zero-section pair.

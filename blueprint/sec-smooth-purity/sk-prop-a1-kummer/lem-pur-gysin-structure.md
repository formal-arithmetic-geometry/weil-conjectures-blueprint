+++
id = "lem-pur-gysin-structure"
kind = "lemma"
title = "Structure of the exceptional inverse image of the zero section"
order = 2286
uses = ["def-pur-affine-line-datum", "def-pur-conventions", "def-weil-derived-direct-image", "def-weil-exceptional-inverse-image", "fix-prop-adjunctions", "lem-amb-cartier-kummer-map", "lem-amb-closed-support-hom", "lem-pur-support-localization-triangle", "lem-weil-derived-direct-image-composition", "prop-pur-gm-relative-kummer", "thm-pur-with-support-exactness"]
+++
In the purity conventions of this chapter ([def-pur-conventions] fixed setting),
let $\Lambda=A$, and let
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

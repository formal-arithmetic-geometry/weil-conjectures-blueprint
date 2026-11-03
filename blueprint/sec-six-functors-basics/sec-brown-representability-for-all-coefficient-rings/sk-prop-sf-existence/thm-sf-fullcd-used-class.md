+++
id = "thm-sf-fullcd-used-class"
kind = "theorem"
title = "The full cohomological-dimension condition on the blueprint's coefficient class"
lean = ["AlgebraicGeometry.ProEtale.etaleOrigin_isClosedUnderColimitsOfShape", "AlgebraicGeometry.ProEtale.etaleOrigin_unit", "AlgebraicGeometry.ProEtale.etaleOrigin_of_shortExact"]
order = 2576
uses = ["def-sf-fullcd-used-class", "def-weil-derived-cohomology-sheaves", "def-weil-full-cohomological-dimension", "def-weil-pbc-direct-image", "def-weil-pbc-proetale-site", "def-weil-pbc-site-comparison-morphism", "def-weil-scheme-morphism-properties", "lem-sf-fullcd-detection-equivalence", "lem-sf-proetale-constructible-origin", "thm-sf-fullcd-etale-origin"]
+++
Fix the global finite-field datum, a prime $\ell\ne p$, $n\geq1$,
$A=A_{E,n}$, $k=\overline{\mathbf F}_q$, finite-type $k$-schemes $Y$
and $\overline X$ with $\dim\overline X\leq d$
([def-weil-scheme-morphism-properties]) and a proper finite-type
morphism $p:\overline X\to Y$. Then the vanishing required by
[def-weil-full-cohomological-dimension] holds for every coefficient
sheaf of the blueprint's class [def-sf-fullcd-used-class], with the
bound $c=2d$ and uniformly over all base changes $V\to Y$ of
$Y_{\Proet}$; that is,

$$
\mathcal H^r\bigl(R(p_V)_*(\mathcal F|_{\overline X\times_YV})\bigr)=0
\qquad(r>2d)
$$

for every base change $V\to Y$ and every $\mathcal F$ of that class.
Moreover that class is closed under inverse image along morphisms of
finite-type $k$-schemes, under extensions and under colimits, and it
contains the constant coefficient sheaf and every sheaf of étale origin.

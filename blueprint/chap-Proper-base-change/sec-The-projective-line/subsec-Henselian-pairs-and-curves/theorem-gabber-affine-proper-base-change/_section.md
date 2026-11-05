+++
id = "theorem-gabber-affine-proper-base-change"
kind = "theorem"
title = "Gabber's affine analogue of proper base change"
order = 355
lean = ["AlgebraicGeometry.Etale.bijective_cohomologyMap_of_henselianRing"]
uses = ["definition-torsion-sheaves"]
aliases = ["remark-henselian-pairs-facts"]
+++
Let $(B,J)$ be a henselian pair and let $G$ be a torsion abelian sheaf on
$\operatorname{Spec}(B)_{\acute{e}t}$. Then restriction induces isomorphisms

$$
H^q(\operatorname{Spec}B,G)
\xrightarrow{\sim}
H^q(\operatorname{Spec}(B/J),G|_{\operatorname{Spec}(B/J)})
\qquad(q\geq0).
$$

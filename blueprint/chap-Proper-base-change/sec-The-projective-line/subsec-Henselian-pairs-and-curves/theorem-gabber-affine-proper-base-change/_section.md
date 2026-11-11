+++
id = "theorem-gabber-affine-proper-base-change"
kind = "theorem"
title = "Gabber's affine analogue of proper base change"
order = 355
lean = ["AlgebraicGeometry.Etale.bijective_cohomologyMap_of_henselianRing"]
aliases = ["remark-henselian-pairs-facts"]
uses = ["definition-ind-etale-pro-etale-weakly", "lemma-stability", "definition-small-pro-etale-site", "proposition-topos-functoriality", "proposition-comparison-morphism-inverse-image", "definition-underived-base-change-map", "definition-torsion-sheaves", "lemma-acyclic-resolutions", "lemma-finiteness-small-etale-topoi", "lemma-finite-morphisms", "definition-compactification-refinement", "lemma-schematic-closure-uniqueness", "lemma-uniqueness-maps-dense-open", "theorem-chow-s-lemma-projective-form", "lemma-finite-direct-images", "lemma-finite-morphisms-cohomology"]
+++
Let $(B,J)$ be a henselian pair and let $G$ be a torsion abelian sheaf on
$\operatorname{Spec}(B)_{\acute{e}t}$. Then restriction induces isomorphisms

$$
H^q(\operatorname{Spec}B,G)
\xrightarrow{\sim}
H^q(\operatorname{Spec}(B/J),G|_{\operatorname{Spec}(B/J)})
\qquad(q\geq0).
$$

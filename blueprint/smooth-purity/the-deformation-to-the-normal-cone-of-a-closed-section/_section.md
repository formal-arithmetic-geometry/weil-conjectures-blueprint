+++
id = "the-deformation-to-the-normal-cone-of-a-closed-section"
kind = "section"
title = "The deformation to the normal cone of a closed section"
order = 3596
uses = ["cor-pur-vector-bundle-purity", "def-coefficient-twists-detailed", "def-pur-co-smoothness", "def-pur-conventions", "def-pur-normal-bundle", "def-sbc-affine-space", "def-sbc-smooth-morphisms", "def-weil-derived-cohomology-sheaves", "def-weil-derived-direct-image", "def-weil-derived-pullback-tensor-hom", "def-weil-derived-tensor", "def-weil-pbc-proetale-site", "def-weil-scheme-morphism-properties", "fix-prop-adjunctions", "lem-cbc-proetale-stalk-conservative", "lem-pur-divisor-class", "lem-pur-regular-immersion-linearization", "lem-pur-support-localization-triangle", "lemma-weil-pbc-perfect-projection-formula", "prop-weil-pbc-inverse-image-derived-adjunction", "sbc-lem-affine-space-smooth", "sbc-thm-etale-local-normal-form", "thm-pur-affine-line-orientation", "thm-pur-cohomological-smoothness", "thm-pur-p1-decomposition", "thm-pur-rank-one-local-calculation", "thm-pur-td-criterion"]
+++
This section contains the only descent statement of the chapter, and it
belongs to the ordinary abelian category of sheaves: after the family
object has been reduced to a shift of a finite locally constant sheaf,
the glueing is the sheaf axiom. The two statements carrying that
descent are the reduction of a complex with cohomology in a single
degree to a shift of a sheaf, [lem-pur-concentrated-complex-shift],
and the full faithfulness of the pullback along the affine line,
[lem-pur-a1-direct-image] together with
[prop-pur-a1-pullback-full-faithful]: on the overlaps of a cover
the local models of the family differ by an automorphism of a
pulled-back object, and full faithfulness identifies that automorphism
with one on the base, where the normalization at $t=1$ kills it. The
descent itself is the constancy of the deformation family along the
affine line, [prop-pur-dnc-family-constancy]: the family object is
the pullback of its own fibre at $t=1$, and the DNC invariance of the
section invariant, [thm-pur-dnc-invariance], is its restriction
at $t=0$. The remaining lemmas of the section (the rigidity of
morphisms of finite locally constant sheaves, the connected components
of the affine line over a base, and the automorphisms of a rank-one
finite locally constant sheaf) are the one-categorical uniqueness
statements used by [lem-pur-lisse-uniqueness] and in the trace
formula chapter.

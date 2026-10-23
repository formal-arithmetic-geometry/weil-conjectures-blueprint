+++
id = "lem-sfb-pushforward-comp-monoidal"
kind = "lemma"
title = "The composition isomorphism of pushforwards is monoidal"
order = 1112
uses = ["lem-weil-pbc-sheaf-tensor-closed", "def-sfb-finite-lower-star-comp", "def-sfb-finite-lower-star-lax-monoidal"]
lean = ["AlgebraicGeometry.ProEtale.isMonoidal_lowerStarComp"]
+++
Let $\mathcal A$ be a closed braided monoidal Grothendieck abelian category (for
instance $\mathcal A=\Ab$), and let $f\colon X\to Y$, $g\colon Y\to Z$ be morphisms of
schemes. The composition isomorphism $g_*\circ f_*\cong(g\circ f)_*$ of pushforwards
of $\mathcal A$-valued pro-étale sheaves
([def-sfb-finite-lower-star-comp]), induced by the canonical isomorphisms
$(V\times_ZY)\times_YX\cong V\times_ZX$, is a monoidal natural isomorphism for the
lax monoidal structures of [def-sfb-finite-lower-star-lax-monoidal] (composed on
$g_*\circ f_*$) and the tensor product of
[lem-weil-pbc-sheaf-tensor-closed].

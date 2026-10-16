+++
id = "lem-exc-proetale-support-triangle"
kind = "lemma"
title = "Pro-etale closed-support triangle before constructible restriction"
lean = ["AlgebraicGeometry.ProEtale.subsingleton_hom_shift_rightDerivedFunctor_lowerStar", "AlgebraicGeometry.ProEtale.exists_distTriang_derivedLowerStarClosedUpperShriekAdjunction_counit", "AlgebraicGeometry.ProEtale.existsUnique_distTriang_closedSupportTriangle", "AlgebraicGeometry.ProEtale.existsUnique_triangleHom_closedSupportTriangle"]
order = 2210
uses = ["def-weil-derived-direct-image", "def-weil-open-closed-recollement", "def-weil-pbc-proetale-site", "def-weil-scheme-morphism-properties", "lem-exc-proetale-closed-essential-image", "lem-exc-proetale-closed-support", "prop-exc-open-adjoint", "prop-weil-pbc-kinjective-resolutions-exist"]
+++
Let $T$ be Noetherian, let $i:Z\hookrightarrow T$ be a
closed immersion, and
let $j$ be its open complement. For a finite ring $A$, let
$Ri^!$ denote the right adjoint of the
direct image $i_*$ on the
pro-etale sites, taken on
the ambient ordinary derived categories, and let $Rj_*$ and $j^*$
be the direct image and the
inverse image of the open immersion $j$. In addition to the
open–closed triangle,
one has

$$
i_*Ri^!K\longrightarrow K\longrightarrow Rj_*j^*K
\longrightarrow i_*Ri^!K[1]
\qquad(K\in D(T_{\mathrm{proet}},A)).
$$

No constructibility of $Ri^!K$ is part of this assertion.

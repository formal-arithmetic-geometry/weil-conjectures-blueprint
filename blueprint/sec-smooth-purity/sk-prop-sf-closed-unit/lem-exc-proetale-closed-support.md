+++
id = "lem-exc-proetale-closed-support"
kind = "lemma"
title = "Pro-etale closed support before constructible restriction"
lean = ["AlgebraicGeometry.ProEtale.lowerStarClosedUpperShriekAdjunction", "AlgebraicGeometry.ProEtale.derivedLowerStarClosedUpperShriekAdjunction"]
order = 2203
uses = ["def-exc-proetale-sections-with-support", "def-weil-derived-direct-image", "def-weil-pbc-proetale-site", "def-weil-scheme-morphism-properties", "lem-exc-proetale-closed-essential-image", "lem-exc-proetale-closed-exact", "lem-exc-proetale-closed-fully-faithful", "prop-exc-open-adjoint", "prop-weil-pbc-kinjective-resolutions-exist"]
+++
Let $T$ be Noetherian, let $i:Z\hookrightarrow T$ be a
closed immersion, and
let $j$ be its open complement. For a finite ring $A$, the
direct image $i_*$ on
the pro-etale sites has a
right adjoint on the ambient ordinary derived categories, given by
the right derived functor of
$i^!_0$.
No constructibility is assumed of the
values of this right adjoint; it exists on the whole ambient
categories.

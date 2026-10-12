+++
id = "lem-weil-pbc-sheafification-sets-exact"
kind = "lemma"
title = "Sheafification of presheaves of sets commutes with finite limits"
uses = ["def-weil-pbc-sheafification"]
refines = "proof/lem-weil-pbc-etale-inverse-image-algebraic-structures"
lean = ["CategoryTheory.instPreservesFiniteLimitsFunctorOppositeSheafPresheafToSheaf"]
tags = ["sheaf-dag", "mathlib", "stacks-00WJ"]
+++
Let $\mathcal C$ be a site whose underlying category has a set of objects and morphisms, $\mathrm{PSh}(\mathcal C)$ the category of presheaves of sets on $\mathcal C$, $\Sh(\mathcal C)$ the full subcategory of sheaves of sets, and $\#:\mathrm{PSh}(\mathcal C)\to\Sh(\mathcal C)$ the sheafification [def-weil-pbc-sheafification], left adjoint to the inclusion. Then $\#$ commutes with finite limits; in particular it sends the final presheaf $*$ to the final sheaf $*$ and a product $\mathcal F_1\times\mathcal F_2$ (computed sectionwise) to $\mathcal F_1^\#\times\mathcal F_2^\#$ via the projections.

+++
id = "lem-weil-pbc-presheaf-finite-limits-objectwise"
kind = "lemma"
title = "Finite limits of A-valued presheaves are objectwise; the inclusion of sheaves preserves them; the sheafification counit is an isomorphism"
refines = "proof/lem-weil-pbc-free-sheaf-flat"
lean = ["CategoryTheory.preservesFiniteLimits_of_evaluation"]
tags = ["sheaf-dag", "mathlib", "stacks-03CO"]
+++
Let $\mathcal C$ be a category with a Grothendieck topology $J$, let $\mathcal A$ be a category with finite limits, let $\mathrm{PSh}(\mathcal C;\mathcal A)$ be the category of functors $\mathcal C^{op}\to\mathcal A$ and $\iota:\mathrm{Sh}(\mathcal C,J;\mathcal A)\to\mathrm{PSh}(\mathcal C;\mathcal A)$ the inclusion of the full subcategory of sheaves. Then: (1) for every object $V$ of $\mathcal C$ the evaluation $\mathrm{ev}_V:G\mapsto G(V)$ preserves finite limits, and a functor $\Phi:\mathcal D\to\mathrm{PSh}(\mathcal C;\mathcal A)$ from any category $\mathcal D$ preserves finite limits as soon as $\mathrm{ev}_V\circ\Phi$ does for every object $V$ (finite limits of presheaves are computed objectwise); (2) $\iota$ preserves finite limits; (3) if a left adjoint $a$ of $\iota$ (sheafification) exists, then the counit $a\iota F\to F$ is an isomorphism for every sheaf $F$.

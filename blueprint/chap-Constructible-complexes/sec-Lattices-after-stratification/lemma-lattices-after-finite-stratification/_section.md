+++
id = "lemma-lattices-after-finite-stratification"
kind = "lemma"
title = "Lattices after a finite stratification"
order = 289
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.exists_stratified_lisse_integral_lattice"]
uses = ["definition-ind-etale-pro-etale-weakly", "lemma-stability", "definition-small-pro-etale-site", "proposition-topos-functoriality", "example-locally-constant-functions-w-local", "proposition-pro-etale-site-separably-closed", "corollary-finite-quotients-their-transition-maps", "lemma-inverse-image-coefficient-sheaves"]
+++
Let $L$ be a [lisse](@definition-lisse-sheaves) [$E_X$](@lemma-comparison-completed-coefficients)-module. There is a finite stratification of $X$
by locally closed subschemes $S$ such that each $L|_S$ contains a [lisse](@definition-lisse-sheaves)
[$\mathcal O_{E,S}$](@lemma-comparison-completed-coefficients)-submodule $L_0$ with $L_0[1/\ell]=L|_S$.

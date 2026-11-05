+++
id = "lemma-lattices-after-finite-stratification"
kind = "lemma"
title = "Lattices after a finite stratification"
order = 289
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.exists_stratified_lisse_integral_lattice", "AlgebraicGeometry.ProEtale.CondensedRing.continuousLisse_stratified_lattices"]
uses = ["definition-ind-etale-pro-etale-weakly", "lemma-stability", "definition-small-pro-etale-site", "proposition-topos-functoriality", "example-locally-constant-functions-w-local"]
+++
Let $L$ be a lisse $E_X$-module. There is a finite stratification of $X$
by locally closed subschemes $S$ such that each $L|_S$ contains a lisse
$\mathcal O_{E,S}$-submodule $L_0$ with $L_0[1/\ell]=L|_S$.

+++
id = "lemma-lattices-lisse-e-sheaves"
kind = "lemma"
title = "Lattices in lisse $E$-sheaves"
order = 260
lean = ["AlgebraicGeometry.ProEtale.exists_lisse_lattice_etale_local", "AlgebraicGeometry.ProEtale.CondensedRing.continuousLisse_etale_lattice"]
uses = ["definition-ind-etale-pro-etale-weakly", "lemma-stability", "definition-small-pro-etale-site", "proposition-topos-functoriality", "lemma-proper-direct-image-unbounded-complexes"]
+++
Let $E/\mathbf Q_\ell$ be finite and let $L$ be a lisse $E_X$-module. The sheaf on
$X_{\mathrm{pro}\acute{e}t}$ of lattices in $L$ is represented
by a separated surjective étale $X$-scheme, with a universal lattice.
In particular, $L$ admits a lattice étale locally on $X$.

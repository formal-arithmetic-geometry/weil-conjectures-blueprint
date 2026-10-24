+++
id = "lem-weil-pbc-ind-etale-basis"
kind = "lemma"
title = "The ind-etale subsite is a basis"
order = 958
lean = ["AlgebraicGeometry.Scheme.AffineProEt.isCoverDense_toProEt", "AlgebraicGeometry.Scheme.AffineProEt.exists_finite_jointly_surjective_of_mem_topology", "AlgebraicGeometry.Scheme.AffineProEt.isEquivalence_sheafPushforwardContinuous_toProEt"]
uses = ["def-weil-pbc-ind-etale-basis", "def-weil-pbc-proetale-site", "lem-weil-pbc-ind-etale-stability", "thm-weil-pbc-weak-etale-refinement"]
+++
Let $X$ be a scheme. Every object of $X_{\Proet}$ has a covering by objects
of $\mathcal B_X$. Every covering of a basis object has a refinement by a
finite jointly surjective family of basis objects. Fibre products of basis
objects over a basis object remain in the basis. Restriction to this basis
induces an equivalence between sheaves on $X_{\Proet}$ and sheaves on
$\mathcal B_X$ (with values in abelian groups, or in any category with
sufficiently large limits); in particular it determines a sheaf and its
morphisms uniquely and detects isomorphisms of sheaves.

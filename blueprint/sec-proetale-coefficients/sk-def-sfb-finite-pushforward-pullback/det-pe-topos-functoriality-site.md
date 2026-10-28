+++
id = "det-pe-topos-functoriality-site"
kind = "lemma"
title = "The pro-étale site is subcanonical and essentially small"
lean = ["AlgebraicGeometry.Scheme.ProEt.topology", "CategoryTheory.GrothendieckTopology.subcanonical_of_full_of_faithful", "CategoryTheory.GrothendieckTopology.hasSheafify_proEtTopology"]
order = 916
uses = ["def-weil-pbc-proetale-site", "def-weil-pbc-proetale-covering", "lem-trf-weakly-etale-between-objects", "lem-weil-pbc-ind-etale-stability"]
+++
Let $X$ be a scheme and $X_{\mathrm{proét}}$ its small pro-étale site
[def-weil-pbc-proetale-site].

1. The pro-étale coverings [def-weil-pbc-proetale-covering] of objects of
   $X_{\mathrm{proét}}$ satisfy the axioms of a site: isomorphisms are coverings; if
   $\{U_i\to U\}$ is a covering and $\{U_{ij}\to U_i\}$ are coverings, then
   $\{U_{ij}\to U\}$ is a covering; if $\{U_i\to U\}$ is a covering and $V\to U$ is a
   morphism of $X_{\mathrm{proét}}$, then the fibre products $U_i\times_UV$ exist in
   $X_{\mathrm{proét}}$ and $\{U_i\times_UV\to V\}$ is a covering.
2. For every object $T$ of $X_{\mathrm{proét}}$ the representable presheaf
   $h_T=\Hom_X(-,T)$ is a sheaf; that is, the topology is subcanonical.
3. $X_{\mathrm{proét}}$ is essentially small (with respect to the universe one above that of
   the schemes), so for every Grothendieck abelian category $\mathcal A$ (with morphism groups
   of that size) sheafification of $\mathcal A$-valued presheaves on $X_{\mathrm{proét}}$
   exists.

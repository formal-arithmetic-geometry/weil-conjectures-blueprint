+++
id = "the-comparison-of-the-etale-and-pro-etale-sites"
kind = "section"
title = "The comparison of the etale and pro-etale sites"
order = 1316
uses = ["def-weil-pbc-cartesian-square-detailed", "def-weil-pbc-derived-categories", "def-weil-pbc-direct-image", "def-weil-pbc-etale-cohomology", "def-weil-pbc-etale-sheaves", "def-weil-pbc-etale-site", "def-weil-pbc-etale-sum-extension", "def-weil-pbc-ind-etale-algebra", "def-weil-pbc-inverse-image", "def-weil-pbc-proetale-modules", "def-weil-pbc-proetale-operations", "def-weil-pbc-proetale-site", "def-weil-pbc-scheme-conventions", "lem-weil-pbc-derived-cohomology-continuity", "lem-weil-pbc-etale-finite-data-descent", "lem-weil-pbc-etale-restriction-injectives", "lem-weil-pbc-etale-section-continuity", "lem-weil-pbc-ind-etale-stability", "prop-weil-pbc-inverse-image-exact", "prop-weil-pbc-kinjective-resolutions-exist", "prop-weil-pbc-proetale-constant-exact", "thm-weil-pbc-weak-etale-refinement"]
+++
The comparison morphism of sites $\nu_T:T_{\Proet}\to T_{\Et}$
[def-weil-pbc-site-comparison-morphism] is fully faithful on bounded-below
complexes of finite-coefficient sheaves
[thm-weil-pbc-site-comparison]. The geometric input is that the affine
ind-etale objects form a basis [def-weil-pbc-ind-etale-basis],
[lem-weil-pbc-ind-etale-basis] on which sections of $\nu^*F$ are a filtered
colimit of etale sections [lem-weil-pbc-comparison-sections], so that pulled
back etale injectives are acyclic
[lem-weil-pbc-comparison-injective-acyclicity] — checked through the Cech
criterion [lem-weil-pbc-cech-criterion]. Comparison commutes with pullback
[lem-weil-pbc-comparison-pullback] and with direct image
[prop-weil-pbc-comparison-direct-image], hence transports the etale exchange
map to the pro-etale one [lem-weil-pbc-transport-identifies-exchange], which
gives proper base change on the pro-etale site for every complex carrying an
etale-origin witness [def-weil-pbc-etale-origin-witness],
[thm-weil-pbc-finite-level-proetale].

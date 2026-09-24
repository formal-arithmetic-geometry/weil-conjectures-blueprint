+++
id = "pro-etale-transport-of-the-exchange-map"
kind = "section"
title = "Pro-etale transport of the exchange map"
order = 1925
uses = ["def-weil-pbc-cartesian-square", "def-weil-pbc-derived-exchange", "def-weil-pbc-etale-origin-witness", "def-weil-pbc-proetale-operations", "def-weil-pbc-scheme-conventions", "def-weil-pbc-site-comparison-morphism", "lem-weil-pbc-comparison-pullback", "prop-weil-pbc-comparison-direct-image", "thm-weil-pbc-bounded-below", "thm-weil-pbc-site-comparison"]
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

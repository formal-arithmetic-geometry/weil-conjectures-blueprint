+++
id = "lem-sp-couple-morphism"
kind = "lemma"
title = "Morphisms of couples give morphisms of spectral sequences"
order = 519
uses = ["def-sp-convergence", "def-sp-exact-couple", "def-sp-filtration", "thm-sp-half-plane-convergence"]
+++
A morphism $(t_D,t_E):(D,E,\alpha,f,g)\to(D',E',\alpha',f',g')$ of exact
couples [def-sp-exact-couple] (two maps compatible with all structure maps)
induces, for every $r$, a morphism $E_r\to E'_r$ of the spectral sequences,
compatible with the differentials. If both couples satisfy the hypotheses of
[thm-sp-half-plane-convergence], then the map $t_D:D^{0,n}\to D'^{0,n}$ of
their canonical abutments respects the filtrations
[def-sp-filtration] constructed there, and induces $t_E$ on the associated
graded pieces.

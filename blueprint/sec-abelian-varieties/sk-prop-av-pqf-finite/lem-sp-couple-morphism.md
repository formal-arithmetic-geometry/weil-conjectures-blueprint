+++
id = "lem-sp-couple-morphism"
kind = "lemma"
title = "Morphisms of couples give morphisms of spectral sequences"
lean = ["CategoryTheory.ExactCouple.Hom", "CategoryTheory.ExactCouple.Hom.spectralSequenceMap", "CategoryTheory.ExactCouple.Hom.derived", "CategoryTheory.ExactCouple.Hom.derivedIter", "CategoryTheory.ExactCouple.halfPlaneFiltration_F_eq"]
order = 535
uses = ["def-sp-exact-couple", "def-sp-filtration", "thm-sp-half-plane-convergence"]
+++
A morphism $(t_D,t_E):(D,E,\alpha,f,g)\to(D',E',\alpha',f',g')$ of exact
couples [def-sp-exact-couple] (two maps compatible with all structure maps)
induces a morphism of the derived couples, hence of all iterated derived
couples, and so, for every $r$, a morphism of complexes
$(E_r,d_r)\to(E'_r,d'_r)$; these form a morphism of spectral sequences, i.e.
they are compatible with the identifications $\mathcal H(E_r)\cong E_{r+1}$.
If both couples satisfy the hypotheses of [thm-sp-half-plane-convergence],
then the map $t_D:D^{0,n}\to D'^{0,n}$ of their canonical abutments respects
the filtrations [def-sp-filtration] constructed there.

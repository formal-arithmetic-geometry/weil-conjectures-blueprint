+++
id = "lemma-vanishing-generic-points-principal-divisor"
kind = "lemma"
title = "Vanishing at the generic points of a principal divisor"
order = 1630
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.exists_dense_isZero_specializationDefect"]
uses = ["definition-ind-etale-pro-etale-weakly", "lemma-stability", "definition-small-pro-etale-site", "proposition-topos-functoriality", "lemma-inverse-image-coefficient-sheaves", "definition-constructible-sheaves", "definition-lisse-sheaves", "lemma-proper-direct-image-unbounded-complexes"]
+++
Suppose that $X$ is normal, that $Z\subset X$ is an effective principal Cartier
divisor, and that $i^*L=0$.  Then $C_{X,Z}(L)$ vanishes at every generic
point of $Z$.

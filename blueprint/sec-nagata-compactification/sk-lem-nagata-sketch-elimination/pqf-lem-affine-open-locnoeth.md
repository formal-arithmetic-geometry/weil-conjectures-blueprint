+++
id = "pqf-lem-affine-open-locnoeth"
kind = "lemma"
title = "Local Noetherianity can be checked on an affine covering"
order = 204
lean = ["AlgebraicGeometry.isLocallyNoetherian_of_affine_cover", "AlgebraicGeometry.isLocallyNoetherian_iff_of_iSup_eq_top"]
uses = ["pqf-def-locnoeth"]
+++
Let $S$ be a scheme and let $S=\bigcup_iU_i$ be a covering by affine
opens. Then $S$ is locally Noetherian if and only if $\mathcal O_S(U_i)$
is Noetherian for every $i$. In particular, if $S$ admits some affine open
covering by spectra of Noetherian rings, then for every affine open
$\operatorname{Spec}A\subset S$ the ring $A$ is Noetherian.

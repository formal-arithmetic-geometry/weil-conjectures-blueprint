+++
id = "det-pe-replete-on-contractible"
kind = "lemma"
title = "Sequential limits along epimorphisms on a weakly contractible object"
lean = ["AlgebraicGeometry.Scheme.proetale_surjective_sections_of_epi_tower"]
order = 976
uses = ["det-pe-replete-definition", "det-pe-weak-contractible-equivalences"]
+++
Let $(F_n,t_n)$ be an inverse sequence of sheaves of sets on $X_{\mathrm{proét}}$ with
epimorphic transition maps, and let $W$ be a weakly contractible object. Then every
$t_n(W)\colon F_{n+1}(W)\to F_n(W)$ is surjective, and for every $m$ the projection
$(\varprojlim_nF_n)(W)\to F_m(W)$ is surjective.

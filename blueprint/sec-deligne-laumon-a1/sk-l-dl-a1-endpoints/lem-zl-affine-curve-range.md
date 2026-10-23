+++
id = "lem-zl-affine-curve-range"
kind = "lemma"
title = "Cohomological range of an affine curve"
order = 3981
uses = ["def-compact-support-direct-image-detailed", "def-weil-ordinary-compact-cohomology", "sk-lem-coefficient-heart", "sk-def-sf-weil-complexes", "sk-thm-sfb-qlbar-two-colimit", "sk-prop-sfb-finite-extension-compatibility", "sk-lem-stratified-lattice", "sk-prop-scalar-six", "sk-prop-integral-criterion", "sk-thm-sf-ctf-stability", "def-pe-derived-complete", "lem-sc-cohomological-dimension", "lem-sc-compactification", "lem-weil-pbc-mittag-leffler", "sbc-thm-finiteness-finite-type"]
lean = ["AlgebraicGeometry.WeilSheaf.subsingleton_compactlySupportedCohomology_of_isAffine"]
+++
If $C_0$ is a smooth affine curve over $k_0$ (affine and smooth of
relative dimension one) and $\mathcal F$ is a constructible $\Qlb$-Weil sheaf on
$C_0$, that is, $\mathcal F\in\Cons(C,\Qlb)$ ([sk-lem-coefficient-heart]) with a Weil
structure ([sk-def-sf-weil-complexes]), then
$H_c^i(C,\mathcal F)=0$ for $i\notin\{0,1,2\}$.

+++
id = "sbc-thm-finite-proetale-smooth-base-change"
kind = "theorem"
title = "Finite pro-étale smooth base change"
order = 5240
lean = ["AlgebraicGeometry.Proetale.smooth_base_change_finiteLevel"]
uses = ["sbc-thm-smooth-base-change", "sbc-thm-bounded-derived-smooth-base-change", "sbc-def-base-change-square", "def-sbc-smooth-morphisms"]
+++
In the square [sbc-def-base-change-square] of [sbc-thm-smooth-base-change],
assume $f$ smooth, $g$ quasi-compact and quasi-separated, and all schemes
Noetherian. For $K\in\Dbc(T_{\Proet},\Lambda)$ (constructed over the
pro-étale site) whose finite-level reductions $K_n$ come from the étale
site, the pro-étale exchange map
$$
Lf^*_{\Proet}Rg_{*,\Proet}K\xrightarrow{\ \sim\ }Rh_{*,\Proet}Le^*_{\Proet}K
$$
is an isomorphism, obtained by conjugating the étale exchange isomorphism of
[sbc-thm-bounded-derived-smooth-base-change] by the site comparison
equivalences.

## Proof

The bounded étale comparison makes $\nu^*$ an equivalence between the
bounded constructible étale and pro-étale categories; the comparison
isomorphisms for pullback and direct image transfer the exchange map of
[sbc-thm-bounded-derived-smooth-base-change] to the pro-étale site, and the
transport-identifies-exchange lemma shows that the transferred map is the
unit–counit exchange of the pro-étale six-functor calculus. The finite-level
reductions being étale, $K$ is in the essential image of $\nu^*$, so the
transported isomorphism is the displayed one.

Unresolved dependencies: def:weil-pbc-proetale-modules, def:weil-pbc-proetale-site, thm:weil-pbc-site-comparison, lem:weil-pbc-comparison-pullback, prop:weil-pbc-comparison-direct-image

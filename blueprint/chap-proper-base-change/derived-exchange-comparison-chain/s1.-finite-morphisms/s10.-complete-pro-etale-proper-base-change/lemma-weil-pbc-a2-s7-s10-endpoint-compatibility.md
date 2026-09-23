+++
id = "lemma-weil-pbc-a2-s7-s10-endpoint-compatibility"
kind = "lemma"
title = "A2 compatibility with every S7–S10 endpoint"
order = 1893
uses = ["lemma-weil-pbc-a2-comparison-rfshriek-transport", "lemma-weil-pbc-a2-reduction-tensor-transport", "lemma-weil-pbc-bounded-constructible-reconstruction", "lemma-weil-pbc-completed-exchange-coherence", "lemma-weil-pbc-completed-map-reduction", "lemma-weil-pbc-completed-pullback-reduction", "lemma-weil-pbc-completed-tensor-reduction", "lemma-weil-pbc-projection-formula-identity-compactification", "prop-weil-pbc-proet-finite-level-transport", "prop-weil-proet-finite-derived-proper-base-change"]
+++
Let $K\in\mathsf C_\square(X)$. After the transports $\chi$ and $\omega$:

1. the A2 finite etale map $b_n$ is the S7 unit–counit exchange map;
1. the A2 transported pro-etale map $\widetilde\beta_n$ is the S8 map
$v'_n$;
1. the A2 product-cone map $\beta_K^{\mathrm{proet}}$ is the S10 completed
map $\xi_K$;
1. the $n$-th reduction of either completed alias is exactly
$\widetilde\beta_n$, and the equations are compatible with every tower
transition, compatible tower endomorphism, identity square, and pasted
square.

All four equalities are independent of the rebinding certificate chosen for
$K$.

## Proof

The A2 definition of $b_n$ and the S7 definition both use the adjunction unit,
the chosen Cartesian equality $fg'=gf'$, and the adjunction counit, in that
order. Hence their resolved representatives are the same chain map. By the
preceding lemma, the four A2 etale/pro-etale comparison arrows are the four S8
arrows. Pasting the same comparison squares around the common middle map
$b_n$ therefore makes $\widetilde\beta_n=v'_n$.

The A2 completed map and the S10 completed map are both induced from the
tower $(v'_n)_n$ on the product-cone model. The reduction and tensor
transports commute with the transitions, so the induced maps on both products
are componentwise equal and their cone maps are equal. The completed
reduction square then gives

$$
\delta_n\,\xi_K=v'_n\,\alpha_n,
$$

which is precisely the fourth assertion under $\chi$. S7 naturality, S8
comparison naturality, the S9 tower equations, and S10 completed coherence
give the transition, operator, identity, and pasting equations. Finally,
the certificate supplies only membership and bound witnesses: none occurs in
the unit–counit formula or in the product-cone map. Changing it therefore
leaves every displayed morphism unchanged.

Unresolved dependencies: def:weil-a2-finite-etale-proper-base-change-map, def:weil-a2-proetale-proper-base-change-map, def:weil-a2-transported-finite-level-base-change-map

+++
id = "lem-a1-unramified-at-infinity"
kind = "lemma"
title = "Removing a regular point to arrange infinity"
lean = ["AlgebraicGeometry.WeilSheaf.hasWeightsAtMostOver_compactlySupportedCohomology_one_of_projectiveLine", "AlgebraicGeometry.WeilSheaf.LisseOnDenseOpen.hasWeightsAtMostOver_compactlySupportedCohomology_one_of_isPunctuallyPureOfWeight", "AlgebraicGeometry.exists_toProjectiveLine_isFinite_etale_near_infinity"]
order = 4256
uses = ["def-weil-open-closed-recollement", "def-weil-ordinary-compact-cohomology", "def-weil-pbc-scheme-conventions", "def-weil-punctual-weights", "def-wf-middle-extension", "lem-a1-finite-boundary-cohomology", "lem-wf-dense-open-pi1-surjective", "prop-sf-open-closed-triangle-all-stages"]
+++
Let $\mathcal F$ be a punctually pure lisse Weil sheaf of weight $w$
on a dense open $W_0\subset\mathbf P^1_{k_0}$.
After a finite constant-field extension, there are a dense open
$V_0\subset\mathbf A^1$ and a lisse sheaf $\mathcal E$ on $V_0$,
punctually pure of the same weight, with trivial local inertia at
infinity, together with a Frobenius-equivariant surjection

$$
H_c^1(V,\mathcal E)\twoheadrightarrow H_c^1(W,\mathcal F).
$$

Geometric irreducibility is preserved.

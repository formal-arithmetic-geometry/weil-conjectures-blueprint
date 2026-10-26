+++
id = "lem-sc-line-bundle-rational-section"
kind = "lemma"
title = "Rational sections of line bundles"
order = 678
lean = ["AlgebraicGeometry.Scheme.Modules.exists_nonempty_iso_dual_toModules_idealSheaf_tensorObj"]
uses = ["def-pc-divisor-line-bundle", "def-sc-divisor", "def-sc-function-field", "lem-sc-point-cartier", "lem-sc-regular-dim1-dvr", "lem-sc-smooth-regular"]
+++
Let $k$ be a field and $C$ a Noetherian integral scheme which is smooth
of relative dimension $1$ over $k$, and let $\mathcal L$ be an invertible
$\mathcal O_C$-module. Then there are effective divisors $E_1,E_2$ on $C$
([def-sc-divisor]) with

$$
\mathcal L\;\cong\;\mathcal O_C(E_1)\otimes\mathcal O_C(-E_2),
$$

where $\mathcal O_C(-E)=\mathcal I_E=\prod_P\mathcal I_P^{n_P}$ is the ideal
sheaf of the effective divisor $E=\sum_Pn_P[P]$ and
$\mathcal O_C(E)=\mathcal I_E^\vee$ ([def-pc-divisor-line-bundle]).

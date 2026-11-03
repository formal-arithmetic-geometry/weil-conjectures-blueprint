+++
id = "prop-pc-serre-duality-field-extension"
kind = "proposition"
title = "Serre duality commutes with field extension"
order = 732
tags = ["not-formalized"]
uses = ["det-thm-picard-duality", "lem-pc-flat-base-change-cohom", "def-pc-base-change", "def-sc-kahler-differentials"]
+++
Let $C$ be a smooth proper curve over a field $k$ with $H^0(C,\cO_C)=k$, let $K/k$ be a
field extension, and let $\cL$ be an invertible sheaf on $C$. Identify
$H^i(C_K,\cL_K)=H^i(C,\cL)\otimes_kK$ by flat base change and
$\omega_{C_K/K}=(\omega_{C/k})_K$. Then the Serre duality isomorphism
([det-thm-picard-duality])

$$
H^1(C_K,\cL_K)^\vee\simeq H^0(C_K,\omega_{C_K/K}\otimes\cL_K^{-1})
$$

for $\cL_K$ on $C_K$ is the $K$-linear extension of the one for $\cL$ on $C$.

*Not formalized in Lean.* This is Corollary app:picard-duality-base-change of the tex,
split off from Theorem app:picard-riemann-roch. Nothing uses it; the numerical part
(genus and degree) is in the theorem. It is recorded here and will not be formalized.

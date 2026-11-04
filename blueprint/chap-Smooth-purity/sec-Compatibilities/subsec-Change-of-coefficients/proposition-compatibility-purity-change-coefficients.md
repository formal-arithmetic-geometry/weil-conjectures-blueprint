+++
id = "proposition-compatibility-purity-change-coefficients"
kind = "proposition"
title = "Compatibility of purity with change of coefficients"
order = 805
lean = ["AlgebraicGeometry.Etale.map_smoothPurityIso_hom_comp", "AlgebraicGeometry.Etale.map_smoothPurityTrace"]
uses = ["proposition-six-operations-change-coefficients"]
+++
Let $f:X\to Y$ be smooth of pure relative dimension $d$, let
$\Lambda\to\Lambda'$ be a coefficient map of
Proposition [proposition-six-operations-change-coefficients] and let
$K\in D^b_{\mathrm{ctf}}(Y,\Lambda)$. Then the change-of-coefficients isomorphism
$(f^!K)_{\Lambda'}\to f^!(K_{\Lambda'})$ carries
$(\gamma_{f,\Lambda}(K))_{\Lambda'}$ to $\gamma_{f,\Lambda'}(K_{\Lambda'})$, the
sources being identified by the change-of-coefficients isomorphism for $f^*$.
The same holds for the trace maps: the change-of-coefficients isomorphism for
$Rf_!$ carries $(\operatorname{Tr}_{f,\Lambda}(K))_{\Lambda'}$ to
$\operatorname{Tr}_{f,\Lambda'}(K_{\Lambda'})$.

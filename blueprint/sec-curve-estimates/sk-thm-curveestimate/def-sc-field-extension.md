+++
id = "def-sc-field-extension"
kind = "definition"
title = "Field extensions, base change, pullback maps"
lean = ["AlgebraicGeometry.Scheme.Hom.baseChangeField", "AlgebraicGeometry.Scheme.Hom.fieldExtensionCohomologyMap"]
order = 1515
uses = ["def-sc-curves"]
+++
Let $k\subseteq k'$ be a field extension and let $C$ be a scheme over $k$
(in this chapter $k\subseteq k'$ are algebraically closed and $C$ is a
curve over $k$). Put

$$
\pi_{k'}:C_{k'}:=C\times_kk'\longrightarrow C,
\qquad
F_{k'}:=\pi_{k'}^{-1}F
$$

for an etale sheaf $F$ on $C_{\Et}$, and let

$$
\rho^q_{k'/k}(C,F):H^q(C_{\Et},F)\longrightarrow
H^q((C_{k'})_{\Et},F_{k'})
$$

be the pullback map.

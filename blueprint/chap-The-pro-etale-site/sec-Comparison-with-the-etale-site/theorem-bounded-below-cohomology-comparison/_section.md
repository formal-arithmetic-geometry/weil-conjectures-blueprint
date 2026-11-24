+++
id = "theorem-bounded-below-cohomology-comparison"
kind = "theorem"
title = "Bounded-below cohomology comparison"
order = 123
lean = ["AlgebraicGeometry.ProEtale.boundedBelowComparison", "AlgebraicGeometry.ProEtale.boundedBelowComparisonGlobalSections"]
uses = ["definition-small-pro-etale-site", "proposition-comparison-morphism-inverse-image"]
+++
For $K\in D^+(X_{\acute{e}t},\Lambda)$ the unit of the adjunction between
$\href{@proposition-comparison-morphism-inverse-image}{\nu_X^*}:D^+(X_{\acute{e}t},\Lambda)\to D^+(\href{@definition-small-pro-etale-site}{X_{\mathrm{pro}\acute{e}t}},\Lambda)$ and
[$R\nu_{X,*}$](@proposition-comparison-morphism-inverse-image) is an isomorphism

$$
K\xrightarrow{\ \sim\ }\href{@proposition-comparison-morphism-inverse-image}{R\nu_{X,*}}\href{@proposition-comparison-morphism-inverse-image}{\nu_X^*K}.
\tag{2.7}
$$

Consequently $\href{@proposition-comparison-morphism-inverse-image}{\nu_X^*}:D^+(X_{\acute{e}t},\Lambda)\to D^+(\href{@definition-small-pro-etale-site}{X_{\mathrm{pro}\acute{e}t}},\Lambda)$ is fully faithful,
and there is a canonical isomorphism

$$
R\Gamma(\href{@definition-small-pro-etale-site}{X_{\mathrm{pro}\acute{e}t}},\href{@proposition-comparison-morphism-inverse-image}{\nu_X^*K})
\simeq R\Gamma(X_{\acute{e}t},K).
$$

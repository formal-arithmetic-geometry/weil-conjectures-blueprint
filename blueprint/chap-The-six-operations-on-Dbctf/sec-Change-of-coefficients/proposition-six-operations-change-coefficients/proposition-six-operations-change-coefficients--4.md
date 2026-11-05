+++
id = "proposition-six-operations-change-coefficients--4"
kind = "proposition"
title = "Compactly supported direct image: coefficient comparison"
order = 645008
aliases = ["bp-r197-4"]
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.boundedConstructibleLowerShriekExtendScalarsIso", "AlgebraicGeometry.ProEtale.CondensedRing.boundedConstructibleLowerShriekToPadicAlgClIso", "AlgebraicGeometry.ProEtale.CondensedRing.etaleReductionLowerShriekIsoOfCompactification"]
uses = ["definition-change-of-coefficients-maps", "proposition-six-operations-change-coefficients--1"]
+++
Let $f:X\to Y$ be a morphism of separated schemes of finite type over a field of characteristic $p\ne\ell$, and let $E\subset\Qbarl$ be finite over $\Qell$. For $\Lambda\to\Lambda'$ equal to $\mathcal O_E\to E$ or $E\to\Qbarl$, there is a natural isomorphism on bounded constructible complexes
$$
(Rf_{!,\Lambda}K)_{\Lambda'}\xrightarrow{\sim}Rf_{!,\Lambda'}(K_{\Lambda'}).
$$

For $n\geq 0$, let $\mathrm{red}_X:\Dbc(X,\mathcal O_E)\to D(X_{\acute{e}t},\mathcal O_E/\ell^n)$ denote derived reduction followed by the étale reading. Every compactification $c$ of $f$ gives a natural isomorphism
$$
\mathrm{red}_Y(Rf_{!,\mathcal O_E}K)\xrightarrow{\sim}Rf_{!,\mathcal O_E/\ell^n}(\mathrm{red}_XK),
$$
where the functor on the right is on the étale site.

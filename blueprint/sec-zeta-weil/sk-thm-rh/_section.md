+++
id = "sk-thm-rh"
kind = "theorem"
title = "Riemann hypothesis for smooth proper schemes"
order = 3253
lean = ["AlgebraicGeometry.Scheme.weil_conjectures", "Polynomial.IsUniversallyPureOfWeight"]
uses = ["sk-def-roots", "sk-def-zeta", "sk-prop-rootpurity", "sk-thm-intfactors"]
tags = ["sketch"]
+++
Let $X_0/\Fq$ be smooth, proper and geometrically connected of pure dimension
$d$, and let $P_i\in\Z[T]$ be the integral Frobenius factors of
[sk-thm-intfactors]. Then every reciprocal root $\alpha$ of $P_i$ is an
algebraic integer and a $q$-Weil number of weight $i$:

$$
|\tau(\alpha)|=q^{i/2}
\qquad\text{for every embedding }\tau:\Q(\alpha)\hookrightarrow\C .
$$

Equivalently, $|\tau(\beta)|=q^{-i/2}$ for every ordinary root $\beta$.

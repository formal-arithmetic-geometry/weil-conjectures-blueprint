+++
id = "sk-prop-deg0"
kind = "lemma"
title = "The degree-zero calculation"
order = 2054
uses = ["sk-def-bc", "sk-def-exchange"]
lean = ["AlgebraicGeometry.Etale.baseChangeProperty_zero", "AlgebraicGeometry.Etale.baseChangeProperty_zero_of_smooth"]
tags = ["sketch"]
+++
Consider a cartesian square with $u:X'\to X$, $f':X'\to Y'$, $f:X\to Y$ and $g:Y'\to Y$, and
the exchange map of étale sheaves of [sk-def-exchange].
Suppose that $g$ is flat and locally of finite
presentation with geometrically reduced fibres, and that $f$ is qcqs.
Then the exchange map
$g^{-1}f_*F_{\mathrm{\acute et}}\to f'_*u^{-1}F_{\mathrm{\acute et}}$ of sheaves
on $Y'_{\mathrm{\acute et}}$ is an isomorphism for every sheaf of sets
$F_{\mathrm{\acute et}}$ on $X_{\mathrm{\acute et}}$.

*Complement.* Let $\Lambda$ be a commutative ring. For a Cartesian square as in
[sk-def-bc] (so $g$ is quasi-compact and quasi-separated) in which
$f:X\to S$ is flat and locally of finite presentation with geometrically
reduced fibres (in particular for $f$ smooth), the degree-zero
base-change map

$$
f^{-1}g_*\mathcal F\longrightarrow h_*e^{-1}\mathcal F
$$

is an isomorphism, for *every* sheaf $\mathcal F$ of $\Lambda$-modules on
$T_{\Et}$ — no torsion hypothesis is needed in degree zero. Hence
$\mathrm{BC}(f,\Lambda,0)$ holds for such $f$, in particular for smooth $f$.

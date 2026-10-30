+++
id = "sk-prop-deg0"
kind = "lemma"
title = "The degree-zero calculation"
order = 400
lean = ["AlgebraicGeometry.Etale.baseChangeProperty_zero", "AlgebraicGeometry.Etale.baseChangeProperty_zero_of_smooth"]
uses = ["sk-def-bc", "sk-def-exchange"]
tags = ["sketch"]
+++
Suppose that $g$ in (9.1) is flat and locally of finite
presentation with geometrically reduced fibres, and that $f$ is qcqs.
Then the base change map $g^{-1}f_*F_{\acute{e}t}\to f'_*g'^{-1}F_{\acute{e}t}$ is an isomorphism for every sheaf of sets $F_{\acute{e}t}$ on
$X_{\acute{e}t}$.

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

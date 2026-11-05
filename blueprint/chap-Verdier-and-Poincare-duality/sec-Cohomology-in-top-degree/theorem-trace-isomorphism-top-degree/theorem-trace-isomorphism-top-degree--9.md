+++
id = "theorem-trace-isomorphism-top-degree--9"
kind = "theorem"
title = "Top-degree isomorphisms: algebraically closed coefficients"
order = 865018
aliases = ["bp-r260-9"]
lean = ["AlgebraicGeometry.WeilSheaf.traceIsomorphism_adicConstant"]
uses = ["definition-weil-structure", "definition-frobenius-operator", "definition-tate-twists"]
+++
Let $X_0/\Fq$ be smooth, separated, of finite type and geometrically connected of pure dimension $d$, and put $X=X_0\times_{\Fq}\Fbar$. For $\ell\ne\operatorname{char}\Fq$, there are linear isomorphisms
$$
t_d:H_c^{2d}(X,\QbarX(d))\xrightarrow{\sim}\overline{\mathbf Q}_\ell,
\qquad t:H_c^{2d}(X,\QbarX)\xrightarrow{\sim}\overline{\mathbf Q}_\ell(-d),
$$
with $t_d(Fz)=t_d(z)$ and $t(Fz)=q^dt(z)$. If $X_0$ is proper, there is also an isomorphism
$$
t_{\mathrm{prop}}:H^{2d}(X,\QbarX)\xrightarrow{\sim}\overline{\mathbf Q}_\ell(-d),
\qquad t_{\mathrm{prop}}(Fz)=q^dt_{\mathrm{prop}}(z).
$$
The Lean statement asserts existence of these isomorphisms; it does not identify them with the specified trace of Definition [definition-trace-map]. Its degree-zero clause is [theorem-trace-isomorphism-top-degree--1].

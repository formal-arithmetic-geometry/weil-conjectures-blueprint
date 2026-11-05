+++
id = "corollary-point-counting-zeta-function"
kind = "corollary"
title = "Point counting and the zeta function"
order = 1039
lean = ["AlgebraicGeometry.WeilSheaf.pointCount_eq_finsum_trace_compactlySupportedCohomology", "AlgebraicGeometry.Scheme.Hom.zetaSeries", "AlgebraicGeometry.Scheme.Hom.zetaSeries_eq_tprod", "AlgebraicGeometry.Scheme.Hom.exists_int_zetaSeries", "AlgebraicGeometry.Scheme.Hom.constantCoeff_zetaSeries", "AlgebraicGeometry.Scheme.zetaSeries_rational"]
uses = ["definition-small-pro-etale-site", "definition-weil-structure", "definition-frobenius-operator", "definition-categorical-trace"]
+++
Give $\Lambda_X$ the Weil structure of constant sheaves defined after
Definition [definition-weil-structure]. For every coefficient
ring $\Lambda$ of Theorem [theorem-grothendieck-lefschetz-trace-formula] and every $m\geq1$ we have

$$
\operatorname{tr}_{\Lambda}
(\operatorname{Frob}_{X,\Lambda_X}^m\mid R\Gamma_c(X_{\mathrm{pro}\acute{e}t},\Lambda_X))
=\#X_0(\mathbf F_{q^m})\cdot1_{\Lambda}.
\tag{12.9}
$$

For $\Lambda=\mathbf Q_\ell,E,\overline{\mathbf Q}_\ell$, this gives

$$
\#X_0(\mathbf F_{q^m})
=\sum_i(-1)^i\operatorname{Tr}
(\operatorname{Frob}_{X,\Lambda_X}^m\mid H_c^i(X_{\mathrm{pro}\acute{e}t},\Lambda_X)),
$$

and

$$
\begin{aligned}
Z(X_0,T)
&:=\exp\left(\sum_{m\geq1}
\#X_0(\mathbf F_{q^m})\frac{T^m}{m}\right)\\
&=\prod_{x\in|X_0|}(1-T^{\deg(x)})^{-1}
=\prod_i\det(1-T\operatorname{Frob}_{X,\Lambda_X}\mid H_c^i(X_{\mathrm{pro}\acute{e}t},\Lambda_X))^{(-1)^{i+1}}.
\end{aligned}
$$

The first two series lie in $1+T\mathbf Z[[T]]$, and the last equality
holds in $\Lambda[[T]]$. Moreover, $Z(X_0,T)$ belongs to
$\mathbf Q(T)$.

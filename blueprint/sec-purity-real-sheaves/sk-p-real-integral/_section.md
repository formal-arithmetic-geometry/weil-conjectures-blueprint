+++
id = "sk-p-real-integral"
kind = "proposition"
title = "Lattices and representations on a normal scheme"
order = 3786
uses = ["sk-lem-wrp-normal-geometric-cover", "sk-lem-stratified-lattice", "sk-prop-sfb-qlbar-colimit-x", "sk-thm-pe-constructible-comparison"]
lean = ["AlgebraicGeometry.WeilGroup.IsLisse.exists_lattice"]
tags = ["sketch"]
+++
Let $X$ be a nonempty connected normal scheme of finite type over a
field, let $E/\Ql$ be finite, and fix a geometric point $\bar x$.
Every lisse $E_X$-module $\mathcal F$, in the pro-étale coefficient
category, contains a lisse $\mathcal O_{E,X}$-submodule $\mathcal M$ with
$\mathcal M[1/\ell]=\mathcal F$. Its finite reductions are finite
locally constant étale sheaves, and

$$
 \mathcal M\simeq\varprojlim_n\mathcal M/\pi_E^n\mathcal M.
$$

The continuous fibre functor, formed from the finite reductions,
gives an equivalence between lisse $E_X$-modules and finite-dimensional
continuous $E$-representations of the ordinary profinite group
$\pi_1(X,\bar x)$.

*Complement.* For regular $X$ and coefficients $\mathcal O_E$, $E$,
$\overline{\mathbf Q}_\ell$, the equivalence is also
[thm-lisse-qlbar-representations]. On a smooth geometrically connected curve
$C_0/\Fq$ with a nonempty open $U_0\subseteq C_0$, every lisse Weil sheaf
$(V,\rho)$ on $U_0$ has, after a finite extension of $E$, an
$\mathcal O_E$-lattice $L\subset V$ with $\rho(\pi_1(U))L=L$, whose
reductions $L/\mathfrak m_E^nL$ have finite images of $\pi_1(U)$ and are the
stalks of the finite reductions of a lisse $\mathcal O_{E,U}$-lattice in the
underlying sheaf ([p-real-integral]).

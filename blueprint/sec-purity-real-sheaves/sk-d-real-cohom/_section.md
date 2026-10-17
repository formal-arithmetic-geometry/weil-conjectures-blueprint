+++
id = "sk-d-real-cohom"
kind = "definition"
title = "Cohomology and the Euler series"
order = 2946
uses = ["sec-smooth-purity", "sk-d-real-operations", "sk-d-real-setup", "sk-d-real-weights", "sk-d-real-weil", "sk-lem-coefficient-heart", "sk-lem-integral-models", "sk-prop-sfb-qlbar-colimit-x", "sk-thm-sf-ctf-stability", "sk-thm-sfb-qlbar-two-colimit"]
lean = ["AlgebraicGeometry.WeilGroup.eulerSeries"]
tags = ["sketch"]
+++
For an abelian sheaf $A$ on the étale site (for instance a torsion sheaf),
ordinary cohomology means $H^i(C,A)=R^i\Gamma(C_{\mathrm{ét}},A)$, computed by an
injective resolution.
For a constructible Weil sheaf $\mathcal K$ on a
curve, an object of $\Cons(C,\Qlb)$ with a Weil structure, $H^i(C,\mathcal K)$ and
$H_c^i(C,\mathcal K)$ are the cohomology groups
$H^iR\Gamma(C_{\mathrm{proét}},\mathcal K)$ and $H^i(Ra_!\mathcal K)$ in
$D(-_{\mathrm{proét}},\Qlb)$, finite-dimensional by
[sk-thm-sf-ctf-stability]. As a consequence of descent to a finite $E$
([sk-thm-sfb-qlbar-two-colimit]), integral models ([sk-lem-integral-models]) and
[sk-prop-sfb-qlbar-colimit-x], they are computed from a lattice by the derived limit of
its finite levels, then inverting $\ell$ and extending scalars.
They carry geometric Frobenius $F$, with the
Tate convention fixed above.
Using the local polynomials, the Euler series is
the locally finite formal product

$$
L_\iota(C_0,\mathcal K,T)
=\prod_{x\in|C_0|}\iota P_x(\mathcal K,T^{e_x})^{-1}
\in 1+T\mathbf C[[T]].
$$

Locally finite means that only finitely many factors contribute to any
fixed coefficient; there are finitely many closed points of bounded degree.

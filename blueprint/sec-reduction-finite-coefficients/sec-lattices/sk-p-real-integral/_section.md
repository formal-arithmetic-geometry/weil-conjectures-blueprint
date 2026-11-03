+++
id = "sk-p-real-integral"
kind = "proposition"
title = "Lattices and representations on a normal scheme"
order = 256
lean = ["AlgebraicGeometry.ProEtale.exists_lisseMonodromy"]
uses = ["sk-lem-finite", "sk-lem-stratified-lattice", "sk-lem-wrp-normal-geometric-cover", "sk-prop-sfb-qlbar-colimit-x", "sk-thm-pe-constructible-comparison", "sk-lem-lisse-finite-descent"]
tags = ["sketch"]
+++
Let $X$ be a nonempty connected normal scheme of finite type over a
field, let $E/\Ql$ be finite, and fix a geometric point $\bar x$.
Every lisse $E_X$-module $L$, in the pro-étale coefficient
category defined above, contains a lisse
$\mathcal O_{E,X}$-submodule $M$ with
$M[1/\ell]=L$. Its finite reductions are finite
locally constant étale sheaves, and

$$
M\simeq\varprojlim_nM/\pi_E^nM.
$$

The fibre functor at $\bar x$, $L\mapsto\bigl(\varprojlim_n(M/\pi_E^nM)_{\bar x}\bigr)\otimes_{\mathcal O_E}E$,
gives an equivalence between lisse
$E_X$-modules and finite-dimensional continuous $E$-representations
of the ordinary profinite group $\pi_1(X,\bar x)$.

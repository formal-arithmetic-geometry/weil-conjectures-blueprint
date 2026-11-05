+++
id = "prose-C-15"
kind = "hidden"
title = "Descent to the ground field (1)"
order = 1561
+++
To compare the Galois action on the cohomology of a curve over $\bar k$
with a Tate module, we need the Jacobian over the ground field $k$.
For example, in Proposition [proposition-no-fixed-class-degree-one]
we work over a finite field, and Frobenius acts on
$\varprojlim_nH^1(C,\mathbf Z/\ell^n(1))$. It has no fixed vector there
because this module is $T_\ell J_0$ for an abelian variety $J_0$ over
$\mathbf F_q$ (Proposition [proposition-no-frobenius-fixed-vector]).
The construction so far works over a separably closed field and uses a
rational point for the rigidification. However, a curve over $k$ need not
have a $k$-point; for instance, the conic $x^2+y^2+z^2=0$ over $\mathbf R$ has none.
We therefore define $J_0$ as the scheme representing the degree-zero part
of the fppf Picard sheaf. Concretely, we obtain it from the Jacobian over $k_s$
by Galois descent through a finite Galois extension $k'/k$
(Proposition [proposition-jacobian-over-ground-field]). The Kummer sequence then
identifies $H^1(C,\mathbf Z/\ell^n(1))$ with $J_0[\ell^n](\bar k)$
compatibly with the Galois action and the transition maps
(Proposition [proposition-h-1-curve-tate-module]).

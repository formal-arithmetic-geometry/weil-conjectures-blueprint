+++
id = "prose-C-14"
kind = "hidden"
title = "The Jacobian over the ground field and the Galois action"
order = 903
+++
To compare the Galois action on the cohomology of a curve over $\bar k$
with a Tate module, we need the Jacobian over the ground field $k$.
Over a finite field this is what Proposition [sk-prop-wrp-h1-no-fixed] uses:
Frobenius acts on $\varprojlim_nH^1(C,\mathbf Z/\ell^n(1))$, and it has
no fixed vector there because this module is $T_\ell J_0$ for an abelian
variety $J_0$ over $\mathbf F_q$ (Proposition [sk-p-tate]).
The construction so far works over a separably closed field and uses a
rational point for the rigidification. A curve over $k$ need not have a
$k$-point; the conic $x^2+y^2+z^2=0$ over $\mathbf R$ has none. We
therefore define $J_0$ as the scheme representing the degree-zero part
of the fppf Picard sheaf, and we obtain it from the Jacobian over $k_s$
by Galois descent, through a finite Galois extension $k'/k$
(Proposition [sk-prop-jacobian-descent]). The Kummer sequence then
identifies $H^1(C,\mathbf Z/\ell^n(1))$ with $J_0[\ell^n](\bar k)$
compatibly with the Galois action and the transition maps
(Proposition [sk-prop-app-jacobian-equivariant-kummer]).

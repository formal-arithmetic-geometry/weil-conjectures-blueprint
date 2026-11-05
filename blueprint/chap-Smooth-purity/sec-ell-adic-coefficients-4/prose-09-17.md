+++
id = "prose-09-17"
kind = "hidden"
title = "$\\ell$-adic coefficients"
order = 762
+++
Let $f:X\to Y$ be smooth of pure relative dimension $d$. For
$\mathcal O_E$-coefficients we want an isomorphism of functors
$f^*(-)(d)[2d]\simeq f^!$ on $\Dbc(-,\mathcal O_E)$. Here $f^!_{\mathcal O_E}$ is
defined by Brown representability, not as a limit of the finite $f^!$.
The reduction principle of Section [sec-Reduction-to-finite-coefficients] does not apply,
because it checks that a given morphism is an isomorphism, and we have
no morphism $f^*(-)(d)[2d]\to f^!$ with $\mathcal O_E$-coefficients yet.
Instead we deduce
Theorem [theorem-smooth-purity-all-admissible-coefficients] for $\mathcal O_E$, $E$ and $\overline{\mathbf Q}_\ell$ from
Proposition [proposition-smooth-purity-finite-coefficients] by building the
right adjoint ourselves. The key input is that the finite isomorphisms
$\gamma_{f,A}$ commute with change of finite coefficients (9.17),
which lets us construct an explicit right adjoint of $Rf_{!,\mathcal O_E}$ from towers
(Proposition [proposition-sp-integral-adjunction]). Inverting $\ell$
then gives the cases $E$ and $\overline{\mathbf Q}_\ell$
(Proposition [proposition-sp-rational] and Theorem [theorem-sp-qbar]).
Each right adjoint we build is identified with $f^!$ by the uniqueness of
adjoints, normalized by the counits.

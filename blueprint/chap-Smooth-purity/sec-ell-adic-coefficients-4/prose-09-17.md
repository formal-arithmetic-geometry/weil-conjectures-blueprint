+++
id = "prose-09-17"
kind = "hidden"
title = "$\\ell$-adic coefficients"
order = 762
+++
Let $f:X\to Y$ be smooth of pure relative dimension $d$. For
$\mathcal O_E$-coefficients we want an isomorphism of functors
$f^*(-)\href{@definition-tate-twists}{(d)}[2d]\simeq \href{@theorem-existence-exceptional-inverse-image}{f^!}$ on [$\Dbc(-,\mathcal O_E)$](@definition-constructible-sheaves). Here [$f^!_{\mathcal O_E}$](@theorem-existence-exceptional-inverse-image) is
defined by Brown representability, not as a limit of the finite [$f^!$](@theorem-existence-exceptional-inverse-image).
The [reduction principle](@proposition-isomorphisms-reduce-finite-coefficients) of Section [sec-Reduction-to-finite-coefficients] does not apply,
because it checks that a given morphism is an isomorphism, and we have
no morphism $f^*(-)\href{@definition-tate-twists}{(d)}[2d]\to \href{@theorem-existence-exceptional-inverse-image}{f^!}$ with $\mathcal O_E$-coefficients yet.
Instead we deduce
Theorem [theorem-smooth-purity-all-admissible-coefficients] for $\mathcal O_E$, $E$ and $\overline{\mathbf Q}_\ell$ from
Proposition [proposition-smooth-purity-finite-coefficients] by building the
right adjoint ourselves. The key input is that the finite isomorphisms
[$\gamma_{f,A}$](@proposition-smooth-purity-finite-coefficients) commute with change of finite coefficients (9.17),
which lets us construct an explicit right adjoint of [$Rf_{!,\mathcal O_E}$](@proposition-construction-independence-rf-shriek) from towers
(Proposition [proposition-sp-integral-adjunction]). Inverting $\ell$
then gives the cases $E$ and $\overline{\mathbf Q}_\ell$
(Proposition [proposition-sp-rational] and Theorem [theorem-sp-qbar]).
Each right adjoint we build is identified with [$f^!$](@theorem-existence-exceptional-inverse-image) by the [uniqueness of
adjoints](@proposition-sp-unique-adjoint), normalized by the counits.

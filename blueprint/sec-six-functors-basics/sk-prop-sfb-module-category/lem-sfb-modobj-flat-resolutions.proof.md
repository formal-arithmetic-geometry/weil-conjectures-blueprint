+++
kind  = "proof"
of    = "lem-sfb-modobj-flat-resolutions"
+++
The category $\Mod_{\mathcal R}(\mathcal C)$ is abelian ([lem-sfb-modobj-abelian]) and
symmetric monoidal ([def-sfb-modobj-symmetric-tensor]).

Let $F$ be flat in $\mathcal C$. Then $(\mathcal R\otimes F)\otimes_{\mathcal R}M\cong
F\otimes(\mathcal R\otimes_{\mathcal R}M)\cong F\otimes M$, naturally in $M$. So after the
forgetful functor, $(\mathcal R\otimes F)\otimes_{\mathcal R}-$ becomes $F\otimes-$, which
is exact. The forgetful functor is faithful and exact
([lem-sfb-modobj-forget-faithful], [lem-sfb-modobj-forget-left-exact],
[lem-sfb-modobj-forget-right-exact]), so it reflects exactness, and
$(\mathcal R\otimes F)\otimes_{\mathcal R}-$ is exact. By the symmetry, so is
$-\otimes_{\mathcal R}(\mathcal R\otimes F)$. Hence the free module $\mathcal R\otimes F$ is
flat.

The map $\gamma_M(\mathcal R\otimes\pi_M)$ is $\mathcal R$-linear by associativity of
$\gamma_M$, and it is natural in $M$. It is an epimorphism:
- $\mathcal R\otimes\pi_M$ is an epimorphism because $\mathcal R\otimes-$ is right exact;
- $\gamma_M$ is a split epimorphism with section $(\eta\otimes M)\lambda_M^{-1}$, by the
  unit law.

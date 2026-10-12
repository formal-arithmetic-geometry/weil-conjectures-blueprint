+++
kind  = "proof"
of    = "def-sfb-modobj-transport"
+++
A lax monoidal functor sends monoid objects to monoid objects. The monoid axioms for
$F\mathcal R$ follow from those of $\mathcal R$, naturality of $\mu^F$, and the
associativity and unitality axioms of the lax structure.

Unit law for $FM$: by naturality of $\mu^F$ and lax unitality
$F(\lambda_M)\mu^F_{\mathbf 1,M}(\varepsilon^F\otimes FM)=\lambda_{FM}$,
$$
F(\gamma_M)\mu^F(F\eta\,\varepsilon^F\otimes FM)
=F(\gamma_M(\eta\otimes M))\mu^F(\varepsilon^F\otimes FM)
=F(\lambda_M)\mu^F(\varepsilon^F\otimes FM)=\lambda_{FM}.
$$
Associativity of the action follows in the same way, from naturality of $\mu^F$, the
associativity axiom of the lax structure, and associativity of $\gamma_M$. Linearity of
$Ff$ is naturality of $\mu^F$ applied to $\gamma_N(\mathcal R\otimes f)=f\gamma_M$.

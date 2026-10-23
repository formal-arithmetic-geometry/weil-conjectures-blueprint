+++
kind = "proof"
of = "det-def-sfb-module-objects-category"
uses = ["det-def-sfb-ring-object-monoid"]
+++
1. $\mathrm{id}_M\circ\gamma_M=\gamma_M=\gamma_M\circ(\mathcal R\otimes\mathrm{id}_M)$ since
   $\mathcal R\otimes-$ is a functor. If $f\colon M\to N$ and $g\colon N\to P$ are morphisms of module
   objects, then
   $$
   gf\gamma_M=g\gamma_N(\mathcal R\otimes f)=\gamma_P(\mathcal R\otimes g)(\mathcal R\otimes f)=\gamma_P(\mathcal R\otimes gf).
   $$
   Associativity and unitality of composition are inherited from $\mathcal C$.
2. The forgetful functor preserves identities and composition by definition, and it is injective on
   each Hom-set because a morphism of module objects is a morphism of $\mathcal C$ satisfying a
   condition.
3. The unit axiom for $\gamma=\mu$ is the left unit law $\mu(\eta\otimes\mathcal R)=\lambda_{\mathcal R}$,
   and the associativity axiom is the associativity law
   $\mu(\mu\otimes\mathcal R)=\mu(\mathcal R\otimes\mu)\alpha_{\mathcal R,\mathcal R,\mathcal R}$ of the
   monoid object $\mathcal R$ ([det-def-sfb-ring-object-monoid]).

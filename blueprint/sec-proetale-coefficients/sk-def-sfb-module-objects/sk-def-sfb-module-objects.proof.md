+++
kind  = "proof"
of    = "sk-def-sfb-module-objects"
+++
Identities are morphisms of module objects. If $f\colon M\to N$ and $g\colon N\to P$ are
morphisms of module objects, then so is $gf$:
$$
gf\gamma_M=g\gamma_N(\mathcal R\otimes f)=\gamma_P(\mathcal R\otimes g)(\mathcal R\otimes f)
=\gamma_P(\mathcal R\otimes gf).
$$
So $\Mod_{\mathcal R}(\mathcal C)$ is a category, and the forgetful functor is a functor. For
the regular module, the two axioms are the left unit law
$\mu(\eta\otimes\mathcal R)=\lambda_{\mathcal R}$ and the associativity law
$\mu(\mu\otimes\mathcal R)=\mu(\mathcal R\otimes\mu)\alpha_{\mathcal R,\mathcal R,\mathcal R}$
of $\mathcal R$. In part 3, $\Lambda_X$ is a monoid object of
$\Sh(X_{\mathrm{proét}},\Ab)$ because $p_X^*$ is strong monoidal
([sk-def-sfb-pulled-back-coefficients]), so part 2 applies.

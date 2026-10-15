+++
kind  = "proof"
of    = "lem-sfb-modobj-grothendieck"
+++
Since $\mathcal C$ is closed, $\mathcal R\otimes-$ preserves colimits, so
$\Mod_{\mathcal R}(\mathcal C)$ is abelian ([lem-sfb-modobj-abelian]).

Small colimits of module objects are computed in $\mathcal C$. Let $L=\colim M_i$ in
$\mathcal C$. Then $\mathcal R\otimes L=\colim(\mathcal R\otimes M_i)$, and the actions
$\gamma_{M_i}$ induce an action on $L$. This makes $L$ a colimit in
$\Mod_{\mathcal R}(\mathcal C)$, by the argument of the cokernel case. Finite limits are
computed in $\mathcal C$ by [lem-sfb-modobj-forget-left-exact]. Hence a filtered colimit of
short exact sequences of module objects is computed in $\mathcal C$, where it is exact. The
forgetful functor is faithful and exact ([lem-sfb-modobj-forget-faithful],
[lem-sfb-modobj-forget-left-exact], [lem-sfb-modobj-forget-right-exact]), so it reflects
exactness. Thus filtered colimits are exact in $\Mod_{\mathcal R}(\mathcal C)$.

Let $G$ be a generator of $\mathcal C$. The free module $\mathcal R\otimes G$, with action
$(\mu\otimes G)\alpha^{-1}$, satisfies
$\Hom_{\Mod_{\mathcal R}}(\mathcal R\otimes G,M)\cong\Hom_{\mathcal C}(G,M)$. A linear map
$f$ goes to $f(\eta\otimes G)\lambda_G^{-1}$, and the inverse sends $g$ to
$\gamma_M(\mathcal R\otimes g)$. Hence $\mathcal R\otimes G$ is a generator of
$\Mod_{\mathcal R}(\mathcal C)$.

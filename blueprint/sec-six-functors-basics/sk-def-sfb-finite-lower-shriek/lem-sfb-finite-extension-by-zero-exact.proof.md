+++
kind  = "proof"
of    = "lem-sfb-finite-extension-by-zero-exact"
uses = ["def-sfb-finite-extension-by-zero-adjunction"]
+++
By the computation in the proof of [def-sfb-finite-extension-by-zero], the presheaf
$\operatorname{Lan}_{\ell^{\mathrm{op}}}F$ takes at $W$ either the value $F(W\to U)$ or
$0$, depending only on $W$. So $\operatorname{Lan}_{\ell^{\mathrm{op}}}$ preserves finite
limits. The inclusion of sheaves into presheaves preserves limits, and sheafification is
left exact for a Grothendieck abelian $\mathcal A$. Hence $j_!$ is left exact. It is right
exact because it is a left adjoint ([def-sfb-finite-extension-by-zero-adjunction]).

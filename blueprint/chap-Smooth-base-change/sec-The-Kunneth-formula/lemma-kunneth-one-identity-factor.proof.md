+++
kind = "proof"
of = "lemma-kunneth-one-identity-factor"
order = 719
uses = ["lemma-base-change-along-product-projection"]
+++
We show that the cone $N$ of $\kappa_{M,Q}$ vanishes modulo every maximal
ideal of $A$, and conclude by derived Nakayama on stalks. The source and
target of $\kappa_{M,Q}$ are in
$D^b_{\mathrm{ctf}}(Y\times T,A)$ by Proposition [proposition-six-operations-dctf], so every
geometric stalk of $N$ is a perfect $A$-complex. Now let
$\mathfrak m\subset A$ be a maximal ideal and put $k=A/\mathfrak m$. The
change-of-coefficients maps of
Proposition [proposition-six-operations-change-coefficients] for pullback, tensor product and
ordinary direct image respect the counit defining the
Künneth map. Hence they identify the reduction $\kappa_{M,Q}\otimes^{\mathbf L}_A k$
with $\kappa_{M\otimes^{\mathbf L}_Ak,\,Q\otimes^{\mathbf L}_Ak}$, which is
an isomorphism by
Lemma [lemma-kunneth-field-coefficients]. This means that
$N\otimes^{\mathbf L}_A k=0$ for every maximal ideal. Since the
Artinian ring $A$ is a product of local rings, derived Nakayama for the
perfect complex $N_{\bar z}$ at a geometric point $\bar z$ shows that
$N_{\bar z}=0$. Finally, since $N$ lies in $D^b_{\mathrm{ctf}}(Y\times T,A)$, it comes
from a complex on the small étale site by
Theorem [theorem-comparison-constructible-sheaves], where vanishing is
detected on geometric stalks, so $N=0$.

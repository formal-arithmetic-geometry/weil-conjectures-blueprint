+++
kind  = "proof"
of    = "lem-sfb-modobj-symmetric-bimodules"
+++
The right unit law says that $\rho_M(M\otimes\eta)$ is the right unitor of $M$. It
follows from naturality of $\beta$, which gives
$\beta_{M,\mathcal R}(M\otimes\eta)=(\eta\otimes M)\beta_{M,\mathbf 1}$, together with the
left unit law and the fact that braiding with $\mathbf 1$ is the unitor identification. Right associativity and the compatibility of the two actions
follow from naturality of $\beta$ and the hexagon identities. These reduce both sides to
the action of $\mathcal R\otimes\mathcal R$ on $M$, up to the order of the two factors of
$\mathcal R$. The two orders agree because $\mathcal R$ is commutative:
$\mu\beta_{\mathcal R,\mathcal R}=\mu$, so
$\gamma_M(\mu\beta_{\mathcal R,\mathcal R}\otimes M)=\gamma_M(\mu\otimes M)$.

A morphism of module objects commutes with the right actions by naturality of $\beta$.
A morphism of bimodules is in particular a morphism of left modules. Morphisms in both
categories are morphisms of $\mathcal C$, so the functor is fully faithful. The values are
symmetric by the definition of $\rho_M$.

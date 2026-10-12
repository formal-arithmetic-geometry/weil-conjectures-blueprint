+++
kind  = "proof"
of    = "def-sfb-modobj-symmetric-tensor"
+++
Write $\pi_{M,N}\colon M\otimes N\to M\otimes_{\mathcal R}N$ for the projection
([def-sfb-modobj-relative-tensor]). For the descent, $\pi_{N,M}\beta_{M,N}$ must coequalize
the two maps $M\otimes\mathcal R\otimes N\rightrightarrows M\otimes N$. By naturality of
$\beta$, the composite with $(\gamma_M\beta_{M,\mathcal R})\otimes N$ becomes the action of
$\mathcal R$ on the factor $M$ inside $N\otimes M$. By the hexagon identities, the
composite with $(M\otimes\gamma_N)\alpha$ becomes the action on the factor $N$. The two
expressions differ by a double braiding $\beta_{\mathcal R,M}\beta_{M,\mathcal R}$. This is
the identity because $\mathcal C$ is symmetric, and then the relation defining
$N\otimes_{\mathcal R}M$ identifies them. For a merely braided $\mathcal C$ the descent
fails.

The descended map is $\mathcal R$-linear. This is checked after precomposing with the
epimorphism $\mathcal R\otimes\pi_{M,N}$, where it is again naturality of $\beta$ and the
relation in $N\otimes_{\mathcal R}M$. The projections, and their tensor products with
objects, are epimorphisms because $\otimes$ preserves coequalizers. So naturality, the
hexagon identities and $\beta_{N,M}\beta_{M,N}=\mathrm{id}$ can be checked after
precomposing with them. There they become the corresponding identities in $\mathcal C$,
because the associator of $\otimes_{\mathcal R}$ is induced by the associator of
$\mathcal C$.

+++
kind  = "proof"
of    = "def-sfb-modobj-transport-adjunction"
+++
For a monoidal adjunction the unit $u\colon\mathrm{id}\to GF$ is a monoidal natural
transformation, and the components of a monoidal natural transformation at a monoid object
are morphisms of monoid objects.

Let $\varphi\colon FM\to N$ correspond to $\psi=G(\varphi)u_M\colon M\to GN$. Write
$\delta=(\mu^F)^{-1}$. Linearity of $\varphi$ reads
$\varphi\circ F(\gamma_M)=\gamma_N(F\mathcal R\otimes\varphi)\delta_{\mathcal R,M}$. Since
$u$ is monoidal, $G(\delta_{\mathcal R,M})u_{\mathcal R\otimes M}
=\mu^G_{F\mathcal R,FM}(u_{\mathcal R}\otimes u_M)$. Hence, by naturality of $u$ and
$\mu^G$,
$$
\psi\gamma_M=G(\varphi F\gamma_M)u_{\mathcal R\otimes M}
=G(\gamma_N)\mu^G_{F\mathcal R,N}(u_{\mathcal R}\otimes\psi).
$$
The right side is the action of $\mathcal R$ on $GN$ through $u_{\mathcal R}$
([def-sfb-modobj-restriction], [def-sfb-modobj-transport]), applied after
$\mathcal R\otimes\psi$. So $\psi$ is $\mathcal R$-linear. The converse is the same
computation with the counit. Naturality of the bijection is inherited from $F\dashv G$.

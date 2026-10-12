+++
kind  = "proof"
of    = "def-sfb-modobj-linearization"
+++
We use the notation of [def-sfb-projection-formula]. The monoid $S\mathcal B$ has unit
$S(\eta_{\mathcal B})\epsilon^{-1}$ and multiplication
$S(\mu_{\mathcal B})\delta_{\mathcal B,\mathcal B}^{-1}$.

Unit law. By naturality of $\pi$ in $L$,
$$
P(\gamma_M)\pi^{-1}_{\mathcal B,M}(\eta_{\mathcal B}\otimes PM)
=P\bigl(\gamma_M(S\eta_{\mathcal B}\otimes M)\bigr)\pi^{-1}_{\mathbf 1,M}.
$$
The unit law of $M$ gives $\gamma_M(S\eta_{\mathcal B}\otimes M)=\lambda_M(\epsilon\otimes M)$.
By the unit compatibility of $\pi$, the right side is therefore $\lambda_{PM}$.

Associativity. Naturality of $\pi$ in $L$, applied to $\mu_{\mathcal B}$, reduces the
associativity of the action to the associativity of $\gamma_M$ for the multiplication of
$S\mathcal B$. This multiplication involves $\delta_{\mathcal B,\mathcal B}$. The
associativity compatibility of $\pi$, together with naturality of $\pi$ in $M$ applied to
$\gamma_M$, identifies the two sides.

Linearity of $Pf$ is naturality of $\pi$ in $M$.

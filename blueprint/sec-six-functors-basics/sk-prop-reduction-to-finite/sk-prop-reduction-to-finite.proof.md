+++
kind = "proof"
of = "sk-prop-reduction-to-finite"
uses = ["sk-prop-scalar-six", "sk-prop-integral-criterion", "sk-lem-pe-derived-nakayama", "sk-lem-integral-models", "sk-thm-sfb-qlbar-two-colimit"]
+++
For $\Lambda=\mathcal O_E$, both $F(K)$ and $G(K)$ lie in $\Dbc(Y,\mathcal O_E)$, hence are derived
$\pi_E$-complete ([sk-prop-integral-criterion]), and so is $\operatorname{Cone}(\theta(K))$.
Reduction modulo $\pi_E$ is the cone of multiplication by $\pi_E$, so by the hypothesis it
carries $\theta(K)$ to $\theta_{\mathcal O_E/\pi_E}(K/\pi_E)$, which is an isomorphism by
hypothesis. Thus $\operatorname{Cone}(\theta(K))/\pi_E=0$, and $\operatorname{Cone}(\theta(K))=0$
by derived Nakayama ([sk-lem-pe-derived-nakayama]). The case $E=\mathbf Q_\ell$ gives
$\Lambda=\mathbf Z_\ell$.

For $\Lambda=E$, the objects $K$ for which $\theta(K)$ is an isomorphism form a triangulated
subcategory, so by part (4) of [sk-lem-integral-models] it suffices to treat $K=K_0[1/\ell]$
with $K_0\in\Dbc(X,\mathcal O_E)$. Inverting $\ell$ is a coefficient comparison, so
$\theta_E(K_0[1/\ell])$ is $\theta_{\mathcal O_E}(K_0)[1/\ell]$, an isomorphism by the integral
case. For $\Lambda=\Qlb$, every $K$ is $K_E\otimes_E\Qlb$ for a finite $E$
([sk-thm-sfb-qlbar-two-colimit]), and $\theta_{\Qlb}(K)$ is $\theta_E(K_E)\otimes_E\Qlb$. Again
$E=\mathbf Q_\ell$ is included.

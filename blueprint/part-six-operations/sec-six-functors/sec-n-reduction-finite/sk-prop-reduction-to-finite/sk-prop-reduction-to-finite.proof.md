+++
kind = "proof"
of = "sk-prop-reduction-to-finite"
uses = ["sk-prop-integral-criterion", "sk-lem-pe-derived-nakayama", "sk-lem-integral-models", "sk-prop-qlbar-two-colimit"]
+++
For $\Lambda=\mathcal O_E$, both $F(K)$ and $G(K)$ lie in
$\Dbc(Y,\mathcal O_E)$, hence are derived $\pi_E$-complete
(Proposition [sk-prop-integral-criterion]), and so is $\Cone(\theta(K))$.
Reduction modulo $\pi_E$ is the cone of multiplication by
$\pi_E$, so by the hypothesis it carries $\theta(K)$ to
$\theta_{\mathcal O_E/\pi_E}(K/\pi_E)$, which is an isomorphism by
hypothesis. Thus $\Cone(\theta(K))/\pi_E=0$, and $\Cone(\theta(K))=0$ by derived Nakayama
(Lemma [sk-lem-pe-derived-nakayama]). The case $E=\Ql$ gives $\Lambda=\Zl$.

For $\Lambda=E$, the objects $K$ for which $\theta(K)$ is an isomorphism
form a triangulated subcategory, so by
Lemma [sk-lem-integral-models](4) it suffices to treat
$K=K_0[1/\ell]$ with $K_0\in\Dbc(X,\mathcal O_E)$. Inverting $\ell$ is a
change of coefficients, so $\theta_E(K_0[1/\ell])$ is
$\theta_{\mathcal O_E}(K_0)[1/\ell]$, an isomorphism by the integral case.
For $\Lambda=\overline{\mathbf Q}_\ell$, every $K$ is $K_E\otimes_E\overline{\mathbf Q}_\ell$ for a finite $E$
(Proposition [sk-prop-qlbar-two-colimit]), and $\theta_{\overline{\mathbf Q}_\ell}(K)$ is
$\theta_E(K_E)\otimes_E\overline{\mathbf Q}_\ell$. Again $E=\Ql$ is included.

+++
kind = "proof"
of = "proposition-isomorphisms-reduce-finite-coefficients--3"
order = 654007
uses = ["proposition-isomorphisms-reduce-finite-coefficients--2", "lemma-integral-models"]
+++
Let $\Lambda=E$. Here completeness is of no help, since a complex over
$E$ is killed by reduction modulo $\pi_E$. Instead we use integral models.
Both $F_E$ and $G_E$ are exact and $\theta_E$ is a transformation of exact
functors. Hence the objects $K$ for which $\theta_E(K)$ is an isomorphism
form a triangulated subcategory. By Lemma [lemma-integral-models](4),
every object of $\Dbc(X,E)$ is built by finitely many cones and shifts from
objects $K_0[1/\ell]$ with $K_0\in\Dbc(X,\mathcal O_E)$. It therefore
suffices to treat these. Inverting $\ell$ is the change of coefficients
along $\mathcal O_E\to E$. By hypothesis, $\theta_E(K_0[1/\ell])$ is
therefore identified with $\theta_{\mathcal O_E}(K_0)[1/\ell]$. This is an
isomorphism by the integral case.

*Source:* the proof of Proposition [proposition-isomorphisms-reduce-finite-coefficients].

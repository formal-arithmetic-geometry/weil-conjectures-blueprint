+++
kind = "proof"
of = "proposition-isomorphisms-reduce-finite-coefficients"
order = 655
uses = ["proposition-pro-etale-affines-form-basis", "lemma-acyclicity-pulled-back-injectives", "proposition-locally-constant-sheaves-finite-presentation", "lemma-acyclic-resolutions"]
+++
The three kinds of coefficients are reached from finite ones in three
different ways: $\mathcal O_E$ by completion, $E$ by inverting $\ell$, and
$\overline{\mathbf Q}_\ell$ as a colimit over finite extensions. We treat them in this order,
each case using the previous one.

Let $\Lambda=\mathcal O_E$, and put $C=\Cone(\theta(K))$; we must show
$C=0$. Since the complexes $F(K)$ and $G(K)$ lie in $\Dbc(Y,\mathcal O_E)$, they are derived $\pi_E$-complete by
Proposition [proposition-integral-constructibility-criterion]. Moreover, derived complete complexes are closed under cones, and so $C$ is derived complete
too. Derived Nakayama (Lemma [lemma-reduction-derived-nakayama]) therefore reduces $C=0$ to $C/\pi_E=0$. Now reduction modulo $\pi_E$ is a change of coefficients along $\mathcal O_E\to\mathcal O_E/\pi_E$. By the
compatibility assumed in the statement, it identifies $\theta(K)/\pi_E$
with $\theta_{\mathcal O_E/\pi_E}(K/\pi_E)$. This is an isomorphism by the
hypothesis for finite rings, applied to $A=\mathcal O_E/\pi_E$. Thus
$C/\pi_E=0$, and so $C=0$. In particular, the case $E=\mathbf Q_\ell$ gives $\Lambda=\mathbf Z_\ell$.

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

Let $\Lambda=\overline{\mathbf Q}_\ell$. By Proposition [proposition-dctf-x-qbar-2-colimit], every $K$ is
isomorphic to $K_E\otimes_E\overline{\mathbf Q}_\ell$ for some finite $E$ and some
$K_E\in D^b_{\mathrm{ctf}}(X,E)$. By hypothesis, applied to $E\to\overline{\mathbf Q}_\ell$, the map
$\theta_{\overline{\mathbf Q}_\ell}(K)$ is identified with $\theta_E(K_E)\otimes_E\overline{\mathbf Q}_\ell$, which
is an isomorphism by the case of $E$. Again $E=\mathbf Q_\ell$ is included.

+++
kind = "proof"
of = "theorem-riemann-roch-coherent-serre-duality--2"
order = 1525002
uses = []
+++
Choose a finite flat map $\phi:C\to\mathbf P^1_k$ that is unramified at
the generic points. Such a map is obtained on each connected component
from a rational function with nonzero differential. Since $\phi$ is
affine and $\phi_*\mathcal F$ is finite locally free, duality on
$\mathbf P^1_k$ and duality along $\phi$ give natural isomorphisms

$$
H^1(C,\mathcal F)^\vee
\simeq H^1(\mathbf P^1_k,\phi_*\mathcal F)^\vee
\simeq \operatorname{Hom}_{\mathcal O_{\mathbf P^1_k}}
  (\phi_*\mathcal F,\omega_{\mathbf P^1_k/k})
\simeq H^0(C,\mathcal F^\vee\otimes\omega_{C/k}).
$$

This is the case $(p,q)=(0,1)$. Apply it to
$\mathcal F^\vee\otimes\omega_{C/k}$ and use
$(\mathcal F^\vee\otimes\omega_{C/k})^\vee\otimes\omega_{C/k}
\simeq\mathcal F$. Dualizing and using finite-dimensional biduality
gives the case $(p,q)=(1,0)$. These are the only possibilities, and
each construction is natural in $\mathcal F$.

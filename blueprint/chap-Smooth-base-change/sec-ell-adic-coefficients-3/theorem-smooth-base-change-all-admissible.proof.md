+++
kind = "proof"
of = "theorem-smooth-base-change-all-admissible"
order = 696
uses = ["theorem-comparison-constructible-sheaves", "proposition-six-operations-dctf", "proposition-isomorphisms-reduce-finite-coefficients", "theorem-smooth-base-change-classical-torsion-2", "lemma-change-coefficients"]
+++
For finite rings the theorem is the torsion theorem once we know that $K$
is classical, and the other rings follow by the reduction principle. By
Proposition [proposition-six-operations-dctf], both sides lie in
$D^b_{\mathrm{ctf}}(Y',\Lambda)$, so we only have to show that the canonical map
(4.5) is invertible.

*Finite rings $A$.* The torsion theorem is stated for classical
complexes, so we first check that $K$ is one. By Theorem [theorem-comparison-constructible-sheaves], constructible
pro-étale sheaves with discrete Noetherian coefficients are
classical. The cohomology sheaves of $K$ are constructible, and so $K$ is a bounded classical complex. Since $A$ is
killed by a power of $\ell$, which is invertible on $Y$, smooth base change
for torsion complexes (Theorem [theorem-smooth-base-change-classical-torsion-2]) applies to $K$.

*Other rings.* We apply Proposition [proposition-isomorphisms-reduce-finite-coefficients] with
$F_\Lambda=g^*Rf_*$, $G_\Lambda=Rf'_*g'^*$ and $\theta_\Lambda$ the base
change map. Both functors are exact. The proposition also requires that
the base change map commute with change of coefficients, and this is
Lemma [lemma-change-coefficients]. Since $\theta_A$ is an isomorphism for every finite
$A$ by the first case, the proposition shows that $\theta_\Lambda$ is an
isomorphism for every admissible $\Lambda$.

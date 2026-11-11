+++
kind = "proof"
of = "theorem-smooth-base-change-all-admissible"
order = 703
uses = ["proposition-etale-implications", "proposition-pro-etale-coverings", "definition-w-local-w-strictly-local", "lemma-extremally-disconnected-covers", "proposition-splitting-ind-etale-covers", "theorem-existence-contractible-covers", "theorem-pro-etale-refinements-weakly-etale", "proposition-pro-etale-affines-form-basis", "lemma-w-contractible-affines-projective", "definition-weak-contractibility", "proposition-exact-products", "theorem-classical-sheaves-essential-image", "theorem-bounded-below-cohomology-comparison", "proposition-comparison-immersions", "proposition-locally-constant-sheaves-finite-presentation", "lemma-reduction-derived-nakayama", "lemma-descent-finite-coefficient-field", "proposition-inverting-ell", "definition-derived-base-change-map", "lemma-naturality-pasting-comparison", "proposition-comparison-etale-derived-category", "definition-change-of-coefficients-maps", "lemma-extension-scalars-preserves-dctf", "lemma-change-coefficients-direct-image", "proposition-six-operations-change-coefficients", "theorem-smooth-base-change-classical-torsion-2", "lemma-change-coefficients", "definition-compactification-refinement"]
+++
For finite rings the theorem is the torsion theorem once we know that $K$
is classical, and the other rings follow by the reduction principle. By
Proposition [proposition-six-operations-dctf], both sides lie in
$D^b_{\mathrm{ctf}}(Y',\Lambda)$, so we only have to show that the canonical map
(4.5) is invertible.

*Finite rings $A$.* The torsion theorem is stated for classical
complexes, so we first check that $K$ is one. By Theorem [theorem-comparison-constructible-sheaves], constructible
pro-étale sheaves with discrete Noetherian coefficients are
classical, and since the cohomology sheaves of $K$ are constructible, $K$ is a bounded classical complex. Since $A$ is
killed by a power of $\ell$, which is invertible on $Y$, smooth base change
for torsion complexes (Theorem [theorem-smooth-base-change-classical-torsion-2]) applies to $K$.

*Other rings.* We apply Proposition [proposition-isomorphisms-reduce-finite-coefficients] with
$F_\Lambda=g^*Rf_*$, $G_\Lambda=Rf'_*g'^*$ and $\theta_\Lambda$ the base
change map. Both functors are exact, as the proposition requires, and
the base change map commutes with change of coefficients, which is
Lemma [lemma-change-coefficients]. Since $\theta_A$ is an isomorphism for every finite
$A$ by the first case, the proposition shows that $\theta_\Lambda$ is an
isomorphism for every admissible $\Lambda$.

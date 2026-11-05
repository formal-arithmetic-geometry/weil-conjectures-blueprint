+++
kind = "proof"
of = "theorem-smooth-base-change-all-admissible--4"
order = 701009
uses = ["theorem-smooth-base-change-all-admissible--3", "proposition-isomorphisms-reduce-finite-coefficients--4"]
+++
Apply the $\overline{\mathbf Q}_\ell$ clause [proposition-isomorphisms-reduce-finite-coefficients--4] of the reduction principle, with the finite comparison established in clause [theorem-smooth-base-change-all-admissible--1]. The following argument checks the required compatibility for this specific base-change map.

*Other rings.* We apply Proposition [proposition-isomorphisms-reduce-finite-coefficients] with
$F_\Lambda=g^*Rf_*$, $G_\Lambda=Rf'_*g'^*$ and $\theta_\Lambda$ the base
change map. Both functors are exact. The proposition also requires that
the base change map commute with change of coefficients, and this is
Lemma [lemma-change-coefficients]. Since $\theta_A$ is an isomorphism for every finite
$A$ by the first case, the proposition shows that $\theta_\Lambda$ is an
isomorphism for every admissible $\Lambda$.

*Source:* the proof of Theorem [theorem-smooth-base-change-all-admissible].

+++
kind = "proof"
of = "theorem-smooth-base-change-all-admissible--3"
order = 701007
uses = ["theorem-bounded-below-cohomology-comparison--2", "theorem-smooth-base-change-classical-torsion-2--1"]
+++
Apply the $E$ clause [proposition-isomorphisms-reduce-finite-coefficients--3] of the reduction principle, with the finite comparison established in clause [theorem-smooth-base-change-all-admissible--1]. The following argument checks the required compatibility for this specific base-change map.

*Other rings.* We apply Proposition [proposition-isomorphisms-reduce-finite-coefficients] with
$F_\Lambda=g^*Rf_*$, $G_\Lambda=Rf'_*g'^*$ and $\theta_\Lambda$ the base
change map. Both functors are exact. The proposition also requires that
the base change map commute with change of coefficients, and this is
Lemma [lemma-change-coefficients]. Since $\theta_A$ is an isomorphism for every finite
$A$ by the first case, the proposition shows that $\theta_\Lambda$ is an
isomorphism for every admissible $\Lambda$.

*Source:* the proof of Theorem [theorem-smooth-base-change-all-admissible].

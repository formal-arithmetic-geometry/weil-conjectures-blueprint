+++
kind = "proof"
of = "theorem-smooth-base-change-all-admissible--2"
order = 701005
uses = ["proposition-pro-etale-affines-form-basis", "definition-ind-etale-pro-etale-weakly--1", "definition-ind-etale-pro-etale-weakly--2", "proposition-etale-implications--1", "lemma-stability--6", "lemma-stability--7", "lemma-stability--8", "proposition-pro-etale-coverings--2", "proposition-topos-functoriality--1", "definition-w-local-w-strictly-local--4", "lemma-extremally-disconnected-covers--3", "proposition-splitting-ind-etale-covers--1", "theorem-existence-contractible-covers--1", "theorem-pro-etale-refinements-weakly-etale--1", "proposition-pro-etale-affines-form-basis--1", "proposition-pro-etale-affines-form-basis--2", "definition-weak-contractibility--1", "proposition-exact-products--2", "proposition-comparison-morphism-inverse-image--1", "proposition-comparison-morphism-inverse-image--2", "proposition-comparison-morphism-inverse-image--3", "theorem-classical-sheaves-essential-image--1", "theorem-bounded-below-cohomology-comparison--1", "theorem-bounded-below-cohomology-comparison--2", "proposition-comparison-immersions--1", "proposition-comparison-immersions--2", "proposition-locally-constant-sheaves-finite-presentation--3", "lemma-reduction-derived-nakayama--3", "proposition-comparison-etale-derived-category--5", "definition-change-of-coefficients-maps--1", "definition-change-of-coefficients-maps--4", "lemma-extension-scalars-preserves-dctf--1", "lemma-change-coefficients-direct-image--2", "proposition-six-operations-change-coefficients--14", "theorem-smooth-base-change-all-admissible--1", "definition-compactification-refinement--1"]
+++
Apply the $\mathcal O_E$ clause [proposition-isomorphisms-reduce-finite-coefficients--2] of the reduction principle, with the finite comparison established in clause [theorem-smooth-base-change-all-admissible--1]. The following argument checks the required compatibility for this specific base-change map.

*Other rings.* We apply Proposition [proposition-isomorphisms-reduce-finite-coefficients] with
$F_\Lambda=g^*Rf_*$, $G_\Lambda=Rf'_*g'^*$ and $\theta_\Lambda$ the base
change map. Both functors are exact. The proposition also requires that
the base change map commute with change of coefficients, and this is
Lemma [lemma-change-coefficients]. Since $\theta_A$ is an isomorphism for every finite
$A$ by the first case, the proposition shows that $\theta_\Lambda$ is an
isomorphism for every admissible $\Lambda$.

*Source:* the proof of Theorem [theorem-smooth-base-change-all-admissible].

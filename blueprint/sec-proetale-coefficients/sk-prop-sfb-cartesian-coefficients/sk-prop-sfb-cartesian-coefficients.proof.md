+++
kind  = "proof"
of    = "sk-prop-sfb-cartesian-coefficients"
uses = ["sk-def-sfb-pullback-from-point-comp"]
+++
(1) For every condensed ring $\Lambda$, the identity $p_Y\circ f=p_X$ gives
$$
f^{-1}\Lambda_Y=f^{-1}p_Y^*\Lambda\simeq p_X^*\Lambda=\Lambda_X,
$$
which gives the assertion uniformly, including finite $A$. This is [lem-sfb-alpha-iso]:
$\alpha_f$ is a component of the natural isomorphism of [sk-def-sfb-pullback-from-point-comp].
Its compatibility with identities and composition, in the adjoint form $\eta_f$, is
[lem-sfb-eta-id] and [lem-sfb-eta-comp].

The torsion twists $\mu_{\ell^n}$ are represented by finite étale group schemes, which commute
with base change. Their inverse limit is represented by the inverse limit of these schemes,
so its inverse image is represented by the base change (\stacks{09A5}). This gives the
assertion for $\cO_E(1)$. For a finite $A$ killed by $\ell^n$, its twist is obtained by
extending scalars from $\mathbf Z/\ell^n\mathbf Z$ in the finite-level twist, so inverse image
commutes with it as well. Inverting $\ell$, extending scalars, and taking tensor powers and
duals gives the other twists. Details: [det-prop-sfb-cartesian-coefficients-twists].

(2) An $\cO_E$-basis of $\cO_F$ is an isomorphism of topological $\cO_E$-modules
$\cO_F\cong\cO_E^{[F:E]}$, hence of condensed modules
$\underline{\cO_F}\cong\underline{\cO_E}^{[F:E]}$. Pull it back along $p_X$, and invert $\ell$
for the fields. Details: [det-prop-sfb-cartesian-coefficients-finite-free] and, for the
fields, [lem-sfb-subfield-flat].

+++
kind  = "proof"
of    = "thm-pur-affine-line-orientation"
+++
The Kummer boundary defines the global morphism in the statement by
[lem-pur-gysin-structure], [def-pur-affine-line-datum].
Its target is already a sheaf in degree zero, identified there with
$\Lambda_Y$ through the boundary $\delta$ of the localization triangle
of [lem-pur-support-localization-triangle] pushed forward to $Y$:
$\delta$ carries $R^1\pi_*\Lambda(1)$, free of rank one on $\kappa(t)$
by [prop-pur-gm-relative-kummer](2), isomorphically onto
$\mathcal H^2(Rs^!\Lambda(1))$. So $\operatorname{pur}_s$, which sends
$1$ to the boundary of $\kappa(t)$, already maps $1$ to a generator of
this free rank-one sheaf.
The Kummer class and the support boundary are natural for the base
changes of the zero section, so the geometric fibre of
$\operatorname{pur}_s$ at $\bar y$ is the boundary of the Kummer class of
the coordinate of $\mathbf A^1_{\bar y}$. By
[thm-pur-rank-one-local-calculation] that boundary is $1$. Consequently the morphism of degree-zero
sheaves has every stalk equal to the identity, and is an isomorphism.
The etale-origin comparison of [thm-weil-pbc-site-comparison]
transports the assertion and its normalization to the stated site.
Uniqueness follows because a section of a sheaf is determined by its
stalks; this does not require a conservativity assertion for morphisms
of arbitrary derived objects.

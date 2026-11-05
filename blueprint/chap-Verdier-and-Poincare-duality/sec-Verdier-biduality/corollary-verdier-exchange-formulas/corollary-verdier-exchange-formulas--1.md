+++
id = "corollary-verdier-exchange-formulas--1"
kind = "corollary"
title = "Dual of compact direct image"
order = 847002
aliases = ["bp-r254-1"]
lean = ["AlgebraicGeometry.Etale.nonempty_iso_verdierDual_rightDerivedLowerShriek"]
uses = ["definition-verdier-dual-evaluation", "definition-compactification-refinement"]
+++
Let $\Lambda$ be a finite commutative ring, let $a_Y:Y\to S$ and
$f:X\to Y$, and put $a_X=a_Y\circ f$. Assume that $f$, $a_Y$, and
$a_X$ admit compactifications. With
$\omega_Y=a_Y^!\Lambda_S$, $\omega_X=a_X^!\Lambda_S$, and
$\mathbb D=\cHom(-,\omega)$ on the small étale sites, for every
$K\in D(X_{\mathrm{\acute{e}t}},\Lambda)$ there exists an isomorphism

$$
\mathbb D_Y(Rf_{!,\Lambda}K)\simeq Rf_{*,\Lambda}(\mathbb D_XK).
$$

No boundedness, constructibility, or finite Tor-amplitude hypothesis on
$K$ is needed. The tagged theorem asserts the existence of an isomorphism
for each $K$.

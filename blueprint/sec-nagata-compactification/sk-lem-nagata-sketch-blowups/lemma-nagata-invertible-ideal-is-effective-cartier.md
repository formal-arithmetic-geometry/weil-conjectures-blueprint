+++
id = "lemma-nagata-invertible-ideal-is-effective-cartier"
kind = "lemma"
title = "An invertible ideal is effective Cartier"
order = 99
lean = ["AlgebraicGeometry.Scheme.IdealSheafData.IsInvertible.isEffectiveCartierCenter"]
uses = ["def-nagata-effective-cartier-ideal", "def-nagata-invertible-ideal"]
+++
Let $\mathcal J$ be an invertible ideal on $X$. Then the closed immersion
$V(\mathcal J)\hookrightarrow X$ is an effective Cartier centre, i.e. it is
the closed subscheme cut out by an invertible ideal.

## Proof

Take the invertible ideal $\mathcal J$ itself and the identity
isomorphism of $V(\mathcal J)$ over $X$. Concretely, on an affine open
$V\subseteq X$ where $\mathcal J(V)=(a)$ with $a$ a non-zero-divisor
([def-nagata-invertible-ideal]), the closed subscheme
$V(\mathcal J)\cap V$ is $\operatorname{Spec}(\mathcal O_X(V)/(a))$, cut
out by the single regular equation $a$; such opens cover $X$.

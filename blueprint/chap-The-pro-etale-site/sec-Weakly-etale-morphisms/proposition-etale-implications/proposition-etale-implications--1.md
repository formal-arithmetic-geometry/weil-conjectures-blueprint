+++
id = "proposition-etale-implications--1"
kind = "proposition"
title = "Étale, ind-étale and weakly étale ring maps (1)"
name_showing = false
order = 29002
aliases = ["bp-r002-1"]
lean = ["AlgebraicGeometry.proAffineEtale.of_isAffine", "RingHom.IndEtale.weaklyEtale"]
uses = ["definition-ind-etale-pro-etale-weakly"]
+++
Let $f:X\to Y$ be an étale morphism of schemes with $X$ affine.
Then $X$ is a pro-étale affine over $Y$. In particular, if a ring map
$R\to B$ is étale, it is ind-étale.

If $R\to B$ is ind-étale, it is weakly étale: both $R\to B$ and
the multiplication map $B\otimes_RB\to B$ are flat.

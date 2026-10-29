+++
id = "sk-prop-sf-existence"
kind = "theorem"
title = "Existence of the exceptional inverse image"
order = 2533
uses = ["sk-def-localizing-closure", "sk-prop-sf-comp-coherence"]
lean = ["AlgebraicGeometry.ProEtale.rightDerivedUpperShriekAdjunction"]
tags = ["sketch"]
+++
Let $\Lambda\in\{A,\Zl,\mathcal O_E,\Ql,E,\Qlb\}$ be any admissible coefficient
ring. For every separated morphism of finite type $f:X\to Y$, the
coproduct-preserving functor
$Rf_!:\Loc(\Dctf(X,\Lambda))\to\Loc(\Dctf(Y,\Lambda))$
([sk-def-localizing-closure], [sk-prop-sf-comp-coherence]) has an exact right
adjoint

$$
f^!:\Loc(\Dctf(Y,\Lambda))\longrightarrow\Loc(\Dctf(X,\Lambda)),\qquad
\Hom(Rf_!M,N)\simeq\Hom(M,f^!N),
$$

for $M\in\Loc(\Dctf(X,\Lambda))$ and $N\in\Loc(\Dctf(Y,\Lambda))$. It is unique
up to unique isomorphism compatible with the adjunction, and it preserves
arbitrary direct sums.

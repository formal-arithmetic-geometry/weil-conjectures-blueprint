+++
id = "sk-prop-sf-existence"
kind = "theorem"
title = "Existence of the exceptional inverse image"
order = 314
lean = ["AlgebraicGeometry.ProEtale.rightDerivedUpperShriekAdjunction"]
uses = ["sk-def-localizing-closure", "sk-prop-sf-comp-coherence"]
tags = ["sketch"]
+++
Let $\Lambda\in\{A,\Zl,\mathcal O_E,\Ql,E,\overline{\mathbf Q}_\ell\}$ be any admissible
coefficient ring. For every separated morphism of finite type $f:X\to Y$,
the coproduct-preserving functor
$Rf_!:\Loc(D^b_{\mathrm{ctf}}(X,\Lambda))\to\Loc(D^b_{\mathrm{ctf}}(Y,\Lambda))$ has an exact
right adjoint

$$
f^!:\Loc(D^b_{\mathrm{ctf}}(Y,\Lambda))\longrightarrow\Loc(D^b_{\mathrm{ctf}}(X,\Lambda)),
\qquad
\Hom(Rf_!M,N)\simeq\Hom(M,f^!N),
$$

for $M\in\Loc(D^b_{\mathrm{ctf}}(X,\Lambda))$ and $N\in\Loc(D^b_{\mathrm{ctf}}(Y,\Lambda))$.
It is unique up to unique isomorphism compatible with the adjunction,
and it preserves arbitrary direct sums.

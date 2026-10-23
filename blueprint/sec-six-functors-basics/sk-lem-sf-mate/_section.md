+++
id = "sk-lem-sf-mate"
kind = "proposition"
title = "Composition, open restriction and compactifications for $f^!$"
order = 2341
uses = ["sk-def-sf-admissible", "sk-prop-sf-open-closed-triangle", "sk-prop-sf-comparison", "sk-prop-sf-existence", "sk-thm-sf-comp-composition", "sk-def-localizing-closure"]
lean = ["AlgebraicGeometry.Etale.nonempty_iso_rightDerivedUpperShriek_comp"]
tags = ["sketch"]
+++
For every admissible $\Lambda$, the adjoints $f^!$ on $\Loc(\Dctf(-,\Lambda))$ of
[sk-prop-sf-existence] have the following canonical compatibilities.

1. For composable $X\xrightarrow{f}Y\xrightarrow{g}Z$ there are canonical
isomorphisms $(gf)^!\simeq f^!g^!$ of functors
$\Loc(\Dctf(Z,\Lambda))\to\Loc(\Dctf(X,\Lambda))$, associative and compatible
with the identity.
2. For an open immersion $j:U\to X$, $j^!\simeq j^*$ as functors
$\Loc(\Dctf(X,\Lambda))\to\Loc(\Dctf(U,\Lambda))$.
3. Let $v:V\to Y$ be an open immersion, $X_V=f^{-1}(V)$ with inclusion
$u:X_V\to X$, and $f_V:X_V\to V$ the restriction of $f$. Then
$u^*f^!\simeq f_V^!v^*$ as functors
$\Loc(\Dctf(Y,\Lambda))\to\Loc(\Dctf(X_V,\Lambda))$.
4. If $f=p\circ j$ is a compactification, then $f^!\simeq j^*\circ p^!$ on
$\Loc(\Dctf(Y,\Lambda))$.

In particular, $f^!$ can be computed locally on $X$ and on $Y$ for open
coverings.

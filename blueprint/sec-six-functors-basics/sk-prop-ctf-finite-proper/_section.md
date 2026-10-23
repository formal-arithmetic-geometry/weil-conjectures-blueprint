+++
id = "sk-prop-ctf-finite-proper"
kind = "proposition"
title = "Proper direct image for finite coefficients"
order = 2303
uses = ["sk-prop-ctf-finite-comparison", "sk-def-localizing-closure"]
tags = ["sketch"]
+++
Let $A$ be a finite commutative ring annihilated by a power of $\ell$, and let $p\colon X\to Y$ be proper. Then
$Rp_*$ sends $\Dctf(X,A)$ to $\Dctf(Y,A)$ and sends $\Loc(\Dctf(X,A))$ to $\Loc(\Dctf(Y,A))$, preserving arbitrary
direct sums on the latter categories. For a cartesian square as in
[sk-prop-proper-base-change-unbounded], the proper base change map $g^*Rp_*\to Rp'_*g'^*$ is an isomorphism
of functors $\Loc(\Dctf(X,A))\to\Loc(\Dctf(Y',A))$. Extension by zero along an open immersion preserves
$\Dctf(-,A)$ and arbitrary sums, so a compactification $f=p\circ j$ supplies the same properties for
$Rp_*j_!$.

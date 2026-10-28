+++
id = "sk-prop-ctf-finite-proper"
kind = "proposition"
title = "Proper direct image for finite coefficients"
order = 2348
uses = ["sk-def-localizing-closure", "sk-def-cd"]
tags = ["sketch"]
+++
Let $A$ be a finite admissible ring and let $p\colon X\to Y$ be proper. Then $Rp_*$ maps $\Dctf(X,A)$ into
$\Dctf(Y,A)$, and it maps $\Loc(\Dctf(X,A))$ into $\Loc(\Dctf(Y,A))$ ([sk-def-localizing-closure]) and
preserves arbitrary direct sums there. More precisely, if $C\in\Dctf(X,A)$ has Tor amplitude in $[a,b]$ and
$\operatorname{cd}_\ell(X_{\bar y})\leq d$ ([sk-def-cd]) for all geometric points $\bar y$ of $Y$, then
$Rp_*C$ has Tor amplitude in $[a,b+d]$.

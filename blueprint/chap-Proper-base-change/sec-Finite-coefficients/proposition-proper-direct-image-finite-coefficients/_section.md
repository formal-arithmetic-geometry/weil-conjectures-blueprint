+++
id = "proposition-proper-direct-image-finite-coefficients"
kind = "proposition"
title = "Proper direct image for finite coefficients"
order = 410
lean = ["AlgebraicGeometry.ProEtale.boundedConstructible_rightDerivedLowerStar_of_isProper_of_isNoetherian"]
uses = ["definition-constructible-sheaves", "definition-cohomological-dimension"]
+++
Let $A$ be a finite admissible ring, and let $p:X\to Y$ be a proper
morphism of separated schemes of finite type over $k$. Then $Rp_*$ maps
$D^b_{\mathrm{ctf}}(X,A)$ into $D^b_{\mathrm{ctf}}(Y,A)$. More precisely, if $C\in D^b_{\mathrm{ctf}}(X,A)$ has Tor
amplitude in $[a,b]$ and $\operatorname{cd}_\ell(X_{\bar y})\leq d$ for all
geometric points $\bar y$ of $Y$, then $Rp_*C$ has Tor amplitude in $[a,b+d]$.

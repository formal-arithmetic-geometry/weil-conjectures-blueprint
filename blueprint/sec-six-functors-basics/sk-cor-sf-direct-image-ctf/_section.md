+++
id = "sk-cor-sf-direct-image-ctf"
kind = "proposition"
title = "Open direct image preserves finite Tor amplitude"
order = 2695
uses = ["sk-def-sfb-constructible", "sk-def-cd"]
lean = ["AlgebraicGeometry.ProEtale.boundedConstructible_rightDerivedLowerStar", "AlgebraicGeometry.ProEtale.torAmplitudeIn_rightDerivedLowerStar"]
tags = ["sketch"]
+++
Let $A$ be a finite commutative $\ell$-primary ring and let
$j:U\hookrightarrow X$ be an open immersion. Then
$Rj_*\colon D(U_{\mathrm{proét}},A)\to D(X_{\mathrm{proét}},A)$ restricts to

$$
Rj_*:\Dctf(U,A)\longrightarrow\Dctf(X,A)
$$

([sk-def-sfb-constructible]). More precisely, if $K$ has Tor amplitude in $[a,b]$ and
$d\ge\operatorname{cd}_\ell(j)$ ([sk-def-cd]), then $Rj_*K$ has Tor amplitude in $[a,b+d]$.

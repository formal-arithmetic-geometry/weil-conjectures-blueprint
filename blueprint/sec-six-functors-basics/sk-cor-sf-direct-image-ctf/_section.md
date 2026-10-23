+++
id = "sk-cor-sf-direct-image-ctf"
kind = "proposition"
title = "Open direct image preserves finite Tor amplitude"
order = 2389
uses = ["sk-prop-sf-comparison", "sk-thm-sf-direct-image-tor-amplitude", "sk-cor-geo-open-finiteness", "sk-cor-geo-open-finiteness-ii", "sk-def-cd"]
lean = ["AlgebraicGeometry.ProEtale.boundedConstructible_rightDerivedLowerStar", "AlgebraicGeometry.ProEtale.torAmplitudeIn_rightDerivedLowerStar"]
tags = ["sketch"]
+++
Let $A$ be a finite commutative $\ell$-primary ring and let
$j:U\hookrightarrow X$ be an open immersion. Then
$Rj_*\colon D(U_{\mathrm{proét}},A)\to D(X_{\mathrm{proét}},A)$ restricts to

$$
Rj_*:\Dctf(U,A)\longrightarrow\Dctf(X,A).
$$

More precisely, if $K$ has Tor amplitude in $[a,b]$ and
$d\ge\operatorname{cd}_\ell(j)$, then $Rj_*K$ has Tor amplitude in $[a,b+d]$.

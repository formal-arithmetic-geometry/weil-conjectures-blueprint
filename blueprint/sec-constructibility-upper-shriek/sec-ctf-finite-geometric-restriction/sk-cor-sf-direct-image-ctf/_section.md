+++
id = "sk-cor-sf-direct-image-ctf"
kind = "proposition"
title = "Open direct image preserves finite Tor amplitude"
order = 351
lean = ["AlgebraicGeometry.ProEtale.boundedConstructible_rightDerivedLowerStar", "AlgebraicGeometry.ProEtale.torAmplitudeIn_rightDerivedLowerStar"]
uses = ["sk-def-sfb-constructible", "sk-def-cd"]
tags = ["sketch"]
+++
Let $j:U\hookrightarrow X$ be an open immersion. Then
$Rj_*:D(U_{\mathrm{pro}\acute{e}t},A)\to D(X_{\mathrm{pro}\acute{e}t},A)$ restricts to

$$
Rj_*:D^b_{\mathrm{ctf}}(U,A)\longrightarrow D^b_{\mathrm{ctf}}(X,A).
$$

More precisely, if $K$ has Tor amplitude in $[a,b]$ and $d\ge \operatorname{cd}_\ell(j)$, then $Rj_*K$ has Tor amplitude in $[a,b+d]$.

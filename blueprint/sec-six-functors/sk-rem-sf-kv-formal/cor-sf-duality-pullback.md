+++
id = "cor-sf-duality-pullback"
kind = "theorem"
title = "Duality against pullback"
order = 3528
tags = ["latex:corollary"]
uses = ["def-sf-datum", "def-sf-orientation", "fix-prop-adjunctions", "lem-sf-mate", "lem-sf-verdier-biduality-equivalence", "thm-sf-verdier-exchange"]
+++
In the setting of [def-sf-datum], assume moreover that $k$ is algebraically
closed and that the exponent of $\Lambda$ is invertible in $k$, and let
$f:X\to Y$ be separated of finite type. Then

$$
D_XLf^*\xrightarrow{\ \sim\ }Rf^!D_Y
$$

as functors $D^b_{ctf}(Y,\Lambda)\to D^b_{ctf}(X,\Lambda)$, naturally in $f$.
If an orientation datum is fixed and $f$ is smooth of pure relative
dimension $d$, this reads $D_XLf^*\cong Lf^*D_Y(d)[2d]$.

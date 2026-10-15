+++
id = "sk-i-dl-a1-local"
kind = "proposition"
title = "Local boundary duality and ramification at infinity"
order = 3068
uses = ["sk-d-dl-a1-setup", "sk-d-real-boundary", "sk-prop-sf-biduality-general", "sk-prop-sf-closed-unit", "sk-prop-sf-open-closed-triangle", "sk-rem-sf-kv-formal", "sk-thm-sf-ctf-stability", "sk-thm-sf-dual-perfect", "sk-thm-sf-verdier-exchange"]
lean = ["AlgebraicGeometry.exists_linearEquiv_dual_stalk_higherDirectImage"]
tags = ["sketch"]
+++
For a dense open immersion $j:U_0\hookrightarrow C_0$ of smooth curves,
a lisse Weil sheaf $F$, and a missing closed point $s$, there is a
Frobenius-equivariant perfect pairing

$$
(j_*F^\vee)_{\bar s}\otimes (R^1j_*F)_{\bar s}
\longrightarrow\DLAQ(-1).
$$

Also, for a nontrivial character $\psi:\mathbf F_p\to\DLAQ^\times$
and $a\in k^\times$, the geometric linear Artin–Schreier sheaf
$\mathcal L_{\psi(ax)}$ is ramified at infinity.

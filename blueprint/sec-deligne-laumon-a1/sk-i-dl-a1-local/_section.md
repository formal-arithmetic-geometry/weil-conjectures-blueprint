+++
id = "sk-i-dl-a1-local"
kind = "lemma"
title = "Local boundary duality"
order = 4020
uses = ["sk-prop-sf-closed-unit", "sk-prop-sf-open-closed-triangle", "sk-thm-pd-verdier-duality", "sk-thm-purity-transport", "sk-thm-sf-verdier-exchange"]
lean = ["AlgebraicGeometry.exists_linearEquiv_dual_stalk_higherDirectImage"]
tags = ["sketch"]
+++
Let $j_0:U_0\hookrightarrow C_0$ be a dense open in a smooth curve
over $k_0$, and let $F$ be a lisse Weil $\Qlb$-sheaf on $U_0$.
For a geometric point $\bar s$ over a closed point
$s\in C_0\setminus U_0$, there is a canonical perfect pairing,
equivariant for the local geometric Frobenius at $s$,

$$
 (j_*F^\vee)_{\bar s}\otimes(R^1j_*F)_{\bar s}
                       \longrightarrow\Qlb(-1).
$$

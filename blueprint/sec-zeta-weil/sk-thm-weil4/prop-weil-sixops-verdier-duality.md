+++
id = "prop-weil-sixops-verdier-duality"
kind = "theorem"
title = "Verdier exchange and biduality on the coefficient class"
order = 3163
tags = ["latex:proposition"]
uses = ["def-weil-exceptional-adjoint-admissibility", "prop-functor-package", "thm-sf-biduality-class"]
+++
In the setting of [prop-functor-package], let $f:X\to Y$
have the exceptional adjoint on the specified constructible categories.
Put $\omega_T=Ra_T^!\Lambda$ and
$D_T=R\mathcal Hom(-,\omega_T)$. Then

$$
D_Y(Rf_!M)\cong Rf_*D_XM.
$$

For $\Lambda=A_{E,n},\mathcal O_E,E$, or $\Qlb$,
the canonical map $K\to D_YD_YK$ is an isomorphism on
$D^b_{ctf}(Y,\Lambda)$, and $D_Y$ is an exact contravariant
anti-equivalence. At the integral and field stages this is the
whole constructible category specified by the coefficient conventions.

## Proof

The exchange is item (7) of [prop-functor-package].
The anti-equivalence and the scope at all four coefficient stages
are [thm-sf-biduality-class]. Its integral and field cases use
the separately established coefficient comparisons.

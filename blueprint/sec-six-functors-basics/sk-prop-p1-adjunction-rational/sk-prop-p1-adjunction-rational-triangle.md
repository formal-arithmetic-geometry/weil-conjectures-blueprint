+++
id = "det-prop-p1-adjunction-rational-triangle"
kind = "lemma"
title = "Triangle identities for the rational projective line"
order = 2758
uses = ["det-prop-p1-adjunction-rational-unit-counit", "sk-prop-diagonal-tower", "sk-prop-geo-p1-adjunction", "sk-thm-sf-pf-field", "sk-prop-proper-base-change-unbounded", "sk-prop-sf-existence"]
+++
With $\eta$ and $\varepsilon$ as in
[det-prop-p1-adjunction-rational-unit-counit], for
$M\in\Loc(\Dbc(\mathbf P^1_Y,\Lambda))$ and $K\in\Loc(\Dbc(Y,\Lambda))$,

$$
\begin{aligned}
\varepsilon_{Rq_*M}\circ Rq_*(\eta_M)
&=Rq_*\bigl(1_M\otimes(\operatorname{Tr}_{p_1}\circ Rp_{1*}\delta_\Lambda)\bigr),\\
q^*(\varepsilon_K)(1)[2]\circ\eta_{q^*K(1)[2]}
&=1_{q^*K(1)[2]}\otimes(\operatorname{Tr}_{p_2}\circ Rp_{2*}\delta_\Lambda),
\end{aligned}
$$

and both right sides are identities. Consequently $(\eta,\varepsilon)$ is the
unit and counit of an adjunction $Rq_*\dashv q^*(1)[2]$ between
$\Loc(\Dbc(\mathbf P^1_Y,\Lambda))$ and $\Loc(\Dbc(Y,\Lambda))$, and
$q^!\simeq q^*(1)[2]$, with $q^!$ the right adjoint of
[sk-prop-sf-existence].

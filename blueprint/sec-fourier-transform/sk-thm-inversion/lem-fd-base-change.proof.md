+++
kind  = "proof"
of    = "lem-fd-base-change"
uses = ["det-def-sfb-open-base-change", "sk-thm-sfb-proper-base-change", "det-thm-sfb-shriek-base-change", "lem-fd-as-lisse", "def-fd-kernel", "def-fd-transform"]
+++
The compactly supported pushforward $p_{2,!}$ of [def-fd-transform] is the composite of extension by zero along a chosen compactification $\bar p_2$ of $p_2$ with the direct image along the proper morphism $\bar p_2$; on bounded constructible $\Lambda$-complexes extension by zero commutes with arbitrary base change ([det-def-sfb-open-base-change]) and the direct image of a proper morphism satisfies proper base change ([sk-thm-sfb-proper-base-change]); together these give the compact-support base change of [det-thm-sfb-shriek-base-change], so for the cartesian square of the base change the identification

$$
g^*p_{2,!}\cong p'_{2,!}\,g_V^*,\qquad g_V:V'\times_{S'}V'^\vee\to V\times_SV^\vee,
$$

holds. The integrand base changes by pullback: $g_V^*(p_1^*K\otimes^L\mathcal K_\psi)\cong{p_1'}^*(g^*K)\otimes^Lg_V^*\mathcal K_\psi$, and $g_V^*\mathcal K_\psi\cong\mathcal K'_\psi$ because the pairing $b'$ is the base change of $b$ and the lisse Artin–Schreier sheaf of [lem-fd-as-lisse] pulls back to the sheaf attached to the base-changed function ([def-fd-kernel]). Combining these identifications, and noting that the shift $[r]$ of [def-fd-transform] commutes with pullback, gives the displayed isomorphism.

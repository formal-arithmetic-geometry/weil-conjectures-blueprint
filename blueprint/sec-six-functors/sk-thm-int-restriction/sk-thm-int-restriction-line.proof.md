+++
kind = "proof"
of = "det-thm-int-restriction-line"
+++
(1) Define the unit $\eta$ and counit $\varepsilon$ by the formulas of
[det-prop-p1-adjunction-rational-unit-counit], with $\Lambda=\mathcal O_E$ and
the $\mathcal O_E$-linear class $\delta_{\mathcal O_E}$ and trace
$\operatorname{Tr}_q$ of [sk-prop-diagonal-tower]. The ingredients of that
definition are the identification
$\Delta_*M\simeq p_1^*M\otimes^{\mathbf L}\Delta_*\mathcal O_{E}$ (proved by
restriction to the diagonal and its complement, for any coefficients), proper
base change and the proper projection formula on
$\Loc(\Dbc(-,\mathcal O_E))$, which hold by [sk-thm-sf-pf-adic]. The proof of
[det-prop-p1-adjunction-rational-triangle] uses only these identifications,
composition of direct images and the integration identities
$\operatorname{Tr}_{p_i}\circ Rp_{i*}\delta_{\mathcal O_E}=1$, which hold over
$\mathcal O_E$ by [sk-prop-diagonal-tower]. So the triangle identities hold,
$Rq_*\dashv q^*(1)[2]$, and since $Rq_!=Rq_*$, uniqueness of right adjoints
gives $q^!\simeq q^*(1)[2]$.

(2) For $d=1$, write $p=q\circ j$ with $j:\mathbf A^1_Y\hookrightarrow\mathbf P^1_Y$.
$j_!$ and $j^*$ preserve the integral localizing categories
([sk-cor-int-compactness-ii]) and $j_!\dashv j^*$, so as in
[det-cor-affine-space-rational-line] $Rp_!=Rq_*j_!\dashv j^*q^*(1)[2]=p^*(1)[2]$,
and $p^!\simeq p^*(1)[2]$. The induction on $d$ of
[det-cor-affine-space-rational-induction] uses only the composition
isomorphisms for $(-)^!$ and is coefficient-independent, giving
$p^!\simeq p^*(d)[2d]$.

(3) Pullback preserves $\Dbc(-,\mathcal O_E)$ by
[sk-def-sfb-dc-restricted-functors]; the Tate twist is tensor product with
the invertible object $\mathcal O_E(d)$, which lies in $\Dbc$, and tensor
product preserves $\Dbc(-,\mathcal O_E)$ by the same lemma; shifts preserve
$\Dbc$.

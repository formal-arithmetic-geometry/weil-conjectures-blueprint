+++
id = "def-wf-constant-weil-twist"
kind = "definition"
title = "Constant Weil twist"
lean = ["AlgebraicGeometry.WeilSheaf.constantTwist", "AlgebraicGeometry.WeilSheaf.nonempty_equiv_stalk_constantTwist", "AlgebraicGeometry.WeilGroup.constLine", "AlgebraicGeometry.WeilGroup.tateLine"]
order = 3786
uses = ["def-weil-weil-sheaf-complex", "def-wf-weil-group", "sk-def-sf-weil-complexes", "det-def-sfb-pulled-back-coefficients"]
+++
For $b\in\Qlb^\times$, let $\mathcal B_b$ be the rank-one
Weil sheaf on a separated finite-type
$k_0$-scheme $X_0$ whose underlying sheaf is the constant module
$\overline{\mathbf Q}_{\ell,X}=p_X^*\underline{\Qlb}$ on $X_{\mathrm{proét}}$
([det-def-sfb-pulled-back-coefficients]) and whose Weil structure is $b\,\varphi_{\Qlb}$,
the canonical structure $\varphi_{\Qlb}$ of [sk-def-sf-weil-complexes] multiplied by $b$
([def-weil-weil-sheaf-complex]). Its
Weil representation sends
$g\in W(X_0)$ to $b^{\deg(g)}$ and is trivial on
$\pi_1(X)$. Tensoring by $\mathcal B_b$ is called a *constant
Weil twist*.

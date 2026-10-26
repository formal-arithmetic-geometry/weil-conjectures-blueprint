+++
id = "def-weil-derived-tensor"
kind = "definition"
title = "Derived tensor product of pro-étale sheaves"
lean = ["AlgebraicGeometry.ProEtale.derivedTensor"]
order = 1160
uses = ["def-weil-pbc-proetale-site", "det-def-sfb-sheaf-tensor-structure", "lem-sfb-derived-monoidal"]
+++
Let $\mathcal A$ be a closed symmetric monoidal Grothendieck abelian category whose tensor
product is additive and which has functorial flat resolutions, and let $Y$ be a scheme with
small pro-étale site $Y_{\mathrm{proét}}$ [def-weil-pbc-proetale-site]. The *derived tensor
product*

$$
-\otimes^{\mathrm L}-\colon D(Y_{\mathrm{proét}},\mathcal A)\times D(Y_{\mathrm{proét}},\mathcal A)\to D(Y_{\mathrm{proét}},\mathcal A)
$$

is the tensor product of the monoidal structure of [lem-sfb-derived-monoidal] on the
derived category of $\Sh(Y_{\mathrm{proét}},\mathcal A)$, equipped with the sheaf tensor
product of [det-def-sfb-sheaf-tensor-structure].

Concretely, a complex $P$ of sheaves is *K-flat* if tensoring it with every acyclic complex
preserves acyclicity. For complexes $K_1,K_2$, choose a quasi-isomorphism $P\to K_1$ with
$P$ K-flat; then

$$
 K_1\otimes^{\mathrm L} K_2=P\otimes K_2 .
$$

For $\mathcal A$ the category of modules over a commutative ring $A$ (so that complexes are
complexes of $A_Y$-modules) this is written $K_1\otimes_A^{\mathrm L}K_2$ in
$D(Y_{\mathrm{proét}},A)$. For a ring map $A\to B$ and a complex $K_1$, write
$K_1\otimes_A^{\mathrm L} B$ for the derived tensor product with the constant $B_Y$-module.

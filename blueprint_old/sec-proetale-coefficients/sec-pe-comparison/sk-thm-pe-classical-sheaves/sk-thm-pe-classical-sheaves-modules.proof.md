+++
kind = "proof"
of = "det-pe-classical-sheaves-modules"
+++
The inverse image $\nu_X^*$ preserves finite products, so it carries the
action map $\Lambda_{X,\Et}\times M\to M$ of a $\Lambda$-module sheaf and the
addition $M\times M\to M$ to the corresponding maps for $\nu_X^*M$, and the
module axioms (equalities of maps built from finite products) are preserved.
The direct image $\nu_{X,*}$ is restriction, so it carries a
$\Lambda_X$-module structure on $G$ to a $\nu_{X,*}\Lambda_X$-module structure,
and $\nu_{X,*}\Lambda_X=\nu_{X,*}\nu_X^*\Lambda_{X,\Et}\cong\Lambda_{X,\Et}$ by
[det-pe-classical-sheaves-unit]. The unit and counit are linear because they
are natural transformations between functors commuting with finite products,
so the adjunction restricts to module sheaves.

Exactness: on module sheaves $\nu_X^*$ preserves kernels (finite limits) and
cokernels (it is a left adjoint), as recorded in
[prop-weil-pbc-site-comparison-finite-level] for finite rings; the argument
uses only that $\nu_X^*$ preserves finite limits and colimits, so it applies to
any discrete $\Lambda$.

Full faithfulness: a $\Lambda$-linear map is in particular a map of sheaves,
and by [det-pe-classical-sheaves-unit] every map of sheaves
$\nu_X^*M\to\nu_X^*M'$ is $\nu_X^*\varphi$ for a unique map of sheaves
$\varphi\colon M\to M'$. If $\nu_X^*\varphi$ is linear, then so is $\varphi$:
the two maps $\Lambda_{X,\Et}\times M\to M'$ expressing linearity agree after
$\nu_X^*$, hence agree by faithfulness.

Essential image: a module sheaf is classical if and only if its underlying sheaf of sets is. If $G$ is a
classical $\Lambda_X$-module sheaf, then the linear counit $\nu_X^*\nu_{X,*}G\to G$ is an isomorphism of sheaves, hence
of module sheaves. Conversely every $\nu_X^*M$ is classical. Together with the
unit isomorphism this shows that $\nu_X^*$ and $\nu_{X,*}$ are inverse
equivalences between $\Mod(X_{\Et},\Lambda)$ and classical
$\Lambda_X$-modules.

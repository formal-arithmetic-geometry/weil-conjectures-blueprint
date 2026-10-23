+++
kind  = "proof"
of    = "lem-sfb-finite-upper-star-unit"
uses = ["def-weil-pbc-proetale-modules", "lem-sfb-finite-upper-star-exact"]
+++
The unit sheaf $\mathbf 1$ on $Y_{\mathrm{proét}}$ is the sheafification of the constant
presheaf $\underline{\mathbf 1}$ ([lem-weil-pbc-sheaf-tensor-closed]). For every presheaf $P$ on
$Y_{\mathrm{proét}}$ there is an isomorphism
$g^*(\operatorname{sheafify}P)\cong\operatorname{sheafify}(\operatorname{Lan}_{b^{\mathrm{op}}}P)$,
since both are left adjoint to restriction along $b^{\mathrm{op}}$ followed by the
inclusion of sheaves. The value of $\operatorname{Lan}_{b^{\mathrm{op}}}\underline{\mathbf 1}$ at
$W$ is a colimit of the constant diagram $\mathbf 1$ over the opposite of a nonempty
cofiltered category (see the proof of [lem-sfb-finite-upper-star-exact]). Such a category
is connected, so the colimit is $\mathbf 1$. Hence
$g^*\mathbf 1\cong\operatorname{sheafify}\underline{\mathbf 1}=\mathbf 1$. Tracing the
adjunctions identifies this isomorphism with the mate of the unit map.

For the special case: a continuous map $\pi_0(|U|)\to\Lambda$ to the finite discrete
$\Lambda$ is locally constant, so it is constant on each member of a finite cover of $U$
by clopen subobjects, which is a covering in the pro-étale topology. Hence the presheaf
$U\mapsto\operatorname{Cont}(\pi_0(|U|),\Lambda)$ and the constant presheaf
$\underline\Lambda$ have the same sheafification, i.e. $\Lambda_{Y,\Proet}$
([def-weil-pbc-proetale-modules]) is the unit $\mathbf 1$ of
$\Sh(Y_{\mathrm{proét}},\Mod_\Lambda)$, and the structure map is the map of the first part.

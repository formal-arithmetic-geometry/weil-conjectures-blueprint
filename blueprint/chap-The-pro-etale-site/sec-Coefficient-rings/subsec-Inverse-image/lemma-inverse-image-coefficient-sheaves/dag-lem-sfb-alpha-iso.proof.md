+++
kind = "proof"
of = "dag-lem-sfb-alpha-iso"
tags = ["sheaf-dag"]
uses = ["dag-def-sfb-pullback-from-point-comp-iso", "dag-sk-def-sfb-pullback-from-point-comp"]
+++
1. Let $c_f\colon f^*\circ p_Y^*\cong p_X^*$ be the natural isomorphism of
[dag-def-sfb-pullback-from-point-comp-iso]. By `def-sfb-alpha`,
$\alpha_f=(c_f)_{\Lambda}$. Put $\beta_f=(c_f^{-1})_{\Lambda}$.
Evaluating $c_f^{-1}\circ c_f=\mathrm{id}$ and
$c_f\circ c_f^{-1}=\mathrm{id}$ at $\Lambda$ gives
$\beta_f\circ\alpha_f=\mathrm{id}_{f^*\Lambda_Y}$ and
$\alpha_f\circ\beta_f=\mathrm{id}_{\Lambda_X}$, respectively.
Thus $\beta_f$ is a two-sided inverse to $\alpha_f$. (uses [dag-def-sfb-pullback-from-point-comp-iso])

Proof dependencies not drawn: `def-sfb-upper-star-from-point`.

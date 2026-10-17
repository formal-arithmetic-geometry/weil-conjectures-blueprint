+++
kind = "proof"
of = "lem-weil-pbc-mittag-leffler"
uses = ["sk-prop-pe-milnor", "det-pe-milnor-sequence"]
+++
Descending chains of subgroups of a finite group stabilize, so the tower is
Mittag--Leffler and $\varprojlim{}^1=0$ by the cokernel description
$R^1\varprojlim_nM_n=\coker(1-T)$ of [det-pe-milnor-sequence](2) (Stacks, Tag 07KV).
Applied to the towers $H^{q-1}(K_n)$, the left term of the Milnor sequence
[det-pe-milnor-sequence](3) vanishes, which identifies
$H^q(R\varprojlim_nK_n)$ with $\varprojlim_nH^q(K_n)$.

+++
kind  = "proof"
of    = "lem-per-lisse-tensor-permanence"
+++
For the $\le$-direction: the cohomology sheaves of
$K\otimes^L\mathcal L$ have support contained in the support of the
corresponding sheaves of $K$ (the tensor with the lisse sheaf is
exact, and the module over each point is the tensor with the free
$\mathcal L_{\bar x}$, of the same support), so the support
inequalities of [def-per-support-condition] for $K$ imply the
ones for $K\otimes^L\mathcal L$. For the $\ge$-direction: by
[lem-per-dual-lisse-tensor],
$D_X(K\otimes^L\mathcal L)\cong D_XK\otimes^L\mathcal L^\vee$, and
applying the $\le$-direction to the lisse sheaf
$\mathcal L^\vee$ gives
$\operatorname{SuppCon}(D_X(K\otimes^L\mathcal L))$ from
$\operatorname{SuppCon}(D_XK)$, which is
$\mathrm{CosuppCon}(K\otimes^L\mathcal L)$ from
$\mathrm{CosuppCon}(K)$ by [def-per-support-condition].

+++
kind = "proof"
of = "lem-weil-pbc-free-etale-module-shriek-comparison"
uses = ["def-weil-pbc-etale-sum-extension"]
+++
For a sheaf $F$ of $\Lambda$-modules, the free–forgetful adjunction, the Yoneda lemma and the sheafification adjunction give a natural bijection $\operatorname{Hom}(P_W,F)\cong F(W)$.

On the other side, the adjunction between extension by zero along the etale morphism $j_W$ and pullback [def-weil-pbc-etale-sum-extension], together with the identification of the pullback along $j_W$ with the restriction to the localized site at $W$, gives $\operatorname{Hom}(j_{W!}\underline\Lambda_W,F)\cong\operatorname{Hom}(\underline\Lambda_W,F|_W)$. The constant-sheaf adjunction evaluates the latter at the terminal object $(W,\mathrm{id})$, giving $\operatorname{Hom}_\Lambda(\Lambda,F(W))\cong F(W)$ by evaluation at $1$.

Both bijections are natural in $F$, so by the Yoneda lemma $P_W\cong j_{W!}\underline\Lambda_W$.

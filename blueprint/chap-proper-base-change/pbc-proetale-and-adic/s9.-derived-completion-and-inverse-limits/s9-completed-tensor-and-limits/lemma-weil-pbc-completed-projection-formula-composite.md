+++
id = "lemma-weil-pbc-completed-projection-formula-composite"
kind = "lemma"
title = "Completed projection-formula composite"
order = 1966
uses = ["def-weil-pbc-completed-tensor-product", "lemma-weil-pbc-direct-image-r-lim", "lemma-weil-pbc-projection-formula-totalization", "lemma-weil-pbc-projection-formula-tower-compatibility"]
+++
Let $B$ be an object on $Y_{\mathrm{proet}}$ such that
$B_n:=B\otimes^LP_n$ is perfect for every $n$. Locally choose a
strict-perfect package for each $B_n$. Then the ordered composite

$$
\begin{aligned}
(Rf_*E)\widehat\otimes^LB
&=R\varprojlim_n((Rf_*E)\otimes^LB_n)\\
&\xrightarrow{R\varprojlim\pi_{E,B_n}}
R\varprojlim_nRf_*(E\otimes^LLf^*B_n)\\
&\xrightarrow{(Rf_*\text{-}R\varprojlim)^{-1}}
Rf_*R\varprojlim_n(E\otimes^LLf^*B\otimes^LP_n)\\
&=Rf_*(E\widehat\otimes^LLf^*B)
\end{aligned}
$$

is an isomorphism, natural in $E,B$, compatible endomorphisms, and base-change
squares.
Its inverse is the reverse composite using direct-image/limit commutation
and $R\varprojlim\rho_{E,B_n}$.

## Proof

Naturality in the coefficient maps $B_{n+1}\to B_n$ makes the levelwise
projection formulas a map of towers. Every $\pi_{E,B_n}$ is an isomorphism
locally by signed totalization, with inverse $\rho_{E,B_n}$; uniqueness of
an inverse glues the local inverses. The second displayed arrow is an
isomorphism because direct image commutes with the product-cone limit. The
forward composite followed by the stated reverse composite is

$$
R\varprojlim(\rho_{E,B_n}\pi_{E,B_n})=R\varprojlim1=1;
$$

the reverse order uses
$R\varprojlim(\pi_{E,B_n}\rho_{E,B_n})=1$ and the two inverse equations for
direct-image/limit commutation. Levelwise operator and base-change
naturality passes through products and the product-cone fibre, proving the
last assertion.

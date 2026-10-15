+++
kind  = "proof"
of    = "sk-lem-coprojection"
+++
Test against an arbitrary $A\in D^b_{ctf}(Z,\Lambda)$ and use that $i$ is a
closed immersion, so $Ri_!=Ri_*$ and $Ri_*\dashv Ri^{!}$:

$$
\begin{aligned}
\operatorname{Hom}_Z\bigl(A,Ri^{!}(K\otimes L)\bigr)
&\cong\operatorname{Hom}_X\bigl(Ri_*A,\ K\otimes L\bigr)
&&\text{(adjunction)}\\
&\cong\operatorname{Hom}_X\bigl(Ri_*A\otimes L^{-1},\ K\bigr)
&&\text{($L$ invertible)}\\
&\cong\operatorname{Hom}_X\bigl(Ri_*(A\otimes Li^{*}L^{-1}),\ K\bigr)
&&\text{(projection formula for $Ri_*$)}\\
&\cong\operatorname{Hom}_Z\bigl(A\otimes Li^{*}L^{-1},\ Ri^{!}K\bigr)
&&\text{(adjunction)}\\
&\cong\operatorname{Hom}_Z\bigl(A,\ Ri^{!}K\otimes Li^{*}L\bigr)
&&\text{($Li^{*}L$ invertible).}
\end{aligned}
$$

The composite is natural in $A$ and is induced by the canonical co-projection
map, so Yoneda gives the asserted isomorphism. The displayed diagonal
identity is this applied twice on $W$, with $K=\Lambda_W$ and the invertible
factors $Lp_1^{*}\omega_f$, $Lp_2^{*}\omega_f$ — invertible because
$\omega_f$ is, being locally isomorphic to $\Lambda_X(d)[2d]$ by [sk-prop-cohsm].

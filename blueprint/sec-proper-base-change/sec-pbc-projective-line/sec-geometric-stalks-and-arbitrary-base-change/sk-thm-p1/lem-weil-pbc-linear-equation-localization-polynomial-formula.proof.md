+++
kind = "proof"
of = "lem-weil-pbc-linear-equation-localization-polynomial-formula"
+++
The class of $\sum_jf_jX_j-1$ in $B$ is zero, so $\sum_{j=1}^rf_jx_j=1$ in $B_{f_i}$, with the
coefficients $f_j$ read in $A_{f_i}$. Separating the $i$-th term gives
$f_ix_i+\sum_{j\ne i}f_jx_j=1$. Apply $\varphi^{-1}$, which is $A_{f_i}$-linear and sends
$x_j$ to $Y_j$ for $j\ne i$:
$$
f_i\,\varphi^{-1}(x_i)+\sum_{j\ne i}f_jY_j=1.
$$
Since $f_i$ is a unit of $A_{f_i}$, multiplying by $f_i^{-1}$ gives
$\varphi^{-1}(x_i)=f_i^{-1}\bigl(1-\sum_{j\ne i}f_jY_j\bigr)$.

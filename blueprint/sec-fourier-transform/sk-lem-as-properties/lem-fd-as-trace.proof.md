+++
kind  = "proof"
of    = "lem-fd-as-trace"
+++
Fix a closed point $u$ of $\mathbf A^1_{k_0}$ of degree $n$, with
$u\in\kappa(u)\subset \overline k$ its image and geometric point
$\bar u$, and let $F_u$ be the local Frobenius operator of
[def-weil-local-frobenius-trace] (the $n$-fold iterate of the
geometric Frobenius), which acts on functions on the fibre by pullback
along $y\mapsto y^{q^n}$. By the affine-line covering
[lem-fd-as-cover-affine-line], the fibre of
$\pi:Y\to\mathbf A^1_{k_0}$, $y\mapsto y^p-y$, over $\bar u$ is
the set

$$
Y_{\bar u}=\{y\in\overline k:\ y^p-y=au\},
$$

which is an $\mathbf F_p$-torsor (the difference of two roots is a
root of $X^p-X$, hence lies in $\mathbf F_p$; the polynomial
$T^p-T-au$ is separable). The stalk
$(\pi_*\overline{\mathbf Q}_\ell)_{\bar u}$ is the space of functions on
$Y_{\bar u}$, with $\sigma_c$ ($c\in\mathbf F_p$) acting by pullback along
$y\mapsto y+c$, and $(\mathcal L_{\psi,ax})_{\bar u}$ is the image of the
idempotent $e_\Psi$ of [def-fd-artin-schreier-sheaf], on which $\sigma_c$
acts by $\Psi(c)$. For $y\in Y_{\bar u}$, induction on $j$ gives

$$
y^{p^j}=y+\sum_{0\leq i<j}(au)^{p^i},
\qquad\text{so}\qquad
y^{q^n}=y^{p^m}=y+\operatorname{Tr}_{\kappa(u)/\mathbf F_p}(au),
\quad m=[\kappa(u):\mathbf F_p],
$$

because the conjugates of $au\in\kappa(u)$ over $\mathbf F_p$ are the
$(au)^{p^i}$, $0\le i<m$. Hence $F_u$ acts on the functions on
$Y_{\bar u}$ as $\sigma_t$ with
$t=\operatorname{Tr}_{\kappa(u)/\mathbf F_p}(au)\in\mathbf F_p$, and so on
the rank-one $\Psi$-isotypic stalk by the scalar $\Psi(t)$. By
transitivity of the trace,
$\Psi(\operatorname{Tr}_{\kappa(u)/\mathbf F_p}(au))
=\Psi(\operatorname{Tr}_{k_0/\mathbf F_p}\operatorname{Tr}_{\kappa(u)/k_0}(au))
=\psi(\operatorname{Tr}_{\kappa(u)/k_0}(au))$, which is the announced
formula; for an $\mathbf F_{q^n}$-point the same computation applies with
$\kappa(u)$ replaced by $\mathbf F_{q^n}$.

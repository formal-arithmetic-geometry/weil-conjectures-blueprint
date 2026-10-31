+++
id = "prose-21-05"
kind = "hidden"
title = "Integrality and independence of $\\ell$"
order = 799
+++
The zeta function is a rational power series with integer coefficients,
so it has a unique reduced fraction $A/B$ with $A,B\in\mathbf Z[T]$ and
$A(0)=B(0)=1$ (Lemma [sk-lem-wweil-integer-rationality]). By purity, the
characteristic polynomials $P_{i,\ell}$ for different $i$ have
reciprocal roots of different absolute values, so they are pairwise
coprime, and the products over odd and over even $i$ form this reduced
fraction. Grouping the reciprocal roots of $A$ and $B$ by absolute value
then recovers each $P_{i,\ell}$ from $Z(X_0,T)$ alone. For smooth proper
$X_0$ of pure dimension $d$, put

$$
H^i_\ell=H^i(X_{\mathrm{pro}\acute{e}t},\Ql),\qquad
P_{i,\ell}(T)=\det(1-T\operatorname{Frob}_{X,\Lambda_X}\mid H^i_\ell),\qquad
b_{i,\ell}=\dim_{\Ql}H^i_\ell.
$$

Since $X_0$ is proper, $H^i_c=H^i$, and the determinant identity of
Corollary [sk-cor-tf-point-counting] for $\Lambda=\Ql$ reads

$$
Z(X_0,T)=\prod_{i=0}^{2d}P_{i,\ell}(T)^{(-1)^{i+1}}.
\tag{21.1}
$$

Since Frobenius is invertible, $\deg P_{i,\ell}=b_{i,\ell}$.
A *reciprocal root* of a polynomial $P$ is a scalar $\alpha$ such
that $1-\alpha T$ divides $P$. Thus the reciprocal roots of
$P_{i,\ell}$ are the Frobenius eigenvalues on $H^i_\ell$.

+++
kind  = "proof"
of    = "sk-cor-hasse"
+++
Over $\mathbf C$ each $P_i$ splits, and since $P_i(0)=1$ none of its roots is
$0$; writing $\alpha_{i,1},\dots,\alpha_{i,b_i}$ for the inverses of its
complex roots, listed with multiplicity, one has
$P_i(T)=\prod_{j=1}^{b_i}(1-\alpha_{i,j}T)$ in $\mathbf C[T]$. By the second
hypothesis, $|\alpha_{i,j}|=q^{i/2}$ for all $i,j$.

All power series in the factorization identity have constant term $1$, so it
may be compared through logarithmic derivatives $T\,\frac{d}{dT}\log$ in
$\mathbf C[[T]]$. By definition of the zeta series,
$T\,Z'(X_0,T)/Z(X_0,T)=\sum_{n\ge1}N_n(X_0)T^n$, and
$$
T\,\frac{P_i'(T)}{P_i(T)}=\sum_{j=1}^{b_i}\frac{-\alpha_{i,j}T}{1-\alpha_{i,j}T}
=-\sum_{n\ge1}\Bigl(\sum_{j=1}^{b_i}\alpha_{i,j}^{n}\Bigr)T^n .
$$
Taking the logarithmic derivative of
$Z(X_0,T)\prod_{i\ \text{even}}P_i=\prod_{i\ \text{odd}}P_i$ and comparing
coefficients of $T^n$ gives, for every $n\ge1$,
$$
N_n(X_0)=\sum_{i=0}^{2d}(-1)^{i}\sum_{j=1}^{b_i}\alpha_{i,j}^{n}.
$$
For $n=1$: since $P_0=1-T$ and $P_{2d}=1-q^dT$, the terms $i=0$ and $i=2d$
are $1$ and $q^d$; they are distinct terms because $d\ge1$, and both carry the
sign $+1$. Hence
$$
N_1(X_0)-(q^d+1)=\sum_{i=1}^{2d-1}(-1)^{i}\sum_{j=1}^{b_i}\alpha_{i,j},
$$
and the triangle inequality with $|\alpha_{i,j}|=q^{i/2}$ gives the stated
bound. The same argument gives
$|N_n(X_0)-(q^{dn}+1)|\le\sum_{i=1}^{2d-1}b_iq^{in/2}$ for every $n\ge1$.

Both endpoint terms must be subtracted: for $X_0=\mathbf P^1$ one has
$b_1=0$ and $N_1=q+1$, so $|N_1-q^d|=1$. For a smooth projective curve $X_0$
of genus $g$ (so $d=1$, and $b_1=\deg P_1=2g$ for the cohomological factors
of [sk-thm-rh]), the bound reads $|N_1-(q+1)|\le2g\sqrt q$.

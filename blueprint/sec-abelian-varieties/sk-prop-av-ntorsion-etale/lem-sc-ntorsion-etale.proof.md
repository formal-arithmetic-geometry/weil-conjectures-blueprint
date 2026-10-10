+++
kind  = "proof"
of    = "lem-sc-ntorsion-etale"
+++
By [lem-sc-isogeny-facts](b), $A[n]$ is a finite flat group
scheme of order $n^{2g}$ over the field $k$, and $n^{2g}$ is prime to
$\operatorname{char}k$ ([lem-sc-mult-n-finite-flat]); by
[lem-sc-fg-order-prime-etale], which holds over any field, it is
etale (equivalently, $[n]$ is etale, by [lem-sc-mult-n-etale-kernel]).

Now let $k$ be algebraically closed. By [lem-sc-finite-etale-points]
the map $A[n](k)\to A[n](k')$ is a bijection. It remains to identify
the group structure. Since $[n]$ is surjective on $k$-points for
every $n$ ([lem-sc-isogeny-surjective]), the group $A(k)$
is divisible; by [lem-sc-av-commutative] it is abelian. For a
prime power $\ell^e$ with $\ell\neq\operatorname{char}k$, the
subgroup $A(k)[\ell^e]=A[\ell^e](k)$ has order
$\ell^{2ge}$ ([lem-sc-finite-etale-points] applied to
$A[\ell^e]$, of order $\ell^{2ge}$ by
[lem-sc-isogeny-facts](b)), so the divisible group $A(k)$
satisfies $|A(k)[\ell]|=\ell^{2g}$, and by
[lem-sc-divisible-group-structure]

$$
A[\ell^e](k)\cong(\mathbf Z/\ell^e\mathbf Z)^{2g}.
$$

For general $n=\prod_i\ell_i^{e_i}$ prime to
$\operatorname{char}k$, the closed subgroup schemes
$A[\ell_i^{e_i}]$ have coprime orders, so
$A[n]=A[\ell_1^{e_1}]\times\cdots\times A[\ell_r^{e_r}]$ as group
schemes (by Bezout's identity the multiplication maps give the
direct product decomposition), and

$$
A[n](k)\cong\prod_i(\mathbf Z/\ell_i^{e_i}\mathbf Z)^{2g}
\cong(\mathbf Z/n\mathbf Z)^{2g}
$$

by the Chinese remainder theorem.

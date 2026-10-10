+++
kind  = "proof"
of    = "sk-prop-av-ntorsion-etale"
uses = ["sk-cor-av-commutative", "sk-def-av-group-scheme", "sk-prop-av-prime-p-etale"]
+++
By [sk-prop-av-isogeny], $A[n]$ is a finite flat group scheme of order
$n^{2g}$ over $k$, with $n$ prime to $\operatorname{char}k$; by
[sk-prop-av-prime-p-etale], valid over any field, it is étale. Now let
$k$ be algebraically closed. By
[sk-prop-av-finite-etale-points] $\lvert A[n](k)\rvert=n^{2g}$ and
$A[n](k)\to A[n](k')$ is bijective. For the group structure: $A(k)$
is abelian by [sk-cor-av-commutative] and divisible by
[sk-prop-av-divisible], and for a prime power $\ell^e$ with
$\ell\ne\operatorname{char}k$ the subgroup $A(k)[\ell^e]=A[\ell^e](k)$
has order $\ell^{2ge}$ by the above, so $\lvert A(k)[\ell]\rvert =\ell^{2g}$ and [sk-prop-av-divisible-structure] gives
$A[\ell^e](k)\cong(\Z/\ell^e\Z)^{2g}$. For general
$n=\prod_i\ell_i^{e_i}$ prime to $\operatorname{char}k$ the subgroup
schemes $A[\ell_i^{e_i}]$ have coprime orders, so
$A[n]=\prod_iA[\ell_i^{e_i}]$ and the Chinese remainder theorem gives
$A[n](k)\cong(\Z/n\Z)^{2g}$.

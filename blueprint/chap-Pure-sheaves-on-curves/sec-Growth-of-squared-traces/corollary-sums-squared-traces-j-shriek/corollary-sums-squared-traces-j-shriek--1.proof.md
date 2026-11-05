+++
kind = "proof"
of = "corollary-sums-squared-traces-j-shriek--1"
order = 1211003
uses = ["definition-trace-function", "proposition-topos-functoriality", "proposition-weights-j-boundary-points"]
+++
Put $B=\mathbf A^1_{\mathbf F_q}-U_0$. Since $j^*j_*\mathcal G\simeq
\mathcal G$, the trace functions agree on $U_0$. Splitting the rational
points into those in $U_0$ and those in $B$ gives

$$
S_n(j_*\mathcal G)=S_n(\mathcal G)+E_n,\qquad
E_n=\sum_{x\in B(\mathbf F_{q^n})}|\iota t_{j_*\mathcal G,n}(x)|^2\ge0.
$$

This is `AlgebraicGeometry.WeilSheaf.LisseOnDenseOpen.traceEnergy_directImage_eq_add`;
nonnegativity gives the first inequality.

For the second, Proposition [proposition-weights-j-boundary-points]
gives punctual weights $\le w$ for $j_*\mathcal G$. The boundary is a
finite set of closed points. Let $N$ be the maximum dimension of its
stalks, with $N=0$ if $B$ is empty, and put
$d=\sum_{s\in B}[k(s):\mathbf F_q]$. Each squared trace in $E_n$ is
at most $N^2q^{nw}$, and a closed point $s$ contributes at most
$[k(s):\mathbf F_q]$ rational points at any level. Thus
$E_n\le dN^2q^{nw}$, as in
`AlgebraicGeometry.WeilSheaf.LisseOnDenseOpen.exists_boundaryEnergy_le`.
Taking $C=dN^2$ in the decomposition proves the bound.

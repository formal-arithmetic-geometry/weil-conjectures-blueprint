+++
kind  = "proof"
of    = "prop-weil-pbc-projective-line"
+++
Higher direct images and cohomology of a sheaf of $\Lambda$-modules agree
with those of the underlying abelian sheaf, so the torsion-sheaf results below
apply to torsion sheaves of $\Lambda$-modules.

Let $F$ be a torsion sheaf of $\Lambda$-modules on $\mathbf P^1_S$ and $q\ge0$.
On every geometric stalk $\bar t\to T$ (over $\bar s\to S$),
[lemma-weil-pbc-p1-exchange-geometric-stalk] identifies the exchange map
$g^{-1}R^qp_*F\to R^qp'_*g'^{-1}F$ with the pullback
$H^q(\mathbf P^1_{\kappa(\bar s)},F|)\to H^q(\mathbf P^1_{\kappa(\bar t)},F|)$
between proper curves over separably closed fields;
[prop-weil-pbc-proper-curve-sepclosed-invariance] makes it an isomorphism.
By conservativity of geometric stalks
([lemma-weil-pbc-geometric-stalk-conservative]) the exchange map is an
isomorphism on every cohomology sheaf, i.e. the derived exchange morphism is
an isomorphism at $F$ placed in degree $0$.

(2): if $I$ is a torsion injective sheaf of $\Lambda$-modules, then
$R^qp_*I=0$ for $q>0$, so $R^qp'_*g'^{-1}I\cong g^{-1}R^qp_*I=0$ by the
previous paragraph.

(1): fix $m$. Both $g^{-1}Rp_*$ and $Rp'_*g'^{-1}$ are triangulated, the
exchange morphism is compatible with the triangles, and both functors carry
$D^{\ge m+1}$ into $D^{\ge m+1}$. Applied to the triangle
$\tau_{\le m}K\to K\to\tau_{>m}K\to$, this identifies $H^m$ of both sides at
$K$ with $H^m$ at the bounded complex $\tau_{\le m}K$, compatibly with the
exchange morphism. Induction on the number of nonzero cohomology sheaves of
$\tau_{\le m}K$, using the triangles
$\tau_{\le n-1}K\to\tau_{\le n}K\to H^n(K)[-n]\to$ and the five lemma,
reduces to the shifted torsion sheaves $H^n(K)[-n]$, which is the previous
paragraph. Hence the exchange morphism is an isomorphism at $K$. (For
$\Lambda=\mathbf F_r$, (2) is $\mathrm{IA}_r$ of
[def-weil-pbc-injective-acyclicity-property] for the projection, from which
[lemma-weil-pbc-property-iff-acyclicity] also recovers (1) for torsion
sheaves.)

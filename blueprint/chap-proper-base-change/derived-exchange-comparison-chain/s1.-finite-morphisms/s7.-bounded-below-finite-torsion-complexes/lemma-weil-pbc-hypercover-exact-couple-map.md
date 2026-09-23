+++
id = "lemma-weil-pbc-hypercover-exact-couple-map"
kind = "lemma"
title = "Hypercover model and $E_1$-map"
order = 1634
uses = ["def-weil-pbc-truncation-exact-couples", "prop-weil-proet-finite-proper-base-change"]
+++
On every split etale hypercover, the exchange maps define a morphism between
the two exact couples. Its first exact-couple page is

$$
\bar e_1^{p,q}:
g^{-1}R^pf_*\mathcal H^q(K)\longrightarrow
R^pf'_*g'^{-1}\mathcal H^q(K),
$$

the S6 finite-torsion map, and
$d'_1\bar e_1^{p,q}=\bar e_1^{p+2,q-1}d_1$ with no residual sign.

## Proof

Evaluate the two rows of truncation triangles on an etale object and choose
a split etale hypercover $U_\bullet$. A Cartan–Eilenberg representative
gives on each side a double complex $C^{m,r}$, where $m$ is the cosimplicial
degree and $r$ the complex degree. Write

$$
d_{\mathrm{simp}}=\sum_{t=0}^{m+1}(-1)^t d_t^*,\qquad
d_{\mathrm{tot}}=d_{\mathrm{simp}}+(-1)^m d_{\mathrm{int}}.
$$

The simplicial identities give $d_{\mathrm{simp}}^2=0$; naturality of the
face maps gives
$d_{\mathrm{simp}}d_{\mathrm{int}}= d_{\mathrm{int}}d_{\mathrm{simp}}$, and the factor $(-1)^m$ makes
$d_{\mathrm{tot}}^2=0$. The left and right totalizations use this same
sign convention.

The sectionwise exchange map pulls a section on every $U_m$ through the
Cartesian square. It commutes with every face and degeneracy map and with
$d_{\mathrm{int}}$, hence is a chain map of the two total complexes.
Filtering by canonical truncation gives exactly the objects
$A_q,G_q$ and $B_q,H_q$ of Definition
[def-weil-pbc-truncation-exact-couples]. Naturality with respect to
$\tau_{\leq q-1}K\to\tau_{\leq q}K$ gives the first three squares of the
displayed triangle.

For the last square, use the cohomological cone convention

$$
\operatorname{Cone}(u)^n=Y^n\oplus X^{n+1},\qquad
d(y,x)=(d_Yy+u(x),-d_Xx).
$$

The connecting map is induced by $(y,x)\mapsto x$. Applying exchange
before or after this projection gives $e_{q-1}[1](x)$ in both routes; the
minus sign belongs to the shifted differential on both sides and does not
change the map. Thus
$k'_q\bar e_q=e_{q-1}[1]k_q$, with no extra sign.

Taking cohomology yields a map of exact couples. On the graded object
$\mathcal H^q(K)[-q]$, degree $p+q$ cohomology is
$g^{-1}R^pf_*\mathcal H^q(K)$ on the left and
$R^pf'_*g'^{-1}\mathcal H^q(K)$ on the right. The induced map is the S0
exchange for that torsion sheaf and therefore the specified S6 map. Finally

$$
\begin{aligned}
d'_1\bar e_1
&=(j'_{q-1})_*(k'_q)_*\bar e_1\\
&=(j'_{q-1})_*(e_{q-1}[1])_*(k_q)_*
=\bar e_1(j_{q-1})_*(k_q)_*
=\bar e_1d_1,
\end{aligned}
$$

which proves differential compatibility.

+++
kind  = "proof"
of    = "lem-sc-c1-brauer-trivial"
uses  = ["cor-sc-hilbert-90-field"]
+++
We use the elementary structure theory of central simple algebras:
a finite central division algebra $D/K$ has dimension $d^2$,
and over a separable closure $K_s$ it becomes $M_d(K_s)$.
The algebraic inputs are the splitting and Wedderburn theorems
([Stacks Project, Tag 03R2](https://stacks.math.columbia.edu/tag/03R2))
and the fact that automorphisms of a matrix algebra are inner
([Stacks Project, Tag 074P](https://stacks.math.columbia.edu/tag/074P)).
Choose a $K$-basis $b_1,\ldots,b_{d^2}$ and a splitting
$\phi:D\otimes_KK_s\simeq M_d(K_s)$. Form the polynomial

$$
P(T_1,\ldots,T_{d^2})=
\det\left(\sum_i T_i\phi(b_i)\right).
$$

It is homogeneous of degree $d$. Changing the splitting conjugates
the matrix, leaving its determinant unchanged. For every
$\sigma\in\operatorname{Gal}(K_s/K)$, applying $\sigma$ to the
splitting gives another splitting, so every coefficient of $P$
is fixed by $\sigma$. Hence $P\in K[T_1,\ldots,T_{d^2}]$.
This defines the reduced norm; it is distinct from the determinant
of left multiplication on the $d^2$-dimensional space $D$.
For any nonzero $x\in D$, its inverse in $D$ remains an inverse
after applying $\phi$, so $P(x)\ne0$. If $d>1$, then
$d^2>d$, and [def-sc-cr-field] supplies a nonzero zero of
$P$, a contradiction. Therefore every central division algebra
has $d=1$ and equals $K$. Wedderburn's theorem now shows that
every central simple algebra is a matrix algebra over $K$, so
the Brauer group of central simple algebras is zero.

For the cohomological Brauer group, embed $\mathbf G_m$ into an
injective sheaf $I$ on $\operatorname{Spec}K_{\Et}$ with cokernel $Q$.
Every quasi-compact etale $K$-scheme is a finite disjoint union of
spectra of finite separable extensions of $K$, so by Hilbert 90
([cor-sc-hilbert-90-field], applied to each of these fields) the
sequence $0\to\mathbf G_m\to I\to Q\to0$ stays exact on sections over
such schemes, and the Čech complexes of $\mathbf G_m$, $I$, $Q$ for a
covering by such schemes form a short exact sequence. Since
$H^2(\mathbf G_m)=H^1(Q)$ and $I$ has trivial Čech cohomology, a class
in $H^2(\operatorname{Spec}K_{\Et},\mathbf G_m)$ vanishes as soon as the
second Čech cohomology of $\mathbf G_m$ vanishes on a cofinal family of
coverings. Every etale covering of $\operatorname{Spec}K$ is refined by
$\operatorname{Spec}M\to\operatorname{Spec}K$ for a finite Galois
extension $M/K$, and the Čech complex of $\mathbf G_m$ for this covering
is the complex of homogeneous cochains of $G=\operatorname{Gal}(M/K)$
with values in $M^\times$. A $2$-cocycle $f$ of $G$ with values in
$M^\times$ defines the crossed product algebra
$\bigoplus_{\sigma\in G}Mu_\sigma$, with $u_\sigma a=\sigma(a)u_\sigma$
and $u_\sigma u_\tau=f(\sigma,\tau)u_{\sigma\tau}$, a central simple
$K$-algebra of dimension $[M:K]^2$; it is a matrix algebra over $K$ by
the first part, and a splitting
$\bigoplus_\sigma Mu_\sigma\cong\operatorname{End}_K(M)$ restricting to
the identity on $M$ exhibits $f$ as a coboundary. Hence
$H^2(G,M^\times)=0$ for every such $M$, and
$H^2(\operatorname{Spec}K_{\Et},\mathbf G_m)=0$.

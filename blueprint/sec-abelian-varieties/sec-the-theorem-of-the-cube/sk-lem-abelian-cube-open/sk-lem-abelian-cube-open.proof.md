+++
kind = "proof"
of = "sk-lem-abelian-cube-open"
+++
Put $X=P\times Q$. Since $X_{\bar k}=P_{\bar k}\times Q_{\bar k}$ is a
product of integral varieties, $X$ is geometrically integral
[Stacks, Tag 05P3](https://stacks.math.columbia.edu/tag/05P3). We may assume that $T=\operatorname{Spec}R$ is affine, and
we let $\mathfrak p$ be the prime of $t$. Below, “shrinking $T$” means
replacing $R$ by $R_g$ for some $g\notin\mathfrak p$; everything already
constructed survives this. Consider the projections

$$
f:X\times T\to T,\qquad f_1:P\times T\to T,\qquad f_2:Q\times T\to T,
$$

and the restrictions $\mathcal L_1$ and $\mathcal L_2$ of $\mathcal L$ to
$P\times q_0\times T$ and $p_0\times Q\times T$, which are trivial. The complexes
$E=Rf_*\mathcal L$ and $E_i=Rf_{i*}\mathcal L_i$ are perfect, and their
formation commutes with base change [Stacks, Tag 0B91](https://stacks.math.columbia.edu/tag/0B91). Restriction of
sections gives a map $E\to E_1\oplus E_2$, compatible with base change.
Since $T$ is affine, $H^0(X\times T,\mathcal L)=H^0(E)$ and likewise for
$E_i$.

*Minimal complexes.* Put $h^j=\dim H^j(X_t,\mathcal O)$ and
$h_i^j=\dim H^j$ of $\mathcal O$ on the fibres $P_t$ and $Q_t$. Since
$\mathcal L$ is trivial on $X_t$ and the $\mathcal L_i$ are trivial,
$E\otimes^{\mathbf L}_R\kappa(t)$ and $E_i\otimes^{\mathbf L}_R\kappa(t)$
have cohomology of dimensions $h^j$ and $h_i^j$, with $h^0=h_i^0=1$.
After shrinking $T$, we may therefore represent $E$ and $E_i$ by
complexes of finite free modules

$$
R\xrightarrow{d}R^{h^1}\to R^{h^2}\to\cdots,\qquad
R\xrightarrow{d_i}R^{h_i^1}\to R^{h_i^2}\to\cdots
$$

whose differentials vanish modulo $\mathfrak p$ [Stacks, Tag 0BCD](https://stacks.math.columbia.edu/tag/0BCD), and the
map $E\to E_i$ by a map of complexes [Stacks, Tag 064B](https://stacks.math.columbia.edu/tag/064B), with components
$a_i:R\to R$ in degree $0$ and $b_i:R^{h^1}\to R^{h_i^1}$ in degree $1$.
Modulo $\mathfrak p$ the differentials vanish, so
$b_i\otimes\kappa(t)$ is the restriction map on $H^1$ of the fibre
over $t$.

*The differentials $d_i$ vanish.* Fix a trivialization
$\mathcal L_1\simeq\mathcal O$, and let $u\in H^0(E_1)=\ker d_1\subset R$
be the section corresponding to $1$. Its image in
$H^0(E_1\otimes^{\mathbf L}\kappa(t))=H^0(P_t,\mathcal O)$ is $1\ne0$,
so $u\notin\mathfrak p$. Since $d_1(u)=u\,d_1(1)=0$, after inverting
$u$ we get $d_1=0$. The same argument gives $d_2=0$.

*The differential $d$ vanishes.* The map
$(b_1,b_2)\otimes\kappa(t)$ is restriction

$$
H^1(P_t\times Q_t,\mathcal O)\longrightarrow
H^1(P_t,\mathcal O)\oplus H^1(Q_t,\mathcal O)
$$

to the slices $P_t\times q_0$ and $p_0\times Q_t$.
By the Künneth formula [Stacks, Tag 0BED](https://stacks.math.columbia.edu/tag/0BED), and since $H^0$ of $\mathcal O$ is
$\kappa(t)$ on both factors, the source is
$\operatorname{pr}_1^*H^1(P_t,\mathcal O)\oplus \operatorname{pr}_2^*H^1(Q_t,\mathcal O)$; in particular
$h^1=h_1^1+h_2^1$. Restriction to $P_t\times q_0$ is the identity on the
first summand and kills the second, because on the second it factors
through $H^1$ of the point $q_0$; restriction to $p_0\times Q_t$ does the
opposite. Hence this map is an isomorphism, so the square matrix
$(b_1,b_2)$ has determinant outside $\mathfrak p$, and after inverting
it $(b_1,b_2)$ is an isomorphism. Since the maps form a map of complexes,
$b_i\circ d=d_i\circ a_i=0$, and therefore $d=0$.

*Conclusion.* Now $H^0(X\times T,\mathcal L)=H^0(E)=\ker d=R$, and
its generator $\sigma$ maps to a generator of
$H^0(E\otimes^{\mathbf L}\kappa(t))=H^0(X_t,\mathcal L_t)$. Since
$\mathcal L_t\simeq\mathcal O_{X_t}$ and $H^0(X_t,\mathcal O)=\kappa(t)$,
the section $\sigma$ vanishes nowhere on $X_t$. Its zero locus is
closed in $X\times T$ and disjoint from $X_t$, and since $f$ is proper,
its image in $T$ is a closed set not containing $t$. On the complement
$U$ of this image, $\sigma$ trivializes $\mathcal L$.

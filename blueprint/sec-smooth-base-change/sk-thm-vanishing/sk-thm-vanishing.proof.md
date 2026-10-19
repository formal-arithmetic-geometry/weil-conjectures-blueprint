+++
kind = "proof"
of = "sk-thm-vanishing"
uses = ["sk-thm-curve-package", "sk-lem-pe-torsor-comparison", "sk-prop-input-spreading", "sk-prop-input-torsors", "sk-prop-normal-form"]
+++
By the comparison theorem it suffices to work on the étale site. By
[Stacks, Tag 03Q8](https://stacks.math.columbia.edu/tag/03Q8), the sheaf
$R^qh_*\underline{\mathbf Z/d}$ is the
sheafification of the presheaf

$$
 U\longmapsto H^q(U\times_S\operatorname{Spec}K,
                      \mathbf Z/d),
 \qquad U\to C\text{ étale},
$$

so we must show that every such class dies on an étale covering of
$U$. For $q\geq2$ the groups vanish already. For $q=1$ they can be
nonzero, and a class is killed by spreading the corresponding torsor
from the generic fibre to a finite étale cover of the curve.

We may take $U$ affine. For $q\geq2$, $U_K$ is empty or a smooth affine
curve over the algebraically closed field $K$, and its cohomology in
these degrees vanishes by $(C_2)$ of [sk-thm-curve-package].

Let $q=1$. By [Stacks, Tag 0EY4](https://stacks.math.columbia.edu/tag/0EY4), after an étale
covering of $U$ the map
$U\to S$ factors as $U\to V\to S$ with $U,V$ affine, $V\to S$ étale,
and $U\to V$ smooth with geometrically connected fibres and a section.
Since $S$ is normal and integral with separably closed function field,
the separated étale map $V\to S$ is a finite disjoint union of open
immersions ([Stacks, Tag 09Z9](https://stacks.math.columbia.edu/tag/09Z9)). Since it suffices
to kill classes on
$U$, we may replace $S$ by one of these opens and $C$ by the
corresponding part of $U$. This keeps the fraction field $L$ and
provides a section $\sigma\colon S\to C$ and geometrically connected
fibres.

Let $\xi\in H^1(C_K,\mathbf Z/d)$. By $(C_6)$ of
[sk-thm-curve-package], the pullback
$H^1(C_L,\mathbf Z/d)\to H^1(C_K,\mathbf Z/d)$ is an isomorphism, since
$d$ is prime to the characteristic; here it is used for the affine
curve $C_L$, as in [Stacks, Tag 03SC](https://stacks.math.columbia.edu/tag/03SC). So there is
a unique

$$
 \xi_L\in H^1(C_L,\mathbf Z/d)
       \quad\text{mapping to }\xi.
$$

By the classification of $H^1$ by torsors
([Stacks, Tag 03AJ](https://stacks.math.columbia.edu/tag/03AJ)) and
[sk-lem-pe-torsor-comparison], $\xi_L$ is the class of a finite
étale $\mathbf Z/d$-torsor $P\to C_L$. The curve $C_L$ is connected.
Let $Z$ be a connected component of $P$ and $G\subseteq\mathbf Z/d$ its
stabilizer, the image of the monodromy of $P$; then $Z\to C_L$ is a
finite étale Galois cover with group $G$, and the pullback of $P$ to
$Z$ has a section, so it kills $\xi_L$.

Since $L$ is algebraically closed, the nonempty fibre of $Z$ over
$\sigma(\eta)$, where $\eta$ is the generic point of $S$, has an
$L$-rational point, and $|G|$ divides $d$, so it is invertible on $S$.
The extension theorem for generic Galois covers
([sk-prop-input-spreading]) states the following. Let $S$ be
integral, normal and qcqs with generic point $\eta$, and let $C\to S$
be qcqs and smooth with geometrically connected fibres and a section
$\sigma$. Let $Z\to C_\eta$ be a finite étale Galois cover with group
$G$ of order invertible on $S$, having a $\kappa(\eta)$-rational point
over $\sigma(\eta)$. Then $Z$ extends to a finite étale Galois cover
$\widetilde Z\to C$ with group $G$. All these hypotheses hold here,
with $C_\eta=C_L$. It remains to see that $\widetilde Z\to C$ is
surjective, so that it is an étale covering. The scheme $C$ is connected,
because $C\to S$ is open and surjective with connected fibres over a
connected base; the image of $\widetilde Z$ is open and closed and
contains the generic fibre, so $\widetilde Z\to C$ is surjective. The
restriction of $\widetilde Z$ over $L$ is $Z$, so the pullback of $\xi$
to $\widetilde Z_K$ is zero, the pulled-back torsor having the
tautological section. Thus every degree-one class is locally zero.

*Complement.*

*Reduction to $\Z/d\Z$.* The higher direct images of a sheaf of
$\Lambda$-modules are those of its underlying abelian sheaf. As an abelian
group $\Lambda/d\Lambda$ has exponent dividing $d$, so it is a direct sum of
cyclic groups $\Z/d'\Z$ with $d'\mid d$, and the constant sheaf
$\Lambda/d\Lambda$ is the corresponding direct sum of constant sheaves
$\Z/d'\Z$. Since $h$ is affine (a base change of $f$), it is quasi-compact
and quasi-separated, so $R^qh_*$ commutes with direct sums. Each $d'\mid d$
is invertible on $S$. It therefore suffices to prove $R^qh_*(\Z/d\Z)=0$ for
$q\ge1$ and every integer $d$ invertible on $S$.

$R^qh_*(\Z/d\Z)$ is the sheaf associated with
$U\mapsto H^q(U\times_S\Spec K,\Z/d\Z)$ on $X_{\Et}$; we must kill
each $\xi$ in one of these groups on an étale cover of $U$.

- $q>1$: $U\times_S\Spec K$ is an affine smooth curve over
$K$, and [sk-prop-cd-affine] gives the vanishing.
- $q=1$: by [sk-prop-normal-form] replace $U$ by an étale
cover with $U\to V\to S$, $U\to V$ affine with geometrically connected fibres
and a section $\sigma$, $V\to S$ étale ($f$ is smooth, so it has
geometrically reduced fibres, and $U\to V$ is smooth because $U\to S$ is
smooth and $V\to S$ is étale); by
[sk-prop-etale-normal], $V$ is an open
of the normal $S$, so we may assume $X\to S$ affine smooth, with
geometrically connected fibres and a section $\sigma$, and
$\xi\in H^1(Y,\Z/d\Z)$. By [sk-prop-ext-invariance] the pullback
map $H^1(X_L,\Z/d\Z)\to H^1(Y,\Z/d\Z)$ is an isomorphism, so $\xi$ comes from a class on
$X_L$; by [sk-prop-input-torsors] this
class is a $\Z/d\Z$-torsor $P\to X_L$, a finite étale cover with a
free transitive $\Z/d\Z$-action. It need not be connected ($X_L$ is
connected, and $P$ is connected only when the class corresponds to a
*surjection* $\pi_1(X_L)\to\Z/d\Z$), so it need not be Galois;
let $P_0\subseteq P$ be a connected component. Then $P_0\to X_L$ is
a finite étale Galois cover whose group is the stabiliser
$G\subseteq\Z/d\Z$ of $P_0$ (the image of $\pi_1(X_L)$), $|G|$
divides $d$, and $P$ is the torsor induced from the $G$-torsor
$P_0$; in particular $P_0\to X_L$ trivializes $P$ (the diagonal
section of $P_0\times_{X_L}P_0$). Over the $L$-point $\sigma(\eta)$
the cover $P_0$ is split ($L$ algebraically closed), so $P_0$ has an
$L$-point above $\sigma(\eta)$; by [sk-prop-input-spreading] $P_0$
($G$ is a finite abelian group of order invertible on $S$, and $P_0$ is a
$G$-torsor) spreads to a $G$-torsor $X'\to X$ with $X'\times_XX_L\cong P_0$
$G$-equivariantly; then $X'\times_XY\to Y$ is the pullback of
$P_0\to X_L$, over which $P$, hence $\xi$, is trivial, so the class
of $\xi$ is killed in $H^1(X'\times_XY,\Z/d\Z)$: $\{X'\to X\}$ is
the required étale cover and the sheaf is zero.

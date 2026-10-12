+++
kind  = "proof"
of    = "sk-thm-vanishing"
uses = ["sk-prop-input-spreading", "sk-prop-input-torsors", "sk-prop-normal-form"]
+++
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

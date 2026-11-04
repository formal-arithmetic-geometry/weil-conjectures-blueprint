+++
kind = "proof"
of = "theorem-verdier-s-theorem-specialization-zero"
order = 1634
uses = ["lemma-base-change-cone-x-z", "lemma-vanishing-generic-points-principal-divisor"]
+++
The main step is that $C_{X,Z}(L)=0$ for every $L\in
D^b_c(X_{\acute et},A)$, which the last paragraph transports to
$D^b_{\mathrm{ctf}}$.  We need the vanishing for all bounded constructible
complexes, because the cokernels $j_!G'$ in the dimension shifting of
Lemma [lemma-vanishing-generic-points-principal-divisor] may have infinite Tor dimension.

By Lemma [lemma-base-change-cone-x-z], we may replace $L$ by $j_!j^*L$
and so assume that $i^*L=0$.  We may then
replace $X$ by its blow-up $\pi:X'=\operatorname{Bl}_ZX\to X$ along $Z$.
The reason is that a complex that vanishes on the centre is recovered
from its pullback to the blow-up, that is, the unit
$L\to R\pi_*\pi^*L$ is an isomorphism. Away from $Z$ this holds because
$\pi$ is an isomorphism there. On $Z$ it holds because proper base
change identifies the target with the cohomology of a fibre with zero
coefficients.  The base change isomorphism for proper maps now gives
$C_{X,Z}(L)\simeq C_{X,Z}(R\pi_*\pi^*L)\simeq R\pi_{Z*}C_{X',\pi^{-1}Z}(\pi^*L)$,
and it suffices to treat the pair $(X',\pi^{-1}Z)$.  The pullback
of the ideal is invertible on the blow-up, so we are reduced to the case of a Cartier divisor.

To have linear projections available, we move the pair into affine space.
By the base change isomorphism for
open immersions the assertion is local, so we may assume that $X$ is affine and
$Z=V(h)$ for a function $h$.  Choosing algebra generators for
$\mathcal O(X)$ and appending $h$ as the last coordinate gives a
closed immersion

$$
\iota:X\hookrightarrow\mathbf A^n,\qquad
Z=\iota^{-1}(\mathbf A^{n-1}\times\{0\})
$$

schematically.  The base change isomorphism for proper maps identifies $R\iota_{Z*}C_{X,Z}(L)$
with $C_{\mathbf A^n,\mathbf A^{n-1}\times\{0\}}(R\iota_*L)$, and since direct
image along a closed immersion is conservative, it suffices to
treat the pair $(\mathbf A^n,\mathbf A^{n-1}\times\{0\})$. This is a
principal divisor in a normal scheme, so
Lemma [lemma-vanishing-generic-points-principal-divisor] applies to it.

We argue by induction on $n\geq1$, again assuming that $L|_Z=0$.
By Lemma [lemma-vanishing-generic-points-principal-divisor], the closure $Y$ of the
support of $C_{X,Z}(L)$ is a proper closed subset of the hyperplane
$Z$; for $n=1$ it is empty, and the assertion follows.  For $n>1$,
choose a line $\lambda$ in the vector space $Z$ such that the linear
projection

$$
q:X\longrightarrow X'=X/\lambda\simeq\mathbf A^{n-1}
$$

is finite on $Y$.  Such a line exists: if the projective point
$\mathbf P(\lambda)$ lies outside the part at infinity of the projective
closure of $Y$ in $\mathbf P(Z\oplus k)$, the usual proof of linear
Noether normalization shows that the projection is finite on $Y$.
Set $Z'=Z/\lambda$, a coordinate hyperplane in $X'$, and compactify
the $\lambda$-direction:

$$
\bar q:\bar X=\mathbf P^1\times X'\longrightarrow X',\qquad
\bar Z=\bar q^{-1}(Z'),\qquad
v:X\hookrightarrow\bar X,\qquad \bar L=v_!L.
$$

Let $\bar q_Z:\bar Z\to Z'$ be the restriction of $\bar q$.
By the base change isomorphism for proper maps and the induction hypothesis,

$$
R\bar q_{Z*}C_{\bar X,\bar Z}(\bar L)
\simeq C_{X',Z'}(R\bar q_*\bar L)=0.
$$

Since the cone commutes with restriction to the open subscheme $X$ of
$\bar X$, the complex $C_{\bar X,\bar Z}(\bar L)$ is supported on
$Y\cup(\bar Z\setminus Z)$.  This is a closed subset finite over
$Z'$. Indeed, $Y$ is finite over $Z'$ and therefore remains closed in
$\bar Z$, and $\bar Z\setminus Z$ is the section at infinity of
$\bar Z\to Z'$. As in Lemma [lemma-nearby-cycles-constant-family],
direct image along a finite map is conservative on complexes with this
support. Hence $C_{\bar X,\bar Z}(\bar L)=0$, and restriction to $X$
gives $C_{X,Z}(L)=0$ on the étale site.

By the comparison for finite coefficients, $K$ and its maps
descend to the classical étale constructible category, where
$C_{X,Z}$ vanishes.  The comparison is exact and
fully faithful, and it identifies pullback, proper direct image and
their adjunction units, so the étale map
(E.1) corresponds to the map in the statement,
which is therefore an isomorphism.

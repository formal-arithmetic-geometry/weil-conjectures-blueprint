+++
kind = "proof"
of = "sk-thm-tf-sp-zero-section"
uses = ["sk-lem-tf-sp-defect-exchanges", "sk-lem-tf-sp-generic-divisor", "sk-lem-tf-sp-constant-family", "sk-thm-pe-constructible-comparison", "sk-cor-pe-finite-tor-comparison"]
+++
We first show that $C_{X,Z}(L)=0$ for every $L\in D^b_c(X_{\acute et},A)$. In the last paragraph we transport this to
$D^b_{\mathrm{ctf}}$. We need the vanishing for all bounded constructible
complexes, because the cokernels $j_!G'$ in the dimension shifting of
Lemma [sk-lem-tf-sp-generic-divisor] may have infinite Tor dimension.

By Lemma [sk-lem-tf-sp-defect-exchanges], we may replace $L$ by $j_!j^*L$,
and hence we may assume that $i^*L=0$. Let $\pi:X'=\operatorname{Bl}_ZX\to X$.
The unit $L\to R\pi_*\pi^*L$ is an isomorphism. Away
from $Z$ this holds because $\pi$ is an isomorphism there, and on $Z$ proper base
change identifies the target with the cohomology of a fibre with zero
coefficients. By the base change isomorphism for proper maps, we then get
$C_{X,Z}(L)\simeq C_{X,Z}(R\pi_*\pi^*L)\simeq R\pi_{Z*}C_{X',\pi^{-1}Z}(\pi^*L)$,
and this reduces the assertion to the pair $(X',\pi^{-1}Z)$. The pullback
of the ideal is invertible on the blow-up, and hence we have reduced to the case of a Cartier divisor.

The assertion is local, so we may assume that $X$ is affine and
$Z=V(h)$ for a function $h$. Choose algebra generators for
$\mathcal O(X)$ and append $h$ as the last coordinate. This gives a
closed immersion

$$
\iota:X\hookrightarrow\mathbf A^n,\qquad
Z=\iota^{-1}(\mathbf A^{n-1}\times\{0\})
$$

schematically. The base change isomorphism for proper maps identifies $R\iota_{Z*}C_{X,Z}(L)$
with $C_{\mathbf A^n,\mathbf A^{n-1}\times\{0\}}(R\iota_*L)$, and direct
image along a closed immersion is conservative. Hence it suffices to
treat the pair $(\mathbf A^n,\mathbf A^{n-1}\times\{0\})$, which is a
principal divisor in a normal scheme, so that
Lemma [sk-lem-tf-sp-generic-divisor] applies to it.

We argue by induction on $n\geq1$. Again we may assume that $L|_Z=0$.
Lemma [sk-lem-tf-sp-generic-divisor] shows that the closure $Y$ of the
support of $C_{X,Z}(L)$ is a proper closed subset of the hyperplane
$Z$. For $n=1$, this subset is empty and the assertion follows. For $n>1$,
choose a line $\lambda$ in the vector space $Z$ such that the linear
projection

$$
q:X\longrightarrow X'=X/\lambda\simeq\mathbf A^{n-1}
$$

is finite on $Y$. To see that such a line exists, choose the projective point
$\mathbf P(\lambda)$ outside the part at infinity of the projective
closure of $Y$ in $\mathbf P(Z\oplus k)$. The projection is then
finite on $Y$ by the usual proof of linear Noether normalization.
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

By locality, $C_{\bar X,\bar Z}(\bar L)$ is supported on
$Y\cup(\bar Z\setminus Z)$. This is a closed subset finite over
$Z'$, because $Y$ is finite and therefore remains closed in $\bar Z$,
and $\bar Z\setminus Z$ is the section at infinity of $\bar Z\to Z'$.
As in Lemma [sk-lem-tf-sp-constant-family], direct image along a finite
map is conservative on complexes with this support. Thus
$C_{\bar X,\bar Z}(\bar L)=0$, and by restriction we get
$C_{X,Z}(L)=0$. This proves the vanishing on the étale site.

Finally, by the comparison for finite coefficients, $K$ and its maps
descend to the classical étale constructible category, where we have
just proved the vanishing of $C_{X,Z}$. The comparison is exact and
fully faithful, and it identifies pullback, proper direct image and
their adjunction units. Therefore it carries the étale map
(E.1) to the map in the statement, which is
an isomorphism.

+++
id = "lem-pc-dim-base-change"
kind = "lemma"
title = "Dimension is unchanged under base change along field extensions"
order = 4348
lean = ["AlgebraicGeometry.dim_baseChange_field"]
uses = ["def-pc-morphism-conventions", "def-pc-field-tower", "def-pc-curve", "def-pc-dimension"]
+++
Let $k$ be a field, $A$ a $k$-algebra of finite type and $K/k$ a field
extension. Then $\dim(A\otimes_kK)=\dim A$; hence for a curve
[def-pc-curve] $X$ over $k$, the scheme
$X_K=X\times_{\operatorname{Spec} k}\operatorname{Spec} K$ has dimension
$1$.

## Proof

Write $A=k[x_1,\dots,x_n]/I$, so
$A\otimes_kK=K[x_1,\dots,x_n]/I\cdot K[x]$. For a Noetherian ring the
dimension formula $\dim k[x]/I=n-\operatorname{ht}(I)$ holds, and the
extension of an ideal under a faithfully flat ring map preserves height:
the map $k[x]\to K[x]$ is faithfully flat (base change of the faithfully
flat $k\to K$), and for flat ring maps $\varphi:R\to R'$ and a prime
$\mathfrak p\subset R$ one has
$\operatorname{ht}(\mathfrak pR')=\operatorname{ht}(\mathfrak p)$. Indeed
$\mathfrak pR'\cap R=\mathfrak p$ (faithful flatness: the tensor
$R/\mathfrak p\to R'/\mathfrak pR'$ is faithfully flat, hence injective, so
the preimage of $\mathfrak pR'$ is $\mathfrak p$); and
$\operatorname{ht}(\mathfrak pR')\ge\operatorname{ht}(\mathfrak p)$ because
a chain $\mathfrak p_0\subsetneq\cdots\subsetneq\mathfrak p_r=\mathfrak p$
of primes of $R$ lifts by going-down for flat ring maps (Algebra, Lemma
10.39.19, [Tag 00HS](https://stacks.math.columbia.edu/tag/00HS)); and
$\operatorname{ht}(\mathfrak pR')\le\operatorname{ht}(\mathfrak p)$ because
a chain of primes in $R'$ above $\mathfrak pR'$ intersects $R$ in a chain
of primes all containing $\mathfrak p$. So the two heights agree.
Combining:
$\dim(A\otimes_kK)=n-\operatorname{ht}(I\cdot K[x])=n-\operatorname{ht}(I)=\dim A$.

For the last assertion: $X$ is a curve, covered by affine opens
$\operatorname{Spec}(A_i)$ with $A_i$ finite type over $k$ and
$\dim A_i\le1$ (and $\dim X=\max_i\dim A_i=1$); the $X_K$ are covered by
the $\operatorname{Spec}(A_i\otimes_kK)$ of dimension $\dim A_i$, so
$\dim X_K=1$.

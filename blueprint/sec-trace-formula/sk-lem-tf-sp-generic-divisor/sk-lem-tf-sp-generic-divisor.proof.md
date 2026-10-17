+++
kind = "proof"
of = "sk-lem-tf-sp-generic-divisor"
uses = ["sk-lem-tf-sp-thick-origin", "sk-lem-tf-sp-defect-exchanges"]
+++
The question is local at such a generic point $\zeta$; discard the other irreducible components of
$X$ and $Z$. First take $L=j_!M_U$, where $U=X\setminus Z$ and $M$ is a finite $A$-module.
Normality makes $X$ regular in codimension one. After shrinking around $\zeta$, both $X$ and
$Z_{\mathrm{red}}$ are smooth over $k$, and a local equation $h$ of $Z_{\mathrm{red}}$ defines a
smooth map $h:X\to\mathbf A^1$. For some $m\geq1$ the ideal of $Z$ is $(h^m)$ on a further
neighbourhood: in the discrete valuation ring at $\zeta$ its defining equation has order $m$, and
its remaining factor is a unit after shrinking. Smooth exchange and [sk-lem-tf-sp-thick-origin]
give $C_{X,Z}(M_X)=0$ there. The last assertion of [sk-lem-tf-sp-defect-exchanges] gives the same
vanishing for $j_!M_U$.

For general $L$, truncation triangles reduce to a constructible sheaf $F$ with $F|_Z=0$. Shrink
around $\zeta$ until $F=j_!G$ for a finite locally constant sheaf $G$ on $U$. This is possible
since the closure of its non-lisse locus in $U$ cannot contain a generic point of the divisor $Z$.
We prove by induction on $r$, simultaneously for all such normal pairs and all $G$, that
$H^r(C_{X,Z}(j_!G))$ vanishes generically. Nearby cycles are left $t$-exact and $i^*j_!G=0$, so

$$
C_{X,Z}(j_!G)=e^*\operatorname{Sp}_{X,Z}(j_!G)[1]\in D^{\geq-1}.
$$

Thus the induction starts with every $r<-1$.

Choose a finite étale surjection $f_U:U'\to U$ trivializing $G$, and let $f:X'\to X$ be the
normalization of $X$ in $U'$. It is finite since $X$ is excellent; $X'$ is normal. Put
$Z'=f^{-1}Z$ and $j':U'\hookrightarrow X'$. The sheaf $f^*F=j'_!f_U^*G$ has constant restriction
on each component of $U'$. Hence the first part of the proof and proper exchange show that
$C_{X,Z}(f_*f^*F)$ vanishes generically on $Z$; here the points over a generic point of the
principal divisor are generic points of its inverse-image divisor in the normal components of
$X'$.

The unit of the finite étale cover is injective, on a geometric stalk being the diagonal inclusion
into a nonempty finite product. Consequently there is a short exact sequence

$$
0\longrightarrow F\longrightarrow f_*f^*F\longrightarrow j_!G'\longrightarrow0,
$$

where $G'$ is again finite locally constant on $U$. Applying $C$ and the long exact sequence, at a
generic point where its middle term vanishes, gives

$$
H^r(C_{X,Z}(F))\simeq H^{r-1}(C_{X,Z}(j_!G')).
$$

The induction hypothesis kills the right side. The argument uses only the injectivity of the unit,
which holds for every $A$.

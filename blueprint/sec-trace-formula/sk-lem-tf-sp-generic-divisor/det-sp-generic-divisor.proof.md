+++
kind = "proof"
of = "det-sp-generic-divisor"
uses = ["det-sp-generic-divisor-constant", "det-sp-defect-proper-smooth", "det-sp-defect-definition", "def-fin-normalization-extension", "lem-fin-normalization-extension-finite"]
+++
Fix a generic point $\zeta$ of $Z$; the question is local at $\zeta$, and we discard the other
irreducible components of $X$ and $Z$. Write $j\colon U=X\setminus Z\hookrightarrow X$.

*Reduction to $j_!G$.* Since $C_{X,Z}$ is exact, truncation triangles reduce to a constructible
sheaf $F$ with $F|_Z=0$. Shrink around $\zeta$ until $F=j_!G$ for a finite locally constant sheaf
$G$ on $U$. This is possible since the closure of its non-lisse locus in $U$ cannot contain a
generic point of the divisor $Z$.

*Induction on the degree.* We prove by induction on $r$, simultaneously for all such normal pairs
and all $G$, that $H^r(C_{X,Z}(j_!G))$ vanishes generically on $Z$. Nearby cycles are left
$t$-exact and $i^*j_!G=0$, so

$$
C_{X,Z}(j_!G)=e^*\operatorname{Sp}_{X,Z}(j_!G)[1]\in D^{\geq-1}.
$$

Thus the induction starts with every $r<-1$.

Choose a finite étale surjection $f_U\colon U'\to U$ trivializing $G$, and let $f\colon X'\to X$
be the normalization of $X$ in $U'$, taken componentwise as in [def-fin-normalization-extension].
It is finite [lem-fin-normalization-extension-finite], and $X'$ is normal. Put $Z'=f^{-1}Z$ and
$j'\colon U'\hookrightarrow X'$. The sheaf $f^*F=j'_!f_U^*G$ has constant restriction on each
component of $U'$, so [det-sp-generic-divisor-constant] applies to each normal component of $X'$
with the principal divisor $Z'$. The points over a generic point of $Z$ are generic points of
$Z'$. Hence the proper case of [det-sp-defect-proper-smooth] shows that
$C_{X,Z}(f_*f^*F)\simeq f_{Z*}C_{X',Z'}(f^*F)$ vanishes generically on $Z$.

The unit $F\to f_*f^*F$ is injective: on a geometric stalk in $U$ it is the diagonal inclusion into
a nonempty finite product, and both sides vanish on $Z$. Consequently there is a short exact
sequence

$$
0\longrightarrow F\longrightarrow f_*f^*F\longrightarrow j_!G'\longrightarrow0,
$$

where $G'$ is again finite locally constant on $U$. Applying $C_{X,Z}$ and the long exact sequence
of cohomology sheaves, at a generic point where the middle term vanishes, gives

$$
H^r(C_{X,Z}(F))\simeq H^{r-1}(C_{X,Z}(j_!G')).
$$

The induction hypothesis kills the right side. The argument uses only the injectivity of the unit,
which holds for every $A$.

+++
kind = "proof"
of = "lemma-vanishing-generic-points-principal-divisor"
order = 1631
+++
For a constant sheaf extended by zero, a smooth map
$X\to\mathbf A^1$ near the generic point reduces the claim to
Lemma [lemma-case-z-v-x-m]. Near the generic point, a general sheaf
is $j_!G$ with $G$ locally constant. After a finite étale cover, $G$
becomes constant, while the cokernel of the unit of the cover is again of
the form $j_!G'$. Passing to this cokernel shifts the cohomological
degree by one, so an induction on the degree proves the claim for all
$G$ at once.

Since the question is local at a generic point $\zeta$ of $Z$, we may
discard the other irreducible components of $X$ and $Z$.  Consider first
$L=j_!M_U$, where $U=X\setminus Z$ and $M$ is a finite $A$-module.
Since $X$ is normal, it is regular in codimension one.  After shrinking
around $\zeta$, both $X$ and $Z_{\mathrm{red}}$ are smooth over $k$,
and a local equation $h$ of $Z_{\mathrm{red}}$ defines a smooth map
$h:X\to\mathbf A^1$.  The local ring $\mathcal O_{X,\zeta}$ is a
discrete valuation ring with uniformizer $h$, so a local equation $g$
of $Z$ can be written $g=wh^m$ with $m\geq1$ and $w$ a unit of
$\mathcal O_{X,\zeta}$.  The function $w$ is regular and invertible on a
neighbourhood of $\zeta$, and there the ideal of $Z$ is $(h^m)$, that
is, $Z=h^{-1}(V(x^m))$ schematically.  By the base change isomorphism
for smooth maps and Lemma [lemma-case-z-v-x-m], we see that $C_{X,Z}(M_X)=0$
there, and the last assertion of Lemma [lemma-base-change-cone-x-z]
yields the same vanishing for $j_!M_U$.

For general $L$, truncation triangles reduce us to a
constructible sheaf $F$ with $F|_Z=0$.  Shrinking around $\zeta$, we may
assume that $F=j_!G$ for a finite locally constant sheaf $G$ on $U$,
since the closure in $X$ of the locus in $U$ where $F$ is not
locally constant cannot contain a generic point of the divisor $Z$.
We prove by induction on $r$, simultaneously for all such normal
pairs and all $G$, that $H^r(C_{X,Z}(j_!G))$ vanishes generically.
As nearby cycles are left $t$-exact and $i^*j_!G=0$, we have

$$
C_{X,Z}(j_!G)=
z^*\operatorname{Sp}_{X,Z}(j_!G)[1]\in D^{\geq-1}.
$$

so the statement holds for every $r<-1$, which starts the induction.

For the induction step, we compare $F=j_!G$ with a sheaf to which the
first part of the proof applies. Choose a finite étale surjection $f_U:U'\to U$ trivializing $G$,
and let $f:X'\to X$ be the normalization of $X$ in $U'$; it
is finite since $X$ is excellent, and $X'$ is normal.  Set
$Z'=f^{-1}Z$ and $j':U'\hookrightarrow X'$.
The sheaf $f^*F=j'_!f_U^*G$ is $j'_!$ of a sheaf that is constant on
each component of $U'$, and $Z'$ is a principal divisor in the normal
scheme $X'$. Since $f$ is finite, the points of $Z'$ over a generic
point of $Z$ are generic points of $Z'$, so the first part of the
proof, applied to $(X',Z')$, and the base change isomorphism for proper maps show that
$C_{X,Z}(f_*f^*F)$ vanishes generically on $Z$.

On a geometric stalk, the unit of the finite étale cover is the
diagonal inclusion into a nonempty finite product, so it is injective
and there is a short exact sequence

$$
0\longrightarrow F\longrightarrow f_*f^*F
\longrightarrow j_!G'\longrightarrow0,
$$

where $G'$ is again finite locally constant on $U$.  Applying $C_{X,Z}$
and taking the long exact sequence at a generic point where the middle
term vanishes, we find

$$
H^r(C_{X,Z}(F))\simeq
H^{r-1}(C_{X,Z}(j_!G')).
$$

By the induction hypothesis, the right side vanishes.

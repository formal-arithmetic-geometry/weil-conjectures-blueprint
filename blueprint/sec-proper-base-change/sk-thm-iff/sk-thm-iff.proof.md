+++
kind = "proof"
of = "sk-thm-iff"
uses = ["sk-def-conv", "sk-thm-acyclicity", "sk-prop-pbc-degree-zero", "sk-def-pbc-conventions"]
+++
*Filtered colimits.* The passage from sheaves killed by an integer to all
torsion sheaves uses continuity of étale cohomology. If $u:T\to S$ is
quasi-compact and quasi-separated, then

$$
\varinjlim_iR^qu_*F_i\xrightarrow{\ \sim\ }R^qu_*\bigl(\varinjlim_iF_i\bigr)
\qquad(q\geq0)
$$

for every filtered system of abelian étale sheaves, and the same holds after
any base change of $u$ (Stacks Project, Tag 09Z1). It suffices to check this
on affine étale $V\to S$. There $R^qu_*F$ is the sheafification of
$V\mapsto H^q(T\times_SV,F|)$, and the schemes $T\times_SV$ are quasi-compact
and quasi-separated, so their cohomology commutes with filtered colimits by
the usual argument with finite covers and finite hypercovers: in degree $q$,
a class and a witness that it dies involve only a finite $(q+1)$-skeleton, so
the cocycle and the finitely many equalities come from a single index.

*(1) implies (2)* by placing $F$ in degree zero.

*(2) implies (3).* If (2) holds and $I$ is injective among
$\mathbf Z/r\mathbf Z$-module sheaves, then $Rf_*I=f_*I$ in
$D^+(Y_{\Et},\mathbf Z/r\mathbf Z)$. Compatibility with underlying abelian
cohomology, explained in [sk-def-pbc-conventions], gives the same equality of
underlying derived direct images. Applying (2) to $I$ makes $Rf'_*g'^{-1}I$
isomorphic in $D^+(Y'_{\Et},\mathbf Z)$ to the degree-zero complex
$g^{-1}f_*I$. This proves (3).

*(3) implies (2).* Assume (3). We first prove (2) for sheaves killed by a
prime $r$. Choose an injective resolution $F\to I^\bullet$ among
$\mathbf Z/r\mathbf Z$-module sheaves. Exactness of $g'^{-1}$ makes
$g'^{-1}I^\bullet$ a resolution of $g'^{-1}F$, and (3) makes its terms
$f'_*$-acyclic. [sk-thm-acyclicity] therefore identifies
$f'_*g'^{-1}I^\bullet$ with $Rf'_*g'^{-1}F$. The complex $g^{-1}f_*I^\bullet$
computes $g^{-1}Rf_*F$ because inverse image is exact.
[sk-prop-pbc-degree-zero] gives an isomorphism

$$
g^{-1}f_*I^m\xrightarrow{\ \sim\ }f'_*g'^{-1}I^m
$$

of sheaves of $\mathbf Z/r\mathbf Z$-modules on $Y'_{\Et}$ in each degree.
Naturality makes these into an isomorphism of complexes. The resolution
formula of [sk-def-exchange] identifies that isomorphism with the derived
exchange map $\Ex_{\square,F}$ in $D^+(Y'_{\Et},\mathbf Z/r\mathbf Z)$, and
hence, forgetting the module structure, in $D^+(Y'_{\Et},\mathbf Z)$. This
proves all degrees of (2) for prime-torsion sheaves.

Next suppose $nF=0$. Induct on the number of prime factors of $n$, counted
with multiplicity. The case $n=1$ is trivial. Choose a prime $r\mid n$ and
use

$$
0\longrightarrow F[r]\longrightarrow F\xrightarrow{\ r\ }rF\longrightarrow0.
$$

The kernel is killed by $r$, and the image $rF$ is killed by $n/r$. Applying
the two functors
$g^{-1}Rf_*,\ Rf'_*g'^{-1}:D^+(X_{\Et},\mathbf Z)\to D^+(Y'_{\Et},\mathbf Z)$
gives a morphism of distinguished triangles in $D^+(Y'_{\Et},\mathbf Z)$
whose outer exchange maps are isomorphisms by the preceding case and
induction. The middle exchange is an isomorphism, by the long exact
cohomology sequences and the five lemma. Thus (2) holds for all sheaves
killed by an integer.

For a general torsion sheaf, write $F=\varinjlim_nF[n]$ as in [sk-def-pbc].
Inverse images commute with colimits, and both $f$ and $f'$ are
quasi-compact and quasi-separated. The filtered-colimit isomorphism above
identifies the exchange map in degree $q$ for $F$ with the filtered colimit
of those for $F[n]$. Hence it is an isomorphism. This proves (2).

*(2) implies (1).* Let $K\in D^+(X_{\Et},\mathbf Z)$ have torsion
cohomology. If $K$ is bounded, induction on its cohomological length using
the canonical truncation triangles and (2) proves that its exchange map is an
isomorphism. In general fix a degree $m$ and choose $N\geq m$. The complex
$\tau_{\leq N}K$ is bounded and has the desired comparison. Both functors
$g^{-1}Rf_*$ and $Rf'_*g'^{-1}$ send $D^{\geq N+1}(X_{\Et},\mathbf Z)$ into
$D^{\geq N+1}(Y'_{\Et},\mathbf Z)$, since inverse images are exact and
derived direct images are left $t$-exact. Applying them to

$$
\tau_{\leq N}K\longrightarrow K\longrightarrow\tau_{\geq N+1}K
\xrightarrow{+1}
$$

shows that comparison for $K$ in degree $m$ is the comparison for
$\tau_{\leq N}K$. It is an isomorphism. Since $m$ was arbitrary, (1)
follows; no bound on the cohomological dimension of $f$ enters.

*Fixed coefficients.* For the fixed ring $\Lambda$ annihilated by an
integer, every module sheaf is torsion. The same injective-resolution
argument proves the sheaf assertion directly from $\mathrm{IA}_\Lambda(f)$,
and the same truncation argument proves it for $D^+$. The reverse
implication follows by applying exchange to an injective $\Lambda$-module
sheaf.

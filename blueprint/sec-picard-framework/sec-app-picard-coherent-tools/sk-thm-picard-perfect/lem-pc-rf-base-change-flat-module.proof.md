+++
kind  = "proof"
of    = "lem-pc-rf-base-change-flat-module"
+++
The intersections $U_y$ of members of $\mathcal U$ are affine since $f$
is separated, and the pulled back cover $\mathcal U_T$ of $X_T$ again
consists of affine opens with affine intersections $U_y\times_ST$. Each
term of $\check C^\bullet(\mathcal U,\mathcal G)$ is a finite product of
modules $N_y=\Gamma(U_y,\mathcal G)$ flat over $A$: relative flatness can
be checked on affine charts and localization at primes. Since
$\Gamma(U_y\times_ST,\mathcal G_T)=N_y\otimes_AB$ with the tensored
restriction maps, $\check C^\bullet(\mathcal U_T,\mathcal G_T)=
\check C^\bullet(\mathcal U,\mathcal G)\otimes_AB$.

Write $C=\check C^\bullet(\mathcal U,\mathcal G)$ and $n=|I|$. The ordered
Cech complex $C$ is $A$-linearly homotopy equivalent to the alternating
Cech complex $C'$ of the same cover (choose a total order on $I$), which is
concentrated in degrees $[0,n-1]$. The cone of $C'\to C$ is contractible
and coincides with $C$ in degrees $\ge n-1$, so the part
$0\to Z^{n-1}\to C^{n-1}\to C^n\to\cdots$ of $C$ is split exact and the
cycle module $Z^{n-1}$ is a direct summand of $C^{n-1}$, hence flat.
Therefore the inclusion of the truncation $K\to C$ is a
quasi-isomorphism and $K$ is a bounded complex of flat $A$-modules; by
[lem-pc-flat-complex-derived-pullback] (on the affine schemes $S$ and $T$)
it computes the derived pullback as $K\otimes_AB$. Split exactness
survives $\otimes_AB$, so $K\otimes_AB\to C\otimes_AB=
\check C^\bullet(\mathcal U_T,\mathcal G_T)$ is still a quasi-isomorphism.
By [lem-pc-cech-resolution] for $\mathcal U_T$, the target represents
$Rf_{T,*}\mathcal G_T$, which proves the claimed isomorphism.

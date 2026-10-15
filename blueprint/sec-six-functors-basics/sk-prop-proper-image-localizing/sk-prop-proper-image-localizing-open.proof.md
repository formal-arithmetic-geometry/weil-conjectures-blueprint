+++
kind = "proof"
of = "det-proper-image-localizing-open"
+++
*Formal properties.* $j_!$ on sheaves is exact, so it is computed termwise on complexes and is an exact
functor of triangulated categories. It is left adjoint to $j^*$, hence preserves all direct sums.

*Constructibility.* If $K\in\Dbc(U,\Lambda)$ has cohomology sheaves locally constant on the strata of a
finite stratification of $U$, then $\mathcal H^n(j_!K)=j_!\mathcal H^n(K)$ (exactness) is locally constant on the
same strata, viewed in $X$, and zero on the added closed stratum $X\setminus U$.

*Finite Tor amplitude.* For finite $A$: [lem-trf-open-ctf] (stalkwise, extension by zero does not change
the Tor amplitude). For $\mathcal O_E$, $E$ and $\Qlb$: $\Dctf=\Dbc$, and preservation of $\Dbc$ is the
extension-by-zero part of [sk-def-sfb-dc-restricted-functors] (via the local models of constructible
sheaves).

*Localizing categories.* Apply [det-proper-image-localizing-principle] with $F=j_!$, $\mathcal G=\Dctf(U,\Lambda)$,
$\mathcal G'=\Dctf(X,\Lambda)$.

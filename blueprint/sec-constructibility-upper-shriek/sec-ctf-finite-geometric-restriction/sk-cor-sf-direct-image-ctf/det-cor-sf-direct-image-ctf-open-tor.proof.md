+++
kind = "proof"
of = "det-cor-sf-direct-image-ctf-open-tor"
+++
Testing with $N=\underline A_U$ shows that $K$ has cohomology in $[a,b]$; in
particular $K$ is bounded.

*(1).* Let $C$ be a cone of the projection morphism. For an object
$V\to X$ of $X_{\mathrm{ét}}$ and $n\in\mathbf Z$,
$H^n(V,C)=\Hom(\underline A_V,C[n])$, and the cohomology sheaf
$\mathcal H^n(C)$ is the sheafification of $V\mapsto H^n(V,C)$; so it suffices
to show $R\Gamma(V,C)=0$ for all quasi-compact étale $V\to X$, i.e. that the
projection morphism induces an isomorphism on $R\Gamma(V,-)$. Such $V$ and
$V_U=V\times_XU$ are of finite type over the separably closed field $k$, so
$\operatorname{cd}(V),\operatorname{cd}(V_U)<\infty$ by [lem-kun-0f10] (2).
By [lem-kun-0f12], applied on $V$ to $E=(Rj_*K)|_V$ and on $V_U$ to
$E=K|_{V_U}$, with the constant complex $M$,

$$
R\Gamma\bigl(V,(Rj_*K)\otimes^{\mathbf L}_A\underline M\bigr)
\cong R\Gamma(V,Rj_*K)\otimes^{\mathbf L}_AM
\cong R\Gamma(V_U,K)\otimes^{\mathbf L}_AM
\cong R\Gamma\bigl(V_U,K\otimes^{\mathbf L}_A\underline M\bigr)
\cong R\Gamma\bigl(V,Rj_*(K\otimes^{\mathbf L}_A\underline M)\bigr),
$$

where the second and fourth isomorphisms are $R\Gamma(V,Rj_*-)=R\Gamma(V_U,-)$.
All maps are the canonical ones built from the same cup-product pairing, so
the composite is $R\Gamma(V,-)$ of the projection morphism.

*(2).* Fix an $A$-module $M$. The complex $K\otimes^{\mathbf L}_A\underline M_U$
has cohomology in $[a,b]$ by hypothesis. Since $A$ is $\ell$-primary, its
cohomology sheaves are torsion, so $R^qj_*$ of each of them vanishes for $q>d$;
induction on the number of nonzero cohomology sheaves via truncation triangles
puts $Rj_*(K\otimes^{\mathbf L}_A\underline M_U)$ in degrees $[a,b+d]$. By
(1), so is $(Rj_*K)\otimes^{\mathbf L}_A\underline M_X$. Taking the stalk at a
geometric point $\bar x$ (an exact, tensor-compatible functor),
$(Rj_*K)_{\bar x}\otimes^{\mathbf L}_AM$ has cohomology in $[a,b+d]$ for every
$A$-module $M$, i.e. the complex of $A$-modules $(Rj_*K)_{\bar x}$ has Tor
amplitude in $[a,b+d]$. For an arbitrary $A$-module sheaf $N$ on
$X_{\mathrm{ét}}$,
$(Rj_*K\otimes^{\mathbf L}_AN)_{\bar x}\cong(Rj_*K)_{\bar x}\otimes^{\mathbf L}_AN_{\bar x}$
therefore has cohomology in $[a,b+d]$, and since geometric stalks are
conservative, $Rj_*K\otimes^{\mathbf L}_AN$ has cohomology in $[a,b+d]$.

*(3).* $K$ and $Rj_*K$ are bounded below and $j$ is quasi-compact and
quasi-separated, so [prop-weil-pbc-comparison-direct-image] gives
$\nu_X^*Rj_*K\cong Rj_{\mathrm{proét},*}\nu_U^*K$. By (2) and
[lem-exc-comparison-tor-interval] (which pulls back a bounded flat model in
degrees $[a,b+d]$), $\nu_X^*Rj_*K$ has Tor amplitude in $[a,b+d]$ against
every pro-étale module sheaf, classical or not.

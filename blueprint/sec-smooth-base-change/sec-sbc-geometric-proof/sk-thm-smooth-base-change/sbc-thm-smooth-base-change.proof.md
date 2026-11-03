+++
kind  = "proof"
of    = "sbc-thm-smooth-base-change"
+++
The case $q=0$ is [sbc-lem-degree-zero-flat-base-change], since by
[lem-pc-smooth-characterization] a
smooth morphism is flat of finite presentation and by
[sbc-lem-smooth-geometrically-reduced] it has geometrically
reduced fibres. We now assume $q>0$ and the theorem in all degrees
$<q$.

*(Filtered torsion.)* For every $n\geq1$ invertible on $S$, let
$\mathcal F[n]$ be the subsheaf of sections of $\mathcal F$ annihilated
by $n$; by [lemma-weil-pbc-torsion-filtered-union]
$\mathcal F=\varinjlim_n\mathcal F[n]$ with $n$ ranging over the
integers invertible on $S$. Inverse images ($f^{-1}$, $h^{-1}$,
$e^{-1}$) commute with filtered colimits as left adjoints, and the
higher direct images $R^qg_*$, $R^qh_*$ commute with filtered colimits
by [lemma-weil-pbc-direct-image-filtered-colimit] (the morphisms
$g$, $h$ being quasi-compact and quasi-separated), so the assertion
for $\mathcal F$ reduces to the case of a sheaf $\mathcal F$
annihilated by some $n$ invertible on $S$; fix such an $n$.

*(Etale locality and the normal form.)* By
[sbc-lem-etale-locality] the question is etale local on $X$ and
$S$. By [sbc-thm-etale-local-normal-form] (the local structure of
smooth morphisms) we may assume $X$ and $S$ are affine and that $X\to S$
factors through an etale morphism $X\to\mathbf A^d_S$. Writing $X\to S$
as the composition
$X\to\mathbf A^{d-1}_S\to\mathbf A^{d-2}_S\to\dots\to\mathbf A^1_S\to S$,
[sbc-lem-base-change-composition] shows that the theorem need
only be proved when $X$ and $S$ are affine and $X\to S$ has relative
dimension one.

*(The induction step.)* For the affine smooth morphism of relative
dimension one $f:X\to S$, the induction hypothesis (the theorem in
degrees $<q$) gives $\mathrm{BC}(f,n,q')$ universally for all
$q'\leq q-1$ in the sense of [sbc-def-base-change-property]: every base
change $f'$ of $f$ along a morphism $S'\to S$ is again smooth
(smoothness being stable under base change, as is immediate from
[def-sbc-smooth-morphisms])
and $n$ is invertible on $S'$, so the theorem in degrees $<q$ applies to
$f'$ and every quasi-compact quasi-separated $g:T\to S'$;
[sbc-lem-rel-dim-one-induction] then gives $\mathrm{BC}(f,n,q)$
universally, in particular $\mathrm{BC}(f,n,q)$, and (a degree-$q$ statement being etale local and stable under
composition, by the first two steps) the theorem holds in degree $q$
for every smooth $f$, every quasi-compact quasi-separated $g$, and
every $n$-torsion $\mathcal F$. Running the filtered colimit back over
the $n$'s gives the theorem in degree $q$ for every torsion $\mathcal F$
with orders invertible on $S$; induction on $q$ finishes the proof.

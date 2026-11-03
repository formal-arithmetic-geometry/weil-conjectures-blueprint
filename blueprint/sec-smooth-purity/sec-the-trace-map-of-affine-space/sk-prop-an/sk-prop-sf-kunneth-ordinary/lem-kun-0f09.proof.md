+++
kind  = "proof"
of    = "lem-kun-0f09"
+++
*Step 1 (the sheaf case).* The assertion is local on $S$: for an open
$V\subseteq S$ the restriction of the square over $V$ is the square of the
same form for $S_i\times_SV$ and $f^{-1}(V)\to V$, and the formation of
$Rf_*$ and of the inverse images commutes with restriction to opens. So we
may assume $S$ affine; then $S$, every $S_i$ and every $X\times_SS_i$ are
quasi-compact and quasi-separated ($f$ being so), as [lem-kun-0ezt] requires. Let $F$ be an abelian sheaf on
$X_{\Et}$ with torsion stalks of orders invertible on $S$, and fix
$p\ge0$. For every $i$ form the cartesian square

$$
\begin{array}{ccc}
X&\xleftarrow{\;g'_i\;}&X\times_SS_i\\
\Big\downarrow{\scriptstyle f}&&\Big\downarrow{\scriptstyle f_i}\\
S&\xleftarrow{\;g_i\;}&S_i
\end{array}
$$

with $g_i:S_i\to S$ smooth and quasi-compact and quasi-separated
([def-sbc-smooth-morphisms],
[def-weil-pbc-scheme-conventions]) and
$f_i=f\times_S\id_{S_i}$. The schemes $X\times_SS_i$ form an inverse
system with affine transition morphisms whose limit is
$X'=X\times_SS'$, by
[lem-kun-fibre-product-limits] (limits and fibre products commute), so
the squares displayed above form an inverse system of cartesian squares, in
the sense of [lem-kun-0ezt], with limit the square of the
statement.

Since $g_i$ is smooth and $f$ is quasi-compact and quasi-separated, the
smooth base change theorem [sbc-thm-smooth-base-change] of the smooth-base-change chapter,
applied to the displayed square in the transposed orientation, gives

$$
g_i^{-1}R^pf_*F\xrightarrow{\ \sim\ }R^pf_{i,*}(g'_i)^{-1}F ,
$$

the coefficient $F$ having torsion stalks of orders invertible on $S$,
hence on the smooth $S$-scheme $S_i$. The sheaves
$F_i:=(g'_i)^{-1}F$ form a compatible system with
$\varinjlim_ip_i^{-1}F_i=(g')^{-1}F$, so the higher-direct-image form
[lem-kun-0ezt] of the limit statement, applied for the fixed $p$,
yields

$$
g^{-1}R^pf_*F\xrightarrow{\ \sim\ }R^pf'_*(g')^{-1}F .
$$

*Step 2 (the complex case).* Let $E\in\Dplus(X_{\Et})$ be as in the
statement. By [thm-sp-truncation-e2] the two
hypercohomology spectral sequences

$$
E_2^{p,q}=R^pf_*\mathcal H^q(E)\Longrightarrow\mathcal H^{p+q}(Rf_*E),
\qquad
E_2'^{p,q}=R^pf'_*(g')^{-1}\mathcal H^q(E)
\Longrightarrow\mathcal H^{p+q}(Rf'_*(g')^{-1}E)
$$

are defined by the truncation filtrations, and by
[lemma-weil-pbc-hypercohomology-convergence] the induced filtrations in
each degree are finite, exhaustive and separated. The exchange morphism
$g^{-1}Rf_*E\to Rf'_*(g')^{-1}E$ of [def-kun-unbounded-exchange] is
natural in the coefficient object
([lem-kun-bc-base-change]), so it is compatible with the truncation
triangles and induces a morphism of filtered objects, hence a morphism of
the two spectral sequences which on $E_2^{p,q}$ is the base-change map
$g^{-1}R^pf_*\mathcal H^q(E)\to R^pf'_*(g')^{-1}\mathcal H^q(E)$. By Step
1 this is an isomorphism for every $(p,q)$; a morphism of spectral
sequences which is an isomorphism on $E_2$ is an isomorphism on every
$E_r$ and hence on the associated graded objects of the abutments. Since
the filtrations are finite, [lem-sp-finite-filtration-induction]
upgrades this to an isomorphism of the abutments in every degree, i.e. to

$$
\mathcal H^n\bigl(g^{-1}Rf_*E\bigr)\xrightarrow{\ \sim\ }
\mathcal H^n\bigl(Rf'_*(g')^{-1}E\bigr)\qquad(n\in\mathbf Z).
$$

A morphism in $D(S'_{\Et})$ which is an isomorphism on all cohomology
sheaves is an isomorphism ([def-weil-pbc-derived-categories]), which is
the assertion.

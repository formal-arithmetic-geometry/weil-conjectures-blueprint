+++
id = "prop-cohomological-finiteness-detailed"
kind = "theorem"
title = "Compact-support finiteness and Frobenius"
order = 5823
tags = ["latex:proposition"]
lean = ["AlgebraicGeometry.Weil.compactSupportCohomology_finite_and_frobenius"]
uses = ["def-weil-derived-complete-integral", "def-weil-small-proetale-site", "prop-finite-compact-support-constructibility-detailed", "sbc-thm-finiteness-finite-type", "thm-weil-cohomological-finiteness"]
+++
Fix the finite-field datum $p,a,q,k_0,k$, where $q=p^a$, choose a prime
$\ell\neq p$, write $\Ql=\mathbf Q_\ell$, choose an algebraic closure
$\Qlb$ of $\Ql$, and choose a finite extension $E/\Ql$ contained in $\Qlb$.
Let $Y_0$ be a separated finite-type $k_0$-scheme, put $Y=Y_0\times_{k_0}k$,
and choose $K\in D^b_{c,\mathrm W}(Y,E)$, a Weil complex. Write $E_Y$ for
the constant Weil sheaf. Then the $E$-coefficient abbreviations mean
$H^i(Y,E)=H^i(Y,E_Y)$ and $H_c^i(Y,E)=H_c^i(Y,E_Y)$.

The ordinary and compact-support cohomology groups, in particular
$H_c^i(Y,K)$ meaning $H_c^i(Y,\operatorname{For}K)$, are
finite-dimensional, vanish outside a finite interval, and carry the
geometric Frobenius automorphism. If $Y_0$ is proper, the canonical
isomorphism
$$
H_c^i(Y,K)\xrightarrow{\ \sim\ }H^i(Y,K)
$$
is Frobenius-equivariant.

If $Y$ has dimension $e\in\mathbf Z_{\geq0}$ and $K=E_Y$ is the constant
Weil sheaf, then $H_c^i(Y,E)=0$ for $i<0$ or $i>2e$. For proper $Y$, the
ordinary cohomology also satisfies $H^i(Y,E)=0$ for $i<0$ or $i>2e$. In
particular, if $X_0/\Fq$ is smooth, proper, geometrically connected of pure
dimension $d\in\mathbf Z_{\geq0}$, and $X=X_0\times_{\Fq}k$, then
$$
H^i(X,\Ql)=0\qquad\text{for }i\notin[0,2d].
$$
Moreover $H^0(X,\Ql)\cong\Ql$, and the geometric Frobenius acts as the
identity on this group.

## Proof

*Step 1 (the finite level).* Work with the finite-field datum
$p,a,q,k_0,k$, the small pro-étale site [def-weil-small-proetale-site] of $Y$, and the geometric hypotheses
imposed on $Y_0$. Write $a_Y:Y\to s=\Spec k$ for the structure morphism, a
separated morphism of finite type over the field $k$ whose geometric fibres
have dimension at most $e$, and let $\mathcal R$ be the amplitude interval
of the Weil complex $K$. The $E$-category has the same objects as the
derived-complete integral category [def-weil-derived-complete-integral] $\Dbc(Y,\mathcal O_E)$; choose an
integral model $K_{\mathcal O}$ of $K$ and let
$K_n=K_{\mathcal O}\otimes^L_{\mathcal O_E}A_{E,n}\in D^b_{ctf}(Y,A_{E,n})$
be its finite-level reductions, objects of the finite-torsion constructible
category forming a uniformly bounded tower with common amplitude
$\mathcal R$.

*Step 2 (compact-support finiteness at finite level).* Apply
[prop-finite-compact-support-constructibility-detailed] to $a_Y$: there are
integers $u\leq v$, depending only on $\mathcal R$ and on $e$, such that
$Ra_{Y,!,n}K_n\in D_c^{[u,v]}(s,A_{E,n})$ for every $n$. The category
$\Dbc(s,A_{E,n})$ is $D^b_{\mathrm{fin}}(A_{E,n})$, so each $H^i_c(Y,K_n)$
is a finite $A_{E,n}$-module vanishing outside $[u,v]$, and these modules
are the compact-support cohomology of $Y$ with coefficients in $K_n$.

*Step 3 (ordinary cohomology at finite level).* By the constructibility
clause of [sbc-thm-finiteness-finite-type] the sheaves $R^qa_{Y,*}F$ are
constructible on $s_{\Et}$ for every constructible $A_{E,n}$-sheaf $F$,
hence finite at the geometric point $\bar s$; the fibre is the cohomology
group in the proper case by the geometric-fibre formula. The vanishing
$H^i(Y,F)=0$ for $i>2e$ is the fibrewise cohomological-dimension bound, and
for $i<0$ it is immediate from the definition of the cohomology groups.

*Step 4 (the stage $E$).* The $E$-coefficient cohomology is the
rationalization of the $\mathcal O_E$-object; the uniform boundedness of
Step 2 makes the $\mathcal O_E$-cohomology finitely generated over the
Noetherian ring $\mathcal O_E$, and tensoring along the flat map
$\mathcal O_E\to E$ gives finite-dimensional $E$-vector spaces with the same
vanishing range. This is the asserted finiteness, boundedness and
finite-dimensionality of $H^i_c(Y,K)$ and $H^i(Y,K)$.

*Step 5 (Frobenius).* The Weil structure of $K$ is the datum
$\varphi_K:Lg_\gamma^*K\to K$, natural in $K$; transported along the
functoriality of the direct image it gives the geometric-Frobenius
automorphism on the ordinary and on the compact-support groups, as
asserted.

*Step 6 (the proper case).* If $Y_0$ is proper, then $a_Y$ is proper and the
canonical comparison $R\Gamma_c(Y,K)\to R\Gamma(Y,K)$ is an isomorphism; it
is Frobenius-equivariant because both operators are those of Step 5.

*Step 7 (the constant sheaf).* For $K=E_Y$ Step 2 gives $H^i_c(Y,E)=0$ for
$i>2e$, with $e=\dim Y$, and the fibrewise cohomological-dimension bound
gives $H^i(Y,E)=0$ for $i>2e$; for $i<0$ both vanish by definition, and in
the proper case Step 6 transfers the statement to $H^i$. The specialisation
$Y=X$, $e=d$, $E=\Ql$ is the vanishing $H^i(X,\Ql)=0$ for
$i\notin[0,2d]$. Finally, $X$ is connected because $X_0$ is geometrically
connected, and the constant sheaf is the lisse sheaf of the trivial
representation of the fundamental group; its space of invariants is all of
$\Ql$, so $H^0(X,\Ql)\cong\Ql$, and the geometric Frobenius acts as the
identity on this constant Weil sheaf.

Unresolved dependencies: def:weil-ordinary-compact-cohomology, def:weil-geometric-hypotheses, def:weil-finite-field-fiber, def:weil-weil-sheaf-complex, def:weil-scheme-morphism-properties, def:weil-global-geometric-frobenius, def:weil-finite-coefficient-point, def:weil-finite-tor-amplitude, def:weil-rationalization-karoubi, def:weil-finite-torsion-constructibility, fin4-lem-fibrewise-cohomological-dimension, cor:weil-pbc-geometric-fiber-finite, thm:galois-fundamental, cor:galois-lisse-representations

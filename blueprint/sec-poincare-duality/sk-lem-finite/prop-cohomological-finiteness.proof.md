+++
kind  = "proof"
of    = "prop-cohomological-finiteness"
+++
*Step 1 (the finite level).* Work with the
finite-field datum ([def-weil-finite-field-fiber]) $p,a,q,k_0,k$ of
the statement, the
small pro-etale site ([def-weil-pbc-proetale-site]) of $Y$, and
the geometric hypotheses ([def-weil-geometric-hypotheses]) imposed on
$Y_0$. Write $a_Y:Y\to s=\Spec k$ for the
structure morphism, a
separated morphism of finite
type ([def-weil-scheme-morphism-properties]) over the field
$k$ whose geometric fibres ([def-weil-scheme-morphism-properties])
have dimension at most $e$, and let
$\mathcal R$ be the amplitude interval of the Weil complex $K$. By
[def-weil-rationalization-karoubi] the $E$-category has the same
objects as the derived-complete integral category
$D^b_c(Y,\mathcal O_E)$ of [def-weil-derived-complete-integral-detailed];
choose an integral model $K_{\mathcal O}$ of $K$ and let
$K_n=K_{\mathcal O}\otimes^L_{\mathcal O_E}A_{E,n}\in D^b_{ctf}(Y,A_{E,n})$ be its finite-level reductions, objects of the
finite-torsion
constructible category ([def-weil-finite-torsion-constructibility]) forming a uniformly
bounded tower with common amplitude $\mathcal R$
([def-weil-finite-tor-amplitude]).

*Step 2 (compact-support finiteness at finite level).* Apply
[prop-finite-compact-support-constructibility] to $a_Y$: there
are integers $u\leq v$, depending only on $\mathcal R$ and on $e$,
such that $Ra_{Y,!,n}K_n\in D_c^{[u,v]}(s,A_{E,n})$ for every $n$.
By [def-weil-finite-coefficient-point] the category
$D^b_c(s,A_{E,n})$ is $D^b_{\mathrm{fin}}(A_{E,n})$, so each
$H^i_c(Y,K_n)$ is a finite $A_{E,n}$-module vanishing outside
$[u,v]$, and by [def-weil-ordinary-compact-cohomology] these
modules are the compact-support cohomology of $Y$ with coefficients in
$K_n$.

*Step 3 (ordinary cohomology at finite level).* By the
constructibility clause of [sbc-thm-finiteness-finite-type] the
sheaves $R^qa_{Y,*}F$ are constructible on $s_{{\mathrm{et}}}$ for
every constructible $A_{E,n}$-sheaf $F$, hence finite at the
geometric point $\bar s$
([def-weil-finite-coefficient-point]); the fibre is the cohomology
group in the proper case by
[cor-weil-pbc-geometric-fiber-finite]. The vanishing
$H^i(Y,F)=0$ for $i>2e$ is
[fin4-lem-fibrewise-cohomological-dimension], and for $i<0$ it is
immediate from the definition of the cohomology groups.

*Step 4 (the stage $E$).* The $E$-coefficient cohomology is the
rationalization of the $\mathcal O_E$-object
([def-weil-rationalization-karoubi]); the uniform boundedness of
Step 2 makes the $\mathcal O_E$-cohomology finitely generated over the
Noetherian ring $\mathcal O_E$, and tensoring along the flat map
$\mathcal O_E\to E$ gives finite-dimensional $E$-vector spaces with
the same vanishing range. This is the asserted finiteness,
boundedness and finite-dimensionality of $H^i_c(Y,K)$ and
$H^i(Y,K)$.

*Step 5 (Frobenius).* The Weil structure of $K$ is the datum
$\varphi_K:Lg_\gamma^*K\to K$ of
[def-weil-weil-sheaf-complex], natural in $K$; transported along
the functoriality of the direct image it gives the geometric-Frobenius
automorphism of [def-weil-global-geometric-frobenius] on the
ordinary and on the compact-support groups, as asserted.

*Step 6 (the proper case).* If $Y_0$ is proper, then
$a_Y$ is proper and the canonical comparison
$R\Gamma_c(Y,K)\to R\Gamma(Y,K)$ of
[def-weil-ordinary-compact-cohomology] is an isomorphism; it is
Frobenius-equivariant because both operators are those of Step 5.

*Step 7 (the constant sheaf).* For $K=E_Y$ Step 2 gives
$H^i_c(Y,E)=0$ for $i>2e$, with $e=\dim Y$, and
[fin4-lem-fibrewise-cohomological-dimension] gives
$H^i(Y,E)=0$ for $i>2e$; for $i<0$ both vanish by definition, and
in the proper case Step 6 transfers the statement to $H^i$. The
specialisation $Y=X$, $e=d$, $E=\Ql$ is the vanishing
$H^i(X,\Ql)=0$ for $i\notin[0,2d]$. Finally, if $Y_0$ is
geometrically connected then $Y$ is connected, and the constant sheaf is
the lisse sheaf of the trivial representation of the fundamental group
([thm-galois-fundamental],
[cor-galois-lisse-representations]); its space of invariants is all
of $E$, so $H^0(Y,E)\cong E$, and the geometric Frobenius acts
as the identity on this group, since the Weil structure of the constant
Weil sheaf is the identity on the constants ([def-weil-weil-sheaf-complex]).
This argument uses only the connectedness of $Y$, not properness or
smoothness; the case $Y_0=X_0$, $E=\Ql$ gives $H^0(X,\Ql)\cong\Ql$.

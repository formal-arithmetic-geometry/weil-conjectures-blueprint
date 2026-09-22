+++
id = "thm-weil-cohomological-finiteness"
kind = "theorem"
title = "Cohomological finiteness and Frobenius"
order = 5822
lean = ["AlgebraicGeometry.Weil.cohomology_finite_and_frobenius"]
uses = ["def-weil-derived-complete-integral", "def-weil-small-proetale-site", "prop-finite-compact-support-constructibility-detailed", "sbc-thm-finiteness-finite-type"]
+++
Fix the finite-field datum $p,a,q,k_0,k$, where $q=p^a$, and choose a prime
$\ell\neq p$; write $\Ql=\mathbf Q_\ell$, choose an algebraic closure
$\Qlb$ of $\Ql$, and let $Y_0$ be a separated finite-type $k_0$-scheme, put
$Y=Y_0\times_{k_0}k$, choose a finite extension $E/\Ql$ contained in
$\Qlb$, and choose $K_E\in D^b_{c,\mathrm W}(Y,E)$. Let
$K=K_E\otimes_E\Qlb$, with Weil-complex and compact-support cohomology
structures.

The geometric Frobenius acts functorially, and there are integers $u\leq v$
such that $H_c^i(Y,K)=0$ for $i\notin[u,v]$, each $H_c^i(Y,K)$ is
finite-dimensional over $\Qlb$, and the Weil structure induces a functorial
geometric-Frobenius automorphism. If $Y_0$ is proper, the canonical map
$R\Gamma_c(Y,K)\to R\Gamma(Y,K)$ is a Frobenius-equivariant isomorphism.

For a finite-type $k_0$-scheme $Y_0$ whose geometric fibre $Y$ has Krull
dimension $e\in\mathbf Z_{\geq0}$, let $(\Qlb)_Y$ be its constant pro-étale
sheaf with the canonical Weil structure. Then both
$$
H^i(Y,(\Qlb)_Y)=0,\qquad H_c^i(Y,(\Qlb)_Y)=0\qquad(i\notin[0,2e]).
$$
If $Y_0$ is geometrically connected, then $H^0(Y,\Qlb)\cong\Qlb$ and the
geometric Frobenius acts as the identity on this constant Weil sheaf.

## Proof

*Step 1 (the finite level).* Work with the finite-field datum
$p,a,q,k_0,k$ and the small pro-étale site [def-weil-small-proetale-site] of $Y$. Write $a_Y:Y\to s=\Spec k$
for the structure morphism: a separated morphism of finite type over the
field $k$, whose geometric fibres have dimension at most $e$. The
$\Qlb$-object $K$ is represented at a finite stage $E/\Ql$, and it admits an
integral model [def-weil-derived-complete-integral] $K_{\mathcal O}\in\Dbc(Y,\mathcal O_E)$ whose reductions
$K_n\in D^b_{ctf}(Y,A_{E,n})$ satisfy the finite-torsion constructibility
condition and form a uniformly bounded tower.

*Step 2 (compact-support finiteness).* Apply
[prop-finite-compact-support-constructibility-detailed] to $a_Y$: there are
integers $u\leq v$, depending only on the amplitude interval of $K$ and on
$e$, with $Ra_{Y,!,n}K_n\in D_c^{[u,v]}(s,A_{E,n})$ for every $n$. At the
geometric point $\bar s$ the category $\Dbc(s,A_{E,n})$ is
$D^b_{\mathrm{fin}}(A_{E,n})$, so each $H^i_c(Y,K_n)$ is a finite
$A_{E,n}$-module, vanishing outside $[u,v]$; these modules compute the
compact-support cohomology of $Y$.

*Step 3 (ordinary cohomology).* By the constructibility clause of
[sbc-thm-finiteness-finite-type] the sheaves $R^qa_{Y,*}F$ are constructible
on $s_{\Et}$ for constructible $F$, hence finite at $\bar s$; for $F$
constructible the vanishing $H^i(Y,F)=0$ for $i>2e$ is the fibrewise
cohomological-dimension bound over the algebraically closed field $k$, and
for $i<0$ it is a matter of definition. The comparison of the fibre with the
group is the geometric-fibre formula in the proper case, where it is the
case needed below.

*Step 4 (the stages).* At the stage $E$ the cohomology is the
rationalization of the $\mathcal O_E$-object; the uniform boundedness of
Step 2 makes the $\mathcal O_E$-cohomology finitely generated over the
Noetherian ring $\mathcal O_E$, so tensoring along the flat map
$\mathcal O_E\to E$ gives finite-dimensional $E$-vector spaces with the same
vanishing range. At the stage $\Qlb$ the object is already represented at
the finite stage $E$ and the cohomology is obtained from the $E$-case by
extension of scalars, hence is again finite-dimensional with the same
vanishing range.

*Step 5 (Frobenius).* The Weil structure $\varphi_K$ is functorial in $K$
and induces the global geometric-Frobenius automorphism on the ordinary and
on the compact-support groups alike, functoriality being that of the direct
image; this is the automorphism asserted in the statement.

*Step 6 (the proper case).* If $Y_0$ is proper, the identification
$R\Gamma_c(Y,K)\xrightarrow{\sim}R\Gamma(Y,K)$ is Frobenius-equivariant,
both operators being the ones produced in Step 5.

*Step 7 (the constant sheaf).* Take $K=(\Qlb)_Y$. For $i>2e$ the
compact-support groups vanish by the amplitude bound of Step 2 and the
ordinary groups by the fibrewise cohomological-dimension bound; for $i<0$
both are zero by definition. For $i=0$, the constant sheaf is the lisse
sheaf attached to the trivial representation of the fundamental group, whose
invariants are all of $\Qlb$; hence $H^0(Y,\Qlb)\cong\Qlb$, and the
geometric Frobenius acts as the identity on this constant Weil sheaf. The
case of a smooth proper geometrically connected $X_0$ of dimension $d$ is
the specialisation $e=d$ with $Y$ proper, where the same bound gives the
vanishing for $i>2d$, the same argument gives $H^0(X,\Ql)\cong\Ql$, and the
Frobenius statement is Step 5.

Unresolved dependencies: def:weil-finite-field-fiber, def:weil-scheme-morphism-properties, def:weil-weil-sheaf-complex, def:weil-ordinary-compact-cohomology, def:weil-global-geometric-frobenius, def:weil-geometric-hypotheses, def:weil-finite-coefficient-point, def:weil-rationalization-karoubi, def:weil-algebraically-closed-coefficients, def:weil-finite-torsion-constructibility, fin4-lem-fibrewise-cohomological-dimension, cor:weil-pbc-geometric-fiber-finite, thm:galois-fundamental, cor:galois-lisse-representations

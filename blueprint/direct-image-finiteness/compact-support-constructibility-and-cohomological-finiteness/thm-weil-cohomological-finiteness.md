+++
id = "thm-weil-cohomological-finiteness"
kind = "theorem"
title = "Cohomological finiteness and Frobenius"
order = 3291
uses = ["cor-galois-lisse-representations", "cor-weil-pbc-geometric-fiber-finite", "def-weil-algebraically-closed-coefficients", "def-weil-derived-complete-integral-detailed", "def-weil-finite-coefficient-point", "def-weil-finite-field-fiber", "def-weil-finite-torsion-constructibility", "def-weil-geometric-hypotheses", "def-weil-global-geometric-frobenius", "def-weil-ordinary-compact-cohomology", "def-weil-pbc-proetale-site", "def-weil-rationalization-karoubi", "def-weil-scheme-morphism-properties", "def-weil-weil-sheaf-complex", "fin4-lem-fibrewise-cohomological-dimension", "prop-finite-compact-support-constructibility", "sbc-thm-finiteness-finite-type", "thm-galois-fundamental"]
+++
Fix the finite-field datum
$p,a,q,k_0,k$, where $q=p^a$, and choose a prime $\ell\neq p$;
write $\Ql=\mathbf Q_\ell$, choose an algebraic closure $\Qlb$ of
$\Ql$, and let
$Y_0$ be
a separated finite-type
$k_0$-scheme, put $Y=Y_0\times_{k_0}k$, choose a finite extension
$E/\Ql$ contained in $\Qlb$, and choose $K_E\in D^b_{c,\mathrm W}(Y,E)$. Let
$K=K_E\otimes_E\Qlb$, with
Weil-complex and
compact-support cohomology
structures. The geometric
Frobenius acts functorially, and there are integers $u\leq v$ such that
$H_c^i(Y,K)=0$ for $i\notin[u,v]$, each $H_c^i(Y,K)$ is
finite-dimensional over $\Qlb$, and the Weil
structure induces a functorial geometric-Frobenius automorphism. If $Y_0$
is proper, the canonical map
$R\Gamma_c(Y,K)\to R\Gamma(Y,K)$ is a
Frobenius-equivariant isomorphism. For a
finite-type $k_0$-scheme
$Y_0$ whose
geometric fiber $Y$ has
Krull dimension
$e\in\mathbf Z_{\geq0}$, let $(\Qlb)_Y$ be its constant
pro-etale sheaf with the canonical
Weil structure. Then both

$$
H^i(Y,(\Qlb)_Y)=0,\qquad H_c^i(Y,(\Qlb)_Y)=0
\qquad(i\notin[0,2e]).
$$

If $Y_0$ is geometrically
connected, then $H^0(Y,\Qlb)\cong\Qlb$ and the
geometric Frobenius acts as
the identity on this constant
Weil sheaf.

## Proof

*Step 1 (the finite level).* Work with the
finite-field datum ([def-weil-finite-field-fiber]) $p,a,q,k_0,k$ of
the statement and the
small pro-etale site ([def-weil-pbc-proetale-site]) of $Y$. Write
$a_Y:Y\to s=\Spec k$ for the
structure morphism: a
separated morphism of finite
type ([def-weil-scheme-morphism-properties]) over the field
$k$, whose geometric fibres ([def-weil-scheme-morphism-properties])
have dimension at most $e$. By
[def-weil-algebraically-closed-coefficients] the $\Qlb$-object
$K$ is represented at a finite stage $E/\Ql$, and by
[def-weil-derived-complete-integral-detailed] and
[def-weil-rationalization-karoubi] it admits an integral model
$K_{\mathcal O}\in D^b_c(Y,\mathcal O_E)$ whose reductions
$K_n\in D^b_{ctf}(Y,A_{E,n})$ satisfy the
finite-torsion
constructibility condition ([def-weil-finite-torsion-constructibility]) and form a uniformly bounded tower.

*Step 2 (compact-support finiteness).* Apply
[prop-finite-compact-support-constructibility] to $a_Y$: there
are integers $u\leq v$, depending only on the amplitude interval of
$K$ and on $e$, with
$Ra_{Y,!,n}K_n\in D_c^{[u,v]}(s,A_{E,n})$ for every $n$. At the
geometric point $\bar s$ the category $D^b_c(s,A_{E,n})$ is
$D^b_{\mathrm{fin}}(A_{E,n})$ by
[def-weil-finite-coefficient-point], so each $H^i_c(Y,K_n)$ is a
finite $A_{E,n}$-module, vanishing outside $[u,v]$; by
[def-weil-ordinary-compact-cohomology] these modules compute the
compact-support cohomology of $Y$.

*Step 3 (ordinary cohomology).* By the constructibility clause of
[sbc-thm-finiteness-finite-type] the sheaves $R^qa_{Y,*}F$ are
constructible on $s_{{\mathrm{et}}}$ for constructible $F$, hence
finite at $\bar s$ ([def-weil-finite-coefficient-point]); for
$F$ constructible the vanishing $H^i(Y,F)=0$ for $i>2e$ is
[fin4-lem-fibrewise-cohomological-dimension] over the algebraically
closed field $k$, and for $i<0$ it is a matter of definition. The
comparison of the fibre with the group is the geometric-fibre formula
[cor-weil-pbc-geometric-fiber-finite] in the proper case, where it
is the case needed below.

*Step 4 (the stages).* At the stage $E$ the cohomology is the
rationalization of the $\mathcal O_E$-object
([def-weil-rationalization-karoubi]); the uniform boundedness of
Step 2 makes the $\mathcal O_E$-cohomology finitely generated over the
Noetherian ring $\mathcal O_E$
([def-weil-derived-complete-integral-detailed]), so tensoring along the flat
map $\mathcal O_E\to E$ gives finite-dimensional $E$-vector spaces
with the same vanishing range. At the stage $\Qlb$ the object is
already represented at the finite stage $E$
([def-weil-algebraically-closed-coefficients]) and the cohomology
is obtained from the $E$-case by extension of scalars, hence is again
finite-dimensional with the same vanishing range.

*Step 5 (Frobenius).* The Weil structure $\varphi_K$ of
[def-weil-weil-sheaf-complex] is functorial in $K$ and induces
the global geometric-Frobenius automorphism of
[def-weil-global-geometric-frobenius] on the ordinary and on the
compact-support groups alike, functoriality being that of the direct
image; this is the automorphism asserted in the statement.

*Step 6 (the proper case).* If $Y_0$ is proper, the
identification $R\Gamma_c(Y,K)\xrightarrow{\sim}R\Gamma(Y,K)$ of
[def-weil-ordinary-compact-cohomology] is Frobenius-equivariant,
both operators being the ones produced in Step 5.

*Step 7 (the constant sheaf).* Take $K=(\Qlb)_Y$. For $i>2e$
the compact-support groups vanish by the amplitude bound of Step 2 and
the ordinary groups by
[fin4-lem-fibrewise-cohomological-dimension]; for $i<0$ both are
zero by definition. For $i=0$, the constant sheaf is the lisse sheaf
attached to the trivial representation of the fundamental group
([thm-galois-fundamental], [cor-galois-lisse-representations]),
whose invariants are all of $\Qlb$; hence
$H^0(Y,\Qlb)\cong\Qlb$, and the geometric Frobenius acts as the
identity on this constant [def-weil-weil-sheaf-complex]. The case
of a smooth proper geometrically
connected ([def-weil-geometric-hypotheses]) $X_0$ of dimension $d$ is
the specialisation $e=d$ with $Y$ proper, where
[fin4-lem-fibrewise-cohomological-dimension] gives the vanishing for
$i>2d$, the same argument gives $H^0(X,\Ql)\cong\Ql$, and the
Frobenius statement is Step 5.

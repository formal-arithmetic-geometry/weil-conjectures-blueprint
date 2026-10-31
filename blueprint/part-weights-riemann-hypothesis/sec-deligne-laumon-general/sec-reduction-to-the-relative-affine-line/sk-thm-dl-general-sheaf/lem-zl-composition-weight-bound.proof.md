+++
kind  = "proof"
of    = "lem-zl-composition-weight-bound"
+++
By [lem-zl-shriek-composition] there is a Frobenius-compatible
isomorphism $R(gh)_!\mathcal F\simeq Rg_!(Rh_!\mathcal F)$. Apply the
hypercohomology spectral sequence of the truncation construction
[thm-sp-truncation-e2] to the exact functor $Rg_!$
and the bounded complex $K=Rh_!\mathcal F$, whose cohomology sheaves
are $\mathcal H^b(K)=R^bh_!\mathcal F$. This is the compact-support
Leray spectral sequence

$$
E_2^{a,b}=R^ag_!\bigl(R^bh_!\mathcal F\bigr)
\ \Longrightarrow\ R^{a+b}(gh)_!\mathcal F,
$$

a spectral sequence in $\Cons(Y,\Qlb)$ ([sk-lem-coefficient-heart]) whose
terms carry Weil structures and whose differentials are Frobenius-compatible:
the Weil structure of $\mathcal F$ induces Weil structures on
$Rh_!\mathcal F$ and $Rg_!Rh_!\mathcal F$ through the base change
isomorphisms for the Frobenius ([sk-def-sf-weil-complexes]), and the
truncation triangles of $K$ are functorial, hence Frobenius-compatible. It has only finitely many nonzero terms, since
$Rh_!$ preserves bounded constructible complexes
([sk-thm-sf-ctf-stability]), and a finite abutment filtration
([lemma-weil-pbc-hypercohomology-convergence]).

By the assertion for $h$, the sheaf $R^bh_!\mathcal F$ is $\iota$-mixed
of weights at most $w+b$. By the assertion for $g$, applied with
$v=w+b$, the term $E_2^{a,b}$ is $\iota$-mixed of weights at most
$w+a+b$. Each later page $E_{r+1}^{a,b}$ is a subquotient of
$E_r^{a,b}$, so $E_\infty^{a,b}$ is a subquotient of $E_2^{a,b}$, and
the abutment $R^n(gh)_!\mathcal F$ carries a finite filtration whose
graded pieces are the $E_\infty^{a,b}$ with $a+b=n$; all of these are
constructible Weil sheaves and all maps are maps of Weil sheaves. For
$a+b=n$ the sheaf $E_2^{a,b}$ is $\iota$-mixed of weights at most
$w+n$, so by the sheaf-level stability of mixedness under Weil
subsheaves and quotients, [lem-a1-mixed-direct-summand](1), applied
page by page, so is $E_\infty^{a,b}$. Stability under extensions,
[lem-a1-mixed-direct-summand](2), applied along the finite filtration,
gives the same bound for $R^n(gh)_!\mathcal F$, in the sense of
[def-weil-punctual-weights].

+++
kind  = "proof"
of    = "lem-zl-sheaves-to-complexes"
+++
Apply the hypercohomology spectral sequence provided by the truncation
construction of [def-weil-pbc-hypercohomology-filtrations] and the
exact triangulated functor $Rf_!$ of [prop-functor-package]:

$$
E_2^{a,b}=R^af_!\bigl(\mathcal H^b(K)\bigr)
\quad\Longrightarrow\quad \mathcal H^{a+b}\bigl(Rf_!K\bigr),
$$

with the finite image filtration of
[lemma-weil-pbc-hypercohomology-convergence]. Its terms are
constructible $\Qlb$-sheaves ([sk-lem-coefficient-heart]); the Weil
structure of $K$ induces Weil structures on them, and the differentials
and filtration are Frobenius-compatible, because the truncation
triangles are functorial and $Rf_!$ commutes with the Frobenius base
change isomorphisms ([sk-def-sf-weil-complexes]). By
[def-weil-complex-weights], each $\mathcal H^b(K)$ is
$\iota$-mixed of weights at most $w+b$; by the hypothesis of the
lemma every $E_2^{a,b}$ is mixed of weights at most $w+a+b$. Every
later page $E_{r+1}^{a,b}$ is a subquotient of $E_r^{a,b}$, and the
abutment $\mathcal H^n(Rf_!K)$ is filtered with graded pieces
$E_\infty^{a,b}$, $a+b=n$; the subquotient and extension bounds of
[lem-a1-subquotient-extension-bounds], [lem-a1-extension-bounds]
(stalkwise, with the
punctual weight convention of
[def-weil-punctual-weights]) show that $\mathcal H^n(Rf_!K)$ is
$\iota$-mixed of weights at most $w+n$, i.e. $Rf_!K\in D_{\le w}(Y_0)$
by [def-weil-complex-weights].

+++
id = "lemma-weil-pbc-exact-couple-abutment"
kind = "lemma"
title = "Finite rows and the abutment comparison"
order = 1739
uses = ["def-weil-pbc-hypercohomology-filtrations", "def-weil-pbc-truncation-exact-couples", "lemma-weil-pbc-hypercohomology-convergence"]
+++
In total degree $n$, the two exact couples have only the finite row range
$a\leq q\leq n$. Their induced abutment map is the cohomology map

$$
\mathcal H^n(g^{-1}Rf_*K)\longrightarrow
\mathcal H^n(Rf'_*g'^{-1}K)
$$

of the derived exchange morphism, with the image filtrations of Definition
[def-weil-pbc-hypercohomology-filtrations].

## Proof

On $\mathcal E_1^{p,q}$ one has $p\geq0$ and $q\geq a$. The equality
$p+q=n$ therefore forces $a\leq q\leq n$. On a hypercover total complex,
only these finitely many filtered quotients contribute to degree $n$.
Consequently direct-sum and product totalization agree in that degree, the
filtration is finite and separated, and passage from a finite skeleton to
the full hypercover changes none of its graded terms.

The maps $e_q:A_q\to B_q$ commute with
$\tau_{\leq q}K\to K$. For $q\geq n$, the omitted cohomology sheaves of
$K$ have degrees greater than $n$; after a nonnegative right-derived
functor they cannot contribute to total degree $n$. Hence

$$
\mathcal H^n(A_q)\xrightarrow{\sim}
\mathcal H^n(g^{-1}Rf_*K),\qquad
\mathcal H^n(B_q)\xrightarrow{\sim}
\mathcal H^n(Rf'_*g'^{-1}K).
$$

Under these identifications, $\mathcal H^n(e_q)$ is
$\mathcal H^n(\operatorname{Ex}_{\square,K})$ by naturality of exchange in
the truncation map. Its filtration is the image of
$\mathcal H^n(A_q)$ and maps to the image of $\mathcal H^n(B_q)$, exactly
the two filtrations defined earlier. Thus the exact-couple abutment map is
the specified derived exchange map, rather than an unnamed filtered
isomorphism.

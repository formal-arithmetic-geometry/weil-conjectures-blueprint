+++
id = "sk-l-dl-general-composition"
kind = "section"
title = "Composition"
order = 2819
lean = ["AlgebraicGeometry.HasDirectImageWeightBound.comp"]
uses = ["sk-d-dl-general-weights", "sk-thm-sf-comp-composition"]
+++
*Lemma (sketch).*

Let $h_0:X_0\to Z_0$ and $g_0:Z_0\to Y_0$ be separated finite-type
morphisms of $k_0$-schemes, where $Z_0$ and $Y_0$ are quasi-separated of
finite type over $k_0$. If the direct-image weight assertion of
[sk-thm-dl-general-sheaf] holds for $h_0$ and for $g_0$, it holds for
$g_0h_0$.

## Proof

The Frobenius-equivariant compact-support Leray spectral sequence is

$$
E_2^{a,b}=R^ag_{0!}R^bh_{0!}F_0
\ \Longrightarrow\ R^{a+b}(g_0h_0)_!F_0.
$$

For $F_0$ of weights at most $w$, its $E_2^{a,b}$ has weights at most
$w+b+a$. In total degree $n$, the abutment has a finite filtration by
subquotients of these terms, all bounded by $w+n$.

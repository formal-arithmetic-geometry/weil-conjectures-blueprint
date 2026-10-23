+++
id = "def-nagata-relative-affine-space"
kind = "definition"
title = "Relative affine space"
order = 291
lean = ["AlgebraicGeometry.AffineSpace"]
+++
For a scheme $S$ and an index set $n$, define

$$
\mathbb A^n_S=S\times_{\operatorname{Spec}\mathbb Z}
\operatorname{Spec}\bigl(\mathbb Z[T_i : i\in n]\bigr),
$$

the fibre product of $S$ with the spectrum of the polynomial ring over
$\mathbb Z$ in the variables $T_i$, $i\in n$. Concretely, on an affine open
$V=\operatorname{Spec}(R)$ of $S$ this is
$\operatorname{Spec}(R[T_i : i\in n])$; for a principal restriction
$D(a)\subseteq V$ the transition map is induced by
$R[T_i : i\in n]\to R_a[T_i : i\in n]$. For $n\in\mathbb N$ one takes
the index set $\{1,\ldots,n\}$.

Equivalently, for $n\in\mathbb N$,
$\mathbb A^n_S=\underline{\operatorname{Spec}}_S
\bigl(\operatorname{Sym}_{\mathcal O_S}(\mathcal O_S^{\oplus n})\bigr)$.

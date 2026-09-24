+++
id = "lem-pc-projective-space-twist-cohomology"
kind = "lemma"
title = "Monomial cohomology of twists on projective space"
order = 2534
uses = ["def-pc-projective-space-twist", "lem-pc-affine-vanishing", "lem-pc-cech-computes", "lem-pc-twist-cocycle", "pqf-def-cohomology"]
+++
Let $A$ be a commutative ring, $n\ge1$, and $d\in\mathbf Z$.
For the twisting modules
on $P=\mathbf P^n_A$, one has

$$
H^q(P,\mathcal O_P(d))\cong
\begin{cases}
\displaystyle\bigoplus_{\substack{e_i\ge0\\\sum e_i=d}} A\,x^e,&q=0,\\
\displaystyle\bigoplus_{\substack{e_i<0\\\sum e_i=d}} A\,x^e,&q=n,\\
0,&q\notin\{0,n\}.
\end{cases}
$$

In particular all these modules are finite free, and the groups in
positive degree vanish for $d\ge0$.
For $n=0$, every twist is free of rank one on
$\mathbf P^0_A=\operatorname{Spec}(A)$ and has no higher cohomology.

## Proof

The transition rule of [def-pc-projective-space-twist], whose gluing
is well defined by [lem-pc-twist-cocycle], identifies
sections on $U_J=\bigcap_{j\in J}U_j$ with the degree-$d$ part of
$A[x_0,\ldots,x_n,x_j^{-1}:j\in J]$.
Every $U_J$ is affine. By [lem-pc-cech-computes], the alternating
Cech complex on the $n+1$ standard opens computes cohomology.
Its terms are free $A$-modules on Laurent monomials $x^e$, where
$\sum_i e_i=d$ and $e_i\ge0$ for $i\notin J$. The differential
preserves $e$, so the complex is the direct sum, over those exponent
vectors, of complexes $C_e^\bullet$.

Put $N_e=\{i:e_i<0\}$. The degree-$p$ basis of $C_e^\bullet$
consists of the subsets $J\supseteq N_e$ of size $p+1$.
If $N_e=\varnothing$, this is the cochain complex of a simplex;
augmentation by $A$ in degree $-1$ makes it contractible, by
inserting any fixed vertex. Thus its only cohomology is $A$ in
degree zero. If $\varnothing\ne N_e\ne\{0,\ldots,n\}$, choose
$r\notin N_e$. Insertion of $r$ gives a contracting homotopy:
for a component indexed by $J$ not containing $r$, take the
component indexed by $J\cup\{r\}$ with sign
$(-1)^{\#\{j\in J:j<r\}}$, and set it to zero when $r\in J$.
The terms removing vertices other than $r$ cancel in $dh+hd$;
the term removing $r$ is the identity. The condition
$J\supseteq N_e$ is preserved. No degree-$-1$ term is needed,
because $N_e$ is nonempty. Finally, if $N_e=\{0,\ldots,n\}$,
the complex has just one copy of $A$, in degree $n$.

Direct sums of complexes of modules commute with cohomology, so
these three cases give the displayed formula. There are only
finitely many nonnegative exponent vectors of prescribed sum,
and only finitely many strictly negative ones; the latter cannot
occur when $d\ge0$. For $n=0$ the single chart trivializes every
twist, and [lem-pc-affine-vanishing] proves its assertion.
The usual reference for this explicit calculation is
[Stacks, Section 30.8](https://stacks.math.columbia.edu/tag/01XS).

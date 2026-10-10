+++
kind  = "proof"
of    = "lem-pc-projective-coherent-higher-images"
+++
Work over an affine open $V=\operatorname{Spec}(A)\subset S$ and
put $X_V=f^{-1}(V)$. The fixed projective embedding restricts to
$X_V\hookrightarrow\mathbf P^n_A$. By
[lem-pc-projective-coherent-finiteness], the modules
$M^q=H^q(X_V,\mathcal F)$ are finite over $A$ and vanish for $q>n$.

Choose a finite affine cover of $X_V$. Since $X_V$ is separated
over the affine $V$, its finite intersections are affine. For any
$a\in A$, the cover restricted over $D(a)\subset V$ has Cech
complex equal to the localization of the original one, term by term.
Localization is exact; by [lem-pc-cech-computes],

$$
H^q(f^{-1}(D(a)),\mathcal F)=(M^q)_a.
$$

The sheaf $R^qf_*\mathcal F|_V$ is the sheaf associated to these
cohomology groups on opens. On the principal-open basis the last
formula is exactly the associated sheaf $\widetilde{M^q}$.
It is coherent by [pqf-lem-coherent-ft-locnoeth], since $M^q$
is finite and $A$ Noetherian. These affine conclusions prove the
statement on $S$, including the asserted vanishing.

+++
id = "lem-fin-coordinate-finite-boundary"
kind = "lemma"
title = "Coordinate complements give a finite exceptional locus"
order = 5226
lean = ["AlgebraicGeometry.exists_open_finite_coordinateComplement"]
+++
Let $S=\operatorname{Spec}A$ be integral Noetherian and let $Y\to S$ be
proper. Choose a finite affine cover $Y_\alpha$ with closed embeddings
$Y_\alpha\hookrightarrow\mathbf A^{m_\alpha}_S$, $m_\alpha\geq1$, and
coordinate functions $t_{\alpha r}$. For each coordinate choose a dense open
$V_{\alpha r}\subset\mathbf A^1_S$. After restriction to a nonempty open of
$S$, the reduced closed complement of
$$
G=\bigcup_{\alpha,r}t_{\alpha r}^{-1}(V_{\alpha r})\subset Y
$$
is finite over $S$, and in particular quasi-finite.

## Proof

Write $B_{\alpha r}$ for the reduced closed complement of $V_{\alpha r}$.
Its defining ideal in the domain $A[t]$ contains a nonzero polynomial
$P_{\alpha r}$. Invert the product of the finitely many nonzero leading
coefficients. After dividing by the leading coefficients these polynomials
are monic. Consequently each $B_{\alpha r}$ is a closed subscheme of
$\operatorname{Spec}A[t]/(P_{\alpha r})$, which is finite over $S$, with
basis given by powers below the polynomial degree. If the degree is zero
this scheme is empty, which is also finite.

Put $Z=Y\setminus G$, with reduced closed structure. On $Y_\alpha$, all
coordinate functions of $Z$ lie in their respective closed sets
$B_{\alpha r}$. Equivalently their defining ideals pull back to zero on the
reduced $Z\cap Y_\alpha$; an element vanishing at all primes of a reduced
ring is zero. Thus $Z\cap Y_\alpha$ is a closed subscheme of
$\prod_rB_{\alpha r}$, through the given closed affine embedding. The
product is finite over $S$, so every such piece has finite fibres. There are
finitely many $\alpha$, hence every fibre of $Z\to S$ has finitely many
points.

The closed immersion $Z\hookrightarrow Y$ is finite and proper. Its
composition with $Y\to S$ is proper. Apply the theorem that a proper
morphism with finite fibres is finite.

Unresolved dependencies: def:weil-pbc-scheme-conventions, pqf-def-quasifinite, thm:pqf-finite-iff-proper-finite-fibres, lem:weil-pbc-proper-composition, lem:weil-pbc-finite-proper

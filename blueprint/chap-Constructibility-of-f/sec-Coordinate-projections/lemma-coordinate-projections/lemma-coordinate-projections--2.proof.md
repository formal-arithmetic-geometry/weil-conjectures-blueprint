+++
kind = "proof"
of = "lemma-coordinate-projections--2"
order = 572005
uses = []
+++
Let $\eta$ be the generic point of $S$ and put $K=k(S)$. Each
$V_{\alpha r}$ meets $\mathbf A^1_K$: the projection
$\mathbf A^1_S\to S$ is open, so its image contains $\eta$.
Choose a nonzero polynomial $P_{\alpha r}\in K[t]$ whose principal
open lies in this intersection. A point of
$\mathbf A^{m_\alpha}_K$ with every coordinate outside the
corresponding $V_{\alpha r}$ lies in the spectrum of

$$
K[t_{\alpha1},\ldots,t_{\alpha m_\alpha}]/
(P_{\alpha1}(t_{\alpha1}),\ldots,
P_{\alpha m_\alpha}(t_{\alpha m_\alpha})).
$$

Every coordinate in this quotient is algebraic over $K$, hence integral.
The quotient is therefore a finite $K$-algebra, so it is Artinian and
has finitely many prime ideals. The closed immersions of the finitely
many charts show that $(Y\setminus G)\cap p^{-1}(\eta)$ is a finite
set.

Give $Y\setminus G$ its reduced closed subscheme structure, denoted by
$C$. The morphism $C\to S$ is proper and its fibre over $\eta$ has
finitely many points. By Zariski's Main Theorem, a proper morphism with
a finite fibre is finite over an open neighbourhood of that point.
We thus obtain an open neighbourhood $W$ of $\eta$ on which $C\to S$
is finite. This is the step
`AlgebraicGeometry.exists_isFinite_morphismRestrict_of_finite_preimage_singleton`.

For any closed immersion $i:Z\hookrightarrow Y$ supported in
$Y\setminus G$, each fibre of $Z\times_S W\to W$ injects on points
into the corresponding finite fibre of $C\times_S W\to W$.
It is therefore locally quasi-finite. It is also proper, and hence
finite. Since $W$ was chosen using $C$ alone, it works for every such
$Z$.

+++
id = "lem-sc-support-dimension-union"
kind = "lemma"
title = "A sheaf supported in low dimension is a filtered union"
order = 4907
lean = ["AlgebraicGeometry.Etale.isColimit_kernel_of_support_dim_le"]
+++
Let $B$ be a finite-type scheme over a field $K$. Suppose a torsion étale
sheaf $N$ has zero geometric stalk at every point $y$ with
$\operatorname{trdeg}_K\kappa(y)>a$, where $a\geq0$. For each closed
$Z\subset B$ of dimension at most $a$, let $j_Z:B\setminus Z\to B$ and set
$N_Z=\ker(N\to j_{Z*}j_Z^*N)$. Then the canonical map
$\varinjlim_ZN_Z\to N$ is an isomorphism.

## Proof

Finite unions make these closed subsets a directed system. Take a section $s$
of $N$ on a finite-type étale $V\to B$. The set of points where its geometric
germ is zero is open: zero in a stalk means zero on an étale neighborhood,
whose image is open, and the sheaf axiom gives vanishing on that image. Its
complement $S$ is consequently closed in $V$.

At each generic point of a component of $S$, the germ of $s$ is nonzero, so
the hypothesis and étaleness give $\operatorname{trdeg}_K\kappa(v)\leq a$. The
dimension formula for finite-type domains gives $\dim S\leq a$. The closure
$Z$ of the image of $S$ has dimension at most $a$: on each irreducible
component its generic residue field embeds in that of the corresponding
component of $S$.

The restriction of $s$ to $V\times_B(B\setminus Z)$ is zero. Thus
$s\in N_Z(V)$. These objects form a basis of the étale site, so every section
is locally in the proposed union. Each $N_Z\to N$ is injective; exactness of
geometric stalks finishes the verification.

Unresolved dependencies: def:weil-pbc-scheme-conventions, def:weil-pbc-etale-sheaves, prop:weil-pbc-geometric-stalks-exact

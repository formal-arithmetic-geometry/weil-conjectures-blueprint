+++
kind  = "proof"
of    = "lem-sc-support-dimension-union"
+++
Finite unions make these closed subsets a directed system.
Take a section $s$ of $N$ on a finite-type etale $V\to B$.
The set of points where its geometric germ is zero is open:
zero in a stalk means zero on an etale neighborhood, whose
image is open, and the sheaf axiom gives vanishing on that image.
Its complement $S$ is consequently closed in $V$.
At each generic point of a component of $S$, the germ of $s$
is nonzero, so the hypothesis and etaleness give
$\operatorname{trdeg}_K\kappa(v)\leq a$.
The dimension formula for finite-type domains gives
$\dim S\leq a$.
The closure $Z$ of the image of $S$ has dimension at most
$a$: on each irreducible component its generic residue field
embeds in that of the corresponding component of $S$.
The restriction of $s$ to $V\times_B(B\setminus Z)$ is zero.
Thus $s\in N_Z(V)$. These objects form a basis of the
etale site, so every section is locally in the proposed union.
Each $N_Z\to N$ is injective; exact geometric stalks in
[prop-weil-pbc-geometric-stalks-exact] finish the verification.

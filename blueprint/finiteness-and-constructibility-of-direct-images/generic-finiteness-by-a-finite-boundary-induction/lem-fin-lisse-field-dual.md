+++
id = "lem-fin-lisse-field-dual"
kind = "lemma"
title = "Duals of complexes with finite locally constant cohomology"
order = 5804
lean = ["AlgebraicGeometry.Etale.IsLisse.dual_isLisse"]
+++
Let $\lambda=\mathbf F_\ell$, let $T$ be a scheme on which $\ell$ is
invertible, and let $C$ be an ordinary bounded derived complex of étale
$\lambda$-sheaves. Suppose all $\mathcal H^q(C)$ are finite locally
constant. Its derived internal dual
$C^\vee=R\mathcal Hom_\lambda(C,\lambda_T)$ has finite locally constant
cohomology, with
$$
\mathcal H^q(C^\vee)=\mathcal Hom_\lambda(\mathcal H^{-q}(C),\lambda_T).
$$
For every scheme morphism $v:T'\to T$, the canonical morphism
$v^*C^\vee\to(v^*C)^\vee$ is an isomorphism.

## Proof

A finite locally constant $\lambda$-sheaf $E$ is, étale-locally,
$\lambda^r$ for a finite $r$. On such a neighborhood the internal Hom
functor $\mathcal Hom(E,-)$ is the finite product of $r$ copies of the
identity. It is exact. Consequently $\mathcal Ext^a(E,\lambda)=0$ for
$a>0$, and $\mathcal Hom(E,\lambda)$ is finite locally constant.

Apply the finite truncation filtration of $C$ and its spectral sequence. All
internal Ext rows except row zero vanish by this calculation, giving the
formula in the statement and boundedness.

For a sheaf $E$ the pullback comparison is the identity between the two
duals of $\lambda^r$ on each trivializing étale neighborhood. It is
therefore an isomorphism by conservativity of geometric stalks. Apply the
exact pullback functor to the finite truncation triangles of $C$; induction
through these triangles proves the comparison for $C$. No assertion about
global Ext vanishing is used.

Unresolved dependencies: def:weil-pbc-derived-categories, def:weil-pbc-constructible-complexes, def:weil-derived-pullback-tensor-hom, thm:sp-truncation-e2, lem:weil-pbc-geometric-stalk-conservative

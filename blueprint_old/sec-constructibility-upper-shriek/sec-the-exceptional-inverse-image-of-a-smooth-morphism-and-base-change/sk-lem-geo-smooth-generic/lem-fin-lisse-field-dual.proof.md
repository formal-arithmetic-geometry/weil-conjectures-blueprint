+++
kind  = "proof"
of    = "lem-fin-lisse-field-dual"
+++
A finite locally constant $\lambda$-sheaf $E$ is, etale
locally, $\lambda^r$ for a finite $r$. On such a neighborhood
the internal Hom functor $\mathcal Hom(E,-)$ is the finite product
of $r$ copies of the identity. It is exact. Consequently
$\mathcal Ext^{a}(E,\lambda)=0$ for $a>0$, and
$\mathcal Hom(E,\lambda)$ is finite locally constant.
These computations use internal Hom as defined in
[def-weil-derived-pullback-tensor-hom].
Apply the finite truncation filtration of $C$ and its spectral
sequence from [thm-sp-truncation-e2]. All internal Ext rows
except row zero vanish by this calculation, giving the formula
in the statement and boundedness. For a sheaf $E$ the pullback
comparison is the identity between the two duals of $\lambda^r$
on each trivializing etale neighborhood. It is therefore an
isomorphism by [lemma-weil-pbc-geometric-stalk-conservative].
Apply the exact pullback functor to the finite truncation triangles
of $C$; induction through these triangles proves the comparison
for $C$. No assertion about global Ext vanishing is used.

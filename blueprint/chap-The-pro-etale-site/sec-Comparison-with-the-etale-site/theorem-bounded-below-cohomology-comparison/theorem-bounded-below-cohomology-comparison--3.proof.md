+++
kind = "proof"
of = "theorem-bounded-below-cohomology-comparison--3"
order = 123006
uses = ["proposition-comparison-morphism-inverse-image", "theorem-bounded-below-cohomology-comparison--1"]
+++
Both sites have $X$ as terminal object, and $\nu_{X,*}$ is restriction.
Evaluation at $X$ therefore gives the natural identification

$$
\Gamma(X_{\acute{e}t},\nu_{X,*}F)
\simeq\Gamma(X_{\mathrm{pro}\acute{e}t},F).
$$

Since $\nu_{X,*}$ is right adjoint to the exact functor $\nu_X^*$, it
preserves K-injective complexes: by adjunction, maps from an acyclic
complex into $\nu_{X,*}I^\bullet$ correspond to maps from its acyclic
inverse image into $I^\bullet$, and their null-homotopies correspond as
well. A K-injective resolution thus computes both the derived composite
and the composite of the derived functors. Deriving the displayed
identification gives the natural isomorphism for $L$.

For the last assertion, set $\mathcal A=\operatorname{Mod}(\Lambda)$ and
$L=\nu_X^*K$. Apply $R\Gamma(X_{\acute{e}t},-)$ to the inverse of the unit
isomorphism in [theorem-bounded-below-cohomology-comparison--1] and compose
with the inverse of the first displayed isomorphism.

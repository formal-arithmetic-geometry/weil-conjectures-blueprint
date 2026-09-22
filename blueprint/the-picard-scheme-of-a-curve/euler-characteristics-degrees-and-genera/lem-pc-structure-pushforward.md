+++
id = "lem-pc-structure-pushforward"
kind = "lemma"
title = "The pushforward of the structure sheaf"
order = 4306
lean = ["AlgebraicGeometry.pushforward_structureSheaf_baseChange"]
uses = ["def-pc-base-change", "def-pc-morphism-conventions", "lem-pc-coherent-hi", "def-pc-picard-presheaf"]
+++
Let $k$ be a field, $X$ a smooth projective curve
[def-pc-smooth-projective-curve] over $k$ with $H^0(X,\mathcal{O}_X)=k$ and
$T$ a scheme over $k$. Then $f_{T,*}\mathcal{O}_{X_T}\cong\mathcal{O}_T$,
where $f_T:X_T\to T$ is the structure morphism of the base change.

## Proof

Since $X$ is proper over $k$, $f_T$ is proper, hence quasi-compact and
quasi-separated, so $f_{T,*}\mathcal{O}_{X_T}$ is quasi-coherent
[lem-pc-coherent-hi] (1). To identify it with $\mathcal{O}_T$ it suffices
to show that its sections over every affine open
$V=\operatorname{Spec}(A)\subseteq T$ equal $A$ compatibly with
localization: by the flat base change for coherent cohomology of the
divisors chapter, applied to $X$ proper over $k$, the flat $k$-algebra $A$
and $\mathcal{F}=\mathcal{O}_X$,
$$
\Gamma(X_V,\mathcal{O}_{X_V})=H^0(X_V,\mathcal{O}_{X_V})\cong H^0(X,\mathcal{O}_X)\otimes_kA
=k\otimes_kA=A ,
$$
and these identifications are compatible with the localization maps of the
structure sheaf of $T$ (the corresponding identification holds for every
localizing $A\to A_f$). Hence $f_{T,*}\mathcal{O}_{X_T}=\mathcal{O}_T$.

Unresolved dependencies: lem:sc-flat-base-change-coherent

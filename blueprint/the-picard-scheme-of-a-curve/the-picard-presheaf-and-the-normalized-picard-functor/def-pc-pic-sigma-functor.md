+++
id = "def-pc-pic-sigma-functor"
kind = "definition"
title = "The normalized functor Pic_{X/k,sigma}"
order = 4237
lean = ["AlgebraicGeometry.picardFunctorRigidified"]
uses = ["def-pc-picard-presheaf", "def-pc-rational-point", "def-pc-subfunctor", "lem-pc-sigma-k-points"]
+++
Let $k$ be a field, $X$ a scheme over $k$, and $\sigma\in X(k)$ a
$k$-rational point [def-pc-rational-point]. For a scheme $T$ over $k$ put
$$
\operatorname{Pic}_{X/k,\sigma}(T):=\operatorname{Ker}\Bigl(\sigma_T^*:\operatorname{Pic}(X_T)
\longrightarrow\operatorname{Pic}(T)\Bigr),
$$
i.e. the set of isomorphism classes $[\mathcal L]$ for which
$\sigma_T^*\mathcal L$ is isomorphic to $\mathcal O_T$. A trivialization is
not part of an element of this kernel; when a proof chooses one, that
choice is auxiliary. Its value at $T=\operatorname{Spec}(k)$ is computed in
[lem-pc-sigma-k-points].

Unresolved dependencies: def:sc-picard-group

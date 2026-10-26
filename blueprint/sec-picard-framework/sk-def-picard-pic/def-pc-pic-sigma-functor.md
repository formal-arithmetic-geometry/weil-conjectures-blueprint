+++
id = "def-pc-pic-sigma-functor"
kind = "definition"
title = "The normalized functor $\\operatorname{Pic}_{X/k,\\sigma}$"
order = 578
uses = ["def-pc-picard-presheaf", "def-pc-rational-point", "def-pc-subfunctor", "def-sc-picard-group"]
lean = ["AlgebraicGeometry.picardFunctorNormalized"]
+++
Let $f:X\to S$ be a morphism of schemes and $\sigma:S\to X$ a section of
$f$. For a scheme $T$ over $S$, with $\sigma_T:T\to X_T$ the base change
of $\sigma$, put

$$
\operatorname{Pic}_{X/S,\sigma}(T):=\operatorname{Ker}\Bigl(\sigma_T^*:\operatorname{Pic}(X_T)
\longrightarrow\operatorname{Pic}(T)\Bigr),
$$

i.e. the set of isomorphism classes $[\mathcal L]$ for which
$\sigma_T^*\mathcal L$ is isomorphic to $\mathcal O_T$. This is a
subfunctor of the Picard presheaf $T\mapsto\operatorname{Pic}(X_T)$. When
$S=\operatorname{Spec}(k)$ for a field $k$, so that $\sigma\in X(k)$ is a
$k$-rational point, we write $\operatorname{Pic}_{X/k,\sigma}$.

A trivialization of $\sigma_T^*\mathcal L$ is not part of an element of
this kernel; when a proof chooses one, that choice is auxiliary.

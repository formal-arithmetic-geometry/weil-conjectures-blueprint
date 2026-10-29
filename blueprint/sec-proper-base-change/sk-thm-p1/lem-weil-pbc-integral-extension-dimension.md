+++
id = "lem-weil-pbc-integral-extension-dimension"
kind = "lemma"
title = "An integral ring map does not raise Krull dimension"
lean = ["RingHom.IsIntegral.ringKrullDim_le_and_isMaximal_comap"]
order = 1939
+++
Let $f:A\to B$ be a ring map of commutative rings such that $B$ is integral over $A$ (every element of $B$ is a root of a monic polynomial with coefficients in $f(A)$). Then $\dim B\le\dim A$ (Krull dimensions: suprema of lengths of chains of prime ideals), and for every maximal ideal $\mathfrak n$ of $B$ the ideal $f^{-1}(\mathfrak n)$ is a maximal ideal of $A$.

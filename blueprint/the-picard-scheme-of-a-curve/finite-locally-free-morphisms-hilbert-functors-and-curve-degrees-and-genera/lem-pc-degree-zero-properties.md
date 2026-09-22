+++
id = "lem-pc-degree-zero-properties"
kind = "lemma"
title = "Cohomology of a module in degree zero"
order = 4279
lean = ["AlgebraicGeometry.cohomology_of_shift_eq"]
uses = ["def-pc-derived-category", "def-pc-finite-locally-free", "lem-pc-flf-properties"]
+++
Let $X$ be a scheme, $M\in D(\mathcal{O}_X)$ and let $\mathcal{N}$ be an
invertible $\mathcal{O}_X$-module with $M\cong\mathcal{N}[0]$. Then
$H^i(M)=0$ for $i\neq0$ and $H^0(M)\cong\mathcal{N}$. If $M\cong E[-i]$ with
$E$ locally free of rank $r$ (cf. [def-pc-finite-locally-free] and
[lem-pc-flf-properties]), then $H^j(M)=0$ for $j\neq i$ and
$H^i(M)\cong E$.

## Proof

By definition of the shift, $H^j(\mathcal{N}[0])$ is the $j$-th cohomology
of the complex with $\mathcal{N}$ in degree $0$, i.e. $0$ for $j\neq0$ and
$H^0$ is $\mathcal{N}$; cohomology is invariant under quasi-isomorphism,
and $M\cong\mathcal{N}[0]$ is an isomorphism in $D(\mathcal{O}_X)$, which
means that the two complexes are connected by a zig-zag of
quasi-isomorphisms (each of which induces an isomorphism of all cohomology
sheaves). The second assertion is the same argument applied to the complex
$E$ in degree $-i$.

*Import note.* The source writes "$j\,$e$0$", a place where a backslash was
lost in the conversion; it is restored above as $j\neq0$.

Unresolved dependencies: def:sc-invertible-module

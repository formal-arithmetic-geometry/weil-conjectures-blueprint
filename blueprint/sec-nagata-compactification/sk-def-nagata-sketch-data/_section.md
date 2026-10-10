+++
id = "sk-def-nagata-sketch-data"
kind = "section"
title = "Compactification and admissible blow-up"
order = 3
lean = ["AlgebraicGeometry.Compactification", "AlgebraicGeometry.IsSchemeTheoreticallyDominant", "AlgebraicGeometry.IsAdmissible"]
+++
*Definition (sketch).*

A *compactification* of $f:X\to S$ is a factorization

$$
X\xrightarrow{j}\overline X\xrightarrow{p}S,
\qquad p\circ j=f,
$$

where $j$ is an open immersion and $p$ is proper.
It is *scheme-theoretically dense* if $j$ is scheme-theoretically
dominant: no nonzero quasi-coherent ideal of $\mathcal O_{\overline X}$ is
contained in the kernel of $\mathcal O_{\overline X}\to j_*\mathcal O_X$.
For an open $U\subseteq T$ of a scheme $T$, a
*$U$-admissible blow-up* is
$\Bl_{\mathcal I}(T)\to T$, with $\mathcal I$ a finite-type
quasi-coherent ideal whose support $V(\mathcal I)$ is disjoint from $U$,
i.e. $\mathcal I|_U=\mathcal O_U$.

A $U$-admissible blow-up is an isomorphism over $U$.

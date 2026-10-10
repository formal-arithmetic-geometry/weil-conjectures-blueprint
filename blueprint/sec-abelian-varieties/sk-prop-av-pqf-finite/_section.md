+++
id = "sk-prop-av-pqf-finite"
kind = "section"
title = "Proper and quasi-finite implies finite"
lean = ["AlgebraicGeometry.IsFinite.of_isProper_of_locallyQuasiFinite"]
order = 495
uses = ["sk-def-av"]
+++
*Proposition (sketch).*

A morphism of schemes which is proper and locally quasi-finite (for a
proper morphism, equivalently: quasi-finite) is finite.

## Proof

*Reference: Stacks Project, Cohomology of Schemes, Lemma 30.21.1, `02OG`, in
the locally Noetherian case; in general a consequence of Zariski's main
theorem.* Let $f:X\to S$ be proper and locally quasi-finite; finiteness is
local on $S$, so let $S$ be affine. By Zariski's main theorem $f$ factors as
a quasi-compact open immersion $j:X\hookrightarrow T$ followed by a finite
morphism $T\to S$. Since $X\to S$ is proper and $T\to S$ is separated, $j$
is proper, hence has closed image; an open immersion with closed image is a
closed immersion. So $f$ is a closed immersion followed by a finite
morphism, hence finite.

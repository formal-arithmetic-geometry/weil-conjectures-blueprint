+++
id = "definition-tate-twists--9"
kind = "lemma"
title = "Scalar-description of the algebraic twist"
order = 184010
aliases = ["bp-r053-9"]
lean = ["AlgebraicGeometry.ProEtale.tateTwistOne"]
uses = ["definition-tate-twists--8", "lemma-comparison-completed-coefficients"]
+++
The comparison with the colimit in [definition-tate-twists--7] is bypassed by the Lean route. It defines the algebraic-closure twist directly by extension of scalars:
$$
\QbarX(1)=\QbarX\otimes_{\mathbf Z_{\ell,X}}\mathbf Z_{\ell,X}(1),
$$
where $\mathbf Z_{\ell,X}(1)$ is the Tate module of [definition-tate-twists--8].

+++
id = "lem-amb-linear-trace-invariance"
kind = "lemma"
title = "Linear changes of coordinates preserve integration"
order = 5630
lean = ["AlgebraicGeometry.Etale.affineSpace.trace_linear_invariant"]
uses = ["def-coefficient-twists", "lem-amb-affine-space-top-trace", "def-amb-etale-compact-support"]
+++
For every $g\in\operatorname{GL}_d(\mathcal O_S(S))$, the linear
automorphism of $\mathbf A^d_S$ induced by $g$ preserves the affine-space
trace $t_{p_d}:Rp_{d!}A(d)[2d]\to A_S$.

## Proof

Let $G=\operatorname{GL}_{d,S}$, the open subscheme $\det\ne0$ of the affine
scheme of $d$-by-$d$ matrices. Over $G$, the universal invertible matrix
defines an automorphism $a$ of $\mathbf A^d_G$. Functoriality of compact
supports gives an automorphism of $Rp_{d!}A(d)[2d]$ over $G$. By
[lem-amb-affine-space-top-trace], this is an automorphism of the sheaf $A_G$
in degree zero. It is therefore multiplication by a locally constant section
$b$ of the finite constant sheaf $A$. This uses ordinary sheaf
endomorphisms, not cohomology with support on a zero section.

Every geometric fibre of $G\to S$ is connected: its coordinate ring is a
polynomial ring over an algebraically closed field with the determinant
inverted, hence an integral domain. The locally constant section $b$ is
constant on such a fibre. At its identity matrix $a$ is the identity
automorphism, so $b=1$ there and therefore on the whole fibre. Every
geometric point of $G$ belongs to one of these fibres; conservativity of
stalks gives $b=1$ globally.

Finally the given matrix $g$ is a section $S\to G$. Pulling back this
equality and using the base-change compatibility in
[lem-amb-affine-space-top-trace] proves the assertion.

Unresolved dependencies: def:sbc-affine-space, def:weil-pbc-derived-categories, lem:weil-pbc-geometric-stalk-conservative

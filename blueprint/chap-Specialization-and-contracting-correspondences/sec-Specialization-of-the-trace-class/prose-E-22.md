+++
id = "prose-E-22"
kind = "hidden"
title = "Specialization of the trace class (1)"
order = 1688
+++
In a continuous family of maps of a compact manifold, the Lefschetz
number does not change. The algebraic counterpart is the following
proposition: the [trace class](@definition-trace-class-local-terms) of the specialized [correspondence](@definition-correspondence) $u_s$ is the
specialization $\operatorname{sp}_F$ of the [trace class](@definition-trace-class-local-terms) of $u$. Here
$\operatorname{sp}_F$ is a map of sections of [dualizing complexes](@definition-verdier-dual-evaluation) on the
[fixed scheme](@definition-correspondence). A [trace class](@definition-trace-class-local-terms) is
built from three pieces: the [cohomological correspondence](@definition-correspondence) $u$, the
external product $K\boxtimes\mathbb DK$ in which $u$ becomes a section,
and the evaluation map along the diagonal to the [dualizing complex](@definition-verdier-dual-evaluation).
Nearby cycles commute with each piece. They commute with external products
by Proposition [proposition-external-kunneth-formula-nearby-cycles], with [Verdier duality](@definition-verdier-dual-evaluation)
by Proposition [proposition-nearby-cycles-commute-verdier-duality], and with the four
operations through the base change maps of Section [sec-Base-change-for-nearby-cycles].
We prove the proposition by putting these compatibilities together.
Theorem [theorem-contracting-correspondences-local-terms] uses it to
transfer the computation to the normal cone. For this it also needs
Corollary [corollary-specialization-when-fixed-point-scheme]:
$\operatorname{sp}_F$ is the identity when the [fixed scheme](@definition-correspondence) is, up to
nilpotents, a constant family $Y\times S$.

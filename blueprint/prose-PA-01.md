+++
id = "prose-PA-01"
kind = "hidden"
title = "Appendices"
order = 805
+++
Most of what follows is classical algebraic geometry that the
main text uses as a tool: compactifications of morphisms, abelian
varieties and Jacobians, the cohomology of curves with torsion
coefficients, and the structure of algebraic groups in characteristic
zero. A reader who knows these results can skip the proofs; we include
them because the main theorems rest on them. One appendix is of a different kind: it gives a
second computation of the local terms in the trace formula, which the
main text does not use.

*Compactifications.* In Part “The six operations” the direct image
with proper support is defined as $Rf_!=Rp_*j_!$ for a compactification
$f=p\circ j$ (Proposition [sk-prop-sf-comp-coherence]), so we
need that every separated morphism of finite type has one; that two
compactifications are dominated by a third is then elementary
(Proposition [sk-prop-nagata-sketch-comp-category]). Proper base change is reduced
to projective space by Chow's lemma (Section [sec-pbc-reduction]).
Appendix [sec-nagata-compactification] proves Nagata's theorem and Chow's
lemma. Both are statements about schemes, without any cohomology, and
their proofs, by blow-ups and closures of graphs, have nothing in common
with the rest of the notes. Nagata's theorem, followed by normalization,
also provides the smooth compactification of a curve used in
Part “Weights and the Riemann hypothesis” (Lemma [sk-i-real-compactification]).

*Curves and their Jacobians.* Appendices [sec-abelian-varieties],
[sec-picard-framework] and [sec-curve-estimates] serve two theorems at opposite ends
of the notes. Proper base change (Section [sec-proper-base-change])
reduces to the cohomology of curves over an algebraically closed field:
vanishing above degree two, finiteness, and invariance under extension
of the base field (Theorem [sk-thm-curve-package]). In
Part “Weights and the Riemann hypothesis”, the geometric monodromy of a lisse sheaf of
rank one on a curve is finite (Theorem [sk-p-real-rankone]) because
Frobenius has no fixed vector in $H^1$ of the curve
(Proposition [sk-prop-wrp-h1-no-fixed]). Both rest on the Kummer sequence,
which identifies $H^1(C,\mu_n)$ with $\operatorname{Pic}(C)[n]$ for $n$
invertible on the curve, and on
Weil's theorem that $\operatorname{Pic}^0(C)$ is the group of points of
an abelian variety of dimension $g$, the Jacobian, whose $n$-torsion is
$(\mathbf Z/n)^{2g}$. Appendix [sec-abelian-varieties] proves what we need
about abelian varieties, Appendix [sec-picard-framework] constructs the
Jacobian, and Appendix [sec-curve-estimates] combines the two, with the
Artin–Schreier sequence for torsion divisible by the characteristic,
into a proof of Theorem [sk-thm-curve-package]; see
also [geobp].

*Contracting correspondences.* The main text computes the local
term of Frobenius at a fixed point by a calculation on a smooth curve
(Proposition [sk-p-frob]), and reduces the trace
formula to that case. Appendix [sec-specialization-contracting] computes
the local terms of every contracting correspondence at once, by
deforming the correspondence to a normal cone, following
Varshavsky [varshavsky05], whose theorem generalizes one of Fujiwara.
This route needs nearby cycles, which the
main text never uses, and Section [sec-trace-formula] does not depend
on it.

*Algebraic groups.* The determinant weights of tensor and exterior
powers (Proposition [sk-prop-walg-determinant-weights]), which feed Rankin's
argument in Section [sec-purity-real-sheaves], are read off from a central
element of the arithmetic monodromy group. Its existence comes from the
identity $G^\circ=Z(G^\circ)^\circ H^\circ$ of
Lemma [sk-p-product], a statement about algebraic groups
over $\overline{\mathbf Q}_\ell$ that is proved through their Lie algebras.
Appendix [sec-algebraic-groups-lie-algebras] proves the facts of Lie theory that this
uses, in the form in which we use them.

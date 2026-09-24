+++
id = "sec-sf-continuity-what-is-recorded"
kind = "section"
title = "Continuity of the pro-étale cohomology for arbitrary sheaves: what is recorded"
order = 3485
uses = ["def-weil-pbc-etale-sheaves", "def-weil-pbc-etale-site", "def-weil-pbc-etale-sum-extension", "def-weil-pbc-geometric-stalks", "def-weil-pbc-pointed-etale-neighbourhoods", "def-weil-pbc-proetale-modules", "def-weil-pbc-proetale-site", "def-weil-pbc-scheme-conventions", "def-weil-pbc-strict-henselization-limit", "lem-cbc-proetale-stalk-conservative", "lem-weil-pbc-etale-restriction-injectives"]
+++
The items below settle what the passage from the étale site to the
pro-étale site costs. They are the reason why $\operatorname{FullCD}$ is
read on the blueprint's coefficient class [def-sf-fullcd-used-class] —
where its vanishing half is the theorem [thm-sf-fullcd-used-class], with
the sharp comparison bound $M=0$ of [prop-sf-comparison-bound-zero] —
and why the general form, quantified over all sheaves and uniformly over the
base changes, is not a hypothesis but *false*, by
[prop-sf-fullcd-general-form-false] and
[rem-sf-fullcd-counterexample]. The first is the exactness of
the geometric-point stalk functor, applied to the strictly henselian limit
object; the second is the local lifting of sections of an associated sheaf; the
third turns the continuity of the values of the cohomology presheaf along the
pointed étale neighbourhoods into the vanishing of the higher direct images,
with the sharpest possible bound; the fourth draws the consequence for
$\operatorname{FullCD}(p,A;2d)$; and the fifth records exactly what the
recorded proof of the comparison theorem uses and what of it is unavailable
for an arbitrary sheaf. They are collected in this final section so that no
statement, proof or number of the preceding sections is moved.

The four items that follow answer, as far as the recorded tools allow, the
question that the preceding remark leaves open for the sheaves of étale
origin and closes negatively in general. The first is elementary
cohomological algebra on the étale site and is used by the second, which
proves $(\mathrm{C}_q)$ of
[thm-sf-continuity-arbitrary-sheaves-vanishing] for every sheaf of étale
origin; the third proves the pro-étale form of the same statement for
*every* sheaf of $A$-modules, namely that the acyclicity of the strict
henselization limit kills every class on that one pro-étale refinement; and
the fourth exhibits a pointed pro-étale neighbourhood which receives no
morphism from any pointed étale neighbourhood, which is exactly why the
third does not descend to the étale system and why the remaining case of
$(\mathrm{C}_q)$ is the sheaves that are not of étale origin.

The five items that follow close the angle that
[rem-sf-fullcd-general-form] and [rem-sf-continuity-obstruction]
recorded, in the form in which they stated it: whether a bound on the
*length*
of a weakly contractible hypercovering is what the vanishing of
$R^q\nu_{V,*}$ waits for. The first shows that no hypercovering of a nonempty
object has an empty term, so that no hypercovering of a nonempty object is
bounded at all; the second draws the consequence, namely that the criterion
``bounded hypercovering implies vanishing for every sheaf'' has no instance, and
that the question of a length bound is answered negatively for every nonempty
member of the class, independently of the dimension; the third records the
criterion that *does* bound the vanishing degree, and it is a statement
about the coefficient sheaf on the terms of the hypercovering rather than about
the length of the hypercovering; the fourth is the statement that the truncation
of the Čech complex of a single weakly contractible covering needs the
conclusion as input; and the fifth names, for that situation, the missing input
and the structures that do not supply it.

The outcome of the five items is therefore the following. The class of
[cor-sf-no-bounded-hypercover] is not the class of objects whose vanishing
degree is bounded by the dimension, since no member of it has a bounded
weakly contractible hypercovering at all, the same object $\operatorname{Spec}\bar k$ of dimension $0$ having both no bounded hypercovering and vanishing
$H^q=0$ for every $q>0$ and every sheaf of $A$-modules, by
[lem-sf-stalk-limit-acyclic](iii). The hypercover-length route is
therefore closed rather than merely unfinished, and the two statements that do
hold unconditionally on that route are the criterion
[lem-sf-acyclic-hypercover-terms-vanishing] and the negative answer
[cor-sf-no-bounded-hypercover]. The general form of $(\mathrm{G})$ is
*not* left open by them: it is *false*, by
[prop-sf-fullcd-general-form-false], whose counterexample
[rem-sf-fullcd-counterexample] is recorded in the final section
[sec-sf-fullcd-refutation] of this chapter. The condition
$\operatorname{FullCD}(p,A;c_{\mathrm{cd}})$ of
[open-sf-ambient-adjoint-input] is used only on the coefficient class
[def-sf-fullcd-used-class], where the vanishing is the class-restricted
datum [def-sf-fullcd-class] supplied by [thm-sf-fullcd-class] and
the existence of the right adjoint is the theorem
[thm-sf-ambient-adjoint-class], the sharp comparison bound being
$M=0$ by [prop-sf-comparison-bound-zero].

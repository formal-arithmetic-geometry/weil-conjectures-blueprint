+++
id = "finite-etale-covers-the-fibre-functor-and-the-fundamental-group"
kind = "section"
title = "Finite etale covers, the fibre functor, and the fundamental group"
order = 1926
uses = ["def-weil-pbc-constructible-complexes", "def-weil-pbc-etale-cohomology", "def-weil-pbc-etale-sheaves", "def-weil-pbc-finite-torsors", "def-weil-pbc-scheme-conventions"]
+++
Chapter 7 of `weil_conjectures_detailed.tex`: the Galois-theoretic dictionary
for finite etale covers, following SGA 1, Expose V and Stacks Project Chapter
58, with every proof written out.

- [the-two-categories-and-the-fibre-functor] and [two-identifications-proved]
set up finite etale covers and finite locally constant sheaves, and prove the
two identifications the rest of the blueprint leans on: finite locally
constant sheaves are finite etale schemes [thm-galois-lc-etale], and torsors
compute $H^1$ [thm-galois-torsor-h1].
- [abstract-galois-categories] develops Galois categories in the abstract:
Galois objects exist, $\operatorname{Aut}(F)$ is profinite and acts
transitively on fibres, and the abstract equivalence theorem.
- [finite-etale-covers-form-a-galois-category] and [the-fundamental-theorem]
show that finite etale covers of a connected scheme form a Galois category,
so the fibre functor is an equivalence with finite continuous $\pi_1$-sets.
- [the-forms-used-downstream] states the four corollaries later chapters cite:
Galois covers are cofinal, open subgroups are finite etale covers, the abelian
torsor–character–$H^1$ dictionary, and lisse sheaves as continuous
representations.

Two labels of the source name statements of this chapter under their
proper-base-change names: `lem:weil-pbc-finite-locally-constant-etale` is
[thm-galois-lc-etale] and `prop:weil-pbc-torsors-h1` is
[thm-galois-torsor-h1]. The two statements of [chap-proper-base-change] that
cite the first now do so by a `uses` edge.

The only facts used without proof are elementary and named where used:
Nakayama's lemma and finite etale algebras over a separably closed field
([lem-fet-locally-trivial]), glueing along open immersions
([lem-galois-glue]), and the limit arguments spreading finitely presented data
over an etale neighbourhood.

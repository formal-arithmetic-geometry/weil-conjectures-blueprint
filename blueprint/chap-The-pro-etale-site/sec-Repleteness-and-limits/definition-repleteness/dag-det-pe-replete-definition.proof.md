+++
kind = "proof"
of = "dag-det-pe-replete-definition"
tags = ["sheaf-dag"]
+++
1. An inverse sequence is represented by a functor $F:\mathbf N^{\mathrm{op}}\to\Sh(\mathcal C)$. For each $n$, its adjacent transition is the morphism $F(\operatorname{homOfLE}(n\le n+1)^{\mathrm{op}}):F_{n+1}\to F_n$; the functor laws supply the identity maps and the finite composites between any two stages. Thus the tower and its transition maps are exactly the data quantified over in the Lean definition of `IsReplete`.
2. For such a diagram, `lem-weil-pbc-site-sheaf-sets-limits-sectionwise` identifies its limit in $\Sh(\mathcal C)$ with the sectionwise limit. Concretely, at an object $V$ the limit consists of tuples $(x_n)_{n\ge0}$ with $t_n(x_{n+1})=x_n$, and the map `limit.π F (op m)` is the coordinate projection $(x_n)\mapsto x_m$. This is the instance of Mathlib's `CategoryTheory.Sheaf.createsLimitsOfShape` used by the Lean declaration, and it also gives the universal property of these projections.
3. By `lem-weil-pbc-site-sheaf-sets-epi-locally-surjective`, categorical epimorphism for a morphism of sheaves of sets is equivalent to the stated covering-and-local-lifts condition; this is Mathlib's `CategoryTheory.Sheaf.isLocallySurjective_iff_epi`. Therefore requiring `Epi` for every adjacent transition and `Epi (limit.π F (op m))` for every $m$ is precisely the assertion that every tower of epimorphisms has epimorphic limit projections, i.e. the repleteness clause in the statement.

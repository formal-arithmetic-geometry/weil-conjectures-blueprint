+++
id = "rem-trf-classical-framework"
kind = "definition"
title = "Classical framework convention: no $\\infty$-categories"
order = 2616
uses = ["def-exchange-projection", "def-trf-categorical-trace", "def-weil-finite-coefficient-point", "def-weil-pbc-proetale-site", "prop-functor-package", "sk-def-sf-setting", "sk-def-sfb-bounded-constructible", "sk-prop-scalar-six", "sk-lem-integral-models", "sk-thm-sfb-qlbar-two-colimit"]
+++
Throughout this chapter, and in every statement below, the framework is
the *classical* one of the framework chapter: ordinary categories, ordinary
triangulated categories in the sense of Verdier, sets of morphisms,
exact functors, natural transformations, and 2-categorical (bicategorical)
arguments only. No $\infty$-category, no $\infty$-operad, no
model-independent "coherent" higher machinery is used or assumed. The
following conventions fix what this means for every phrase that could be
read either way.

1. *The derived categories.* $D^b_c(X,A)$, $D^b_{ctf}(X,A)$,
$D^b_{\mathrm{fin}}(A)$, and their integral, rational, and
algebraically closed analogues are the classical Verdier derived
categories of the small
pro-etale site (or of the point), localized at quasi-isomorphisms: for a
coefficient ring $\Lambda$ of [sk-def-sf-setting], regarded as a condensed
ring, they are the full subcategories of $D(X_{\mathrm{pro\acute et}},\Lambda)$
of [sk-def-sfb-bounded-constructible]. In particular
$D^b_c(X,A)$ is a triangulated category in the strict sense of
Verdier: the distinguished triangles, the shift functor, and the
octahedral axiom are given data, and there is *no* functorial choice
of mapping cone, no mapping-cone functor, and no model of the derived
category in which cones are strict. Consequently, all arguments below
that involve a distinguished triangle do it in one of two ways:
   1. the statement is about a *functor known to be exact and
triangulated* (e.g. $Lf^*$, $Rf_!$, $Rf^!$, $R\Gamma_c(X,-)$,
$L\bar x^*$), so that the image of a distinguished triangle is
distinguished and the image of a morphism of triangles is a morphism
of triangles, *because the interface records this* (the
exactness clauses of [prop-functor-package]); or
   1. the statement is proved at the level of *explicit bounded
complexes* with the Koszul convention of
[lem-trf-chain-supertrace], i.e. one chooses a representative
(possible because every object of $D^b_{\mathrm{fin}}(A)$ is
represented by a bounded complex of finitely generated projective
$A$-modules), computes there, and shows the result to be a
quasi-isomorphism invariant.
1. *The six-functor package as a 2-categorical datum.* The
six operations, the exchange and projection transformations, the units
and counits of the adjunctions, the composition laws, the smooth-purity
and Verdier-biduality isomorphisms, and the coefficient-passage maps of
the framework chapter, the six-operations
package, are used in the following precise form: they are a datum
consisting of
   - for each $f:X\to Y$ (separated finite type, under the stated
admissibility), the exact functors $Lf^*$, $Rf_*$, $Rf_!$,
$Rf^!$ between the triangulated categories;
   - for each Cartesian square, the exchange transformations
$\operatorname{Ex}_*$, $\operatorname{Ex}_!$ and, for each
$L\in D^b_{ctf}$, the projection transformation
$\operatorname{PF}$ (the framework chapter,
[def-exchange-projection]), each a *natural* transformation
of exact functors;
   - for each composable pair, the composition isomorphisms
$Rg_!\circ Rf_!\cong R(gf)_!$ and their adjoint forms, with the
identity compatibilities and the associativity pentagon;
   - for each $f$, the unit $\eta_f:\operatorname{id}\to Rf^!Rf_!$ and the counit $\varepsilon_f:Rf_!Rf^!\to \operatorname{id}$ of the adjunction $Rf_!\dashv Rf^!$;
   - the compatibility laws connecting these: the base-change
cocycle over a composite of Cartesian squares (the "outer square"
condition), the compatibility of the composition isomorphisms with
the exchanges, the projection-formula–exchange cocycles, and the
adjunction compatibility of the exchanges; each of these is a
*stated, enumerated law of the interface*, not a consequence of
coherence in a higher structure.
Whenever this chapter writes "the canonical map" or "the canonical
isomorphism", it means: a map or isomorphism *built from the
data above* by composition, whiskering, and (where an adjoint is
uniquely determined) the mate construction. Where a needed coherence
is not one of the enumerated laws, the coherence is either proved in
this chapter by an explicit model (e.g. the Koszul computations of
[lem-trf-chain-supertrace] and the split-exact-sequence
computation of [prop-trf-trace-formal-laws]) or proved from the
results of this manuscript.
1. *The trace and the duality data.* The categorical trace of
[def-trf-categorical-trace] is a 1-categorical construction: the
strict symmetric monoidal structure on the model category of bounded
complexes of finitely generated projective modules is made explicit in
[lem-trf-chain-supertrace] (the Koszul braiding, the explicit
coevaluation and evaluation and the verification of the triangle
identities at the level of the model), and the trace is then the
composite of four *morphisms in the model category*, followed by
the identification $\operatorname{End}_{D(A)}(A)\cong A$. No
synthetic or higher-categorical trace is used.
1. *Classical bookkeeping of coefficients.*
The integral, rational and $\Qlb$-coefficient categories are the condensed
categories $\Dbc(X,\Lambda)$ of [sk-def-sf-setting], not categories
constructed from finite stages. Reductions modulo $\pi_E^n$, integral
models (lattices) and descent to a finite coefficient field are used only
as theorems about these categories: [sk-prop-scalar-six],
[sk-lem-integral-models] and [sk-thm-sfb-qlbar-two-colimit]. The
compatibility of the trace with these passages is proved step by step from
explicit formulas on perfect complexes over the point (the scalar-extension
law of [prop-trf-trace-formal-laws] and the chain-level computation of
[lem-trf-chain-supertrace]), never from a general "limits commute with
functors" statement in a higher category.
1. *Koszul sign convention.* In every explicit computation
with complexes, the conventions of
[lem-trf-chain-supertrace] are used: the differential of the
tensor product of complexes is
$d(p\otimes q)=dp\otimes q+(-1)^{|p|}p\otimes dq$, the braiding is
$c(p\otimes q)=(-1)^{|p||q|}q\otimes p$, and the internal-Hom and
duality data are the ones displayed there.

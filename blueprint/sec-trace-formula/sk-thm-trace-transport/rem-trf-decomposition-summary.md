+++
id = "rem-trf-decomposition-summary"
kind = "remark"
title = "Decomposition summary"
order = 2746
uses = ["cor-trf-point-counting", "def-trf-categorical-trace", "def-trf-correspondence", "def-trf-dualizing-complex", "def-trf-fixed-scheme", "def-trf-frobenius-operators", "def-trf-global-operator", "def-trf-graph-correspondence", "def-trf-integration", "def-trf-local-term", "def-trf-strict-weil-complex", "def-trf-trace-class", "lem-trf-adjoint-mate", "lem-trf-chain-supertrace", "prop-trf-adic-coefficient-morphism-systems", "prop-trf-fixed-square-cartesian", "prop-trf-graph-frobenius-operator", "prop-trf-graph-operator", "prop-trf-rational-frobenius-integral-model", "prop-trf-trace-class-additivity", "prop-trf-trace-formal-laws", "rem-trf-classical-framework", "thm-trf-dualizing-complex-composition", "thm-trf-fixed-point-base-change", "thm-trf-fixed-point-localization", "thm-trf-frobenius-fixed-points", "thm-trf-frobenius-local-term", "thm-trf-grothendieck-lefschetz-finite-ring", "thm-trf-grothendieck-lefschetz-qbar", "thm-trf-integral-adic-coefficient-morphism-trace-formula", "thm-trf-internal-hom-pullback", "thm-trf-lefschetz-verdier", "thm-trf-trace-formula-e", "thm-trf-verdier-biduality", "thm-trf-verdier-duality"]
+++
The chapter extracts the two trace-formula inputs of the Weil-conjecture
proof, the fixed-point evaluation and the Lefschetz–Verdier trace
comparison, and decomposes them into the following chain. Throughout,
the framework is the classical 1-categorical one of
[rem-trf-classical-framework] (no $\infty$-categories): the
triangulated categories of the trace-formula chapter, the six-functor package as a
2-categorical datum with the enumerated coherence laws, and the
explicit-model computations of [lem-trf-chain-supertrace].

1. the framework convention and the coefficient conventions
([rem-trf-classical-framework],
[def-trf-strict-weil-complex], [def-trf-frobenius-operators]);
1. the categorical trace and its formal laws
([def-trf-categorical-trace], the explicit Koszul conventions and
computation of [lem-trf-chain-supertrace],
[prop-trf-trace-formal-laws]);
1. the correspondence formalism: [def-trf-correspondence] and
[def-trf-global-operator], the fixed scheme
[def-trf-fixed-scheme] in the Cartesian fixed square
[prop-trf-fixed-square-cartesian], the dualizing complex and Verdier
dual of [def-trf-dualizing-complex] with
[thm-trf-dualizing-complex-composition] and
[thm-trf-verdier-biduality], and the internal-Hom/pullback and
fixed-square base changes ([thm-trf-internal-hom-pullback],
[thm-trf-fixed-point-base-change]); only the displayed valid
exchanges are used, not a naive single-leg identification;
1. the trace class, integration, and local terms
([def-trf-trace-class], [def-trf-integration],
[def-trf-local-term]) built on the fixed-point evaluation
[thm-trf-verdier-duality], whose external-duality construction
comes from the Kunneth–Verdier chain; see also
[rem-trf-verdier-decomposition];
1. the trace-compatibility statements: the proper-pushforward
compatibility [thm-trf-trace-proper-compatibility]
(with its special case [lem-trf-proper-pushforward-trace-class]),
the etale-pullback compatibility
*Etale pullback compatibility of trace maps* and the additivity
[prop-trf-trace-class-additivity]; then the
fixed-point localization
[thm-trf-fixed-point-localization] and the assembly
[thm-trf-lefschetz-verdier] of the comparison; the fixed scheme of a
base-changed correspondence is [lem-trf-fixed-map-proper];
1. the Frobenius graph: [def-trf-graph-correspondence],
[prop-trf-graph-operator], the mate lemma
[lem-trf-adjoint-mate] used in
[prop-trf-graph-frobenius-operator], the fixed-point theorem
[thm-trf-frobenius-fixed-points] (with the complete affine
computation and the transversality check) and the local-term formula
[thm-trf-frobenius-local-term];
1. the coefficient descent to the finite-ring, integral, rational and
algebraically closed statements
([thm-trf-grothendieck-lefschetz-finite-ring],
[thm-trf-integral-adic-coefficient-morphism-trace-formula], [thm-trf-trace-formula-e],
[thm-trf-grothendieck-lefschetz-qbar]) and the point-counting
corollary [cor-trf-point-counting]; for an arbitrary, possibly
non-invertible, Weil map at the stage $E$ the descent passes through an
integral model with non-invertible Frobenius coefficient morphisms
([prop-trf-rational-frobenius-integral-model]), their adic assembly
([prop-trf-adic-coefficient-morphism-systems]) and the integral
coefficient-morphism trace formula
[thm-trf-integral-adic-coefficient-morphism-trace-formula].

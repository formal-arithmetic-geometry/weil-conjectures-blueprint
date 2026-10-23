+++
id = "rem-trf-decomposition-summary"
kind = "remark"
title = "Decomposition summary"
order = 3554
uses = ["cor-trf-point-counting", "det-thm-tf-uniform-formula-weil", "sk-prop-tf-transport-integral", "sk-lem-tf-rational-model", "sk-thm-tf-uniform-formula", "def-trf-categorical-trace", "def-trf-correspondence", "def-trf-dualizing-complex", "def-trf-fixed-scheme", "def-trf-frobenius-operators", "def-trf-global-operator", "def-trf-graph-correspondence", "def-trf-integration", "def-trf-local-term", "def-trf-strict-weil-complex", "def-trf-trace-class", "lem-trf-adjoint-mate", "lem-trf-chain-supertrace", "prop-trf-fixed-square-cartesian", "prop-trf-graph-frobenius-operator", "prop-trf-graph-operator", "prop-trf-trace-class-additivity", "prop-trf-trace-formal-laws", "rem-trf-classical-framework", "thm-trf-dualizing-complex-composition", "thm-trf-fixed-point-base-change", "thm-trf-fixed-point-localization", "thm-trf-frobenius-fixed-points", "thm-trf-frobenius-local-term", "thm-trf-grothendieck-lefschetz-finite-ring", "thm-trf-internal-hom-pullback", "thm-trf-lefschetz-verdier", "thm-trf-verdier-biduality", "thm-trf-verdier-duality"]
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
1. the coefficient passage from the finite-ring statement
[thm-trf-grothendieck-lefschetz-finite-ring] to the other admissible
coefficient rings: the integral trace formula
[sk-prop-tf-transport-integral] for an arbitrary integral Frobenius
correspondence on $\Dbc(X,\mathcal O_E)$, the integral models
[sk-lem-tf-rational-model] of possibly non-invertible rational Frobenius
correspondences, and the uniform formula [sk-thm-tf-uniform-formula] for
$\Lambda\in\{\mathcal O_E,E,\Qlb\}$, stated for Weil complexes over $E$
and $\Qlb$ in [det-thm-tf-uniform-formula-weil]; then the point-counting
corollary [cor-trf-point-counting].

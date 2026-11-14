+++
id = "dag-lem-pe-internal-module-sectionwise-short-exact"
kind = "dag-lemma"
title = "Sectionwise short exactness implies short exactness of internal sheaf modules"
name_showing = false
order = 210502
tags = ["sheaf-dag"]
split_from = "lemma-reduction-derived-nakayama--1"
dag_id = "lem-pe-internal-module-sectionwise-short-exact"
dag_kind = "statement"
dag_status = "split"
serial = false
dag_lean = ["CategoryTheory.sectionwiseShortExactSheafify", "CategoryTheory.sectionwiseShortExactSheafMonoidal", "CategoryTheory.sectionwiseShortExactSheafSymmetric", "CategoryTheory.sectionwiseShortExactSheafClosed", "CategoryTheory.sectionwiseShortExactSheafPreadditive", "CategoryTheory.sectionwiseShortExactSheafLeftColimits", "CategoryTheory.Mod.shortExact_of_sectionwise"]
+++
Let $\mathcal C$ be a site whose underlying category is essentially small relative to the universe of the abelian groups used as coefficients. Give $\mathcal B=\operatorname{Sh}(\mathcal C,\mathrm{Ab})$ the sheafified objectwise tensor over $\mathbf Z$ of `sk-def-sfb-sheaf-tensor`. Let $\mathcal R$ be a ring object of $\mathcal B$ `sk-def-sfb-ring-object`, and use internal left module objects and their forgetful functor $U:\operatorname{Mod}_{\mathcal R}(\mathcal B)\to\mathcal B$ as in `sk-def-sfb-module-objects`. Let $M_0,M_1,M_2$ be such internal modules and let $F:M_0\to M_1$ and $G:M_1\to M_2$ be internal module morphisms with $G\circ F=0$. Suppose that for every object $V$ of $\mathcal C$ the sequence of abelian groups
$$0\longrightarrow U(M_0)(V)\xrightarrow{U(F)_V}U(M_1)(V)\xrightarrow{U(G)_V}U(M_2)(V)\longrightarrow0$$
is short exact. Then the sequence of underlying abelian presheaves is short exact, the sequence of underlying abelian sheaves is short exact, and
$$0\longrightarrow M_0\xrightarrow{F}M_1\xrightarrow{G}M_2\longrightarrow0$$
is short exact in the abelian category $\operatorname{Mod}_{\mathcal R}(\mathcal B)$ of `lem-sfb-modobj-abelian` (its hypotheses hold by the closedness in `sk-def-sfb-sheaf-tensor`), with these prescribed arrows. Here short exactness is as in `def-weil-pbc-exact-sequence`.

(SHEAF DAG node `lem-pe-internal-module-sectionwise-short-exact`; machine-alignment layer.) Split from [lemma-reduction-derived-nakayama--1]. DAG kind: statement. Placed through `det-pe-derived-nakayama-resolution` (ancestor-1). DAG status: split. Statement dependencies not drawn: `def-weil-pbc-exact-sequence`, `lem-sfb-modobj-abelian`, `sk-def-sfb-module-objects`.

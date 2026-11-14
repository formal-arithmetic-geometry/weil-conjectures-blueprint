+++
id = "dag-lem-pur-signed-line-pullback-unit-presentation"
kind = "dag-lemma"
title = "Signed line pullback unit presentation"
name_showing = false
order = 187537
tags = ["sheaf-dag"]
split_from = "lemma-inverse-image-coefficient-sheaves--2"
dag_id = "lem-pur-signed-line-pullback-unit-presentation"
dag_kind = "statement"
dag_status = "split"
serial = false
dag_lean = ["CategoryTheory.SignedLinePullbackConstruction.SheafPullbackUnitPresentation.hom_ext", "CategoryTheory.SignedLinePullbackConstruction.SheafPullbackUnitPresentation.tensor", "CategoryTheory.SignedLinePullbackConstruction.SheafPullbackUnitPresentation.map", "CategoryTheory.SignedLinePullbackConstruction.SheafPullbackUnitPresentation.map_unit"]
uses = ["dag-def-pur-signed-line-pullback-unit-presentation"]
+++
Given unit presentations (S,T,j,i) and (S′,T′,j′,i′) [dag-def-pur-signed-line-pullback-unit-presentation], maps T→Z agree if they agree on j(x) for every source section. A source map a:S→S′ transports to i;L(a);i′^{-1}:T→T′ and sends j(x) to j′(a(x)). If L preserves finite products, presentations tensor to a presentation of the Cartesian product, whose comparison is (i×i′) followed by the inverse product comparison.

(SHEAF DAG node `lem-pur-signed-line-pullback-unit-presentation`; machine-alignment layer.) Split from [lemma-inverse-image-coefficient-sheaves--2]. DAG kind: statement. Placed through `det-prop-sfb-cartesian-coefficients-twists` (ancestor-2). DAG status: split. Statement dependencies not drawn: `def-weil-size-convention`.

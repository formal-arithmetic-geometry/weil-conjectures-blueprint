+++
id = "lemma-nagata-valuation-ring-extension"
kind = "lemma"
title = "Extension of a valuation ring to a field extension, [stacks-project]"
order = 281
lean = ["ValuationSubring.exists_comap_eq"]
uses = ["lemma-nagata-local-domain-valuation-dominates", "lemma-nagata-valuation-intersection"]
+++
Let $A$ be a valuation ring with fraction field $K$, and let
$K\hookrightarrow L$ be a field extension. There exists a valuation ring
$B\subseteq L$ with fraction field $L$ such that $K\cap B=A$; in
particular $B$ dominates $A$.

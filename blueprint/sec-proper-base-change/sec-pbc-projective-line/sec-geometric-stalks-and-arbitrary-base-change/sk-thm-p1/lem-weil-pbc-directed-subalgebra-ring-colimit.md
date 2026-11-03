+++
id = "lem-weil-pbc-directed-subalgebra-ring-colimit"
kind = "lemma"
title = "A directed union of integer subalgebras is a categorical ring colimit"
lean = ["CommRingCat.isColimitSubalgebraCocone"]
order = 1823
+++
Let $R$ be a commutative ring and $\mathcal P$ a property of subrings of $R$. Assume that the set $\mathcal I$ of subrings of $R$ having $\mathcal P$, partially ordered by inclusion, is nonempty and directed, and that these subrings generate $R$ (equivalently, as $\mathcal I$ is directed, $R=\bigcup_{A\in\mathcal I}A$). Consider the diagram $\mathcal I\to(\text{commutative rings})$, $A\mapsto A$, whose transition maps are the inclusions, and the cocone on it with vertex $R$ given by the inclusions $A\hookrightarrow R$. Then this cocone is a colimit cocone in the category of commutative rings.

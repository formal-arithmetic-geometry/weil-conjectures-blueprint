+++
id = "prose-D-13"
kind = "hidden"
title = "Proof of Theorem “Cohomology of curves”"
order = 937
+++
The assertions of Theorem [sk-thm-curve-package] pass along short
exact sequences. To see this, let $0\to F_1\to F\to F_2\to0$ be exact, and
suppose that the assertions are known for $F_1$ and $F_2$. Vanishing and
finiteness follow from the long exact sequence, and invariance under
field extension follows from the map between the two long exact
sequences and the five lemma.
For $(C_8)$, let $b\in H^2(U,F)$. We lift its image in $H^2(U,F_2)$ to
$c_2\in H^2(C,F_2)$. The obstruction to lifting $c_2$ to $H^2(C,F)$
lies in $H^3(C,F_1)$, which vanishes by $(C_1)$. If we choose a lift
$c$, then the difference $b-c|_U$ comes from $H^2(U,F_1)$, and by
$(C_8)$ for $F_1$ this difference lifts to $H^2(C,F_1)$. Adding that
lift to $c$, we get the required global class [Stacks, Tag 0A5C](https://stacks.math.columbia.edu/tag/0A5C).

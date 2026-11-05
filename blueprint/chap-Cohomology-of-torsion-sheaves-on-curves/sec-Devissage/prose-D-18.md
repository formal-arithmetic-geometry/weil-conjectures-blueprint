+++
id = "prose-D-18"
kind = "hidden"
title = "Dévissage"
order = 1617
+++
The assertions of Theorem [theorem-cohomology-curves] pass along short
exact sequences.  To see this, let $0\to F_1\to F\to F_2\to0$ be exact, and
suppose that the assertions are known for $F_1$ and $F_2$.  Vanishing and
finiteness follow from the long exact sequence, and invariance under
field extension follows from the map between the two long exact
sequences and the five lemma.
For $(C_8)$ an extra argument is needed. Let $b\in H^2(U,F)$, and lift its image in $H^2(U,F_2)$ to
$c_2\in H^2(C,F_2)$.  The obstruction to lifting $c_2$ to $H^2(C,F)$
lies in $H^3(C,F_1)$, which vanishes by $(C_1)$, so such a lift
$c$ exists. The difference $b-c|_U$ comes from $H^2(U,F_1)$, and by
$(C_8)$ for $F_1$ it lifts to $H^2(C,F_1)$; adding that
lift to $c$ gives the required global class [Stacks, [0A5C](https://stacks.math.columbia.edu/tag/0A5C)].

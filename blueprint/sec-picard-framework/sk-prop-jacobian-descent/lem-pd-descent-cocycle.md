+++
id = "lem-pd-descent-cocycle"
kind = "lemma"
title = "The cocycle condition for the canonical transport"
lean = ["CategoryTheory.Functor.RepresentableBy.overTransport_overTransport"]
order = 854
uses = ["def-pd-descent-datum"]
+++
Let $p:X\to Y$ be a morphism of schemes, $F$ a presheaf of sets on the
category of schemes over $Y$, and $V$ a scheme over $X$ representing the
restriction of $F$ to schemes over $X$. For $f_1,f_2:T\to X$ with
$p\circ f_1=p\circ f_2$, let $\tau_{f_1,f_2}$ be the transport of
$T$-points of $V$ over $f_1$ to $T$-points over $f_2$ that preserves the
corresponding element of $F(T\to Y)$. Then for $f_1,f_2,f_3:T\to X$ with
the same composite to $Y$,

$$
\tau_{f_2,f_3}\circ\tau_{f_1,f_2}=\tau_{f_1,f_3}.
$$

This is the cocycle condition of [def-pd-descent-datum] in transport form.

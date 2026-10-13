+++
id = "def-sfb-rationalization-morphisms"
kind = "definition"
title = "Morphisms with torsion cone"
order = 1633
uses = ["lem-sfb-torsion-triangulated"]
lean = ["CategoryTheory.Rationalization.W"]
+++
In the situation of [lem-sfb-torsion-triangulated], let $W_M$ be the class of morphisms
$f\colon X\to Y$ of $\mathcal T$ whose mapping cone is $M$-torsion, i.e. those that sit
in a distinguished triangle $X\xrightarrow{f}Y\to Z\to X[1]$ with $Z$ $M$-torsion. These
are the morphisms inverted in the Verdier quotient by the $M$-torsion objects.

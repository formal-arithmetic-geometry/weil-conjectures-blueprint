+++
kind  = "proof"
of    = "det-nagata-refinement-cofiltered"
uses = ["det-nagata-theorem-dense", "det-nagata-refinement-common-dense", "det-nagata-refinement-morphisms"]
+++
Nonemptiness is the dense form of Nagata's theorem
([det-nagata-theorem-dense]). Two objects $c_1,c_2$ admit the common dense
refinement of [det-nagata-refinement-common-dense]. If $u,v:c'\to c$ are two
refinements, then $u\circ j'=j=v\circ j'$, so $u=v$ by the uniqueness part of
[det-nagata-refinement-morphisms]. A nonempty category in which any two
objects have a common lower bound and parallel morphisms are equal is
cofiltered.

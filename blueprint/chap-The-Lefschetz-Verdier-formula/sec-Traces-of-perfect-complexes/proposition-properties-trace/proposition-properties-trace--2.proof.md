+++
kind = "proof"
of = "proposition-properties-trace--2"
order = 895009
uses = ["definition-categorical-trace"]
+++
The trace is cyclic: for $f:P\to P'$ and $g:P'\to P$,
$\operatorname{tr}(g\circ f)=\operatorname{tr}(f\circ g)$.
In `CategoryTheory.MonoidalCategory.trace_comp_comm`, this follows by
moving a map across coevaluation using its dual, applying naturality of
the braiding, and moving the dual map across evaluation. Now write
$v'=e\circ v\circ e^{-1}$, apply cyclicity, and cancel
$e^{-1}\circ e$.

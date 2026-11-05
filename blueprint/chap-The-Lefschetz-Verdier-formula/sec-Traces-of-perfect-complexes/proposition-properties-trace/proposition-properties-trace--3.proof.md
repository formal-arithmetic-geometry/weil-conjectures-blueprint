+++
kind = "proof"
of = "proposition-properties-trace--3"
order = 895010
uses = ["definition-categorical-trace", "proposition-properties-trace--2"]
+++
Transport the exact pairing of $P$ and its right dual along $F$.
The trace may be computed with this transported dual, since it is
independent of the chosen right dual. Naturality of the monoidal
structure and compatibility with the braiding identify the resulting
composite with $F(\operatorname{tr}(v))$, conjugated by the unit
isomorphism. This is `CategoryTheory.Functor.trace_map`. By definition
the conjugated composite is $\rho_F(\operatorname{tr}(v))$.
Apply [proposition-properties-trace--2] to the intertwining isomorphism
$e$ to replace $F(v)$ by $v'$.

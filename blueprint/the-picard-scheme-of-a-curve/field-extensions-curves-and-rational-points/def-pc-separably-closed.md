+++
id = "def-pc-separably-closed"
kind = "definition"
title = "Separably closed fields"
order = 4216
lean = ["IsSepClosed"]
+++
A field $k$ is *separably closed* if every nonconstant separable
polynomial $f\in k[T]$ has a root in $k$ — equivalently, $k$ has no
nontrivial finite separable field extension.

*Import note.* The source's sentence breaks off at the semicolon inside the
parenthesis and the definition then closes; the parenthetical is completed
above as the equivalence it states, and nothing else is added. That the
equivalence holds is [lem-pc-sepclosed-finite-sep-trivial], as
[rem-ptr-pc-separably-closed-1] records.

*The source marks this as already available in Mathlib.*

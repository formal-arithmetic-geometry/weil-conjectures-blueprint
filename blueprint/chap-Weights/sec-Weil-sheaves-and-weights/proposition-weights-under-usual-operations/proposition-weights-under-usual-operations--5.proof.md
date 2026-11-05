+++
kind = "proof"
of = "proposition-weights-under-usual-operations--5"
order = 1070006
uses = ["definition-weights"]
+++
Use `AlgebraicGeometry.WeilSheaf.isMixedOfWeightsAtMost_iff_filtrationClosure`
to express the two hypotheses as finite filtrations with pure quotients
of weights at most $w$. The sequence
$$
0\longrightarrow\mathcal G\xrightarrow{i}\mathcal F
\longrightarrow\operatorname{coker}(i)\longrightarrow0
$$
is short exact. Splice the filtration of $\mathcal G$ with the inverse
images of the filtration of its cokernel. Lean invokes the extension
closure of finite filtrations through
`CategoryTheory.ObjectProperty.prop_X₂_of_shortExact`.

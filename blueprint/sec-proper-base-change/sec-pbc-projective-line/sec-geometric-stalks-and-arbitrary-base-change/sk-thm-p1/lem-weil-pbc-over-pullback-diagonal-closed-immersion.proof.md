+++
kind = "proof"
of = "lem-weil-pbc-over-pullback-diagonal-closed-immersion"
uses = ["def-pc-base-change"]
+++
Write $X_T=X\times_ST$ and $Y_T=Y\times_ST$. The two base-changed projections $a,b:(X\times_YX)\times_ST\to X_T$ have equal composites with $f_T:X_T\to Y_T$, so they induce a morphism $e:(X\times_YX)\times_ST\to X_T\times_{Y_T}X_T$. Conversely, the two projections of $X_T\times_{Y_T}X_T$ to $X_T$ give two morphisms to $X$ with the same composite to $Y$, and a common morphism to $T$; these induce a morphism $v$ in the reverse direction. Checking the projections on both sides shows that $e$ and $v$ are mutually inverse. This uses only the universal property of fibre products and the definition of base change [def-pc-base-change].

The base-changed diagonal $\gamma_T$ composed with $e$ equals the diagonal of $f_T$, as one checks on the two projections. Being a closed immersion is invariant under composition with isomorphisms, and $f_T$ is separated precisely when its diagonal is a closed immersion. Hence $\gamma_T$ is a closed immersion if and only if $f_T$ is separated.

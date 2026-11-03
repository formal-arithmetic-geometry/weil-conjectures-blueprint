+++
id = "lem-kun-derived-tensor-t-est"
kind = "lemma"
title = "Connectivity of the derived tensor product"
lean = ["DerivedCategory.isGE_tensor_of_torAmplitudeGE"]
order = 3114
uses = ["def-kun-derived-tensor", "def-kun-tor-amplitude", "def-kun-truncations", "def-weil-pbc-derived-categories", "lem-kun-0f1m"]
+++
Let $T$ be a scheme, $\Lambda$ a commutative ring, $a,b\in\mathbf Z$,
and $A,B\in D(T_{\Et},\Lambda)$. If $A$ has tor amplitude in
$[a,\infty)$ ([def-kun-tor-amplitude]) and $\mathcal H^i(B)=0$ for
$i<b$, then $\mathcal H^i(A\kunotimes{\Lambda}B)=0$ for $i<a+b$.

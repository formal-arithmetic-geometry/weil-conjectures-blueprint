+++
id = "rem-ptr-pc-hilb-functor-12"
kind = "remark"
title = "Pointer to the properties of the Hilbert functor"
order = 4283
tags = ["latex:remark"]
uses = ["def-pc-hilb-functor", "def-pc-finite-locally-free", "lem-pc-hilb-functorial"]
+++
In the notation of [def-pc-hilb-functor], for a scheme $T$ over $S$ put
$$
\operatorname{Hilb}^d_{X/S}(T):=\bigl\{Z\subset X_T\ \text{a closed subscheme}:\
Z\to T\text{ is finite locally free of degree }d\bigr\},
$$
where "finite locally free of degree $d$" is
[def-pc-finite-locally-free]; the assignment is contravariant by base
change of closed subschemes, and the resulting functor's sheaf properties
are [lem-pc-hilb-functorial].

+++
kind = "proof"
of = "def-weil-pbc-arrows-functor"
+++
The map on objects is $C\mapsto\mathrm{Arrows}(C)$ and on morphisms $v\mapsto\mathrm{Arrows}(v)$. For the identity functor, $\mathrm{Arrows}(\mathrm{id}_C)(X,Y,f)=(X,Y,f)$, so $\mathrm{Arrows}(\mathrm{id}_C)=\mathrm{id}$. For functors $v:C\to D$ and $w:D\to E$, both $\mathrm{Arrows}(w\circ v)$ and $\mathrm{Arrows}(w)\circ\mathrm{Arrows}(v)$ send $(X,Y,f)$ to $(wvX,wvY,wvf)$, so they agree. Hence $\mathrm{Arrows}$ is a functor.

+++
kind = "proof"
of = "lem-weil-pbc-etale-pointed-map-rigidity"
+++
The equality $f\circ u=f\circ v$ defines $d=(u,v):\operatorname{Spec}B\to X\times_SX$. The diagonal $\Delta:X\to X\times_SX$ of an etale morphism is an open immersion (Stacks 02GE). By the pointed equality and the universal property of the fibre product, $d\circ\operatorname{Spec}\beta=(u\circ\operatorname{Spec}\beta,u\circ\operatorname{Spec}\beta)=\Delta\circ u\circ\operatorname{Spec}\beta$.

Since $\beta$ is local, $\operatorname{Spec}\beta$ sends the unique point of $\operatorname{Spec}\Omega$ to the closed point of $\operatorname{Spec}B$. Evaluating the preceding equality there shows that $d$ sends the closed point into the open subset $\Delta(X)$. Every point of the local scheme $\operatorname{Spec}B$ is a generization of its closed point, and open subsets are stable under generization, so $d(\operatorname{Spec}B)\subseteq\Delta(X)$.

Hence $d$ factors through the open immersion $\Delta$, say $d=\Delta\circ l$. The two projections $X\times_SX\to X$ both restrict to the identity along $\Delta$, so composing $d=\Delta\circ l$ with them gives $u=l$ and $v=l$. Hence $u=v$.

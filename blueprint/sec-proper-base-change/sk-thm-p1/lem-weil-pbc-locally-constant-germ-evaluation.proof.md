+++
kind = "proof"
of = "lem-weil-pbc-locally-constant-germ-evaluation"
+++
The neighbourhoods of $x$ form a filtered system, so every element of $L_{R,x}$ is a germ $g_x$ of some $g\in L_R(V)$, and two germs $g_x,h_x$ (with $g$ on $V$, $h$ on $V'$) are equal iff $g$ and $h$ agree on some open neighbourhood $W\subseteq V\cap V'$ of $x$. Define the evaluation of an element of $L_{R,x}$ to be $g(x)$ for any representative $g$. This is well defined: if $g_x=h_x$, then $g$ and $h$ agree on a neighbourhood of $x$, in particular at $x$. It satisfies $g_x\mapsto g(x)$ by construction, and since every element of $L_{R,x}$ is a germ, this formula determines the map uniquely.

The map ev_x is surjective: for each r in R, the constant map U to R with value r is locally constant, and the germ of this map at x is sent by ev_x to r.

The map ev_x is injective: let two elements of $L_{R,x}$ with the same evaluation be represented by $g_a$ on $V_a$ and $g_b$ on $V_b$. Then $g_a(x)=g_b(x)=r$. Since a locally constant map has open fibres, $W_a=g_a^{-1}(r)$ is open in $V_a$ and $W_b=g_b^{-1}(r)$ is open in $V_b$; as $V_a,V_b$ are open in $U$, both are open in $U$. Their intersection $W$ is an open neighbourhood of $x$ on which $g_a$ and $g_b$ are both constantly $r$, so they agree on $W$ and have the same germ at $x$.

+++
kind  = "proof"
of    = "lem-pc-rational-hyp"
+++
The section $\sigma$ verifies the first condition. Since $X$ is an
integral proper scheme over $k$, by [lem-pc-h0-proper-variety] (1)
$k':=H^0(X,\mathcal{O}_X)$ is a finite field extension of $k$; the
$k$-rational point induces a $k$-algebra homomorphism $k'\to k$, and a
field homomorphism over $k$ is injective, so $k'=k$. Hence $X$ is a
proper $k$-scheme with $H^0(X,\mathcal{O}_X)=k$, and
[lem-pc-structure-pushforward] shows that
$\mathcal{O}_T\to f_{T,*}\mathcal{O}_{X_T}$ is an isomorphism for every
scheme $T$ over $k$, in particular for every
$T\in\operatorname{Ob}((\mathit{Sch}/k)_{fppf})$. This proves the claim.

If instead $X$ is smooth of relative dimension $1$, proper and
geometrically integral over $k$, then $H^0(X,\mathcal{O}_X)=k$ by
[lem-pc-h0-proper-variety] (2), and [lem-pc-structure-pushforward] gives
the second condition in the same way, without using $\sigma$.

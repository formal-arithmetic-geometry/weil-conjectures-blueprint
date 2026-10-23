+++
kind  = "proof"
of    = "lem-sfb-open-projection-formula"
+++
For an object $V$ of $X_{\mathrm{proét}}$, the structure map $V\to X$ factors through
the monomorphism $j$ in at most one way. Hence $j^{\Ab}_!N$, the sheafification of the
left Kan extension along the localization functor
([sk-def-sfb-finite-lower-shriek]), is the sheafification of the presheaf

$$
V\longmapsto\begin{cases}N(V)&\text{if }V\to X\text{ factors through }U,\\
0&\text{otherwise.}\end{cases}
$$

The tensor product of sheaves is the sheafification of the objectwise tensor product,
and sheafification is monoidal, $a(P\otimes Q)\cong a(aP\otimes aQ)$
([lem-weil-pbc-sheaf-tensor-closed]); for $V\to X$ factoring through $U$ one has
$(j^*_{\Ab}L)(V)=L(V)$. Therefore both
$j^{\Ab}_!(j^*_{\Ab}L\otimes M)$ and $L\otimes j^{\Ab}_!M$ are the sheafification of
the same presheaf

$$
V\longmapsto\begin{cases}L(V)\otimes M(V)&\text{if }V\to X\text{ factors through }U,\\
0&\text{otherwise,}\end{cases}
$$

and unwinding the definition of the canonical map shows that it is the
sheafification of the identity of this presheaf. So it is an isomorphism.

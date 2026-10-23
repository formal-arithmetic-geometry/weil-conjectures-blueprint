+++
kind = "proof"
of = "lem-weil-pbc-dense-open-component-coproduct"
uses = ["def-weil-pbc-scheme-conventions"]
+++
*Component opens.* Put $Z_i=\iota_i(C_i)$ and let $W_i$ be the complement of the union of the other irreducible components. There are finitely many components (they are the $Z_i$), so $W_i$ is open; the closure of $W_i$ is $Z_i$, so $W_i$ is nonempty and contained in $Z_i$.

*Local isomorphisms.* Over $W_i$, the restriction of $\iota_i$ is a surjective closed immersion into the reduced open subscheme $W_i$, hence an isomorphism (its ideal sheaf consists of nilpotent sections, which vanish on a reduced scheme). Transport $V_i\cap\iota_i^{-1}(W_i)$ through this isomorphism to an open $O_i\subseteq X$. It is nonempty, since $V_i$ is dense and $\iota_i^{-1}(W_i)$ is a nonempty open of the irreducible $C_i$; being open, nonempty and contained in the irreducible $Z_i$, it has closure $Z_i$. The restriction of $\iota_i$ over $O_i$ is an isomorphism.

*Gluing.* Let $U=\bigcup_iO_i$. The $O_i$ are pairwise disjoint, since $W_i$ avoids every other component. Their closures are the components, which cover $X$, so $U$ is dense. The inverse image of $U$ in $C_i$ is the inverse image of $O_i$, contained in $V_i$. Coproducts of schemes are disjoint and stable under base change, so the restriction of $\coprod_iC_i\to X$ over $U$ is the coproduct of the restrictions over the $O_i$; these are open immersions with pairwise disjoint images covering $U$, each an isomorphism onto $O_i$, so their coproduct is an isomorphism onto $U$. For the empty family $X$ is empty and $U=\emptyset$ [def-weil-pbc-scheme-conventions].

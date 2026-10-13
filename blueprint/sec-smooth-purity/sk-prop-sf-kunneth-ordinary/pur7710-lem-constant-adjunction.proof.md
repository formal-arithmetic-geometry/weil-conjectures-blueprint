+++
kind = "proof"
of = "pur7710-lem-constant-adjunction"
uses = ["pur7710-lem-constant-exact"]
+++
A morphism $M_W\to F$ corresponds, by the universal property of sheafification, to a morphism from the constant presheaf, that is to a compatible family of maps $M\to F(U)$, which is determined by its component at the final object $W$; this gives $(-)_W\dashv\Gamma(W_{\Et},-)$, naturally in $M$ and $F$. The left adjoint is exact (Lemma [pur7710-lem-constant-exact]), so it sends acyclic complexes to acyclic complexes, and the right adjoint therefore sends K-injective complexes to K-injective complexes: for acyclic $P$, homotopy classes $P\to\Gamma(W,I)$ correspond to homotopy classes $P_W\to I$, which vanish. For $K\in D(W_{\Et},B)$ with K-injective resolution $K\to I$, the termwise adjunction identifies homotopy classes $M_W\to I$ with homotopy classes $M\to\Gamma(W,I)$, naturally; these compute the Hom sets in the derived categories because $I$ and $\Gamma(W,I)$ are K-injective.

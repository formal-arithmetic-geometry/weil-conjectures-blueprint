+++
kind  = "proof"
of    = "def-sfb-rationalization-linear"
+++
Write $Y\cong Q(X)$. Then $m\cdot\mathrm{id}_{Q(X)}=Q(m\cdot\mathrm{id}_X)$ is invertible,
because $m\cdot\mathrm{id}_X\in W_M$ [lem-sfb-smul-id-in-w] and $Q$ inverts $W_M$.
Invertibility transfers along the isomorphism to $m\cdot\mathrm{id}_Y$. So $R$ acts on
$\mathcal T[M^{-1}]$ through a ring map $R\to Z(\mathcal T[M^{-1}])$ to the center (the
endomorphisms of the identity functor), which sends $M$ to units. By the universal
property of localization, it extends uniquely to $A\to Z(\mathcal T[M^{-1}])$. A ring map
to the center is the same as a linear structure.

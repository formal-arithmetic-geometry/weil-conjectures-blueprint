+++
kind = "proof"
of = "pur713-lem-monoidal-pullback"
+++
Choose K-flat resolutions $P\to M$, $Q\to N$. Then $P\otimes_{\mathcal O_E/\varpi^n}Q$ computes $M\otimes^L_{\mathcal O_E/\varpi^n}N$, and by Lemma “The finite-coefficient derived inverse image is levelwise” (`pur713-lem-finite-pull-levelwise`) the left side is $f^*(P\otimes Q)$. By Input “Fixed-coefficient inverse image preserves K-flat complexes” (`pur713-input-kflat-fixed`), $f^*P$ and $f^*Q$ are K-flat, so the right side is $f^*P\otimes f^*Q$. The strong monoidal structure of Input “Monoidality of fixed-coefficient images” (`pur713-input-fixed-monoidal`), applied termwise, gives the comparison and its unit version; it is independent of the resolutions. The coherence diagrams are the underived diagrams on these resolutions and remain commutative after localization.

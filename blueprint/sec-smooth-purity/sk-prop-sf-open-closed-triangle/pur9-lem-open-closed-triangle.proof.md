+++
kind = "proof"
of = "pur9-lem-open-closed-triangle"
uses = ["pur9-lem-closed-push-levelwise"]
+++
By Lemmas “The finite-coefficient derived inverse image is levelwise” (`pur713-lem-finite-pull-levelwise`), “Finite-coefficient derived open-extension adjunction” (`pur713-lem-open-adjunction`) and [pur9-lem-closed-push-levelwise], all functors are levelwise functors of exact sheaf functors, and $\varepsilon^j,\eta^i$ are induced termwise by the sheaf counit and unit. Represent $M$ by a complex. Input [pur9-input-open-closed], applied in each degree, gives a short exact sequence of complexes $0\to j_!j^*M\to M\to i_*i^*M\to0$, natural in the complex $M$. A short exact sequence of complexes determines a distinguished triangle in the derived category, whose third map is the connecting morphism; it is natural with respect to morphisms of short exact sequences. All three functors preserve quasi-isomorphisms, so these maps define natural transformations on $D(X_{\Proet},\mathcal O_E/\varpi^n)$.

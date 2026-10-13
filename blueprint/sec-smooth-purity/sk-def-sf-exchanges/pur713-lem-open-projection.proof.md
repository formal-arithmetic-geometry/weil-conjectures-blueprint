+++
kind = "proof"
of = "pur713-lem-open-projection"
uses = ["pur713-lem-monoidal-pullback"]
+++
Let $P\to K$ and $Q\to N$ be K-flat resolutions. Since one K-flat factor suffices to compute a derived tensor product, the source of $\sigma$ is $j_{!,\mathcal O_E/\varpi^n}(P\otimes_{\mathcal O_E/\varpi^n}j^*_{\mathcal O_E/\varpi^n}Q)$ and its target is $j_{!,\mathcal O_E/\varpi^n}P\otimes_{\mathcal O_E/\varpi^n}Q$, all functors being exact and levelwise (Lemmas “The finite-coefficient derived inverse image is levelwise” (`pur713-lem-finite-pull-levelwise`) and “Finite-coefficient derived open-extension adjunction” (`pur713-lem-open-adjunction`)). The unit, the monoidal comparison of Lemma [pur713-lem-monoidal-pullback] and the adjunction are levelwise on these complexes, so $\sigma$ is computed by the termwise map adjoint to $1\otimes\mathrm{unit}$ followed by the monoidal comparison. Up to the symmetry isomorphisms, this is the map $\pi_{j,Q,P}$ of Input [pur713-input-open-projection-finite], which is an isomorphism in each degree.

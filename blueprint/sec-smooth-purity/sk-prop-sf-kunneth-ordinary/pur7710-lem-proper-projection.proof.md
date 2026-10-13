+++
kind = "proof"
of = "pur7710-lem-proper-projection"
uses = ["pur7710-def-constant-projection", "pur7710-lem-finite-type-cd", "pur7710-lem-finite-type-module-cd", "pur7710-lem-separably-closed-cd"]
+++
By Input “Geometric stalks on the small étale site” (`pur456-pbc-input-stalks`, see [sk-thm-sf-comp-composition]) it suffices to test the cone on cohomology stalks at geometric points $\bar y$ of $Y$. Write $i_{\bar y}:X_{\bar y}\to X$ for the geometric fibre and $M_{\bar y}\in D(\mathsf{Mod}_{\mathcal O_E/\varpi^n})$ for the derived stalk of $M$, that is $L\bar y^*_{\Et,\mathcal O_E/\varpi^n}M$ on the spectrum of the separably closed residue field, identified with its complex of global sections (Lemma [pur7710-lem-separably-closed-cd]). Input [pur7710-input-unbounded-pbc] identifies the stalk of the map with

$$
R\Gamma_{X_{\bar y},\Et,\mathcal O_E/\varpi^n}(Li^*_{\bar y,\Et,\mathcal O_E/\varpi^n}K)
\otimes^L_{\mathcal O_E/\varpi^n}M_{\bar y}
\longrightarrow
R\Gamma_{X_{\bar y},\Et,\mathcal O_E/\varpi^n}
(Li^*_{\bar y,\Et,\mathcal O_E/\varpi^n}K\otimes^L_{\mathcal O_E/\varpi^n}c_{X_{\bar y},\mathcal O_E/\varpi^n}M_{\bar y}).
$$

The identification respects the defining counit, so this is the constant-tensor map of Definition [pur7710-def-constant-projection], not merely a map between isomorphic objects. The geometric fibre is of finite type over a separably closed field, so Lemmas [pur7710-lem-separably-closed-cd] and [pur7710-lem-finite-type-cd], with Input “Forgetting finite coefficient actions in direct images” (`pur7710-input-cohomology-coefficients`, see [sk-thm-sf-comp-composition]) as in Lemma [pur7710-lem-finite-type-module-cd], give the dimension hypothesis of Input [pur7710-input-constant-projection], which makes the map an isomorphism. All cohomology stalks of the cone vanish, proving the result for arbitrary complexes. This is the stalk argument for Stacks Project, Tag `0F0G`; it does not use generation of all sheaves by global constant free sheaves.

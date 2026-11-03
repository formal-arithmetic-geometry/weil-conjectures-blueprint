+++
id = "lem-weil-pbc-identity-derived-homology-comparison"
kind = "lemma"
title = "Identity derived homology comparison"
uses = ["def-weil-pbc-derived-categories"]
lean = ["CategoryTheory.Functor.identityDerivedHomologyComparison"]
order = 1936
+++
Let $\mathcal C$ be an abelian category with a chosen derived category [def-weil-pbc-derived-categories], let $n\in\mathbf Z$ and let $K$ be an object of the bounded below derived category $D^+(\mathcal C)$. The identity functor $\mathrm{Id}_{\mathcal C}$ is exact, so it induces $D^+(\mathrm{Id}):D^+(\mathcal C)\to D^+(\mathcal C)$ together with the canonical comparison isomorphism $\gamma_K:\mathrm{Id}(H^n(K))=H^n(K)\xrightarrow{\sim}H^n(D^+(\mathrm{Id})(K))$ of an exact functor with cohomology, and with the canonical isomorphism $\iota:D^+(\mathrm{Id})\xrightarrow{\sim}\mathrm{Id}_{D^+(\mathcal C)}$. Then $\gamma_K=H^n(\iota_K^{-1})$.

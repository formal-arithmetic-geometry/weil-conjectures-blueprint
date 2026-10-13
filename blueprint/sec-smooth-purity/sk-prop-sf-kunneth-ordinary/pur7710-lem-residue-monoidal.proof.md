+++
kind = "proof"
of = "pur7710-lem-residue-monoidal"
uses = ["pur713-lem-extension-kflat"]
+++
Choose K-flat resolutions $P\to K$, $Q\to L$. The complex $(\mathcal O_E/\varpi)_W\otimes P$ is K-flat over $\mathcal O_E/\varpi$, by the associativity argument of Lemma [pur713-lem-extension-kflat] on the étale site, and the first isomorphism is the termwise associativity isomorphism $(\mathcal O_E/\varpi)\otimes(P\otimes Q)\cong((\mathcal O_E/\varpi)\otimes P)\otimes_{\mathcal O_E/\varpi}((\mathcal O_E/\varpi)\otimes Q)$ of sheaf tensor products. The second is the strong monoidal structure of the levelwise inverse image (Inputs “Structure of inverse image on the small étale sites” (`pur713-input-etale-structure`) and “K-flat and K-injective resolutions on the small étale sites” (`pur713-input-etale-kflat`)), which sends K-flat complexes to K-flat complexes and constant sheaves to constant sheaves, applied termwise to $(\mathcal O_E/\varpi)_V\otimes P$. The constraints are the termwise ones.

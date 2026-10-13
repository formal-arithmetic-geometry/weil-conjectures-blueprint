+++
kind = "proof"
of = "pur9-cs-lem-invertible-object"
uses = ["pur9-cs-def-lisse", "pur9-cs-input-site-monoidal"]
+++
The evaluation map $\mathcal L_f\otimes_{\mathcal O_E/\varpi^n}\mathcal L_f^{-1}\to(\mathcal O_E/\varpi^n)_X$ is an isomorphism of sheaves on $X_{\Et}$: on each member of the trivializing covering of Definition [pur9-cs-def-lisse] it is the evaluation map of the constant free module of rank one, and geometric stalks are conservative on $X_{\Et}$ (Lemma “Detection by cohomology stalks” (`pur456-pbc-stalk-detection`, see [sk-thm-sf-comp-composition])). As $\mathcal L_f$ is flat, being locally free, this tensor product is also the derived one $\otimes^L_{\mathcal O_E/\varpi^n}$ on $X_{\Et}$. Applying $L\nu^*_{X,\mathcal O_E/\varpi^n}$, using its monoidal structure from Input [pur9-cs-input-site-monoidal] and its compatibility with shifts, and the isomorphism $\omega_f\cong L\nu^*_{X,\mathcal O_E/\varpi^n}(\mathcal L_f)[2d]$ of Lemma [pur9-cs-lem-invertible], one obtains an isomorphism $\omega_f\otimes^L_{\mathcal O_E/\varpi^n}L\nu^*_{X,\mathcal O_E/\varpi^n}(\mathcal L_f^{-1})[-2d]\cong(\mathcal O_E/\varpi^n)_X$.

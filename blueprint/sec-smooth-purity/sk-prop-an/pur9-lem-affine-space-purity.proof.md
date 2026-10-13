+++
kind = "proof"
of = "pur9-lem-affine-space-purity"
uses = ["pur9-input-preservation", "pur9-lem-affine-line-purity", "pur9-lem-upper-shriek-composition"]
+++
For $c=0$ it is the unit isomorphism. For $c=1$ it is Lemma [pur9-lem-affine-line-purity]. For $c\geq2$, Lemma [pur9-lem-affine-space-composition] writes $\gamma_{p_c,K}$ as a composite of $c^{-1}$ (Lemma [pur9-lem-upper-shriek-composition]), $\gamma_{p'}$ (Lemma [pur9-lem-affine-line-purity] over $B'$, applicable as $Rp^!_{c-1,\mathcal O_E/\varpi^n}K\in D^b_{ctf}$ by Input [pur9-input-preservation]) and $Lp'^*_{\mathcal O_E/\varpi^n}$ of $\gamma_{p_{c-1},K}$ (induction).

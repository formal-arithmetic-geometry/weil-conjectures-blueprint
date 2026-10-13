+++
kind = "proof"
of = "pur9-lem-affine-space-composition"
uses = ["pur9-def-affine-space-trace", "pur9-def-purity-comparison", "pur9-def-upper-shriek-composition"]
+++
Both sides are morphisms into $Rp^!_{c,\mathcal O_E/\varpi^n}K$; compare their adjoints under $Rp_{c,!,\mathcal O_E/\varpi^n}\dashv Rp^!_{c,\mathcal O_E/\varpi^n}$. By Definition [pur9-def-upper-shriek-composition], the adjoint of the right side is obtained from the adjoints of $\gamma_{p'}$ and $\gamma_{p_{c-1}}$ through $\alpha_{p_{c-1},p'}$ and the counits. Those adjoints are $(\int\otimes1)\circ\operatorname{PF}^{-1}$ for $p'$ and $p_{c-1}$ (Definition [pur9-def-purity-comparison]). Input [pur9-input-projection-composition] rewrites $\operatorname{PF}_{p_c}$ through $\alpha$ and the two projection maps, and Definition [pur9-def-affine-space-trace] writes $\int_{p_c}$ as the corresponding composite of traces. Hence the two adjoints agree, and so do the morphisms.

+++
kind = "proof"
of = "pur9-rg-lem-frame-independent"
uses = ["pur9-def-kummer-class", "pur9-lem-a1-invariance", "pur9-rg-lem-concentration-sheaf"]
+++
By Lemma [pur9-rg-lem-concentration-sheaf] and Input [pur9-rg-input-supported], frame classes are sections over $Z_U$ of a sheaf on $(Z_U)_{\Et}$ that is free of rank one, so equality may be checked Zariski-locally. There two frames differ by $M\in\mathrm{GL}_c(\mathcal O)$, which after shrinking is a product of diagonal, permutation and elementary matrices. For a unit $w$, $\kappa(w)$ is defined on all of $U$, so $\partial\kappa(w)=0$ and $\partial\kappa(wf_r)=\partial\kappa(f_r)$ by additivity of Kummer classes (Definition [pur9-def-kummer-class]). The factors $\partial\kappa(f_r)$ have even degree, so permuting them introduces no sign. For an elementary matrix, the frame $f_1+tf_2,f_2,\dots$ over $\Aaf^1_U$ gives a section of the constant rank-one sheaf on $\Aaf^1_{Z_U}$, constant along the line by Lemma [pur9-lem-a1-invariance], so its values at $t=0,1$ agree.

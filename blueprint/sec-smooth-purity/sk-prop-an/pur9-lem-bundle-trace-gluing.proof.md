+++
kind = "proof"
of = "pur9-lem-bundle-trace-gluing"
uses = ["pur7710-lem-cover-detection", "pur9-input-ambient-comparison", "pur9-input-ambient-composition", "pur9-input-p1-cohomology", "pur9-lem-affine-space-trace-iso"]
+++
Both objects have cohomology only in degree zero, so such morphisms are morphisms of the $\mathcal H^0$ sheaves, i.e. sections of a $\mathcal Hom$ sheaf on $Z_{\Proet}$. Two trivializations over $U\cap U'$ differ by $g\in\mathrm{GL}_c$, and the local traces agree by Input [pur9-input-linear-invariance-trace]; the recursive definition of $\int_{p_c}$ is compatible with restriction to opens of the base, since the counits, $\theta$, $\alpha$ and $t_q$ are (Inputs [pur9-input-ambient-comparison], [pur9-input-ambient-composition], [pur9-input-p1-cohomology]). The sheaf axiom gives existence and uniqueness. The result is an isomorphism locally (Lemma [pur9-lem-affine-space-trace-iso]), hence globally (Lemma [pur7710-lem-cover-detection]).

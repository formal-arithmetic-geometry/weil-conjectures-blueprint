+++
kind = "proof"
of = "pur7710-lem-constant-monoidal"
uses = ["pur7710-lem-constant-exact"]
+++
On modules, the constant presheaf of $M\otimes N$ is the objectwise tensor product of the constant presheaves; sheafifying, and using that the sheaf tensor product of Definition “Tensor product of sheaves of $\mathcal O_E/\varpi^n$-modules” (`pur713-def-abelian-tensor-finite`) is the sheafification of the objectwise tensor product of the sheafified presheaves, gives $(M\otimes N)_W\cong M_W\otimes N_W$, compatibly with the constraints. For complexes choose K-flat resolutions $P\to M$, $Q\to N$. By Lemma [pur7710-lem-constant-exact] and the stalkwise description, $P_W$ is K-flat: for an acyclic complex $G$ of sheaves, the geometric stalks of $P_W\otimes G$ are $P\otimes G_{\bar w}$, which are acyclic, and Input “Geometric stalks on the small étale site” (`pur456-pbc-input-stalks`, see [sk-thm-sf-comp-composition]) applies. Hence both sides are computed by $(P\otimes Q)_W\cong P_W\otimes Q_W$.

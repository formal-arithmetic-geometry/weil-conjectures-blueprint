+++
kind = "proof"
of = "pur9-cs-lem-phi-model"
uses = ["pur713-lem-projection-naturality"]
+++
By Definition [pur9-def-purity-comparison], $\gamma_{p_d,K}$ corresponds under the standing adjunction to $1_K\otimes\int_{p_d}$ preceded by the projection map, and for $K=(\mathcal O_E/\varpi^n)_Y$ this says $\varepsilon_{p_d}\circ Rp_{d,!,\mathcal O_E/\varpi^n}(\gamma_{p_d,(\mathcal O_E/\varpi^n)_Y})=\int_{p_d}$ after the unit isomorphisms. Naturality of the projection map in its first variable (Lemma [pur713-lem-projection-naturality]) applied to $\gamma_{p_d,(\mathcal O_E/\varpi^n)_Y}$ transforms the composite defining $\varphi_{p_d,K}\circ(1\otimes\gamma_{p_d,(\mathcal O_E/\varpi^n)_Y})$ in Definition [pur9-cs-def-phi] into the composite defining $\gamma_{p_d,K}$. Both maps therefore have the same adjoint, hence are equal.
